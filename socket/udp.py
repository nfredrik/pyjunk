#!/usr/bin/env python
from socket import socket, AF_INET, SOCK_DGRAM, SOL_SOCKET, SO_BROADCAST, timeout
import sys

def usage_and_exit(progname):
    sys.stderr.write("""USAGE: %s host port

Simple test program for talking to a Hella passenger counter over
IBISoIP. It tries all the available request types and addresses using
unicast or broadcast if host is set to 255.255.255.255.

The counter defaults to 192.168.100.10 and 10076.
    """ % progname)
    sys.stderr.flush()
    sys.exit(1)

ADDRESSES = range(0x31, 0x3F)
COMMANDS = ['E', # Request "Call result"
            'F', # Request "Vehicle is in motion"
            'M', # Request "Carry out passenger counting"
            'T', # Request "Initiate passenger counting"
            'S', # Request "Call unit status"
            'V', # Request "Call Firmware version"
            'O', # Request "Call diagnosis-status"
            'D', # Request "Call status of digital inputs"
            'W', # Request "Call door status"
            'A', # Request "switch-off command"
            ]

if __name__ == '__main__':

    if len(sys.argv) != 3:
        usage_and_exit(sys.argv[0])

    host = sys.argv[1]
    port = int(sys.argv[2])

    udp = socket(AF_INET, SOCK_DGRAM)
    udp.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
    udp.settimeout(2)

    for c in COMMANDS:
        for i in ADDRESSES:
            data = 'VDV2b%c%c' % (c, i)
            print data + ' ',
            try:
                udp.sendto(data, (host, port))
                buf = []
                (buf, addr) = udp.recvfrom(1024)
                print 'Response: %s' % buf
            except timeout:
                print 'timed out'

