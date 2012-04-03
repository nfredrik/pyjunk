from  subprocess import Popen
import sys
ip="127.0.0.1"
ping = subprocess.Popen(["ping", "-c", "2", "-w", "1", ip], shell=False)
ping.wait()
if ping.returncode != 0:
    print ping.returncode, "ERROR: failed to ping host. Please check."
    sys.exit(1)
else:
    print "OK"
