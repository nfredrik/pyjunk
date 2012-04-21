from subprocess import Popen, PIPE

# http://moizmuhammad.wordpress.com/2012/01/31/run-oracle-commands-from-python-via-sql-plus/

class Oracle(object):
    
    def __init__(self):
        self.session = Popen(['sqlplus', '-S', 'user/pwd@database'], stdin=PIPE, stdout=PIPE, stderr=PIPE)   
        
    #function that takes the sqlCommand and retuns the output and #error string (if any)
    def runSqlQuery(sqlCommand):
        self.session.stdin.write(sqlCommand)
        return self.session.communicate()


if __name__ == '__main__':
    
    oracle = Oracle()
    #example 1: run a query that returns a numeric value
    queryResult, errorMessage = oracle.runSqlQuery(sqlCommand='select count(*) from jobs;')
    
    
    #example 2: run a query that returns a next value of sequence
    queryResult, errorMessage = oracle.runSqlQuery(sqlCommand='select employees_seq.nextval from jobs;')
    
    #example 3: call stored procedure
    queryResult, errorMessage = oracle.runSqlQuery(sqlCommand='execute  secure_dml;Õ;')
    
    
    
    
    
    