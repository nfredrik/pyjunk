import os
import sys
import shutil
from filestatus import FileStatus
from operator import itemgetter

OK,ERROR = 0, 1
DIRECTORYS = '.'
SAVEDAYS= 2

def enumeratedir(path):
    """Returns all the directories in a directory as a list"""
    dir_collection = [] 
    for dirpath, dirnames, filenames in os.walk(path):
        for dir in dirnames: dir_collection.append(dir)
    return dir_collection

def main(args):
    """
    Script to delete a number directories but saving latest ones, based on SAVDAYS.
    Nothing deleted if number directories are less than SAVEDAYS.
    """
    # Get the directories that need to be checked
    dirs = enumeratedir(DIRECTORYS)
    
    dir_list = []

    # Put them in a list of tuples, (name, date when created) 
    for dir in dirs:
        the_dir = FileStatus(dir)
        dir_list.append((dir,the_dir.get_creation_date()))
        
    # Sort list after date, oldest first    
    dir_list.sort(cmp=None, key=itemgetter(1), reverse=False)
    
    # Delete all _but_ SAVEDAYS
    if dir_list[:len(dir_list)-SAVEDAYS] and len(dir_list) > SAVEDAYS:
        for dir in dir_list[:len(dir_list)-SAVEDAYS]:
            print 'Want to delete:', dir[0]
            shutil.rmtree(dir[0])
    else:
        print 'Nothing to delete'
 
    return OK
 
if __name__ == '__main__':
    sys.exit(main(args=sys.argv[1:]))

