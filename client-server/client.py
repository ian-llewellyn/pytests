#!/bin/python
# -*- coding: utf-8 -*-
# CLIENT

host = '127.0.0.1'
port = 1234

import socket, sys, os

c = socket.socket()

address = (host, port)
c.connect(address)

c.send(sys.argv[1])

print "Server response:\n%s" % c.recv(1024)

c.shutdown(socket.SHUT_RDWR)

c.close()

import time

#time.sleep(10)
