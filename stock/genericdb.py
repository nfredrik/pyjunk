import collections
import sqlite3



class GenDB(object):

    def __init__(self,db_name, fields=None):
        self.c = sqlite3.connect('./' + db_name + '.sqlite')
        self.conn = self.c.cursor()
        self.db_name = db_name
        #self.no_of_fields = '(' + '?,'*(len(fields)) + ')'
        self.no_of_fields = self.add_f(fields)
        print(self.no_of_fields)
        # Create table if does not exist
        #part_str = str([x for x in fields.items()])

        self.conn.execute('''create table if not exists ''' + db_name+'''table
            ('''+ ",".join(fields) + ''')''')

       # self.conn.execute('''create table if not exists pingtable
       #     (date text, pingobj text, ttl real, response real)''')

    def add_f(self, fields):
        if len(fields) == 1:
            return '(?)'
        else:
            return '(?' + ',?'*(len(fields)-1) +')'

    def write(self, f=[]):
        self.hej =  "'" + "','".join(f) + "'"
        print (self.hej)
        #self.conn.execute('insert into ' + self.db_name +'table values' + self.no_of_fields, (f[0], f[1], f[2]))
        self.conn.executescript('insert into ' + self.db_name +'table values' + self.no_of_fields + ',(' + self.hej +')')
        #self.conn.executemany('insert into ' + self.db_name +'table values (?)', self.char_generator(f))
        #self.c.commit()


    def char_generator(self, field):
        for c in field:
            yield (c,)    


    def db_exist(self):
       self.res = self.conn.execute('SELECT CASE WHEN tbl_name = "name" THEN 1 ELSE 0 END FROM sqlite_master WHERE tbl_name = "name" AND type = "table"')
       #print 'db_exist:', self.res

    def __del__(self):
        # We can also close the cursor if we are done with it
        self.conn.close()


if __name__ == '__main__':

    dict = collections.OrderedDict()

    # dict = {"date":"text", "pingobj":"text"}

    arrray = ["date text", "pingobj text", "ttl real"]

    db = GenDB('nisse', fields= arrray)

    db.write(['2012-0-01', 'janne', '36'])

    db.write(['2012-0-01', 'sussi', '51'])