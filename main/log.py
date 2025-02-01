import logging
logging.basicConfig(
    format = "[%(asctime)s]::%(levelname)s:%(filename)s:%(message)s",
    level=logging.INFO,
    filename = 'log.log',
    filemode = 'a'
)

# Create a logger instance
logger = logging.getLogger('main_logger')