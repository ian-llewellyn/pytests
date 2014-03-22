#!/bin/bash
# -*- utf-8 -*-

class Single(object):
    def __init__(self, id):
        self.id = id
        logger.debug('Creating Single instance with id: %d', self.id)

    def do_something(self):
        logger.info('Doing something')

    def do_another_thing(self):
        logger.info('Doing another thing')

def main():
    single = Single(0)
    single.do_something()
    single.do_another_thing()

if __name__ == '__main__':
    # Setupp logging
    import logging
    # file
    # level
    # format
    FILE = 'single.log'
    FORMAT = '%(asctime)s [%(process)d] [%(levelname)s]: %(message)s'
    LEVEL = logging.DEBUG

    NAME = 'single-0'

    logger = logging.getLogger(NAME)
    handler = logging.StreamHandler()
    handler.setLevel(LEVEL)
    logger.addHandler(handler)
    logger.info('info')
    logger.error('error')

    import sys, os
    main() and sys.exit(os.EX_OK)
