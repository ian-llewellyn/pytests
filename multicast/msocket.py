# -*- coding: utf-8 -*-
"""
Multicast Swiss Army Knife
"""
DEFAULT_GROUP_4 = '233.1.2.3'
DEFAULT_GROUP_6 = 'ff15:7079:7468:6f6e:6465:6d6f:6d63:6173'
DEFAULT_PORT = 8150
DEFAULT_TTL = 1

import struct
import socket

class msocket(object):
    """
    Creates a multicast datagram socket that can be read from
    or written to using recvfrom() and sendto() respectively.
    """

    def __init__(self, sender=False, group=DEFAULT_GROUP_4, port=DEFAULT_PORT,
                 ttl=DEFAULT_TTL):

        # Look up multicast group address in name server and find out IP version
        addrinfo = socket.getaddrinfo(group, None)[0]
        # (2, 1, 6, '', ('233.1.2.3', 0))

        self.family = addrinfo[0]
        self.dst_group = addrinfo[4][0]
        self.port = port

        self._sock = socket.socket(self.family, socket.SOCK_DGRAM)

        if sender:
            # Set Time-to-live (optional)
            ttl_bin = struct.pack('@i', ttl)
            # '\x01\x00\x00\x00'
            if self.family == socket.AF_INET:
                # IPv4
                self._sock.setsockopt(socket.IPPROTO_IP,
                                      socket.IP_MULTICAST_TTL, ttl_bin)
            else:
                # IPv6
                self._sock.setsockopt(socket.IPPROTO_IPV6,
                                      socket.IPV6_MULTICAST_HOPS, ttl_bin)

        else:
            # Allow multiple copies of this program on one machine
            # (not strictly needed)
            self._sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

            # Bind it to the port
            self._sock.bind(('', port))

            group_bin = socket.inet_pton(self.family, self.dst_group)
            # Join group
            if self.family == socket.AF_INET:
                # IPv4
                mreq = group_bin + struct.pack('=I', socket.INADDR_ANY)
                self._sock.setsockopt(socket.IPPROTO_IP,
                                      socket.IP_ADD_MEMBERSHIP, mreq)
            else:
                # IPv6
                mreq = group_bin + struct.pack('@I', 0)
                self._sock.setsockopt(socket.IPPROTO_IPV6,
                                      socket.IPV6_JOIN_GROUP, mreq)

    def sendto(self, *args):
        if len(args) != 1:
            return self._sock.sendto(*args)
        return self._sock.sendto(args[0], (self.dst_group, self.port))

    def __getattr__(self, attr):
        return getattr(self._sock, attr)

if __name__ == '__main__':
    import time
    import sys

    group = DEFAULT_GROUP_6 if "-6" in sys.argv[1:] else DEFAULT_GROUP_4

    if "-s" in sys.argv[1:]:
        s = msocket(sender=True, group=group)

        addrinfo = socket.getaddrinfo(group, None)[0]

        while True:
            data = repr(time.time())
            s.sendto(data + '\0')
            #s.sendto(data + '\0', (addrinfo[4][0], DEFAULT_PORT))
            time.sleep(1)

    else:
        s = msocket(group=group)

        # Loop, printing any data we receive
        while True:
            data, sender = s.recvfrom(1500)
            while data[-1:] == '\0': data = data[:-1] # Strip trailing \0's
            print (str(sender) + '  ' + repr(data))
