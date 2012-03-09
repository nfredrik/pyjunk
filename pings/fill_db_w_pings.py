from ping import Ping
from db import PingDB

locs = [Ping('sun.com'), Ping('oracle.com'), Ping('ftp.sunet.se'), Ping('bolagsverket.se')]

db = PingDB()

#
#sun.com 2011-11-26 06:55:28 184.954 229
#oracle.com 2011-11-26 06:55:29 184.796 229
#ftp.sunet.se 2011-11-26 06:55:29 35.066 51
#bolagsverket.se 2011-11-26 06:55:29 45.789 113

for loc in locs:
     print loc.get_dest() , loc.get_time(), loc.get_response(), loc.get_ttl()  
     db.write(date = loc.get_time(),
              pingobj = loc.get_dest(),
              ttl = loc.get_ttl(),  
              response = loc.get_response()
             )
