#!/usr/bin/python

import time
import sys
import os
from  memberfile import *

#path = '~/test'

def invalid_file(tarinfo):
    return tarinfo.islnk() or tarinfo.ischr() or tarinfo.isblk() or tarinfo.isfifo() or tarinfo.isdev() 

def enumeratepaths(path): 
    """Returns the path to all the files in a directory recursively""" 
    path_collection = []
    for dirpath, dirnames, filenames in os.walk(path):
        for file in filenames:
            fullpath = os.path.join(dirpath, file) 
            path_collection.append(fullpath)
    return path_collection


def get_md5( file):
    fh = open(file)
    hsh = hashlib.md5()
    data = fh.read(100*1024)
    while data :
        hsh.update(data)
        data = fh.read(100*1024)

    fh.close()
    return hsh.hexdigest()



def main():



    args = sys.argv[1:]

    if len(args) != 2:
        print 'usage: <new-delivery.tar.gz file> <path to directory>'
        sys.exit(1)

    if not os.path.exists(args[0]):
        print 'Did not find tarfile!'
        sys.exit(1)

    if not os.path.isdir(args[1]):
        print 'Did not find directory!'
        sys.exit(1)

    import tarfile

    dict_old_tar = {}
    oldtar = tarfile.open(args[0], "r:gz")

    for oldtarinfo in oldtar:
        if oldtarinfo.isdir():  continue

        filename = os.path.basename(oldtarinfo.name)

        if filename not in dict_old_tar:
            dict_old_tar[filename] = []
            dict_old_tar[filename].append(1)
        else:
            dict_old_tar[filename][0] += 1

        dict_old_tar[filename].append(oldtarinfo.mtime)
        dict_old_tar[filename].append(oldtarinfo.size)
        dict_old_tar[filename].append(oldtarinfo.name)


    dict_new_tar = {}

    list_of_files = enumeratepaths(args[1])
    print ' '
    print '------------------------'
    print 'In tar file ...'
    print '------------------------'


    for filepath in list_of_files:
        if os.path.isdir(filepath): continue
        
        filename = os.path.basename(filepath)


    # Build dict for new 'list of files' too
        if filename not in dict_new_tar:
            dict_new_tar[filename] = []                
            dict_new_tar[filename].append(filepath)
        else:
            dict_new_tar[filename].append(filepath)


        if filename in dict_old_tar:
   
            tarfile = MemberFile(oldtar, dict_old_tar[filename][3])
            svnfile_md5 = get_md5(dict_new_tar[filename][0])

            print filepath,
            if tarfile.get_md5() == svnfile_md5:
                print ' has _NOT_ changed!!'
            else:
                print ' has changed!!'

    print ' '
    print '------------------------'
    print 'New files ...'
    print '------------------------'
    for file in dict_old_tar:
        if file not in dict_new_tar:
            print dict_old_tar[file][3]
            if dict_old_tar[file][0] != 1:
#        print 'more files:'
                i = dict_old_tar[file][0]  
                print dict_old_tar[file][6]

if __name__ == '__main__':
  main()
