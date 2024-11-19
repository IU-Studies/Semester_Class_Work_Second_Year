import logging

# Create loggers
debug_logger = logging.getLogger("debug_logger")
error_logger = logging.getLogger("error_logger")

# Set log levels for the loggers
debug_logger.setLevel(logging.DEBUG)
error_logger.setLevel(logging.WARNING)

# Create file handlers for each logger
debug_file_handler = logging.FileHandler("debug.log")
error_file_handler = logging.FileHandler("error.log")

# Set levels for the handlers
debug_file_handler.setLevel(logging.DEBUG)
error_file_handler.setLevel(logging.WARNING)

# Create formatters and add them to the handlers
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
debug_file_handler.setFormatter(formatter)
error_file_handler.setFormatter(formatter)

# Add handlers to the loggers
debug_logger.addHandler(debug_file_handler)
error_logger.addHandler(error_file_handler)

# Log messages
debug_logger.debug("This is a DEBUG message.")
debug_logger.info("This is an INFO message.")
error_logger.warning("This is a WARNING message.")
error_logger.error("This is an ERROR message.")
error_logger.critical("This is a CRITICAL message.")
