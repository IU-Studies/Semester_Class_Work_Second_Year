import logging

# Define a custom filter class
class KeywordFilter(logging.Filter):
    def __init__(self, keyword):
        self.keyword = keyword

    def filter(self, record):
        # Only allow log messages that contain the specified keyword in the message
        return self.keyword in record.getMessage()

# Configure the logger
logger = logging.getLogger("custom_logger")
logger.setLevel(logging.DEBUG)

# Create a console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# Create the custom filter and add it to the handler
keyword_filter = KeywordFilter("ERROR")  # Only allow messages containing the keyword "ERROR"
console_handler.addFilter(keyword_filter)

# Create a formatter
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(console_handler)

# Example usage
logger.debug("This is a debug message.")
logger.info("This is an info message.")
logger.warning("This is a warning message.")
logger.error("This is an error message.")
logger.critical("This is a critical message.")
