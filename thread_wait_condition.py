# -*- coding: utf-8 -*-

import threading

from time import sleep

class A(object):
    def __init__(self):
        self.cv = threading.Condition()
        self.flag = False

    def flag_state(self):
        return self.flag

    def thread(self):
        i = 1
        while threading.main_thread().is_alive():
            print('.', end='', flush=True)
            sleep(1)
            if i%5 == 0:
                with self.cv:
                    self.flag = True
                    self.cv.notify()
            if i%5 == 1:
                self.flag = False
            i += 1

    def ds(self):
        threading.Thread(target=self.thread).start()
        with self.cv:
            while not self.flag_state():
                print(':', end='', flush=True)
                self.cv.wait()
            print('BANG')

if __name__ == '__main__':
    a = A()
    a.ds()
