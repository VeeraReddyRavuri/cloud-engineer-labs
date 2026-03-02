import subprocess

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
        print(f"Command {' '.join(command)} failed: {e.stderr}")
        return None
    except subprocess.TimeoutExpired:
        print(f"Command {' '.join(command)} timed out")
        return None

def check_disk():
    output = run_command(["df", "-h"])
    if output:
        print("======Disk Usage======")
        print(output)

def check_service(service_name):
    output = run_command(["systemctl", "status", service_name])
    if output:
        print(f"======={service_name} Status======")
        print(output)

def check_logs(service_name):
    output = run_command(["journalctl", "-u", service_name, "--since", "1 hour ago"])
    if output:
        print(f"======={service_name} Logs======")
        print(output)

check_disk()
check_service("nginx")
check_logs("nginx")