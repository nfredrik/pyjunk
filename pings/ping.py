from command import Command
import re
import datetime

#
#PING sun.com (137.254.16.113) 56(84) bytes of data.
# 64 bytes from bigip-www-legacy-sun-cms-adc.oracle.com (137.254.16.113):
# icmp_seq=1 ttl=235 time=157 ms
#
# TODO: implement different wayt to retrieve time


class Ping(object):

    def __init__(self, dest):
        self.dest = dest
        self.now = datetime.datetime.today()
        self.ptime = self.now.strftime('%Y-%m-%d %H:%M:%S')
        cmd = Command('ping -c 1 ' + dest)

        if cmd.get_status():
            print 'Failed to ping:', dest
            self.ttl = '0' 
            self.response = '0.0'
            return

        self.tnt = re.search(r"ttl=(\d*) time=(\d*.\d*)", cmd.get_string_output())
        self.ttl = self.tnt.group(1)
        self.response = self.tnt.group(2)

    def get_ttl(self):
        return self.ttl

    def get_response(self):
        return self.response

    def get_time(self):
        """
        First perhaps get the time from this machine, later on from some ntp? on net?    
        """
        return self.ptime

    # TODO: possible to solve with __repr__ or __str__?
    def get_dest(self):
        return self.dest

