import unittest
import struct

class ParseBinary(unittest.TestCase):

    filename = "devmem"

    def setUp(self):
        pass
    
    def RFOpen(self, fileName, mode):
        '''Open filename in mode
        '''
        try:
            rffd = open(fileName, mode)
            return rffd
        except IOError:
            print "error %s opening %s" % (IOError, fileName)
    
    def RFReadBytes(self, rffd, noBytes):
        '''
        Read the bytes
        '''
        byte = rffd.read(noBytes)
        return byte
    
    def tearDown(self):
        '''
        Destructor code
        '''
        pass

      
    def testMemFileParseDemo(self):
        '''
        Demo to parse the mem file with 56 records each of length 18 
        '''
        fd = self.RFOpen(self.filename, "rb")
        
        i = 0
        for element in range (0,56):
        #loop 18 since we know the file size and the record length: 1024/18 = 56 records 
        
            buffer = self.RFReadBytes(fd, 18)
            self.assertEqual(len(buffer), struct.calcsize('llh'))
            
            # use of unpack
            sourceAddress = struct.unpack_from('B', buffer,0),struct.unpack_from('B', buffer,1),struct.unpack_from('B', buffer,2),struct.unpack_from('B', buffer,3)
            destinationAddress = struct.unpack_from('B', buffer,4),struct.unpack_from('B', buffer,5),struct.unpack_from('B', buffer,6),struct.unpack_from('B', buffer,7)
            sourcePort = struct.unpack_from('B', buffer,8),struct.unpack_from('B', buffer,9)
            destinationPort = struct.unpack_from('B', buffer,10),struct.unpack_from('B', buffer,11)
            protocolUsed = struct.unpack_from('B', buffer,12),struct.unpack_from('B', buffer,13)
            timeStamp = struct.unpack_from('B', buffer,14),struct.unpack_from('B', buffer,15),struct.unpack_from('B', buffer,16),struct.unpack_from('B', buffer,17)
            
            # redundant step in assign and print can be avoided , has been used ONLY to depict the sample
            i=i+1
            print i
            #printing in expected format
            print "sourceAddress = " ,  (struct.unpack_from('B', buffer,0),struct.unpack_from('B', buffer,1),struct.unpack_from('B', buffer,2),struct.unpack_from('B', buffer,3))
            print "destinationAddress = " , (struct.unpack_from('B', buffer,4),struct.unpack_from('B', buffer,5),struct.unpack_from('B', buffer,6),struct.unpack_from('B', buffer,7))
            print "sourcePort = " , (struct.unpack_from('H',buffer,8))
            print "destinationPort = " , (struct.unpack_from('H',buffer,10))
            print "protocolUsed = " , (struct.unpack_from('H',buffer,12))
            print "timeStamp = " ,  (struct.unpack_from('B', buffer,14),struct.unpack_from('B', buffer,15),struct.unpack_from('B', buffer,16),struct.unpack_from('B', buffer,17))


if __name__ == "__main__":
     unittest.main()