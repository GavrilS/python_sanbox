"""
In this example the logger config is loaded from the file 'config.ini'.
"""
import logging
import logging.config

logging.config.fileConfig(fname='config.ini', disable_existing_loggers=False)

logger = logging.getLogger(__name__)

logger.debug('This is a debug')
logger.warning('This is a warning')
