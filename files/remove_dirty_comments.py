import re

def somepredicate(line):
    if re.match('^(HPC[A-Z\d]{3}\*.*)', line):
        return True
    return False

readfile = open('PAOB.pco', 'r')
writefile = open('PAOB.ng', 'w')

for line in readfile:
  if not somepredicate(line):
    writefile.write(line)

readfile.close()
writefile.close()
