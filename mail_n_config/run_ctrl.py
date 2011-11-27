from DataObject import *
from Protocol import *
from TrafficGenerator import *

import time
import logging
import threading
from Mail import Mail
from ConfigParser import SafeConfigParser
from Watcher import MyEventHandler
from watchdog.observers import Observer

CONFIG_FILENAME = 'config.ini'

FILEWATCH_DIR = './watch'

event = threading.Event()
event.clear()

# Call this routine if the info file has changed
def on_file_change():
    event.set()
    logging.debug('on_file_changed called')

# Read the configuration file for mail and logfile settings
parser = SafeConfigParser()
parser.read(CONFIG_FILENAME)

logger = logging.basicConfig(filename=parser.get('logging', 'logfile'),
                             level=logging.DEBUG)

# Prepare in case we need to send a mail if failure
mail = Mail(parser.get('mail', 'to'),
            parser.get('mail', 'username'),
            parser.get('mail', 'password'),
            parser.get('mail', 'smtpserver'),
           )

# Setup a file event handler
event_handler = MyEventHandler(logger, on_file_change, file2change = 'nisse.txt')
observer = Observer()
observer.schedule(event_handler, FILEWATCH_DIR, recursive=True)
observer.start()

# FIXME : Create a data object
io = NewLoopDataObject()

# FIXME : Create a protocol
protocol = Protocol(io)

generator = TrafficGenerator(protocol, logger)
# FIXME : Create an instance of a traffic generator

try:
    while True:
        time.sleep(1)
        if event.isSet():
            # FIXME: implement a protocol to send a message to the printer over a
            #        serial line 
            print parser.get('printer', 'message')
            generator.generatePrintStatus()
            event.clear() 

except KeyboardInterrupt:
    observer.stop()
# FIXME: if NACK raise a exception
except Exception, e:
    mail.send('Failed to communicate with the printer')
    logging.debug('Failed to communicate with the printer')

observer.join()
