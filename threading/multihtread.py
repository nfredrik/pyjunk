from threading import Thread
from multiprocessing import Queue
from queue import Empty     # queue instead of Queue!!
from time import sleep
import logging


logging.basicConfig(level=logging.DEBUG, format='%(message)s')


class MyThread(Thread):
    """My worker thread"""

    def __init__(self, logger, queue, name, delay):
        """Ctor"""
        Thread.__init__(self)
        self.q = queue
        self.delay = delay
        self.name = name
        self.logger = logger
        self.log("I am alive !")

    def start(self):
        self.log("Starting")
        Thread.start(self)

    def log(self, message):
        """Do some logging"""
        self.logger("    {}  -- {}".format(self.name, message))

    def work(self, item):
        """"Do the real work"""
        self.log("Working on item %s"% item)
        #sleep(self.delay * 0.77)
        return item > 0

    def run(self):
        """Work loop"""
        alive = True
        while alive:
            try:
                item = self.q.get_nowait()
                alive = self.work(item)
            except Empty:
                self.log("No job for me.")
                #sleep(self.delay * 3.13)
        self.log("I am Done")

if __name__ == "__main__":
    logger = logging.debug
    q = Queue()

    def mylog(message):
        logger("%s"%message)

    names = ['Fyodor', 'Mordor', 'Terminator']
    delays = [1, 0.7, 0.47]
    threads = list()

    mylog("Spawning threads")
    
    for i in range(3):
        t = MyThread(logger, q, names[i], delays[i])
        threads.append(t)
    #sleep(1.7)

    mylog("Start the threads")
    for thread in threads:
        thread.start()

    #sleep(4.7)

    mylog("Add some jobs, the allow some jobs to finish")

    for n in range(100, 170, 9):
        q.put(n)
    #sleep(2.2)

    mylog("Kill threads (once all jobs are done")

    for _ in threads:
        q.put(-1)



