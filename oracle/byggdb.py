import os
import re
import sys
from subprocess import Popen, PIPE

ORACLE_ENV='/srv/unireg_build/cm_conf/oracle.env'

class OracleEnv(object):
    def __init__(self, file):
        self.fh = open(file, 'r')
        self.string = self.fh.read()

        self.user = self.pwd = self.db = ' '

        self.u = re.search('USER_ORACLE=(.*)', self.string)
        if self.u != None:
            self.user = self.u.group(1) 

        self.u = re.search('PASS_ORACLE=(.*)', self.string)
        if self.u != None:
            self.pwd = self.u.group(1) 

        self.u = re.search('DB_ORACLE=(.*)', self.string)
        if self.u != None:
            self.db = self.u.group(1) 

    def get_user(self):
        return self.user

    def get_pwd(self):
        return self.pwd

    def get_db(self):
        return self.db
   
class Oracle(object):
    
    def __init__(self,user, pwd, db):
        self.session = Popen(['sqlplus', '-S', user + '/' + pwd + '@' + db], stdin=PIPE, stdout=PIPE, stderr=PIPE)   
        
    # Retuns the output and error string (if any)
    def runSqlQuery(self, sqlCommand):
        self.session.stdin.write(sqlCommand)
        return self.session.communicate()

if __name__ == '__main__':

    # Check if the oracle.env exists ...
    if not os.path.exists(ORACLE_ENV):
        print 'Could not find:', ORACLE_ENV, ' going to exit'
        sys.exit(42)
    
    # Read user, password and database from oracle.env
    oracleenv = OracleEnv(ORACLE_ENV)
  
    # Connect to database  
    oracle = Oracle(oracleenv.get_user(), oracleenv.get_pwd(), oracleenv.get_db())

    # Check available space
    queryResult, errorMessage = oracle.runSqlQuery("select * from user_tablespaces where TABLESPACE_NAME='RDMS_DATA';")

    # Check if this query worked ...
    if re.search('ERROR', queryResult, re.IGNORECASE) != None:
        print 'No contact with database exit compilation '
        sys.exit(42)

    print 'queryResult:', queryResult
    print 'errorMessage:', errorMessage
    
    
    
    
    
