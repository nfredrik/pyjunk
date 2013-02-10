#!/usr/bin/env python
from observer import *
import threading
from Tkinter import *
import time

class View(Subscriber,Frame):
    def __init__(self, master=None):
       
        
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()        
        print'view initiated'
        self.Control = Control(view= self)        
        
    def notify(self,postname):
        self.txt.delete(1.0, END)
        print 'View got:', postname.get_status()
        self.txt.insert(END, str(postname.get_status()))
        #self.txt.insert(END, '2')

        
    def createWidgets(self):
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
        self.txt.pack(fill=BOTH, expand=1)
     
        self.txt.insert(END, '1')     
        self.txt.pack(side=LEFT)
   
    def say_hi(self):
        print "hi there, everyone!"
        
           
class Model(Publisher, threading.Thread):
    def __init__(self,url):
        Publisher.__init__(self)
        threading.Thread.__init__(self)
        self.i=0
        
    def run(self):
        print 'Model started to run'
        while True:
            self.i+=1
            self.postname=self
            self.notifyAll(self)
            time.sleep(3)
        
    def get_status(self):
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
          

    def notify(self,postname):
        print 'Control got:', postname.get_status()
 
    
if __name__ == "__main__":
    root = Tk()
    app = View(master=root)
    app.mainloop()
    root.destroy()
    
    
#    for i in range(60):
#        #print 'in loop'
#        time.sleep(1)

 