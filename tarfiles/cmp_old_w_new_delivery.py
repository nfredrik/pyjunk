import time
import tarfile
import sys

args = sys.argv[1:]

#sys.exit(42)

if len(args) != 2:
  print 'usage: <old-delivery.tar.gz file> <new-delivery.tar.gz file> '
  sys.exit(1)

dict_old_tar = {}
oldtar = tarfile.open(args[0], "r:gz")
for tarinfo in oldtar:
    if tarinfo.name not in dict_old_tar:
        dict_old_tar[tarinfo.name] = []

    dict_old_tar[tarinfo.name].append(tarinfo.mtime)
    dict_old_tar[tarinfo.name].append(tarinfo.size)

oldtar.close()


newtar = tarfile.open(args[1], "r:gz")
for tarinfo in newtar:

    if tarinfo.name in dict_old_tar:
        if dict_old_tar[tarinfo.name][0] != tarinfo.mtime :
            print tarinfo.name, 'has been modified:', time.ctime(tarinfo.mtime), 'old:', time.ctime(dict_old_tar[tarinfo.name][0])

        if dict_old_tar[tarinfo.name][1] != tarinfo.size :
            print tarinfo.name, 'has new size:', tarinfo.size, 'old:', dict_old_tar[tarinfo.name][1]

    else:
        print 'new file:', tarinfo.name

newtar.close()


