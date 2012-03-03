import re
from netstat import Netstat

#discard         9/tcp           sink null
#discard         9/udp           sink null

dict = {}
for line in open("/etc/services"):
    test = re.search('(^[a-zA-Z\-\_\d]+)\s*(\d+)', line)
    if test != None:
#        print test.group(1), test.group(2)
        dict[test.group(1)] = test.group(2)



#for key, value in dict.items():
#    print key, value
#    pass


users = ['-ns', '-dgm', '-ssn']
services= ['netbios']

sum =[ 'netbios'+x for x in users]


netstat = Netstat()                                                                                         
print  netstat.get_port_status(631)
print  netstat.get_port_status(50022)

exit(2)

for m in sum:
#    print dict[m],
    print netstat.get_port_status(str(dict[m]))
