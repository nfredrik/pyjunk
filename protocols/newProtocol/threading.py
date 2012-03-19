import threading



class MyThread(threading.Thread):

    def __init__(self):
        print 'constructor'

    def run(self):
        print 'running'
        return

for i in range(5):
    t = MyThread()
    t.start()
