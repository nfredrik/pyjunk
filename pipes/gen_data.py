#!/usr/bin/env python

import time

if __name__ == '__main__':
#     pipe = open('input', 'w')
     pipe = open('/dev/pts/3', 'w')

     while True:
         time.sleep(1)
         pipe.write('$GPGGA,064746.000,4925.4895,N,00103.9255,E,1,05,2.1,-68.0,M,47.1,M,,0000*4F\r')
         pipe.flush()
         time.sleep(1)
         pipe.write('$GPRMC,081836,A,3751.65,S,14507.36,E,000.0,360.0,130998,011.3,E*62\r')
         pipe.flush()
