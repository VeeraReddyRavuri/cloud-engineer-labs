import logging

#create logger
logger = logging.getLogger("__name___")
logger.setLevel(logging.DEBUG)

#create formatter and setup formatting
formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

#create filehandler and add formatter
file_handler = logging.FileHandler("app.log")
file_handler.setFormatter(formatter)

#add a handler to print to screen
consle_handler = logging.StreamHandler()
consle_handler.setFormatter(formatter)

#add handler
logger.addHandler(file_handler)
logger.addHandler(consle_handler)

logger.info("Fetched 10 incidents from database")
logger.warning("Disk usage at 76%")
logger.error("OpenAI API call failed")