import sys
import rrdtool
import os 
import time

rrd_file='./net.rrd'

def main(args):
    # Check if the the round robin file has been created
    if not os.path.exists(rrd_file): 
        ret = rrdtool.create("rrd_file", "--step", "300", "--start", '0',
         "DS:input:COUNTER:600:U:U",
         "DS:output:COUNTER:600:U:U",
         "RRA:AVERAGE:0.5:1:600",
         "RRA:AVERAGE:0.5:6:700",
         "RRA:AVERAGE:0.5:24:775",
         "RRA:AVERAGE:0.5:288:797",
         "RRA:MAX:0.5:1:600",
         "RRA:MAX:0.5:6:700",
         "RRA:MAX:0.5:24:775",
         "RRA:MAX:0.5:444:797")
         
        if ret:
         print rrdtool.error()
         return 42
         
    
    
    # Update of database
    total_input_traffic = 0
    total_output_traffic = 0
     
    total_input_traffic += random.randrange(1000, 1500)
    total_output_traffic += random.randrange(1000, 3000)
    ret = rrdtool.update('rrd_file','N:' + `total_input_traffic` + ':' + `total_output_traffic`);
    if ret:
        print rrdtool.error()
        return 42    
        
    
if __name__ == '__main__':
    sys.exit(main(sys.argv[1:] or 0))
     