from Packet import *


class PacketInterpreter(object):
    def getPrinterStatusResponse(self, packet):
        self.isValid = (packet.size()  == 14) and (packet.getCommand() == LenkoPacket.PRINT_STATUS_REQUEST)
 #       print 'interpreter:',  packet.size(), packet.getCommand()
        return self.isValid
