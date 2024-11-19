#Implement a custom log filter that only allows messages from specific modules or messages containing certain keywords to be logged

import logging

class KeywordFilter(logging.Filter):
    def __init__(self, keyword):
        self.keyword = keyword

    def filter(self, record):
        return self.keyword in record.getMessage()

logger = logging.getLogger("custom_logger")
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

keyword_filter = KeywordFilter("ERROR")  
console_handler.addFilter(keyword_filter)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)

logger.addHandler(console_handler)

logger.debug("This is a debug message.")
logger.info("This is an info message.")
logger.warning("This is a warning message.")
logger.error("This is an error message.")
logger.critical("This is a critical message.")
