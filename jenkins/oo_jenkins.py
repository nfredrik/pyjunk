import sys
import time
import json
import urllib2

if sys.platform == 'win32':
    from pywinusb import hid

class JenkinsJobError(Exception):pass

class JenkinsJob(object): 

    jenkinsUrl = "http://192.168.1.64:8080/job/"

    def __init__(self,jobName):
        self.jobName = jobName
            
    def get_status(self):
        try:
            self.all = self.jenkinsUrl + self.jobName + "/lastBuild/api/json"
            print self.all
            jenkinsStream   = urllib2.urlopen( self.all )
            buildStatusJson = json.load( jenkinsStream )
            
        except urllib2.HTTPError, e:
            print "URL Error: " + str(e.code) 
            print "      (job name [" + self.jobName + "] probably wrong)"
            raise JenkinsJobError('No contact::%s' % e) 
        except Exception, e:        
            print "Another error: " + str(e.code)    
            raise Exception(e)           
        except:
            raise JenkinsJobError('Failed to parse json')      

        if buildStatusJson.has_key( "result" ):      
            print "[" + self.jobName + "] build status: " + buildStatusJson["result"]
            if buildStatusJson["result"] != "SUCCESS" :
                return False
            else:
                return True
    

class USBDeviceGeneric(object):
    def __init__(self, os ='win32'):
        if os != 'win32':
            raise USBDeviceError("Not implemented on this OS")


class USBDeviceError(Exception):pass


class USBDevice(object):
    COLORS = {
        'BLANK': 0,
        'GREEN': 1,
        'RED': 2,
        "BLUE": 3,
        "AQUA": 4,
        "YELLOW": 5,
        "VIOLET": 6,
        "WHITE": 7}
    
    def __init__(self,vendorid, id):
        try:
            self.device = hid.HidDeviceFilter( vendor_id = 0x1294, product_id = 0x1320 ).get_devices()[ 0 ]
        except:    
            raise USBDeviceError("Device not found")
        
        self.device.open()
    
    def set_status(self,value=True):    
        if True:
            self.setLEDColor(self.COLORS['GREEN'])
        else:
            self.setLEDColor(self.COLORS['RED'])   
    
    def setLEDColor(color):
        report = self.device.find_output_reports()[ 0 ]
        report[ 0xff000001 ][ 0 ] = color
        report.send()   


def main(args):
    try:
        args = args[1:]

        # Create Jenkins job instance(s), take care of exceptions
        thjob = JenkinsJob("5th")
        #usbdev = USBDevice(123, 456)
        # Create USB device instance, take care of exceptions
        
        # Loop eternally only break if user wants to.
        while True:
            
            # Read status of Jenkins job(s)
            result = thjob.get_status()
            # Indicate the outcome the USB device connected to this computer
            #usbdev.set_status(result)
            # Rest for a while until next turn
            time.sleep(2) 

    except JenkinsJobError, e:
        print "JenkinsJobError: " + str(e)
    except USBDeviceError, e:
        print 'USBDeviceError:'  + str(e)   
    except KeyboardInterrupt, e:
        print'User interrupt!'
        usbdev.setLEDColor(USBDevice.COLORS['BLANK'])
    except Exception, e:
        print "URL Error: " + str(e) 
        print 'Last resort, none of the above catched the exception...'
                 
if __name__ == '__main__':
  sys.exit(main(sys.argv))