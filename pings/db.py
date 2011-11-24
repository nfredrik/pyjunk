import sqlite3


class PingDB(object):

    def __init__(self):
        self.c = sqlite3.connect('./pingdb.sqlite3')
        self.conn = self.c.cursor()
        # Create table if does not exist
        self.conn.execute('''create table if not exists pingtable
            (date text, pingobj text, ttl real, response real)''')

    def write(self, date, pingobj, ttl, response):
        self.conn.execute('insert into pingtable values (?,?,?,?)', (date, pingobj, ttl, response))
        self.c.commit()

    def read_responses_order(self):
        pass
        self.conn.execute('select * from pingtable order by response')   # default ascending order
        return self.conn.fetchall()

    def read_pingobj_order(self):
        pass
        self.conn.execute('select * from pingtable order by pingobj')   # default ascending order
        return self.conn.fetchall()


    def read_ttl_order(self):
        pass
        self.conn.execute('select * from pingtable order by ttl')   # default ascending order
        return self.conn.fetchall()


    def read_date_order(self):
        pass
        self.conn.execute('select * from pingtable order by date')   # default ascending order
        return self.conn.fetchall()


    def db_exist(self):
       self.res = self.conn.execute('SELECT CASE WHEN tbl_name = "name" THEN 1 ELSE 0 END FROM sqlite_master WHERE tbl_name = "name" AND type = "table"')
       print 'db_exist:', self.res

    def __del__(self):
        # We can also close the cursor if we are done with it
        self.conn.close()
