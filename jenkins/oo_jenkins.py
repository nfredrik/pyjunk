import sys
import time
import json
import urllib2

#if sys.platform == 'win32':
from pywinusb import hid
    
Success, Building, Failure = 0, 1, 2    

class JenkinsJobError(Exception):pass

class JenkinsJob(object): 

#    jenkinsUrl = "http://192.168.1.67:8080/job/"
#    jenkinsUrl = "http://192.168.0.2:8080/job/"
    jenkinsUrl = "http://localhost:8080/job/"
    
    def __init__(self,jobName):
        self.jobName = jobName
            
    def get_status(self):
        try:
            self.all = self.jenkinsUrl + self.jobName + "/lastBuild/api/json"
            #print self.all
            jenkinsStream   = urllib2.urlopen( self.all, timeout=2 )
            buildStatusJson = json.load( jenkinsStream )
            #print 'buildStatusJson', buildStatusJson
        except urllib2.HTTPError, e:
            print "HTTP Error: " + str(e.code) 
            print "      (job name [" + self.jobName + "] probably wrong)"
            raise JenkinsJobError('No contact::%s' % e) 
        except urllib2.URLError, e:
            raise JenkinsJobError('URLError::%s' % e) 

        except Exception, e:        
            print "Another error: " + str(e.code)    
            raise Exception(e)           
        except:
            raise JenkinsJobError('Failed to parse json')      

        if buildStatusJson.has_key('building'):
            if buildStatusJson["building"] == True :
                print "[" + self.jobName + "] build status: " + "BUILDING"
                return Building


        if buildStatusJson.has_key( "result" ):      
            print "[" + self.jobName + "] build status: " + buildStatusJson["result"]
            if buildStatusJson["result"] != "SUCCESS" :
                return Failure
            else:
                return Success
    
    def get_url(self, type):
        try:
            self.all = self.jenkinsUrl + self.jobName + "/" + type + "/api/json"
            print self.all
            jenkinsStream   = urllib2.urlopen( self.all, timeout=2 )
            return json.load( jenkinsStream )
        except urllib2.HTTPError, e:
            print "HTTP Error: " + str(e.code) 
            print "      (job name [" + self.jobName + "] probably wrong)"
            raise JenkinsJobError('No contact::%s' % e) 
        except urllib2.URLError, e:
            raise JenkinsJobError('URLError::%s' % e) 

        except Exception, e:        
            print "Another error: " + str(e.code)    
            raise Exception(e)           
        except:
            raise JenkinsJobError('Failed to parse json')

                
    def get_lastFailedBuild(self):
        print self.get_url("lastFailedBuild")
    
    def get_lastUnsuccessfulBuild(self):
        print self.get_url("lastUnsuccessfulBuild")
    
    

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
    
    toggle = True
    
    def old__init__(self, v, i):pass
    
    def __init__(self):
        try:
            #self.device = hid.HidDeviceFilter( vendor_id = 0x1294, product_id = 0x1320 ).get_devices()[ 0 ]
            self.device = hid.HidDeviceFilter( vendor_id = 0x1d34, product_id = 0x0004 ).get_devices()[ 0 ]    
        except:    
            raise USBDeviceError("Device could not be found")
        
        self.device.open()
    
    def set_status(self,value=True, lastBuild=Success):
        
        if self.toggle:
            val = value
        else:
            val = lastBuild
        
        self.toggle = not self.toggle
        
        if val == Success:
            self.setLEDColor(self.COLORS['GREEN'])
        elif val == Failure:
            self.setLEDColor(self.COLORS['RED'])   
        elif val == Building:
            self.setLEDColor(self.COLORS['YELLOW'])            
            
    def oldsetLEDColor(self, color):
        print 'setLEDColor got:',  color           
    
    def setLEDColor(self, color):
        report = self.device.find_output_reports()[ 0 ]
        report[ 0xff000001 ][ 0 ] = color
        report.send()   


def main(args):
    try:
        args = args[1:]
        
        lastBuild = Success

        # Create Jenkins job instance(s), take care of exceptions
        thjob = JenkinsJob("5th")
        usbdev = USBDevice()
        # Create USB device instance, take care of exceptions
        
        # Loop eternally only break if user wants to.
        while True:
            
            # Read status of Jenkins job(s)
            result = thjob.get_status()
            
            if result in (Success, Failure):
                lastBuild = result
                
            #thjob.get_lastFailedBuild()
            #thjob.get_lastUnsuccessfulBuild()
            # Indicate the outcome the USB device connected to this computer
            usbdev.set_status(result, lastBuild)
            # Rest for a while until next turn
            time.sleep(5) 

    except JenkinsJobError, e:
        print "JenkinsJobError: " + str(e)
    except USBDeviceError, e:
        print 'USBDeviceError:'  + str(e)   
    except KeyboardInterrupt, e:
        print'User interrupt!'
        usbdev.setLEDColor(USBDevice.COLORS['BLANK'])
    except Exception, e:
        print "Exception: " + str(e) 
        print 'Last resort, none of the above catched the exception...'
                 
if __name__ == '__main__':
  sys.exit(main(sys.argv))