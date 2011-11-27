from Packet import *
#
# TODO:
#

class Protocol(object):
    """Abstract class for all protocols"""
    def __init__(self,  dataObject):
        self.m_dataObject = dataObject
        self.m_dataObject.signalwhenReady(self.OnData)

    def OnData(self,  data,  bytes):
        raise NotImplementedError, "Implement me"

    def connectCallback(self,  callback):
         self.callback = callback

#
# Better enums than this. Possible to change constructor i a sub class and still have to abstract constructor in action?
#
class LinxProtocol(Protocol):

   INVALID = 0
   STARTTOKEN = 1
   COMMAND = 2
   LENGTH = 3
   PAYLOAD = 4
   CHKSUM = 5


   def __init__(self, dataObject):
       Protocol.__init__(self, dataObject)
#       States = self.enum( INVALID = 0, STARTTOKEN = 1,COMMAND = 2, LENGTH = 3,PAYLOAD = 4, CHKSUM = 5)
       self.states = {
                      self.INVALID    : self.invalid,
                      self.STARTESC   :self.startesc, 
                      self.ACKNOWLEDGE:self.acknowledge, 
                      self.PSTATUS    : self.pstatus, 
                      self.CSTATUS    : self.cstatus, 
                      self.COMMAND    : self.command, 
                      self.PAYLOAD    : self.payload, 
                      self.CHKSUM     : self.chksum
                     }
                   

   def enum(**enums):
        return type('Enum', (), enums)

   def ResetState(self):
         self.state = self.STARTESC
  

   def Send(self,  linxPacket):
 
         # Build a packet
         self.buffer = []
         self.buffer.append(linxPacket.getStartTokens())
         self.buffer.append(linxPacket.getCommand())

         for  data in range(linxPacket.size()):
             self.buffer.append(linxPacket.pop())    # pop first element

         self.buffer.append(linxPacket.getEndTokens())

         # Calculate checksum
         self.buffer.append( self.linxPacket.calc_checksum(self.buffer))

#         print 'sent data:', self.buffer
         self.m_dataObject.Write(self.buffer, len(self.buffer))


   def OnData(self,  data,  bytes):
        self.packet = LenkoPacket(254)
       
        for self.d in data:
#              print 'state:', self.state
              try :
                  self.states[self.state](self.d)
              except:
                  print 'we go an invalid state',  self.state
                  self.state = self.STARTTOKEN
                  
              self.checksum+= self.d

   def invalid(self, state):
        print 'invalid'

                  
   def startesc(self, d):
        if d == linxPacket.getStartTokens() :
            self.state = self.ACKNOWLEDGE
        else :
            pass # TODO: log this 

   def acknowledge(self, d):
        linxPacket.setACK(d)
        self.state = self.PSTATUS

   def pstatus(self, d):
        linxPacket.set_pstatus(d)
        self.state = self.CSTATUS

   def cstatus(self, d):
        linxPacket.set_cstatus(d)
        self.state = self.commandid


   def commandid(self, d):
        linxPacket.setCommand(d)
        self.length = linxPacket.len4Command()

        if self.length :
            self.state = self.PAYLOAD
        else:
            self.state = self.ENDESC

   def payload(self, d):
      pass
   def endesc(self, d):
      pass
   def checksum(self, d):
      pass
          
   def length(self, d):
        # Check if it's < than max packet size
        self.m_length = self.d
        self.state = self.PAYLOAD
         
   def payload(self, d):
        if self.m_length:
            self.packet.push_back(self.d)
            self.m_length = self.m_length -1

        if not self.m_length:
            self.state = self.CHKSUM
         
   def chksum(self, d ):
        # For now, compensate for incr from REQ to RESP, see above ...
        if (self.checksum & 255) == (self.d + 1):
            print 'we here now ...'
            self.callback(self.packet)
        else:
            print 'wrong checksum, expected:', (self.checksum & 255), 'got:', self.d
     
     
     
