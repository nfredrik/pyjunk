import sqlite3

conn = sqlite3.connect('/tmp/example')

c = conn.cursor()

# Syntax: select * from <table?> order by <column?> (asc|desc)

c.execute('select * from stocks order by price desc')   # default ascending order

#print ' using fetchall()'
#print c.fetchall()


# iterator, uses fetchone()
print 'Using iterator'
for row in c:
    print row



# We can also close the cursor if we are done with it
c.close()
