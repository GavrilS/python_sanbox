import logging

# Custom logger
logger = logging.getLogger('handler_example')

# Handlers
c_handler = logging.StreamHandler()
c_handler.setLevel(logging.WARNING)

f_handler = logging.FileHandler('test.log')
f_handler.setLevel(logging.ERROR)

# Formatters to add to the handlers
c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
c_handler.setFormatter(c_format)

f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
f_handler.setFormatter(f_format)

# Add handlers to the logger
logger.addHandler(c_handler)
logger.addHandler(f_handler)

# Add logs
logger.warning('This is a warning')
logger.error('This is an error')
