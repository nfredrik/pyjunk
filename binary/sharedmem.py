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
            return 0
        

    
    def read(self):
        return self.read_chunk()
    
    
class Packet(object):
    def __init__(self,buffer):
        self.sourceAddress = struct.unpack_from('B', buffer,0),struct.unpack_from('B', buffer,1),struct.unpack_from('B', buffer,2),struct.unpack_from('B', buffer,3)
        self.destinationAddress = struct.unpack_from('B', buffer,4),struct.unpack_from('B', buffer,5),struct.unpack_from('B', buffer,6),struct.unpack_from('B', buffer,7)
        self.sourcePort = struct.unpack_from('B', buffer,8),struct.unpack_from('B', buffer,9)
        self.destinationPort = struct.unpack_from('B', buffer,10),struct.unpack_from('B', buffer,11)
        self.protocolUsed = struct.unpack_from('B', buffer,12),struct.unpack_from('B', buffer,13)
        self.timeStamp = struct.unpack_from('B', buffer,14),struct.unpack_from('B', buffer,15),struct.unpack_from('B', buffer,16),struct.unpack_from('B', buffer,17)
        
    
    def get_from_ip(self):
        return self.sourceAddress
    
    def get_to_ip(self):
        return self.destinationAddress
    
def main(argv):
    
    print 'Started'
    sharedmem = SharedMem('./devmem')
    
    packets = []
    for i in range(0,56):
        
        print 'Im in....'
        bytes = sharedmem.read()
        
        print 'bytes:', len(bytes)
        
        if len(bytes):
            packet = Packet(bytes)
            packets.append(packet)
        else:
            break
        
    print 'Start printing'        
    for p in packets:
        print 'Looping'
        print p.get_from_ip()    
    
if __name__ == '__main__':
    
  sys.exit(main(sys.argv[1:]))      