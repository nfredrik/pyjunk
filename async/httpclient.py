import asyncore, socket
import logging

class HTTPClient(asyncore.dispatcher):

    def __init__(self, host, path):
        self.logger = logging.getLogger("HTTPClient")
        print '__init__'
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect( (host, 80) )
        self.buffer = 'GET %s HTTP/1.0\r\n\r\n' % path

    def handle_connect(self):
        print ('handle_connect()')
        pass

    def handle_close(self):
        print 'handle_close'
        self.close()

    def handle_read(self):
        #print 
        self.received = self.recv(8192)
        print 'handle read', len(self.received)

    def readable(self):
        print 'readable'        
        return True
    
    def writable(self):
        print 'writable:', len(self.buffer)
        return (len(self.buffer) > 0)

    def handle_write(self):
        print 'handle write'
        sent = self.send(self.buffer)
        self.buffer = self.buffer[sent:]


client = HTTPClient('www.python.org', '/')
print 'loop'
asyncore.loop()