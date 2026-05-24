# Read a datetime string and check if it is older than 10 days
import functools
import time

import datetime


def check_this(last_tight:datetime.datetime, the:datetime.datetime, name:str)-> bool:
    if last_tight < the:
        print(f"{name} {the.isoformat(timespec='seconds')}:✅", end='')

        return True
    print(f"{name} {the.isoformat(timespec='seconds')}:❌", end='')
    return False

latest_tightening = datetime.datetime.now()


later1 = datetime.datetime.now() + datetime.timedelta(seconds=10)
later2 = datetime.datetime.now() + datetime.timedelta(seconds=20)
later3 = datetime.datetime.now() + datetime.timedelta(seconds=30)

my_call = functools.partial(check_this, latest_tightening)
while True:


    #if check_this(later1) and check_this(later2) and check_this(later3):
    if all([my_call(later1, 'olle'),my_call(later2, 'dole'), my_call(later3, 'doff')]):

        break

    print("")
    time.sleep(3)

