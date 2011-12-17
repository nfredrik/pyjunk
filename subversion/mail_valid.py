import re

fh = open('emails.txt', 'r')

list_of_addr = []

for line in fh:
    if re.match('^\w+(\.\w+)*@[a-zA-Z_]+?\.[a-zA-Z_]{2,6}$',line.rstrip() ) != None:
        print line.rstrip(), ' is a valid address' 
        list_of_addr.append(line.rstrip())
    else:
        print line.rstrip(), ' is NOT a valid address' 
    

print list_of_addr






if re.match('^\w+(\.\w+)*@[a-zA-Z_]+?\.[a-zA-Z_]{2,6}$', 'fredrik.svard@gmail.com') != None:
    print ' Hurra we got a match'


if re.match('^\w+(\.\w+)*@[a-zA-Z_]+?\.[a-zA-Z_]{2,6}$', 'fredrik@gmail.com') != None:
    print ' Hurra we got a match'
