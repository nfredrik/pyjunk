

import time

from ConfigParser import SafeConfigParser
from Watcher import MyEventHandler


CONFIG_FILENAME = 'config.ini'

FILEWATCH_DIR = './watch'


# Call this routine if the info file has changed
def on_file_change():
    event.set()
    logging.debug('on_file_changed called')

# Read the configuration file for mail and logfile settings
parser = SafeConfigParser()
parser.read(CONFIG_FILENAME)


# Setup a file event handler
event_handler = MyEventHandler(on_file_change, file2change = 'nisse.txt')


try:
    while True:
        time.sleep(5)
        print 'pong' 

except KeyboardInterrupt:
    print 'keyboard interrupt'
# FIXME: if NACK raise a exception
except Exception, e:
    print 'Other interrupt' 


if __name__ == '__main__':
  sys.exit(main(sys.args[1:]))

