				
#!/usr/bin/python
import sys, time
#from Tkinter import *
import Tkinter
class Logger(Tkinter.Frame):
    def __init__(self):
        Tkinter.Frame.__init__(self)
        self.pack(expand=Tkinter.YES, fill=Tkinter.BOTH)
        self.master.title("Timestamp logging application")
        self.tslist = []
        self.tsdisp = Tkinter.Text(height=20, width=25)
        self.count = Tkinter.StringVar()
        self.cntdisp = Tkinter.Message(font=('Sans',24),
                               textvariable=self.count)
        self.log = Tkinter.Button(text="Log Timestamp",
                          command=self.log_timestamp)
        self.quit = Tkinter.Button(text="Quit", command=sys.exit)
        self.tsdisp.pack(side=Tkinter.LEFT)
        self.cntdisp.pack()
        self.log.pack(side=Tkinter.TOP, expand=Tkinter.YES, fill=Tkinter.BOTH)
        self.quit.pack(side=Tkinter.BOTTOM, fill=Tkinter.BOTH)
    def log_timestamp(self):
        stamp = time.ctime()
        self.tsdisp.insert(Tkinter.END, stamp+"\n")
        self.tsdisp.see(Tkinter.END)
        self.tslist.append(stamp)
        self.count.set("% 3d" % len(self.tslist))

if __name__=='__main__':
    Logger().mainloop()
    
