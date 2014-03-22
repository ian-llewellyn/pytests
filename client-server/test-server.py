#!/usr/bin/python
# -*- coding: utf-8 -*-

def strrev(message):
    output = ''
    for character in reversed(message):
        output += character
    return output

import socket

sock = socket.socket()
host = socket.gethostname()
port = 8171

sock.bind((host, port))
print 'Bound'
sock.listen(0)

while True:
    print 'Awaiting connection'
    connection, address = sock.accept()
    print 'Accepted a connection'

    while True:
        data = connection.recv(1024)
        if len(data) == 0:
            break
        print 'Received:', data
        print 'Sending:', strrev(data)
        connection.send(strrev(data))

# Shutdown the connection to the client
connection.shutdown(socket.RDWR)

# Close the connection to the client
connection.close()

# Close the bound listening connection
sock.close()
