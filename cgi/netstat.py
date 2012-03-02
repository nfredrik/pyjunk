from command import Command
import re
"""
Module to handle netstatcommand
"""


class Netstat(Command):
    """
    Execute netstat command.
    """
    def __init__(self):

        Command.__init__(self, 'netstat -a --numeric-ports')


#tcp        0      0 127.0.0.1:631           0.0.0.0:*               LISTEN
#tcp        0      0 0.0.0.0:17500           0.0.0.0:*               LISTEN 

    def get_port_status(self, portno):
        """
        Get status of port.
        """
        self.get_port_status = self.get_string_output()
#        print self.get_port_status
#        self.result = re.search('\d.\d.\d.\d\:' + str(portno) + '*([\w\d]*)' , self.get_port_status)
        self.result = re.search(r"\d*.\d*.\d*.\d*\:" + str(portno) + "\s*\d*.\d*.\d*.\d*\:\*\s*(\w*)" , self.get_port_status)
#        print self.result.group(1)
        if self.result != None:
            return self.result.group(1)
        return 'Not present'

#        self.tnt = re.search(r"ttl=(\d*) time=(\d*.\d*)", cmd.get_string_output())
 #       self.ttl = self.tnt.group(1)
 #       self.response = self.tnt.group(2)
