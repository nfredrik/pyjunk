import re

class PcoObject(object):
    def __init__(self, filename, filepath):
         self.filename = filename
         self.filepath = filepath
         self.fh = open(filename,'r')
         self.string = self.fh.read()

    def get_filename(self):
        """
        Return the filename as a string 
        """
        self.name = re.search('PROGRAM\-ID\.[\s]*([\w]*)', self.string)
        if self.name != None:
            return self.name.group(1)

    def get_filepath(self):
        return self.filepath

    def get_sql_include(self):
        """
        Return found SQL INCLUDES in a list 
        """
        self.sqls = re.findall('[^\*][\s]*EXEC[\s]*SQL[\s]*INCLUDE[\s]*\'([\w\d\-]+)\'[\s]*END\-EXEC\.', self.string)
        return self.sqls

    def get_copys(self):
        """
        Return found in COPYs in a list 
        """
        self.copys = re.findall('COPY[\s]+([\w\d\-]+)[\s]+IN[\s]+([\w\d\-]+)', self.string)
        return self.copys

    def get_copys_system(self):
        """
        Return found in COPYs in a list 
        """
        self.copys_system = re.findall('COPY[\s]+([\w\d\-]+)\.', self.string)
        return self.copys_system

    def get_pot_rm_stuff(self):
        """
        Return found in COPYs in a list 
        """
#        self.copys = re.findall('(^HPC[A-Z\d]{3}\*.*)', self.string)
        self.copys = re.findall('(HPC[A-Z\d]*\*.*)', self.string)
        return self.copys
