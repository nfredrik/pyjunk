
import threading

class DataObject(object):
    """Base class for Data Objects"""
    def __init(self):
       pass

    def  Write(self, buf,  bytes):
        raise NotImplementedError, "Implement me"

 


class EmulateSerialPort(DataObject,  threading.Thread):
    def __init__(self,  filename):
         threading.Thread.__init__(self)
         DataObject.__init__(self)
         self.fileh = open(filename)
       
    def run(self):  
         while True:
             pass
             # read line
             # split in a list of tokens ['a', 'b', ....]
             
             # rest for a while
            # start from begining file again, rewind
