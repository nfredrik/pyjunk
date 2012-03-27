class InfoObject(object):
    def __init__(self, name, filename, filepath, proclist):
        """
        filename - name of info file 
        proclist - path to copys
        """
        self.fh = open(filename, 'w')
        self.fh.write('<PGM_INFO>:'+ name + ' ' + filepath + ' UCOB\n')

        self.fh.write('<PATH_COPY>:/RDMS/DEFS\n')

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

