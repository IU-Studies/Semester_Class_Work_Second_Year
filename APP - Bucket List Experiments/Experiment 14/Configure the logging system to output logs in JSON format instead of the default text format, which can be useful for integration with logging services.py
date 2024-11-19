import logging
import json

class JsonFormatter(logging.Formatter):
    def format(self, record):
        log_record = {
            "timestamp": self.formatTime(record, self.datefmt),
            "level": record.levelname,
            "message": record.getMessage(),
            "name": record.name,
            "filename": record.filename,
            "line": record.lineno,
        }
        return json.dumps(log_record)

logger = logging.getLogger("json_logger")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("logs.json")
file_handler.setLevel(logging.DEBUG)

json_formatter = JsonFormatter()
file_handler.setFormatter(json_formatter)

logger.addHandler(file_handler)

logger.debug("This is a DEBUG message.")
logger.info("This is an INFO message.")
logger.warning("This is a WARNING message.")
logger.error("This is an ERROR message.")
logger.critical("This is a CRITICAL message.")
