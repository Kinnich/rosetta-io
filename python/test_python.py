import docker
import pytest
import json
from dataclasses import dataclass


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
def docker_container(request):
    """
    Fixture creates a python docker image and spins up a container, executing the
    command passed in as an argument
    """

    client = docker.from_env()
    image_name = 'python-rosetta'
    build_context = './python/'

    image, logs = client.images.build(path=build_context, tag=image_name)

    for log_line in logs:
        print(log_line)

    # If detach=False, container run method will just return the log output, not the
    # container obj bc container is stopped at this point
    container = client.containers.run(image, command=request.param, detach=True)
    yield container

    # Clean up: Stop and remove the container
    container.stop()
    container.remove()


@pytest.fixture
def docker_client():
    return docker.from_env()

@pytest.fixture
def docker_image(docker_client):
    image_name = 'python-rosetta'
    build_context = './python/'

    image, logs = docker_client.images.build(path=build_context, tag=image_name)

    for log_line in logs:
        print(log_line)

    return image

@dataclass
class DockerRunner:
    client: docker.DockerClient
    image: docker.models.images.Image
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

    @pytest.mark.parametrize(
        'docker_container',
        ['python null_char.py'],
        indirect=True,
    )
    def test_null_char(self, docker_container):
        # Have to wait on container to get the logs
        docker_container.wait()
        assert docker_container.logs() == b'Hello World \x00\n'


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
    @pytest.mark.parametrize(
        'docker_container',
        ['python read_file.py hihello.txt'],
        indirect=True,
    )
    def test_read_file(self, docker_container):
        docker_container.wait()
        assert str(docker_container.logs(), 'UTF-8') == expected_read_file_output()


class TestArgs:
    """Test that args can be passed to script"""
    @pytest.mark.parametrize(
        'docker_container',
        ['python arguments.py "Argument Number 1"'],
        indirect=True,
    )
    def test_args(self, docker_container):
        docker_container.wait()
        assert docker_container.logs() == b'argument number 1\n'


class TestReadJsonFile:
    """Test that a JSON file is read correctly"""
    @pytest.mark.parametrize(
        'docker_container',
        [['/bin/sh', '-c', 'python read_json.py < person-records.json']],
        indirect=True,
    )
    def test_read_json_file(self, docker_container):
        # get expected output
        file_path = "./python/person-records.json"
        with open(file_path, "r") as file:
            data = json.load(file)
        expected = "".join(f"Hello, {person['age']} year old {person['first_name']}\n" for person in data)

        docker_container.wait()
        assert str(docker_container.logs(), 'UTF-8') == expected


class TestWriteFile:
    """Test that a script, given a path to a file, can write to that file"""
    @pytest.mark.parametrize(
        'docker_container',
        [['/bin/sh', '-c', 'python write_file.py output.txt "Bob Barker"; cat output.txt']],
        indirect=True,
    )
    def test_write_file(self, docker_container):
        docker_container.wait()
        assert str(docker_container.logs(), 'UTF-8') == "BOB BARKER" # note no new line char
