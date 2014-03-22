#!/usr/bin/python
# -*- coding: utf-8 -*-
import time, socket

port = 8171

for message in ['message1', 'message2', 'message3', 'message4']:
    sock = socket.socket()
    sock.connect(('localhost', port))

    sock.send(message)
    #sock.shutdown(socket.SHUT_WR)

    print sock.recv(1024)
    #sock.shutdown(socket.SHUT_RD)

    #sock.close()

    time.sleep(2)
#sock.send('')
