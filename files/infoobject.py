class InfoObject(object):
    def __init__(self, filename, proclist):
        """
        filename - name of info file 
        proclist - path to copys
        """
        self.filename = filename
        self.fh = open(self.filename, 'w')
        self.fh.write('<PGM_INFO>:'+ filename + ' /PROD/RETULB UCOB\n')

        self.fh.write('<PATH_COPY>:/RDMS/DEFS\n')
        self.fh.write('<PATH_COPY>:/SYSTEM\n')

        for proc in proclist:
            self.fh.write('<PATH_COPY>:/PROD/' + proc + '\n')

    def add_sql_includes(self, includes):
        self.fh.write('<COPY>:/RDMS/DEFS/' + includes + '\n')

    def add_copys(self, proc, copys):
        self.fh.write('<COPY>:/PROD/' + proc + '/' + copys + '\n')

    def add_copys_system(self, copys):
        self.fh.write('<COPY>:/SYSTEM/' + copys + '\n')

    def __del__(self):
        self.fh.close()

