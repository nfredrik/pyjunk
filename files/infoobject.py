class InfoObject(object):
    def __init__(self, name, filename, filepath, proclist):
        """
        filename - name of info file 
        proclist - path to copys
        """
        fh = open(filename, 'w')
        self.write_it(fh, name, filename, filepath, proclist)

    def write_it(self, fh, name, filename, filepath, proclist):
        self.fh = fh
        self.fh.write('<PGM_INFO>:'+ name + ' ' + filepath + ' UCOB\n')

        self.fh.write('<PATH_COPY>:/SYSTEM\n')
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


if __name__ == '__main__':

    from StringIO import StringIO
    from tempfile import mkstemp

    # create temp file
    fh, abspath = mkstemp()
  
    info_obj = InfoObject('filename',abspath,'.', ['test', 'nisse']) 

    fh = StringIO("""  
                  Nisse
                  """)

    info_obj.write_it(fh, 'pgminfoname',abspath,'.', ['copy_path_test', 'copy_pathnisse'])
    info_obj.add_sql_includes('include_hej_hoo')
    info_obj.add_copys('procen', 'hej hoo')
    info_obj.add_copys_system('hej hoo')

    print fh.getvalue()
