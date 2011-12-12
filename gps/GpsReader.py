
class GpsReader(object):
    
    def __init__(self,  dataobject,  signalFix):
        self.m_dataobject = dataobject
        self.m_signalFix = signalFix
        
        self.m_dataobject.SignalOnData = self.OnData 
        
    def OnData(self,  data,  bytes):
         line =""
         
         for item in data:
             if item != '\r' or item != '\n':
                line.append(item)
                data.pop()
            
         # Tokenize the line and process the commands
         if line != "":
            commands = ""
            self.Tokenize(commands, line, ',')
            self.Process(commands)
            line.clear()
            
    def Process(self,  commands):   
        if commands[0] == "$GPGGA" and commands.size() == 15:
            self.m_Valid = commands[6]
            self.m_signalFix(self.m_Valid)
    
    def Tokenize(self,  commands,  line,  splitter):
         commands = line.split(splitter) 
