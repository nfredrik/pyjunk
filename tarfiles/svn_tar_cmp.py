import time
import tarfile
import sys
import os
from  memberfile import *
from command import Command

#path = '~/test'

def invalid_file(tarinfo):
    return tarinfo.islnk() or tarinfo.ischr() or tarinfo.isblk() or tarinfo.isfifo() or tarinfo.isdev() 


def enumeratefiles(path):
    """Returns all the files in a directory as a list""" 
    file_collection = [] 
    for dirpath, dirnames, filenames in os.walk(path):
        for file in filenames: 
            file_collection.append(file)
    return file_collection

def get_md5( file):
    fh = open(file)
    hsh = hashlib.md5()
    data = fh.read(100*1024)
    while data :
        hsh.update(data)
        data = fh.read(100*1024)

    fh.close()
    return hsh.hexdigest()



args = sys.argv[1:]

#print len(args), args
#sys.exit(42)

if len(args) != 2:
  print 'usage: <new-delivery.tar.gz file> <path to directory>'
  sys.exit(1)

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

#newtar = tarfile.open(args[1], "r:gz")
#list_of_files = enumeratefiles(args[1])
#list_of_files = enumeratefiles(args[1])
print ' '
print '------------------------'
print 'In tar file ...'
print '------------------------'

cmd = Command('find ' + args[1])



for filepath in cmd.get_list_output():
#for filepath in list_of_files:
    if os.path.isdir(filepath): continue
    filename = os.path.basename(filepath)

    # Build dict for new 'list of files' too
    if filename not in dict_new_tar:
        dict_new_tar[filename] = []                
        dict_new_tar[filename].append(filepath)
    else:
        dict_new_tar[filename].append(filepath)

#    print 'dict_new_tar', dict_new_tar

    if filename in dict_old_tar:
   
#        print "HURRA:",  dict_new_tar[filename]
        tarfile = MemberFile(oldtar, dict_old_tar[filename][3])
        svnfile_md5 = get_md5(dict_new_tar[filename][0])

#    if dict_old_tar[filename][1] != tarinfo.size :
#            print filename, ' has new size:', tarinfo.size, 'old:', dict_old_tar[filename][1], 

        print filepath,
        if tarfile.get_md5() != svnfile_md5:
            print ' has changed'
        else:
            print ' has _NOT_ changed!!'


print ' '
print '------------------------'
print 'New files ...'
print '------------------------'
for file in dict_old_tar:
    if file not in dict_new_tar:
        print dict_old_tar[file][3]
        if dict_old_tar[file][0] !=1:
#            print 'more files:'
            i = dict_old_tar[file][0]  
            print dict_old_tar[file][6]
