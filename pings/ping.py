from command import Command
import re
import time

#
#PING sun.com (137.254.16.113) 56(84) bytes of data.
# 64 bytes from bigip-www-legacy-sun-cms-adc.oracle.com (137.254.16.113): icmp_seq=1 ttl=235 time=157 ms
#
#
class Ping(object):

    def __init__(self, dest):
        self.ptime = time.ctime()
        cmd = Command('ping -c 1 ' + dest)
        if cmd.get_status():
            print 'Failed to ping:', dest
            self.ttl = self.reponse = 0
            return

#        print cmd.get_string_output()
        self.m = re.search(r".* ttl=(\d*) time=(\d*) .*",cmd.get_string_output())
        self.ttl = self.m.group(1)
        self.response = self.m.group(2)
    def get_ttl(self):
        return self.ttl

    def get_response(self):
        return self.response

    def get_time(self):
        """
        First perhaps get the time from this machine, later on from some ntp? on net?    
        """
        return self.ptime
