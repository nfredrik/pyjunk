#!/usr/bin/env python
from observer import *
import threading
from Tkinter import *
import time

prev_build = '...'           
flip = False

# TODO:

# Plocka bort textrutan och bara visa en ruta for att gora quit, alternativt ha tva fonster
# Howto collapse a widget?
# Spara URLen i title for att se vilket bygge det ar.
# toggle btw the old value and and current status

class View(Subscriber,Frame):
    def __init__(self, master=None):
             
        Frame.__init__(self, master)
        self.master=master
        self.pack()
        self.createWidgets()        
        self.Control = Control(view= self)        
        
    def notify(self,postname):
        (txt, color) = postname.get_status()
        self.l.config(text=txt)
        self.l.config(bg=color)

    def callback(self):
        print self.e.get()
        self.Control.setURL(self.e.get())
        root.title(self.e.get()) 
        
    def createWidgets(self):
        self.e = Entry(self.master)
        self.e.pack()
        self.e.focus_set()        
        
        self.b = Button(self.master, text="poll", width=10, command=self.callback)
        self.b.pack()

        self.l = Label(self.master, 
         fg = "black",
         bg = "white",
         font = "Helvetica 16 bold italic")
        self.l.config(text=str('got no build yet'))
        self.l.pack()
         
        
    def oldcreateWidgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit

        self.QUIT.pack({"side": "left"})

        self.hi_there = Button(self)
        self.hi_there["text"] = "Hello",
        self.hi_there["command"] = self.say_hi

        self.hi_there.pack({"side": "left"})
        
        self.txt = Text(self, height=10, width=10)
        self.txt.bind("<Button-1>", self.on_text_Click)
        self.txt.pack(fill=BOTH, expand=1)
     
        self.txt.insert(END, '1')     
        self.txt.pack(side=LEFT)
        
    def on_text_Click(self):
        print 'we got', self.txt.get()    
   
    def say_hi(self):
        print "hi there, everyone!"
        


class Model(Publisher, threading.Thread):

    def __init__(self,url):
        Publisher.__init__(self)
        threading.Thread.__init__(self)
        self.i=0
        self.url=''
        self.result= tuple()

    def setURL(self,url=""): 
        self.url = url
        
    def getResultFromJenkins(self):
        import urllib2
        pass
    
    def get_jenkins_status(self):
        import json
        import urllib2
        Success, Building, Failure = 0, 1, 2
        global flip
        global prev_build
        try:
            self.all = self.url + "/lastBuild/api/json"
            #print self.all
            jenkinsStream   = urllib2.urlopen( self.all, timeout=2 )
            buildStatusJson = json.load( jenkinsStream )
            #print 'buildStatusJson', buildStatusJson
        except urllib2.HTTPError, e:
            print "HTTP Error: " + str(e.code) 
            print "      (job name [" + self.url + "] probably wrong)"
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
                print "[" + self.url + "] build status: " + "BUILDING"
                print 'flip', flip
                if flip:
                    flip = not flip
                    return ('Building', 'yellow')
                else:
                    flip = not flip
                    return ('Building', prev_build)
                
                flip = not flip
                print 'flip again', flip
                                  

        if buildStatusJson.has_key( "result" ):      
            print "[" + self.url + "] build status: " + buildStatusJson["result"]
            if buildStatusJson["result"] != "SUCCESS" :
                prev_build = 'red'
                return ('Failure', 'red')
            else:
                prev_build = 'green'
                return ('Success', 'green')
    
        
    def run(self):
        print 'Model started to run'
        while True:
            self.i+=1
            self.postname=self
            #self.notifyAll(self)
            time.sleep(1)
            if  self.url !=  '':
                self.result = self.get_jenkins_status()
                self.notifyAll(self)
        
    def get_status(self):
        return(self.result)
    
        return str(self.i)        
    
     
class Control(Subscriber):
    """"
        Controls the behaviour of the Model and inform the Viewer(s)?
    """
    def __init__(self, url_jenkins_job='http://localhost:8080/job/osv', view='None'):
        self.model= Model(url_jenkins_job) 
        self.model.register(view)
        self.model.register(self)
        self.model.start()
    
    def setURL(self, url=""):    
        self.model.setURL(url)

    def notify(self,postname):
        return
        print 'Control got:', postname.get_status()
 
    
if __name__ == "__main__":
    root = Tk()
    app = View(master=root)
    app.mainloop()
    root.destroy()
    

 