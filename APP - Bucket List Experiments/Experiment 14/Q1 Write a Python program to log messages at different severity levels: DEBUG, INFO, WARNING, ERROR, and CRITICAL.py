#Write a Python program to log messages at different severity levels: DEBUG, INFO, WARNING, ERROR, and CRITICAL.

import logging

logging.basicConfig(
    level=logging.DEBUG,  
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("app.log"),  
        logging.StreamHandler()        
    ]
)

logging.debug("This is a DEBUG message, used for detailed diagnostic information.")
logging.info("This is an INFO message, used to confirm normal operations.")
logging.warning("This is a WARNING message, used to indicate a potential problem.")
logging.error("This is an ERROR message, used to report an issue that occurred.")
logging.critical("This is a CRITICAL message, used for serious issues requiring immediate attention.")
