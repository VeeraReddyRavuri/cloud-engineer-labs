import subprocess
import logging

def run_command(command, timeout=10):
    
    try:

        result = subprocess.run(
            command,
            capture_output = True,
            check = True,
            text = True,
            timeout = timeout
        )
        return result.stdout

    except subprocess.CalledProcessError as e:
        print(f"Command {' '.join(command)} failed with error: {e.stderr}")
        return None
    except subprocess.TimeoutExpired:
        print(f"Command {' '.join(command)} timedout")
        return None

def check_docker_images():
    output = run_command(["docker", "images"])
    if output:
        print("===docker images===")
        print(output)

def check_docker_ps_a():
    output = run_command(["docker", "ps", "-a"])
    if output:
        print("===docker ps -a===")
        print(output)

check_docker_images()
check_docker_ps_a()