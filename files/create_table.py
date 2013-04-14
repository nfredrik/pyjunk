
class tableFile(object):
    def __init__(self, filename):
        with open(filename, 'w') as self.fh:
            pass
    def write_row(self,row):
        self.fh.write(row)
    def __del__(self):
        self.fh.close()
        
        
        

tfile = tableFile('dummy')

with open('stora.sql') as fileh:
    
    while True:
        row = fileh.readline()
        test = re.search('CREATE_TABLE ([dw]+',row)
        
        if test != None:
            del tfile           
            tfile = tableFile(test.group(1)+'.sql')
            tfile.write_row(row)
        else:
            tfile.write_row(row)
            
            
if __name__ == "__main__":
    import doctest
    doctest.testmod()