# Read a datetime string and check if it is older than 10 days
import time

import datetime


def check_this(the:datetime.datetime, name:str)-> bool:
    if datetime.datetime.now() > the:
        print(f"{name}:✅", end='')

        return True
    print(f"{name}:❌", end='')
    return False


later1 = datetime.datetime.now() + datetime.timedelta(seconds=10)
later2 = datetime.datetime.now() + datetime.timedelta(seconds=20)
later3 = datetime.datetime.now() + datetime.timedelta(seconds=30)

while True:


    #if check_this(later1) and check_this(later2) and check_this(later3):
    if all([check_this(later1, 'olle'),check_this(later2, 'dole'), check_this(later3, 'doff')]):

        break

    print("")
    time.sleep(3)

