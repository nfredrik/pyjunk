
import struct
import binascii

import threading
import serial

## http://www.doughellmann.com/PyMOTW/struct/index.html#module-struct


class Packet(object):
    """ Abstract class for packets"""
    def __init__(self,  maxPacketSize):
        self.m_maxPacketsize =  maxPacketSize
        self.m_Vector = []
        
    def AddByte(self,  byte):
        self.m_Vector.append(byte)
        
    def GetByte(self):
         self.m_Vector;
         
    def setChkSum(self,  sum):    
         pass 
         
         
    def size(self):    
         return 3
         
class LenkoPacket(Packet):
    """ Packet layout, all fields one byte
          | start token  == '#' | addr | command | errorcode | length | payload | chksum | """
    # Commands/Requests and Replies/Responses
    STARTPRODUCE_REQ = 1
    STARTPRODUCE_RESP = 2
    STOPPRODUCE_REQ   = 3
    STOPPRODUCE_RESP   = 4
    
    ADDR = 18
    
    def __init__(self):
        Packet(254)
        
    def setCommand(self,  command):
        self.m_Command = command
   
    def  getCommand(self):
       return self.m_Command
       

class LenkoPacketResponse(Packet):
        """ Packet layout, all fields one byte. Header fixed to 5 bytes. length comprises
              payload and checksum
          | start token  == '%' | addr | response | errorcode | length | payload | chksum | """
    
 
class DataObject(object):
    """Base class for Data Objects"""
    def __init(self):     
       pass
         
    def  Write(self, buf,  bytes):
         pass
         
    def  signalwhenReady(self,  callback):
         self.callback = callback    
         
       
       
class SerialWrapper(DataObject,  threading.Thread):
     def __init__(self):
         print "Runngin constructor in SerialWrapper"
         threading.Thread.__init__(self)
         self.m_fh = serial.Serial('/dev/pts/3', 38400)
         try:
            self.m_fh.open()
         except serial.SerialException, e:
            sys.stderr.write("Could not open serial port %s: %s\n" % (ser.portstr, e))
            sys.exit(1)
            
     def Write(self,  buf,  bytes):
         pass
         # self.m_fh.write(buf)
            
     
     def run(self):
         print "we reached run hurra!"
         return
         while True:
            data = self.serial.read(1)              # read one, blocking
            n = self.serial.inWaiting()             # look if there is more
            if n:
                data = data + self.serial.read(n)   # and get as much as possible
                
         self.callback(data,  n+1)        
             
class LoopDataObject(DataObject):
 
     def  Write(self, buf,  bytes):
        self.buffer = []
        for d in buf:
            self.buffer.append(d)
            
        self.callback(self.buffer,  bytes) 
         
 #    def  signalwhenReady(self,  callback):
  #       self.callback = callback
        
class Protocol(object):
    """Abstract class for all protocols"""
    def __init__(self,  dataObject):
        self.m_dataObject = dataObject
        self.m_dataObject.signalwhenReady(self.OnData)
     
    def OnData(self,  data,  bytes):
        raise NotImplementedError, "Implement me"
                
                
class BinaryProtocol(Protocol):
    
    def Send(self, LenkoPacket):
         buffer = []
         buffer.append(0x25)
         buffer.append(lenkoPacket.getCommand())
         buffer.append(13)    # checksum  
         
         kalle =''

         for n in buffer:
             kalle += 'B '
         k = struct.Struct(kalle)
         packed_data = k.pack(*buffer)
    
    def OnData(self,  data,  bytes):
         
         
         for d in data:
             r = unpack('B',  d)
             print "we got a token:",  r

        
class LenkoProtocol(Protocol):
    # States
    INVALID = 0
    STARTTOKEN = 1
    COMMAND = 2
    CHKSUM = 3
    
    def connectCallback(self,  callback):
         self.callback = callback
         
    def ResetState(self):
         self.state = self.STARTTOKEN
         
    def Send(self,  lenkoPacket):
         self.buffer = []
         
         # Build a packet!
         self.buffer.append('#')
         self.buffer.append(lenkoPacket.getCommand())
         self.buffer.append(13)    # checksum  
         
         
         # Calculate checksum and add it to the end
         self.checksum = 0
         #for i in range(len(self.buffer)):
         #    self.checksum = binascii.hexlify(unpack('B',  self.buffer[i]))
             
         self.m_dataObject.Write(self.buffer, 3)   
         
    def OnData(self,  data,  bytes):
        """this routine should be called by the data object in a sharp version"""
        self.packet = LenkoPacket()
        
        for d in data:
          
          if (self.state == self.STARTTOKEN):
              if (d == '#'):
                 self.state = self.COMMAND
              else:
                  print "no token yet..."   
                  
          elif (self.state == self.COMMAND):
              # Fake here, turn  Request to a Response by an increment...
              d+= 1
              self.packet.setCommand(d)
              self.state = self.CHKSUM
          elif (self.state == self.CHKSUM):
               self.packet.setChkSum(d)
               self.callback(self.packet)
          else:
              print "Something went wrong"    
       
class PacketGenerator(object):
    def __init__(self):
        pass
        
    def  generateStartProcedure(self):
        self.p = LenkoPacket()
        self.p.setCommand(LenkoPacket.STARTPRODUCE_REQ)
        return self.p


class PacketInterpreter(object):
    def getStartProduceResponse(self, packet):
        self.isValid = (packet.size()  == 3) and (packet.getCommand() == LenkoPacket.STARTPRODUCE_RESP)
        print 'interpreter:',  packet.getCommand()
        return self.isValid                       
                            
        

class TrafficGenerator(object):
    def __init__(self, protocol):
         self.m_protocol = protocol
         self.m_protocol.connectCallback(self.signalOnPacket)
         
         
    def generateSnow(self):
         gen = PacketGenerator()
         query  = gen.generateStartProcedure()
         
         self.m_interpret = PacketInterpreter()
         
         self.m_protocol.ResetState()
         self.m_protocol.Send(query)
        
         # possible to a callback ala siglibc??
         #sleep(1)
         
    def signalOnPacket(self,  packet):
        
         if (self.m_interpret.getStartProduceResponse(packet)):
             print "Hurra we got a packet!"
         else:
             print "we got an invalid packet ...!"   
         # call intepreter and check!
         
         
         



#io = LoopDataObject()

io = SerialWrapper()
io.start()

protocol = LenkoProtocol(io)

generator = TrafficGenerator(protocol)


generator.generateSnow()




