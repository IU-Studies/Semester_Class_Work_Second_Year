import logging

# Configure the logger to write only to a log file
logging.basicConfig(
    level=logging.DEBUG,  # Set the minimum logging level
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='app.log',  # Log messages are written to this file
    filemode='a'         # Append mode: add logs to the end of the file
)

# Log messages at different severity levels
logging.debug("This is a DEBUG message, used for detailed diagnostic information.")
logging.info("This is an INFO message, used to confirm normal operations.")
logging.warning("This is a WARNING message, used to indicate a potential problem.")
logging.error("This is an ERROR message, used to report an issue that occurred.")
logging.critical("This is a CRITICAL message, used for serious issues requiring immediate attention.")
