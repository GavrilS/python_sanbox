import logging


logging.basicConfig(filename='test.log', filemode='a', format='%(name)s - %(levelname)s - %(message)s')
logging.warning('This warning is going to be logged.')
