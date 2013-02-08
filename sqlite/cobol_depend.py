import sqlite3

class CobolDB(object):

    def __init__(self):
        self.c = sqlite3.connect('./coboldb.sqlite')
        self.conn = self.c.cursor()
        # Create table if does not exist
        self.conn.execute('''create table if not exists coboltable
            (pco text, pcopath text, copy text, copypath text)''')

    def write(self, pco, pcopath, copy, copypath):
        self.conn.execute('insert into coboltable values (?,?,?,?)', (pco, pcopath, copy, copypath))
        self.c.commit()

    def read_responses_order(self):

        self.conn.execute('select * from pingtable order by response')   # default ascending order
        return self.conn.fetchall()

    def read_pingobj_order(self):
        self.conn.execute('select * from pingtable order by pingobj')   # default ascending order
        return self.conn.fetchall()


    def read_ttl_order(self):
        self.conn.execute('select * from pingtable order by ttl')   # default ascending order
        return self.conn.fetchall()


    def read_date_order(self):
        self.conn.execute('select * from pingtable order by date')   # default ascending order
        return self.conn.fetchall()


    def read_date_4_object(self, object):
#        self.str ="select ttl, response, date from pingtable where pingobj = 'oracle.com';"
        self.str ="select date, ttl, response from pingtable where pingobj = \'" + str(object) +  "\';"
#        print self.str 
        self.conn.execute(self.str)
        return self.conn.fetchall()


    def db_exist(self):
       self.res = self.conn.execute('SELECT CASE WHEN tbl_name = "name" THEN 1 ELSE 0 END FROM sqlite_master WHERE tbl_name = "name" AND type = "table"')
       print 'db_exist:', self.res

    def __del__(self):
        # We can also close the cursor if we are done with it
        self.conn.close()
        
 
def main(args):
    cobol = CobolDB()
     
    copys1 = ['copy1', 'copy2', 'copy3']
    copys2 = ['copyA', 'copyB', 'copyC']
 
    for i in copys1:
        cobol.write('FUNK', 'FISRT/SECOND', i, 'THIRD/FOURTH')
         
    for i in copys2:
        cobol.write('PUNK', 'MINE/MYNE', i, 'OTTO/LITE')
                  
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv[1:]))
    
    """
    to read all copys that belongs to pco: select copy from coboltable where pco = 'FUNK'
    eller select copy from coboltable where pco like  '%UNK'
    
    to read pco that uses a copy: select pco from coboltable where copy = 'copy3'
    
    select pco, copy from coboltable where copy like  'copy%'
    
    select pco, copy from coboltable where copy in ('copy1', 'copy2')
    
    """       