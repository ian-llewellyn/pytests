#!/bin/env python

import logging

logging.basicConfig(filename='app.log')

error = logging.error
exception = logging.exception

error('abc')

try:
    raise Exception('problem')
except:
    exception('there was some failure')
    raise
