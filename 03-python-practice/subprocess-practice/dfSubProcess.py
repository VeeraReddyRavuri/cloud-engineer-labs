import subprocess

try:
    result = subprocess.run(
        ["df", "-h"],
        capture_output = True,
        text = True,
        check = True,
        timeout = 10
    )
except subprocess.TimeoutExpired:
    print("Command timeout...Something is wrong")
except subprocess.CalledProcessError as e:
    print(f"Command failed: {e.stderr}")


if result and result.stdout:
    lines = result.stdout.splitlines()
    found_issue = False

    for line in lines:

        if "%" in line:
            parts = line.split()
            usage = parts[4]
            if usage == "Use%":
                continue
            mount = parts[5]
            usage_number = int(usage.replace("%", ""))

            if usage_number > 50:
                print(f"WARNING: {mount} is at {usage} - above threshold")
                found_issue = True

    if not found_issue:
        print("All drives are within limit")