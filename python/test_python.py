import docker
import pytest
import json
from dataclasses import dataclass

from .locking import early_bird_lock


def expected_read_file_output():
    """Result of reading/capitalizing example input file"""
    expected = ""
    i = 1
    with open('./python/hihello.txt', 'r') as f:
        for line in f.readlines():
            expected += f"{i} {line.upper()}"
            i += 1
    return expected


@pytest.fixture
def docker_client() -> docker.DockerClient:
    return docker.from_env()

@pytest.fixture
def once_per_test_suite_run(tmp_path_factory, testrun_uid, worker_id):
    def once_per_this_test_run(*lock_keys):
        return early_bird_lock(
            tmp_path_factory.getbasetemp().parent,
            testrun_uid, *lock_keys,
            worker_id=worker_id
        )
    return once_per_this_test_run

@pytest.fixture
def docker_image(docker_client: docker.DockerClient, once_per_test_suite_run) -> str:
    image_name = 'python-rosetta'
    build_context = './python/'

    with once_per_test_suite_run("build-image", image_name) as should_build:
        if should_build:
            _, logs = docker_client.images.build(path=build_context, tag=image_name)
            for log_line in logs:
                print(log_line)

    return image_name


@dataclass
class DockerRunner:
    client: docker.DockerClient
    image: str
    container: docker.models.containers.Container = None

    def run(self, command):
        # save the container so it can be used later by the test
        self.container = self.client.containers.run(self.image, command=command, detach=True)


@pytest.fixture
def docker_runner(docker_client, docker_image):
    runner = DockerRunner(docker_client, docker_image)

    yield runner

    if runner.container: # i.e. if the test called `docker_runner.run(...)`
        runner.container.stop()
        runner.container.remove()


class TestNullChar:
    def test_null_char(self, docker_runner):
        docker_runner.run('python null_char.py')
        # Have to wait on container to get the logs
        docker_runner.container.wait()
        assert docker_runner.container.logs() == b'Hello World \x00\n'


class TestStdIn:
    """Check that input is read from stdin, line by line.
    The script executed in the docker container accepts a text file as input,
    reads each line, capitalizes it, then prints it out.
    """
    def test_stdin(self, docker_runner):
        docker_runner.run(['/bin/sh', '-c', 'python stdin.py < hihello.txt'])
        docker_runner.container.wait()
        assert str(docker_runner.container.logs(), 'UTF-8') == expected_read_file_output()


class TestReadFile:
    """Check that a file is read line by line, when file path is given
    as command line argument
    """
    def test_read_file(self, docker_runner):
        docker_runner.run('python read_file.py hihello.txt')
        docker_runner.container.wait()
        assert str(docker_runner.container.logs(), 'UTF-8') == expected_read_file_output()


class TestArgs:
    """Test that args can be passed to script"""
    def test_args(self, docker_runner):
        docker_runner.run('python arguments.py "Argument Number 1"')
        docker_runner.container.wait()
        assert docker_runner.container.logs() == b'argument number 1\n'


class TestReadJsonFile:
    """Test that a JSON file is read correctly"""
    def test_read_json_file(self, docker_runner):
        # get expected output
        file_path = "./python/person-records.json"
        with open(file_path, "r") as file:
            data = json.load(file)
        expected = "".join(f"Hello, {person['age']} year old {person['first_name']}\n" for person in data)

        docker_runner.run(['/bin/sh', '-c', 'python read_json.py < person-records.json'])
        docker_runner.container.wait()
        assert str(docker_runner.container.logs(), 'UTF-8') == expected


class TestWriteFile:
    """Test that a script, given a path to a file, can write to that file"""
    def test_write_file(self, docker_runner):
        docker_runner.run(['/bin/sh', '-c', 'python write_file.py output.txt "Bob Barker"; cat output.txt'])
        docker_runner.container.wait()
        assert str(docker_runner.container.logs(), 'UTF-8') == "BOB BARKER" # note no new line char
