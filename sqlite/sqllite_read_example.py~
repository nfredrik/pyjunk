import sqlite3

conn = sqlite3.connect('/tmp/example')

c = conn.cursor()


if True:
    # Create table
    c.execute('''create table stocks
    (date text, trans text, symbol text,
     qty real, price real)''')


# Larger example
for t in [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
          ('2006-04-05', 'BUY', 'MSOFT', 1000, 72.00),
          ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
         ]:
    c.execute('insert into stocks values (?,?,?,?,?)', t)

# Save (commit) the changes
conn.commit()

# We can also close the cursor if we are done with it
c.close()
