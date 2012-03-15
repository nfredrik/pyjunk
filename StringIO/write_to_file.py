
class FileWrite(object):

    def __init__(self):
        print 'contructor'

    def __del__(self):
        print 'destructor'

    def write_it(self, filename, text):
        fh = open(filename, 'w')
        self.write_it_to_file(fh, text)

    def write_it_to_file(self, fh, text):
        fh.write(text)
        
    def read_it(self, filename):
        fh = open (filename, 'r')
        return self.read_it_from_file(fh)

    def read_it_from_file(self, fh):
        return fh.read()
