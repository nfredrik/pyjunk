#!/usr/bin/env python
#
# Simple sniffer using Scapy http://www.secdev.org/projects/scapy/
# The format string used here prints the payload as plain text.

# Example output:

#   192.168.1.137:10001 -> 192.168.1.241:2324 PA : 99dc0040,XX,YYYYYYYYYY,C89,091018,110517,091018#
#   192.168.1.241:2324 -> 192.168.1.137:10001  A :
#   192.168.1.137:10001 -> 192.168.1.241:2324 PA : 99dc0038,XX,YYYYYYYYYY,C51,091018,127,2,20,8,1#
#   192.168.1.241:2324 -> 192.168.1.137:10001  A :
#   192.168.1.241:2324 -> 192.168.1.137:10001 PA : 90dc

#
# Scapy is available as a package, python-scapy, on Debian based systems.

from scapy.all import *

FMT_STRING = "%IP.src%:%TCP.sport% -> %IP.dst%:%TCP.dport% %2s,TCP.flags% : %TCP.payload%"


sniff(filter="tcp", store=0,
      prn = lambda x: x.sprintf(FMT_STRING))
