#!/bin/python
# -*- coding: utf-8 -*-
# SERVER

host = '127.0.0.1'
host = ''
port = 1234

import socket, sys, os, pdb

pdb.set_trace()

s = socket.socket()

address = (host, port)
s.bind(address)

s.listen(0)

while True:
    c, c_address = s.accept()
    c_host, c_port = c_address
    print "Accepted connection from %s:%d" % (c_host, c_port)

    data = c.recv(1024)

    print "Received:\n%s" % data

    c.send("Received %d bytes" % len(data))

#    c.shutdown(socket.SHUT_RDWR)

#    c.close()
