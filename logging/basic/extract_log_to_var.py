"""
This is an example of extracting a log into a local variable.
"""
import logging
import io

# Create the logger
logger = logging.getLogger('sample_logger')
logger.setLevel(logging.DEBUG)

# Set handler with a StringIO object
log_string = io.StringIO()
handler = logging.StreamHandler(log_string)
handler.setLevel(logging.DEBUG)

# Set formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)


# Send logs
logger.debug('Debug message')
logger.info('Info message')
logger.warning('Warning message')
logger.error('Error message')
logger.critical('Critical message')

# Pull the contents back into a string and close the stram
log_contents = log_string.getvalue()
log_string.close()

print('----------------------')
print(log_contents.upper())
print(log_contents.lower())
