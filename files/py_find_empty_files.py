from command import Command
import os
from stat import *

def main():

    hash = {}
   
    ls_obj = Command('find .')

    for filepath in ls_obj.get_list_output():
        mode = os.stat(filepath).st_mode
        if S_ISREG(mode):
            (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(filepath)
            if not size:
                print filepath, 'is empty' 

if __name__ == "__main__":
  main()
