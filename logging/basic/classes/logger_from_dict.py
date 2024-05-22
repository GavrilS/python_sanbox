"""
This is an example of loading logger configs from a yaml file.
"""
import logging
import logging.config
import yaml

with open('config.yml', 'r') as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)

logger = logging.getLogger(__name__)

logger.debug('This is a debug message')
