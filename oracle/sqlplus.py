from subprocess import Popen, PIPE

#function that takes the sqlCommand and connectString and retuns the output and #error string (if any)

def runSqlQuery(sqlCommand, connectString):

session = Popen(['sqlplus', '-S', connectString], stdin=PIPE, stdout=PIPE, stderr=PIPE)
session.stdin.write(sqlCommand)
return session.communicate()

