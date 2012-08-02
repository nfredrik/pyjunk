

fh = open('queue.txt', 'rb')
string = fh.read()
list = string.split()

for item in list:
    if item == 'NQ':
        print 'time to enqueue'
    elif item == 'DQ':
        print 'time to dequeue'
    else:
        print 'could not interpret item!'            
print 'Finished!'