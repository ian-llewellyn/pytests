#!/bin/env python

service = '2fm'
format = 'mp2'

import logging

#logging.basicConfig(level=logging.DEBUG)

#log
#logging.debug('This is a DEBUG message')
#logging.info('This is an INFO message')
#logging.warning('This is a WARNING message')
#logging.error('This is an ERROR message')
#logging.exception('This is an EXCEPTION message')
#logging.critical('This is a CRITICAL message')
#logging.fatal('This is a FATAL message')	# This also generates a CRITICAL level msg

# Critical -> Email
# Warning -> Stderr
# Debug -> File

logger = logging.getLogger('logger')
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler('logger_test.log')
file_handler.setLevel(logging.DEBUG)
logger.addHandler(file_handler)

stderr_handler = logging.StreamHandler()
stderr_handler.setLevel(logging.WARNING)
logger.addHandler(stderr_handler)

import logging.handlers

email_handler = logging.handlers.SMTPHandler('localhost', 'af-sync-' + service + '-' + format + '@dub-lx-072', 'test@example.com', 'Log output from af-sync-single')
email_handler.setLevel(logging.CRITICAL)
logger.addHandler(email_handler)


logger.debug('This is a DEBUG message')
logger.info('This is an INFO message')
logger.warning('This is a WARNING message')
logger.error('This is an ERROR message')
logger.exception('This is an EXCEPTION message')
logger.critical('This is a CRITICAL message')
logger.fatal('This is a FATAL message')	# This also generates a CRITICAL level msg












