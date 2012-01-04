import string
import re
fh = open('a.html', 'r')

for line in fh:
    words = line.split()
    for token in words:
        if re.match('[^[:print:]]', token):
             print words

fh.close()
