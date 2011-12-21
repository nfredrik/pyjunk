#ldd libdpsxml.so
#        linux-vdso.so.1 =>  (0x00007fff09d6b000)
#        libunisys.so.0 => not found
#        libxml2.so.2 => /usr/lib64/libxml2.so.2 (0x00007feacf53f000)
#        libdl.so.2 => /lib64/libdl.so.2 (0x00007feacf33b000)
#        libz.so.1 => /lib64/libz.so.1 (0x00007feacf125000)
#        libm.so.6 => /lib64/libm.so.6 (0x00007feaceece000)
#        librt.so.1 => /lib64/librt.so.1 (0x00007feacecc5000)
#        libclntsh.so.11.1 => not found
#        libLogTrace.so.0 => not found
#        libc.so.6 => /lib64/libc.so.6 (0x00007feace966000)
#        /lib64/ld-linux-x86-64.so.2 (0x00007feacfb4e000)
#        libpthread.so.0 => /lib64/libpthread.so.0 (0x00007feace749000)

import sys
from command import Command
import os

def main():

    hash = {}
   
    ls_obj = Command('find . -name \*.so')

#    print 'found file:' ,ls_obj
    for file in ls_obj.get_list_output():
#        print ' file:', file
        concat = 'ldd '+ file  
        print 'Shared object:' ,concat
        ldd = Command(concat)
#        print ldd.get_string_output()
#        sys.exit(42)
        tot_str = ldd.get_string_output()
        list = tot_str.split('\n')
        for row in list:
            if row.find ('not found') != -1 :
                print row
if __name__ == "__main__":
  main()
