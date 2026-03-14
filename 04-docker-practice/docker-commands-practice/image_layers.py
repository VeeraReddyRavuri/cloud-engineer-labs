import subprocess
import logging
from docker_commands_practice.run_containers import run_command

"""
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
        print(f"Command {command} failed with error: {e.stderr}")
        return None
    except subprocess.TimeoutExpired:
        print(f"Command {command} timed out")
        return None
"""

def show_image_layers(image):
    command = ["docker", "history", image]
    output = run_command(command)
    if output:
        print(f"=== Layer history of {image} ===")
        print(output)

def show_image_layer_hashes(image):
    command = ["docker", "inspect", "--format={{json .RootFS.Layers}}", image]
    output = run_command(command)
    if output:
        print(f"=== Layer hashes of {image} ===")
        print(output)

show_image_layers("nginx")
show_image_layer_hashes("nginx")