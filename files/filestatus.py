import os
from stat import *

class FileStatus(object):

    def __init__(self, filepath):
        (self.mode, self.ino, self.dev, self.nlink, self.uid, self.gid, self.size, self.atime, self.mtime, self.ctime) = os.stat(filepath)

    def regular_file(self):
        return S_ISREG(self.mode)
    def invalid_file(self):
        return not S_ISREG(self.mode) and not S_ISDIR(self.mode) 
    def executable(self):
        return S_IMODE(self.mode) & ( S_IXUSR | S_IXGRP | S_IXOTH)
    def size_of(self):
        return self.size
    
    def get_creation_date(self):
        return self.mtime
