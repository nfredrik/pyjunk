#!/usr/bin/python
import sys
import os
import re
def enumeratepaths(path): 
    """Returns the path to all the files in a directory recursively""" 
    path_collection = []
    for dirpath, dirnames, filenames in os.walk(path):
        for file in filenames:
            fullpath = os.path.join(dirpath, file) 
            path_collection.append(fullpath)
    return path_collection


def main():

    args = sys.argv[1:]

    if len(args) != 1:
        print 'usage: <path to directory>'
        sys.exit(1)

    if not os.path.exists(args[0]):
        print 'Did not find directory!'
        sys.exit(1)


    list_of_files = enumeratepaths(args[0])
    print '------------------------'

    for filepath in list_of_files:
        if os.path.isdir(filepath): continue
        
#        print filepath
        (path,filename) = os.path.split(filepath)

        # Check if IPF file AND  no extension *.pl OR digits
        if re.match("[A-Z0-9]+IPF[A-Z0-9]+$",  filename):
            # Rename file with extention *.pl
            print 'found *.pl candidate',  filename
            print filepath, ' to', path+ '/' + filename + '.pl'
            os.rename(filepath, path + '/' + filename + '.pl')
        elif re.match("[A-Z0-9]+$",  filename):
        # Else Check if file with no extention
            # Rename file with extention *.sh
            print 'found *.sh candidate',  filename
            os.rename(filepath, path + '/' + filename + '.sh')




if __name__ == '__main__':
  main()
