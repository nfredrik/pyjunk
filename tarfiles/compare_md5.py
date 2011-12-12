import time
import tarfile
import sys
import os
from  memberfile import *

def invalid_file(tarinfo):
    return tarinfo.islnk() or tarinfo.ischr() or tarinfo.isblk() or tarinfo.isfifo() or tarinfo.isdev() 



args = sys.argv[1:]

print len(args), args
#sys.exit(42)

if len(args) != 2:
  print 'usage: <old-delivery.tar.gz file> <new-delivery.tar.gz file> '
  sys.exit(1)

dict_old_tar = {}
oldtar = tarfile.open(args[0], "r:gz")
for oldtarinfo in oldtar:
    if oldtarinfo.isdir():  continue

    filename = os.path.basename(oldtarinfo.name)
    if filename not in dict_old_tar:
        dict_old_tar[filename] = []

    dict_old_tar[filename].append(oldtarinfo.mtime)
    dict_old_tar[filename].append(oldtarinfo.size)
    dict_old_tar[filename].append(oldtarinfo.name)


dict_new_tar = {}

newtar = tarfile.open(args[1], "r:gz")

print ' '
print '------------------------'
print 'Modified files ...'
print '------------------------'

for tarinfo in newtar:
    if tarinfo.isdir(): continue
    filename = os.path.basename(tarinfo.name)

    # Build dict for new tar too
    if filename not in dict_new_tar:
        dict_new_tar[filename] = tarinfo.name        

    if filename in dict_old_tar:

        if not tarinfo.isfile():
            continue

        if dict_old_tar[filename][1] != tarinfo.size :
            print filename, ' has new size:', tarinfo.size, 'old:', dict_old_tar[filename][1], 

        oldfile = MemberFile(oldtar, dict_old_tar[filename][2])
        newfile = MemberFile(newtar, dict_new_tar[filename])

        if oldfile.get_md5() != newfile.get_md5():
            print filename,  ' md5'


    else:
        print 'new', filename

    if invalid_file(tarinfo):
        print 'we have an invalid file ...:', tarinfo.name
newtar.close()


print ' '
print '------------------------'
print 'Removed files ...'
print '------------------------'
for file in dict_old_tar:
    if file not in dict_new_tar:
        print file
