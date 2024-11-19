import logging

# Define a custom log level
VERBOSE_LEVEL = 15  # Must be between DEBUG (10) and INFO (20)
logging.addLevelName(VERBOSE_LEVEL, "VERBOSE")

# Create a custom logging function
def verbose(self, message, *args, **kwargs):
    if self.isEnabledFor(VERBOSE_LEVEL):
        self._log(VERBOSE_LEVEL, message, args, **kwargs)

# Add the custom log level to the Logger class
logging.Logger.verbose = verbose

# Configure the logger
logging.basicConfig(
    level=logging.DEBUG,  # Allow all log levels from DEBUG upwards
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='custom_levels.log',
    filemode='a'
)

# Get the logger
logger = logging.getLogger()

# Log messages with various levels, including the custom one
logger.debug("This is a DEBUG message.")
logger.info("This is an INFO message.")
logger.verbose("This is a VERBOSE message for detailed logging.")
logger.warning("This is a WARNING message.")
logger.error("This is an ERROR message.")
logger.critical("This is a CRITICAL message.")
