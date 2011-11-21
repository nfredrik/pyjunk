import string
fh = open('a.html', 'r')

for line in fh:
    words = line.split()
    for token in words:
        if token not string.printable :
            print 'Aj'

fh.close()
