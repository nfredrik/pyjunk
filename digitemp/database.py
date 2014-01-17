import sys
import sqlite3

class TemperatureDB(object):
    def __init__(self):
        self.db = sqlite3.connect('./temperature.sqlite3')
        self.cursor = self.db.cursor()
        #self.cursor.execute('''create table if not exists temperature (TemperatureKey bigint UNSIGNED NOT NULL autoincrement,SerialNumber varchar(20) NOT NULL,\
        #          RecTime timestamp NOT NULL, C float NOT NULL, PRIMARY KEY(SerialNumber), KEY(TemperatureKey) ''')
        
        self.cursor.execute("""create table if not exists temperature (TemperatureKey bigint,SerialNumber varchar(20) primary key,\
                  RecTime timestamp, C float)""")
        
    def log(self, serialno, tempkey, rectime, c):
        #self.sql = """insert into temperature (SerialNumber, TemperatureKey, RecTime, C) values ('%s', '%d', '%d', '%d');""" %  (serialno, tempkey, rectime, c)
        #self.cursor.execute(self.sql)
        self.cursor.execute("""insert into temperature (SerialNumber, TemperatureKey, RecTime, C) values ('%s', '%d', '%d', '%d');""" %  (serialno, tempkey, rectime, c))
        ##self.cursor.execute("""insert into temperature (TemperatureKey, SerialNumber, RecTime, C) values ('1', '2', '3', '4');""")
        

def main(args):
    temp = TemperatureDB()
    temp.log(12, 134, 15, 321)
    print 'the end'


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
