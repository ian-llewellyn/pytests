#!/usr/bin/python
# -*- utf-8 -*-

class Multi(object):
    def __init__(self):
        #logger.info('Loading a Multi instance.')
        self.singles = []

    def do_this(self):
        #logger.info('Doing this.')
        pass

    def do_that(self):
        #logger.info('Doing that.')
        pass

    def load_singles(self, number):
        #logger.info('Loading singles/')
        from single import Single
        for i in range(number):
            self.singles.append(Single(i))

def main():
    multi = Multi()
    multi.do_this()
    multi.do_that()
    multi.load_singles(10)
    print len(multi.singles)
    return True

if __name__ == '__main__':
    import sys, os
    main() and sys.exit(os.EX_OK)
