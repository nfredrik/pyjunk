from Mail import Mail
import re
import sys

fh = open('emails.txt', 'r')

list_of_addr = []

for line in fh:
    if re.match('^\w+(\.\w+)*@[a-zA-Z_]+?\.[a-zA-Z_]{2,6}$',line.rstrip() ) != None:
        print line.rstrip(), ' is a valid address' 
        list_of_addr.append(line.rstrip())
    else:
        print line.rstrip(), ' is NOT a valid address' 

print list_of_addr

#sys.exit(42)

mail = Mail(list_of_addr,
            'dummy_user',
            'dummy_passwd',
            'mail01.ad.bolagsverket.se',
           )
mail.send('test mail for jenkins')


