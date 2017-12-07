# -*- coding: utf-8 -*-

import threading

from time import sleep

class A(object):
    def __init__(self):
        self.ev = threading.Event()
        self.flag = False

    def flag_state(self):
        return self.flag

    def thread(self):
        i = 1
        while threading.main_thread().is_alive():
            print('.', end='', flush=True)
            sleep(1)
            if i%5 == 0:
                self.flag = True
                self.ev.set()
            if i%5 == 1:
                self.flag = False
            i += 1

    def ds(self):
        threading.Thread(target=self.thread).start()
        while not self.flag_state():
            print(':', end='', flush=True)
            self.ev.clear()
            self.ev.wait()
        print('BANG')

if __name__ == '__main__':
    a = A()
    a.ds()
