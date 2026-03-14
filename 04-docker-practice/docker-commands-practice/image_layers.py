import subprocess
import logging

def setup_logger():
    logger = logging.getLogger(__name__)

    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )

    file_handler = logging.FileHandler("history.log")
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

logger = setup_logger()

def run_command(command, timeout=10):

    try:
        result = subprocess.run(
            command,
            capture_output = True,
            check = True,
            text = True,
            timeout = timeout
        )
        logger.info(f"=== Running command {' '.join(command)} ===")
        return result.stdout
    except subprocess.CalledProcessError as e:
        logger.error(f"Command {command} failed with error: {e.stderr}")
        return None
    except subprocess.TimeoutExpired:
        logger.error(f"Command {command} timed out")
        return None

def show_image_layers(image):

    command = ["docker", "history", image]
    output = run_command(command)
    if output:
        logger.info(f"=== Layer history of {image} ===")
        logger.info(output)

def show_image_layer_hashes(image):

    command = ["docker", "inspect", "--format={{json .RootFS.Layers}}", image]
    output = run_command(command)
    if output:
        logger.info(f"=== Layer hashes of {image} ===")
        logger.info(output)

def main():
    show_image_layers("nginx")
    show_image_layer_hashes("nginx")

if __name__ == "__main__":
    main()