import re
import os

class PcoObject(object):
    def __init__(self, filename, filepath):
         self.filename = filename
         self.filepath = filepath
         self.fh = open(filename,'r')
         self.read_from_file(self.fh)

    def read_from_file(self, fh):
         """
         Separate open() and read() to be able to Mcok.
         """
         self.string = fh.read()

    def get_filename(self):
        """
        Extract filename without extension
        """
        return  os.path.basename(os.path.splitext(self.filename)[0])

    def get_program_id(self):
        """
        Return the filename as a string 
        """
        self.name = re.search('PROGRAM\-ID\.[\s]*(\'[\w]*\')', self.string)
        if self.name != None:
            return self.name.group(1)

        self.name = re.search('PROGRAM\-ID\.[\s]*([\w]*)', self.string)
        if self.name != None:
            return self.name.group(1)

    def get_filepath(self):
        """
        Get filepath from input
        """
        return self.filepath

    def get_sql_include(self):
        """
        Return found SQL INCLUDES in a list 
        """
        self.sqls = re.findall('^[\s]*EXEC[\s]*SQL[\s]*INCLUDE[\s]*\'([\w\d\-]+)\'[\s]*END\-EXEC\.', self.string)
        return self.sqls

    def get_copys(self):
        """
        Return found in COPYs in a list 
        """
        self.copys = re.findall('COPY[\s]+([\w\d\-]+)[\s]+IN[\s]+([\w\d\-]+)', self.string)
        return self.copys

    def get_uniq_copys(self):
        """
        Collect uniqe copy paths 
        """
        self.copypaths = {}
        self.copys = self.get_copys()
        for self.module, self.copypath in self.copys:
            if self.copypath not in self.copypaths:
                self.copypaths[self.copypath]=1
        return self.copypaths

    def get_copys_system(self):
        """
        Return found in COPYs in a list 
        """
        self.copys_system = re.findall('COPY[\s]+([\w\d\-]+)\.', self.string)
        return self.copys_system

    def get_pot_rm_stuff(self):
        """
        Return found COPYs in a list 
        """
#        self.copys = re.findall('(^HPC[A-Z\d]{3}\*.*)', self.string)
        self.copys = re.findall('(HPC[A-Z\d]*\*.*)', self.string)
        return self.copys


if __name__ == '__main__':

    from StringIO import StringIO
    from tempfile import mkstemp

    # create temp file
    fh, abspath = mkstemp()

    pco_obj = PcoObject(abspath, '.')
    fh = StringIO("""  PROGRAM-ID.   LK1000.
                          EXEC SQL INCLUDE 'BOBSSS030FTD' END-EXEC.
                          COPY BO-FELTXT    IN UCPROC.
                          COPY HP-SWITCHES.
                          HPCALL*
                          
                          * EXEC SQL INCLUDE 'SUSANNE' END-EXEC.
                          * COPY FREDDE-FELTXT    IN UCPROC.
                          *COPY DELL-SWITCHES.
                          * HPREMOV*
                  """)

    pco_obj.read_from_file(fh)
    print 'program id:', pco_obj.get_program_id()
    print 'includes:', pco_obj.get_sql_include()
    print 'copys:', pco_obj.get_copys()
    print 'uniq copys:', pco_obj.get_uniq_copys()
    print 'copys_system:',pco_obj.get_copys_system()
    print 'pot_rm_stuff:', pco_obj.get_pot_rm_stuff()
