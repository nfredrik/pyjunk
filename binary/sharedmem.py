#
#  Class that takes a binary file and reads 18 binary bytes when asked until EOF   
#
#
#  Class that takes a 18 bytes binary buffer. Have a number of getters to get src, dst, port number etc
#  in ASCII. No check that data is valid
#
import sys
import struct


class SharedMem(object):
    def __init__(self, file):
        
        try:
            self.fh = open( file, 'rb')
        
        except IOError:
            print "error %s opening %s" % (IOError, fileName)
            
    def read_chunk(self):
        
        try:
            return self.fh.read(18)
        except:
            return ''
        

    
    def read(self):
        return self.read_chunk()
    
    
class Packet(object):
    def __init__(self,buffer):
       
        self.sourceAddress = self.destinationAddress = self.sourcePort =  self.destinationPort = self.protocolUsed =  self.timeStamp =''
        
        for i in range(3):
            self.sourceAddress+= self._get_byte(buffer, i) + '.'
        self.sourceAddress+=self._get_byte(buffer, 3)
        
        for i in range(4,7):
            self.destinationAddress+= self._get_byte(buffer, i) + '.'
        self.destinationAddress+= self._get_byte(buffer, 7)
        
        #self.destinationAddress = struct.unpack_from('B', buffer,4),struct.unpack_from('B', buffer,5),struct.unpack_from('B', buffer,6),struct.unpack_from('B', buffer,7)
        #self.sourcePort = struct.unpack_from('B', buffer,8),struct.unpack_from('B', buffer,9)
        
        self.sourcePort+= self._get_byte(buffer, 8)
        self.sourcePort+= self._get_byte(buffer, 9)
        
        #self.destinationPort = struct.unpack_from('B', buffer,10),struct.unpack_from('B', buffer,11)
        self.destinationPort+= self._get_byte(buffer,10)
        self.destinationPort+= self._get_byte(buffer,11)
        
        #self.protocolUsed = struct.unpack_from('B', buffer,12),struct.unpack_from('B', buffer,13)
        self.protocolUsed+= self._get_byte(buffer,12)
        self.protocolUsed+= self._get_byte(buffer,13)
        
        #self.timeStamp = struct.unpack_from('B', buffer,14),struct.unpack_from('B', buffer,15),struct.unpack_from('B', buffer,16),struct.unpack_from('B', buffer,17)
        for i in range(14,17):
            self.timeStamp+= self._get_byte(buffer, i) + ':'
        self.timeStamp+= self._get_byte(buffer, 17)
                
        
    def _get_byte(self, bits, offset):
        """
        Turn from binary to integer and than string
        """
        return str(struct.unpack_from('B', bits, offset)[0])
    
    def get_from_ip(self):
        return self.sourceAddress
    
    def get_to_ip(self):
        return self.destinationAddress
    
    def get_src_port(self):
        return self.sourcePort
    
    def get_dest_port(self):
        return self.destinationPort
    
    def get_protocol_used(self):
        return self.protocolUsed
    
    def get_timestamp(self):
        return self.timeStamp
    
def main(argv):
    
    print 'Started'
    sharedmem = SharedMem('./devmem')
    
    packets = []
    for i in range(0,57):
        
        bytes = sharedmem.read()
        
        if len(bytes):
            packet = Packet(bytes)
            packets.append(packet)
        else:
            break
        
    print 'Start printing'       
    cntr = 0 
    for p in packets:
        print '==== Packet #', cntr, '===='
        print 'to ip:', p.get_from_ip()    
        print 'from ip:', p.get_to_ip()
        print 'src port', p.get_src_port()
        print 'dest port', p.get_dest_port()
        print 'protocol used', p.get_protocol_used()
        print 'timestamp', p.get_timestamp()
        cntr+=1
if __name__ == '__main__':
    
  sys.exit(main(sys.argv[1:]))      