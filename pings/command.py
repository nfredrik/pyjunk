import commands

class Command(object):
    def __init__(self, cmd):
        (self.status,self.output) = commands.getstatusoutput(cmd)

    def get_status(self):
        return self.status
    def get_string_output(self):
        return self.output
    def get_list_output(self):
        return self.output.split() 
