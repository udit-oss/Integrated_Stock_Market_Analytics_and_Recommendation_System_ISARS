import logging
import sys
from logging.handlers import RotatingFileHandler

logger = logging.getLogger("isars")
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

file_handler = RotatingFileHandler(
    filename="logs/isars.log",
    maxBytes=5 * 1024 * 1024,  # 5 MB
    backupCount=3
)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

def get_logger() -> logging.Logger:
    """
    Returns the configured 'isars' logger.
    Use this in modules via:
        from isars_commons.src.audit.loggerUtils import get_logger
        logger = get_logger()
    """
    return logger
