import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='context.log',
    filemode='a'
)

class LoggingContextManager:
    def __init__(self, logger):
        self.logger = logger

    def __enter__(self):
        self.logger.info("Entering the context.")
        return self.logger

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            self.logger.exception("An exception occurred.")
        self.logger.info("Exiting the context.")
        return False

with LoggingContextManager(logging.getLogger()) as logger:
    logger.debug("Performing some operations.")
    logger.info("This is an INFO message inside the context.")
    result = 10 / 0  
    logger.info("This message will not be logged due to the exception.")
