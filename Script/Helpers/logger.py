import logging
from logging.handlers import RotatingFileHandler

def setup_logger():
    logger = logging.getLogger('my_logger')  # Create a logger
    logger.setLevel(logging.DEBUG)  # Set the logging level

    # Create a console handler for outputting to console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    # Create a rotating file handler for logging to a file with size limit
    file_handler = RotatingFileHandler('app.log', maxBytes=10 * 1024 * 1024, backupCount=3)
    file_handler.setLevel(logging.DEBUG)

    # Create a formatter and set it for both handlers
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    # Add the handlers to the logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger
