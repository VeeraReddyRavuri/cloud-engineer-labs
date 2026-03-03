import logging
import json

class JsonFormatter(logging.Formatter):
    def format(self, record):
        log_entry = {
            "timestamp": self.formatTime(record),
            "level": record.levelname,
            "module": record.name,
            "message": record.getMessage()
        }
        return json.dumps(log_entry)

logger = logging.getLogger("__name___")
logger.setLevel(logging.DEBUG)

json_formatter = JsonFormatter()
file_handler = logging.FileHandler("appJson.log")
file_handler.setFormatter(json_formatter)
console_handler = logging.StreamHandler()
console_handler.setFormatter(json_formatter)
logger.addHandler(file_handler)
logger.addHandler(console_handler)

logger.info("Fetched 10 incidents from database")
logger.warning("Disk usage at 76%")
logger.error("OpenAI API call failed")
