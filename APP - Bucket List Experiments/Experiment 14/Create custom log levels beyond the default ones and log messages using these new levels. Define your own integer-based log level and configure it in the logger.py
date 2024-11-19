#Create custom log levels beyond the default ones and log messages using these new levels. 
#Define your own integer-based log level and configure it in the logger

import logging

VERBOSE_LEVEL = 15
logging.addLevelName(VERBOSE_LEVEL, "VERBOSE")

def verbose(self, message, *args, **kwargs):
    if self.isEnabledFor(VERBOSE_LEVEL):
        self._log(VERBOSE_LEVEL, message, args, **kwargs)

logging.Logger.verbose = verbose

logging.basicConfig(
    level=logging.DEBUG, 
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='custom_levels.log',
    filemode='a'
)

logger = logging.getLogger()

logger.debug("This is a DEBUG message.")
logger.info("This is an INFO message.")
logger.verbose("This is a VERBOSE message for detailed logging.")
logger.warning("This is a WARNING message.")
logger.error("This is an ERROR message.")
logger.critical("This is a CRITICAL message.")
