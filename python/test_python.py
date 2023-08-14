import docker
import pytest
import os

@pytest.fixture
def docker_container(request):
    """
    Fixture creates a python docker image and spins up a container, executing the
    command passed in as an argument
    """
    
    client = docker.from_env()
    image_name = 'python-rosetta'
    build_context = './'

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
    @pytest.mark.parametrize(
            'docker_container',
            [["/bin/sh", "-c", "python stdin.py < stdin.txt"]],
            indirect=True,
    )
    def test_stdin(self, docker_container):
        expected = ""
        i = 1
        with open('./stdin.txt', 'r') as f:
            for line in f.readlines():
                expected += f"{i} {line.upper()}"
                i += 1
        docker_container.wait()
        assert str(docker_container.logs(), 'UTF-8') == expected

class TestArgs:
    @pytest.mark.parametrize(
            'docker_container',
            ['python arguments.py "Argument Number 1"'],
            indirect=True,
    )
    def test_args(self, docker_container):
        docker_container.wait()
        assert docker_container.logs() == b'Argument Number 1\n'

# to run in command line:
# docker run -it --rm rosetta-python
