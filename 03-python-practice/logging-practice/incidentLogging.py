import logging
import json
from logging.handlers import RotatingFileHandler

def setup_logger(name, log_file = "app.log", level=logging.INFO):

    logger = logging.getLogger(name)
    logger.setLevel(level)
    
    class JSONFormatter(logging.Formatter):
        def format(self, record):
            log_entry = {
                "timestamp": self.formatTime(record),
                "level": record.levelname,
                "module": record.name,
                "message": record.getMessage()
            }
            return json.dumps(log_entry)
    
    json_formatter = JSONFormatter()

    plain_formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s- %(name)s - %(message)s"
    )

    file_handler = RotatingFileHandler(
        log_file,
        maxBytes = 500,
        backupCount = 5
    )

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(plain_formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

logger = setup_logger("__name__")

logger.debug("Connecting to database")
logger.info("Successfully fetched 10 incidents")
logger.warning("Disk usage approaching threshold")
logger.error("OpenAI API call failed")
logger.critical("Database connection lost")