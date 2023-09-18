import docker
import pytest
import json
import subprocess
from dataclasses import dataclass
from abc import ABC, abstractmethod

from locking import early_bird_lock


def expected_read_file_output():
    """Result of reading/capitalizing example input file"""
    expected = ""
    i = 1
    with open('./python/hihello.txt', 'r') as f:
        for line in f.readlines():
            expected += f"{i} {line.upper()}"
            i += 1
    return expected


class Language(ABC):
    name: str

    @abstractmethod
    def script_command_parts(self, test_name):
        pass

    def script(self, test_name):
        return " ".join(self.script_command_parts(test_name))


class Python(Language):
    name = 'python'

    def script_command_parts(self, test_name):
        return [self.name, f'{test_name}.py']


# List of language classes with which to parametrize tests
LANGUAGES = [Python(),]

@pytest.fixture(params=LANGUAGES, ids=[x.name for x in LANGUAGES])
def language(request):
    return request.param

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
def docker_image(docker_client: docker.DockerClient, once_per_test_suite_run, language) -> str:
    """Returns the image name which is all we need for using it, but first ensures that the image is built"""

    image_name = f'{language.name}-rosetta'
    build_context = f'./{language.name}/'

    # Only allow the first pytest-xdist worker that gets here to build the
    # image. Otherwise, they will all try to build it and clobber each other.
    with once_per_test_suite_run("build-image", image_name) as should_build:
        # should_build will be True if this is the the first worker to get here, otherwise False
        if should_build:
            _, logs = docker_client.images.build(path=build_context, tag=image_name)
            for log_line in logs:
                print(log_line)

    return image_name


@dataclass
class DockerRunner:
    client: docker.DockerClient
    image: str
    language: Language
    container: docker.models.containers.Container = None

    def run(self, command):
        # save the container so it can be used later by the test
        self.container = self.client.containers.run(self.image, command=command, detach=True)

    def run_script(self, command):
        # save the container so it can be used later by the test
        self.container = self.client.containers.run(self.image, command=command, detach=True)


@pytest.fixture
def docker_runner(docker_client, docker_image, language):
    runner = DockerRunner(docker_client, docker_image, language)

    yield runner

    if runner.container: # i.e. if the test called `docker_runner.run(...)`
        runner.container.stop()
        runner.container.remove()


class TestNullChar:
    def test_null_char(self, docker_runner, language):
        docker_runner.run_script(language.script("null_char"))
        # Have to wait on container to get the logs
        docker_runner.container.wait()
        assert str(docker_runner.container.logs(), 'UTF-8') == 'Hello World \x00\n'


class TestStdIn:
    """Check that input is read from stdin, line by line.
    The script executed in the docker container accepts a text file as input,
    reads each line, capitalizes it, then prints it out.
    """
    def test_stdin(self, docker_runner, language):
        docker_runner.run_script(['/bin/sh', '-c', f'{language.script("stdin")} < hihello.txt'])
        docker_runner.container.wait()
        assert str(docker_runner.container.logs(), 'UTF-8') == expected_read_file_output()


class TestReadFile:
    """Check that a file is read line by line, when file path is given
    as command line argument
    """
    def test_read_file(self, docker_runner, language):
        docker_runner.run_script(f'{language.script("read_file")} hihello.txt')
        docker_runner.container.wait()
        assert str(docker_runner.container.logs(), 'UTF-8') == expected_read_file_output()


class TestArgs:
    """Test that args can be passed to script"""
    def test_args(self, docker_runner, language):
        docker_runner.run_script(f'{language.script("arguments")} "Argument Number 1"')
        docker_runner.container.wait()
        assert str(docker_runner.container.logs(), 'UTF-8') == 'argument number 1\n'


class TestReadJsonFile:
    """Test that a JSON file is read correctly"""
    def test_read_json_file(self, docker_runner, language):
        # get expected output
        file_path = "./python/person-records.json"
        with open(file_path, "r") as file:
            data = json.load(file)
        expected = "".join(f"Hello, {person['age']} year old {person['first_name']}\n" for person in data)

        docker_runner.run_script(['/bin/sh', '-c', f'{language.script("read_json")} < person-records.json'])
        docker_runner.container.wait()
        assert str(docker_runner.container.logs(), 'UTF-8') == expected


class TestWriteFile:
    """Test that a script, given a path to a file, can write to that file"""
    def test_write_file(self, docker_runner, language):
        docker_runner.run_script(['/bin/sh', '-c', f'{language.script("write_file")} output.txt "Bob Barker"; cat output.txt'])
        docker_runner.container.wait()
        assert str(docker_runner.container.logs(), 'UTF-8') == "BOB BARKER" # note no new line char


