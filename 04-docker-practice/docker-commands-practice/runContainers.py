import subprocess
import logging

def run_command(command, timeout=10):
    try:
        result = subprocess.run(
            command,
            capture_output = True,
            text = True,
            check = True,
            timeout = timeout
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Command {' '.join(command)} failed with error: {e.stderr}")
        return None
    except subprocess.TimeoutExpired:
        print(f"command {' '.join(command)} timed out")
        return None

def run_container(image, name=None, detach=False, ports=None):
    command = ["docker", "run"]
    if name:
        command.extend(["--name", name])
    if detach:
        command.append("-d")
    if ports:
        command.extend(["-p", ports])
    command.append(image)
    output = run_command(command)
    if output:
        print(f"=== Container started with ID: {output.strip()} ===")

def check_all_containers(prev=False):
    command = ["docker", "ps"]
    if prev:
        command.append("-a")
    output = run_command(command)
    if output:
        print("=== docker ps -a ===")
        print(output)

def stop_container(name):
    output = run_command(["docker", "stop", name])
    if output:
        print(f"Stopped the container: {name}")

def start_container(name):
    output = run_command(["docker", "start", name])
    if output:
        print(f"Container {name} started")

def check_container_logs(name, tail=None):
    command = ["docker", "logs"]
    if tail is not None:
        command.extend(["--tail", str(tail)])
    command.append(name)
    # logs go to stderr, so we need to handle this differently
    result = subprocess.run(command, capture_output=True, text=True)
    output = result.stdout + result.stderr   # combine both
    if output:
        print(f"=== Logs for {name} ===")
        print(output)

def exec_container(name, internal):
    command = ["docker", "exec", name] + internal
    output = run_command(command)
    if output:
        print(f"=== exec result: {internal} ===")
        print(output)

def inspect_container(name):
    command = ["docker", "inspect", name]
    output = run_command(command)
    if output:
        print(f"=== report of {name} ===")
        print(output)


def check_container_stats(name):
    command = ["docker", "stats", "--no-stream", name]
    output = run_command(command)
    if output:
        print(f"=== Stats of {name} ===")
        print(output)

def delete_container(name):
    stop_container(name)
    command = ["docker", "rm", name]
    output = run_command(command)
    if output:
        print(f"=== Container {name} is deleted ===")
        print(output)



run_container(image="nginx", name="learning-nginx", detach=True, ports="8080:80")
check_all_containers(prev=False)
stop_container(name="learning-nginx")
check_all_containers(prev=True)
start_container(name="learning-nginx")
check_all_containers(prev=False)
check_container_logs(name="learning-nginx", tail=5)
exec_container(name="learning-nginx", internal=["nginx", "-v"])
inspect_container(name="learning-nginx")
check_container_stats(name="learning-nginx")
delete_container(name="learning-nginx")