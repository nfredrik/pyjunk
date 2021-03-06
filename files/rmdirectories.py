import os
import sys
import shutil
import logging
import logging.handlers
from filestatus import FileStatus
from operator import itemgetter

OK,ERROR = 0, 1
DIRECTORYS = '.'
SAVEDAYS= 2
LOG_FILENAME= 'logfile.log'
MAX_LOGFILE_BYTES = 20000
MAX_LOGFILES=3

def enumeratedir(path):
    """Returns all the directories in a directory as a list"""
    dir_collection = [] 
    for dirpath, dirnames, filenames in os.walk(path):
        for dir in dirnames: dir_collection.append(dir)
    return dir_collection

def main(args):
    """
    Script to delete a number directories but saving latest ones, i.e. SAVEDAYS.
    Nothing deleted if number directories are less or equal than SAVEDAYS.
    """
    
    # Configure how logging should be presented
    logging.basicConfig(level=logging.DEBUG,
                    format='%(name)s: %(message)s',
                    )
    
    # Create logger instance
    logger = logging.getLogger('removing directories')
    
    # Add the log message handler to the logger
    #handler = logging.handlers.RotatingFileHandler(LOG_FILENAME,
    #                                           maxBytes=MAX_LOGFILE_BYTES,
    #                                           backupCount=MAX_LOGFILES,
    #                                           )
    #logger.addHandler(handler)
    
    # Get the directories that need to be checked
    logger.debug('Get directories')
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
            logger.debug('Want to delete: %s', dir[0])
            # Ignore error handling if we should fail to delete
            shutil.rmtree(dir[0],ignore_errors=True)
    else: 
        logger.debug('Nothing to delete:')
        for dir in dir_list:
            logger.debug('We got: %s',dir[0])
 
    return OK

#
# TODO: Decide, make this a jenkins job or cron?

if __name__ == '__main__':
    sys.exit(main(args=sys.argv[1:]))