class TestWriteJsonToStdout:
    def test_json_array(self, docker_runner, language):
        """Test that JSON array is parsed correctly"""
        # Write string args as an array of strings to stdout
        docker_runner.run_script(f'{language.script("json_array")} a b c d')
        docker_runner.container.wait()
        script_output = json.loads(docker_runner.container.logs())
        assert script_output == ["a", "b", "c", "d"]

    def test_json_numbers(self, docker_runner, language):
        """Test that JSON list of numbers is parsed correctly"""
        # Write to stdout the length of each string argument
        docker_runner.run_script(f'{language.script("json_numbers")} a bc def ghij')
        docker_runner.container.wait()
        script_output = json.loads(docker_runner.container.logs())
        assert script_output == [1, 2, 3, 4]

    def test_json_objects(self, docker_runner, language):
        """Test that JSON object is parsed correctly"""
        # Write a dict of {arg:length} to stdout
        # include empty string arg to check handling of empty JSON array
        docker_runner.run_script(f'{language.script("json_stdout_object")} "" a bc def ghij')
        docker_runner.container.wait()
        script_output = json.loads(docker_runner.container.logs())
        assert script_output == {"": 0, "a": 1, "bc": 2, "def": 3, "ghij": 4}

    def test_json_objects_with_arrays(self, docker_runner, language):
        """Test that a JSON object with arrays as values is parsed correctly"""
        # Write a dict of {arg:[list of arg chars]} to stdout
        # include empty string arg to check handling of empty JSON array
        docker_runner.run_script(f'{language.script("json_object_with_array_values")} "" a bc def')
        docker_runner.container.wait()
        script_output = json.loads(docker_runner.container.logs())
        assert script_output == {"": [], "a": ["A"], "bc": ["B", "C"], "def": ["D", "E", "F"]}

    def test_json_object_array(self, docker_runner, language):
        """Test that a JSON array made of objects is parsed correctly"""
        # Write an array of [{arg: length of chars},...] to stdout
        docker_runner.run_script(f'{language.script("json_object_array")} a bc def')
        docker_runner.container.wait()
        script_output = json.loads(docker_runner.container.logs())
        assert script_output == [{"A": 1}, {"BC": 2}, {"DEF": 3}]

    def test_json_control_chars(self, docker_runner, language):
        """Test that control characters and emojis are output in valid JSON
        note: control character "\0" is used by C (and Python) to end strings and so we can't
        pass it as argument in the test string because it will raise "invalid argument" error
        """
        # Pass a single string to the script that inculdes a control character and emoji
        docker_runner.run_script(f'{language.script("json_control_chars")} "hello \n \1 world 🥸"')
        docker_runner.container.wait()
        script_output = json.loads(docker_runner.container.logs())
        # Note: The text in the log is: "hello \n \u0001 world \ud83e\udd78" but Python escapes
        # the escaped characters in the docker container's log so it looks wonky in the test
        assert script_output == "hello \n \u0001 world 🥸"

class TestDecodeBase64:
    """Test that base64 can be decoded as a string"""
    def test_decode(self, docker_runner, language):
        docker_runner.run_script(f'{language.script("decode")} SGVsbG8sIHdvcmxkIQ==')
        docker_runner.container.wait()
        assert str(docker_runner.container.logs(), 'UTF-8') == 'Hello, world!\n'

class TestEncodeBase64:
    """Test that a string can be encoded as base64"""
    def test_encode(self, docker_runner, language):
        docker_runner.run_script(f'{language.script("encode")} "Hello, world!"')
        docker_runner.container.wait()
        assert str(docker_runner.container.logs(), 'UTF-8') == 'SGVsbG8sIHdvcmxkIQ==\n'

class TestStreamingStdin:
    """Test that streaming stdin can be read line by line and can write to stdout
    without waiting for all lines to arrive
    Note: this test uses Docker CLI instead of the Python Docker SDK (implemented in the
    `docker_runner` fixture) since SDK doesn't easily allow writing to a container's stdin"""
    def test_stdin(self, docker_image, language):
        # Subprocess constructor runs the script in a docker container and waits for input
        # Use `script_command_parts` method to format command for Docker CLI as `[...'python', 'script.py']`
        script = subprocess.Popen(
            ['docker', 'run', '-i', docker_image, *language.script_command_parts('streaming_stdin')],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            text=True, # treat standard streams as text, not bytes
            bufsize=1, # set 1 for line buffering, so buffer is flushed when encountering `\n`
        )
        # Give input to the script via stdin, one line at a time, and check result
        for i in range(1, 10):
            script.stdin.write(f"line #{i}\n")
            assert script.stdout.readline() == f"LINE #{i}\n"