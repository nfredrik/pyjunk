class DataObject(object):
    """Base class for Data Objects"""
    def __init__(self):
       pass

    def  Write(self, buf,  bytes):
         pass

    def  signalwhenReady(self,  callback):
         self.callback = callback


class NewLoopDataObject(DataObject):

     def  Write(self, buf,  bytes):
        buffer = [0x1b, 0x06,
                  0x00,
                  0x00,
                  0x14,
                  0x03,
                  0x02,
                  0x00, 0x00, 0x00, 0x00,
                  0x1b, 0x03,
                  0xde
                 ]
        self.callback(buffer,  bytes)



