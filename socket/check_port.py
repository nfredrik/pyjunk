import socket
 
def isOpen(ip,port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((ip, int(port)))
        s.shutdown(2)
        return True
    except:
        return False

print 'sun.com is:',

if isOpen('www.sun.com', '80'):
    print 'open'
else:
    print 'closed'


print 'dn.se is:',

if isOpen('www.dn.se', '80'):
    print 'open'
else:
    print 'closed'


print 'sdmma.se is:',

if isOpen('sdmma.se', '80'):
    print 'open'
else:
    print 'closed'
