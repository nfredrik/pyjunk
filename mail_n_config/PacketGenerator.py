from Packet import *

class PacketGenerator(object):
    def __init__(self):
        pass

    def  generatePrintStatusRequest(self):
        self.p = LinxPacket(254)
        self.p.setCommand(LenkoPacket.PRINT_STATUS_REQUEST)
        payload = [0]
        for p in payload:
            self.p.push_back(p)

        return self.p

    def  generateRequestDataDirectory(self):
        self.p = LenkoPacket(4)
        self.p.setCommand(LenkoPacket.REQUEST_DATA_DIRECTORY)
        payload = [0x4c]  # Data type - Logos
        for p in payload:
            self.p.push_back(p)

        return self.p
