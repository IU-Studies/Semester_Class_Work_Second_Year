import logging

debug_logger = logging.getLogger("debug_logger")
error_logger = logging.getLogger("error_logger")

debug_logger.setLevel(logging.DEBUG)
error_logger.setLevel(logging.WARNING)

debug_file_handler = logging.FileHandler("debug.log")
error_file_handler = logging.FileHandler("error.log")

debug_file_handler.setLevel(logging.DEBUG)
error_file_handler.setLevel(logging.WARNING)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
debug_file_handler.setFormatter(formatter)
error_file_handler.setFormatter(formatter)

debug_logger.addHandler(debug_file_handler)
error_logger.addHandler(error_file_handler)

debug_logger.debug("This is a DEBUG message.")
debug_logger.info("This is an INFO message.")
error_logger.warning("This is a WARNING message.")
error_logger.error("This is an ERROR message.")
error_logger.critical("This is a CRITICAL message.")
