import os
import sys
import shutil
from filestatus import FileStatus
from command import Command
from operator import itemgetter

OK, ERROR = 0, 1

DIRECTORYS = '.'
SAVEDAYS=2

def enumeratedir(path):
    """Returns all the directories in a directory as a list"""
    dir_collection = [] 
    for dirpath, dirnames, filenames in os.walk(path):
        for dir in dirnames: dir_collection.append(dir)
    return dir_collection


def main(args):

    # Get the directories that need to be checked
    dirs = enumeratedir(DIRECTORYS)
    
    dir_list = []

    # Put them in a list of tuples, (name, date when created) 
    for dir in dirs:
        the_dir = FileStatus(dir)
        dir_list.append((dir,the_dir.get_creation_date()))
        
    # Sort list after date, oldest first    
    dir_list.sort(cmp=None, key=itemgetter(1), reverse=False)
    
    
    # Print infomation of list
    print dir_list   
    print dir_list[:len(dir_list)-SAVEDAYS]
    rm_dir_list = dir_list[:len(dir_list)-SAVEDAYS]    
    
    # Delete all but youngest days
    if dir_list[:len(dir_list)-SAVEDAYS]:
        for dir in dir_list[:len(dir_list)-SAVEDAYS]:
            print 'Want to delete:', dir[0]
            #shutil.rmtree()
 
    return OK
 
 
if __name__ == '__main__':
    sys.exit(main(args=sys.argv[1:]))

