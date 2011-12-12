#
# TODO: push_pack, add control for size of vector  if self.maxPacketsize < len(m_Vector) : ...
#
from Protocol import *

class Packet(object):
    """ Abstract class for packets"""
    def __init__(self,  maxPacketSize):
        self.m_maxPacketsize =  maxPacketSize
        self.m_Vector = []

    def pop(self):
        if self.size() == 0:
            raise NameError
            
        return self.m_Vector.pop(0) # pop first element. Default last element

    def push_back(self, byte):
        if self.size() > self.m_maxPacketsize:
            raise NameError
            
        self.m_Vector.append(byte)

    def size(self):
         return len(self.m_Vector)

class LinxPacket(Packet):
    """ Packet specified by Linx
          Special printer protocol implemented by Linx
     """
    # Commands/Requests and Replies/Responses
    PRINT_STATUS_REQUEST  = 0x14
    DOWNLOAD_MESSAGE_DATA = 25
    PRINT_MESSAGE         = 30
    REQUEST_DATA_DIRECTORY = 0x61
    ESC = 0x1b
#    def __init__(self):
#        Packet(254)

    def setCommand(self,  command):
        self.m_Command = command

    def  getCommand(self):
       return self.m_Command

    def getStartTokens(self):
       return 0x1b02     # ESC STX

    def getEndTokens(self):
       return 0x1b03     # ESC STX

    def checksumold(self, buffer):
       sum = 0
       for i in buffer:
           sum = sum + i
       print 'first:' , sum
       sum = sum & 0xff
       print 'second:' , sum
       return (0x100 - sum)

    def calc_checksum(self, buffer):
       sum = 0
       for i in buffer:
           sum = sum + i
       return ((~sum & 0xff) + 1)
 
    def add_esc(self, buffer):

       destbuf = []
       for i in buffer:
           if i == ESC:
               destbuf.append(ESC)
               continue
           destbuf.append(i)

       return destbuf
    def strip_esc(self, buffer):
       destbuf = []
       for i in buffer:
           if i == ESC:
               self.escmode = True
               continue
           
           if self.escmode :
              if i in range(0, 0x1f):
                  continue
              else:
                  self.escmode = False

           destbuf.append(i)

       return destbuf

class LinxPacketResponse(LinxPacket):

    def getStartTokens(self):
       return 0x1b06     # ESC ACK

    def getEndTokens(self):
       return 0x1b15     # ESC NAK


