import logging

a = 5
b = 0

try:
    c = a/b

except Exception as e:
    # logging.error('Exception occurred', exc_info=True) # One way to log the stack trace
    logging.exception('Exception occured') # The same information; log lever error; only from exception handler
