
import datetime

onetd = datetime.timedelta(days=10000)
twotd = datetime.timedelta(days=20000)
two5td = datetime.timedelta(days=25000)
threetd = datetime.timedelta(days=30000)


fredrikbirth = datetime.date(1962,4,15)

print("Fredrik")
print(" 10000 dagar ->", fredrikbirth + onetd)
print(" 20000 dagar ->", fredrikbirth + twotd)
print(" 25000 dagar ->", fredrikbirth + two5td)
print(" 30000 dagar ->", fredrikbirth + threetd)
print('-' * 20)
