#!/usr/bin/env python

import time

if __name__ == '__main__':

     pipe = open('/dev/pts/3', 'w')
     cntr = 1000000000

     while --cntr > 0:
#         time.sleep(1)
         pipe.write('A' *400)
         pipe.flush()
