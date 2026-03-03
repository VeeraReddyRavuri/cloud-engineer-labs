import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger("__name__")
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

rotating_handler = RotatingFileHandler(
    "rotate.log",
    maxBytes = 500,
    backupCount = 5
)

console_handler = logging.StreamHandler()

rotating_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

logger.addHandler(rotating_handler)
logger.addHandler(console_handler)

logger.info("Fetched 10 incidents from database")
logger.warning("Disk usage at 76%")
logger.error("OpenAI API call failed")