
"""
CruiseControl Reporting, Attention & Posting (CRAP)
(Trunk on Windows)

Full green: Build successes (unlikely), quick ship it to the customers.
Blinking yellow green: Building after last attempt was successful.
Blinking yellow red: Building after last attempt failed
Blinking Red: Build failed
Blinking Blue: Connection to Cruise Control is down (Lony, I kill you!).
Blinking purple: Slavik commited some code, if you see the LED in this state, please do revert as quickly as possible!


All rights reserved to Assaf Nativ @ Sentrigo @ Mcafee @ Intel
"""


import urllib2
import threading
import thread
import time
import re
from subprocess import *
from pywinusb import hid

COLORS = {
        'BLANK': 0,
        'GREEN': 1,
        'RED': 2,
        "BLUE": 3,
        "AQUA": 4,
        "YELLOW": 5,
        "VIOLET": 6,
        "WHITE": 7}
DEFAULT_COLORS = ['BLANK']
SPEED = 0.5
Colors = DEFAULT_COLORS
ColorsLock = threading.Lock()
KeepRunning = True
KeepRunningLock = threading.Lock()
# 1294, pID=1320
Device = hid.HidDeviceFilter( vendor_id = 0x1294, product_id = 0x1320 ).get_devices()[ 0 ]
##Device = hid.HidDeviceFilter( vendor_id = 0x1d34, product_id = 0x0004 ).get_devices()
if Device is None or 'MAIL' not in `Device`:
    print "Device not found"
    raise Exception("Device not found")

print Device
Device.open()


def setLEDColor(color):
    global Device
    report = Device.find_output_reports()[0]
    print 'color:', color
    print report[ 0xff000001 ]
    report[ 0xff000001 ][ 0 ] = color
    report[ 0xff000001 ][ 1 ] = color
    report[ 0xff000001 ][ 2 ] = color
    report[ 0xff000001 ][ 3 ] = color
    report[ 0xff000001 ][ 4 ] = color
    #report[ 0xff000001 ][ 0 ][value] = [0, 0, 0, 0, 0]
    #report[ 0xff000001 ][ 0 ] = [color,color, color, color, color]
    report.send()

def ColorsBlinkingThread():
    global KeepRunning
    global KeepRunningLock
    global Colors
    global ColorsLock

    while True:
        KeepRunningLock.acquire()
        if False == KeepRunning:
            KeepRunningLock.release()
            return
        KeepRunningLock.release()
        ColorsLock.acquire()
        colors = Colors[:]
        ColorsLock.release()
        for c in colors:
            if type(c) == type(""):
                colorValue = COLORS[c]
            else:
                colorValue = c
            setLEDColor(colorValue)
            time.sleep(SPEED)

thread.start_new_thread(ColorsBlinkingThread, ())

def readCControlPage(url, build_name, FailColor="RED", SuccessColor="GREEN", BuildingColor="YELLOW"):
    global statusData
    global KeepRunning
    global KeepRunningLock
    global Colors
    global ColorsLock

    try:
        con = urllib2.urlopen(url)
        pageData = con.read()
        con.close()
    except:
        print('Connection to CControl failed')
        return []
    statusData = re.findall('(<td class="data"><a href="buildresults/Sensor_trunk">%s</a></td>\s*?<td class="data date status.*?>)(.*?)(</td>\s*?<td class="data date failure">)(.*?)(</td>)' % build_name, pageData)[0]
    status = statusData[1]
    failure = statusData[3]
    print("Build status for %s is %s (%s)" % (build_name, status, failure))
    if ("waiting" in status) and ("" == failure):
        #print("State: 1")
        newColors = [SuccessColor] 
    elif ("waiting" in status) and ("" != failure):
        #print("State: 2")
        newColors = [FailColor, "BLANK"]
    elif ("building" in status) and ("" != failure):
        #print("State: 3")
        newColors = [BuildingColor, FailColor]
    elif ("building" in status) and ("" == failure):
        #print("State: 4")
        newColors = [BuildingColor, SuccessColor]
    elif ("queued" in status) and ("" != failure):
        #print("State: 5")
        newColors = [BuildingColor, BuildingColor, FailColor]
    elif ("queued" in status) and ("" == failure):
        #print("State: 6")
        newColors = [BuildingColor, BuildingColor, SuccessColor]
    elif ("publishing" in status):
        newColors = [BuildingColor, BuildingColor, "WHITE"]
    elif "" == failure:
        #print("State: 7")
        newColors = []
    else:
        newColors = []
    
    return newColors
    
def KillEverything():
    global Device 
    global KeepRunning
    global KeepRunningLock

    KeepRunningLock.acquire()
    KeepRunning = False
    KeepRunningLock.release()
    Device.close()    

print("Running Cruse Control notifier")
try:
    failCount = 0
    while True:
        ColorsLock.acquire()
        currentColors = Colors[:]
        ColorsLock.release()
        ##sp = Popen("svn log -r HEAD --username someuser --password somepassword http://dev1.sentrigo.com/svn/Sensor/HedgehogSensor", stdout=PIPE, shell=True)
        ##lastCommit = sp.communicate()[0]
        newColors = []
        if False:
            pass
        #if 'slavik' in lastCommit.lower():
        #    newColors = ['VIOLET', 'BLANK']
        else:
            newColors=[]
            #newColors = readCControlPage(r'http://192.168.150.228:9090/', 'Sensor_trunk')
            if newColors == []:
                failCount += 1
                print("Fail count++ (%d)" % failCount)
                if failCount > 0:
                    #newColors = ["RED", "BLANK"]
                    newColors = [7, 0]
        if newColors != currentColors and newColors != []:
            ColorsLock.acquire()
            Colors = newColors
            ColorsLock.release()
            failCount = 0
        time.sleep(10)
except KeyboardInterrupt, e:
    print('User interrupt!')
    setLEDColor(0)
    KillEverything()

