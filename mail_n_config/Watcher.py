import os
from watchdog.events import FileSystemEventHandler


class MyEventHandler(FileSystemEventHandler):
    """Custom EventHandler"""
    def __init__(self, logging, callback, file2change):
        self.logging = logging
        self.callback = callback
        self.file2change = file2change
    def catch_all_handler(self, event):
#        self.logging.debug(event)
#         print 'EventHandler called!'
        pass

    def on_moved(self, event):
        self.catch_all_handler(event)

    def on_created(self, event):
        self.catch_all_handler(event)

    def on_deleted(self, event):
        self.catch_all_handler(event)

    def on_modified(self, event):
        global ext
        self.catch_all_handler(event)
#        print 'EventHandler got:', event.event_type        
        if not event.is_directory:
            print 'EventHandler sr_path::', os.path.basename(event.src_path)
            self.callback()
        if os.path.basename(event.src_path) == self.file2change :
            print 'this is cool'
#        fileextension = os.path.splitext(event.src_path)[-1]
#        if fileextension in extensions.split(';'):
#            pass

