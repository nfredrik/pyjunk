import os
import tarfile

def txt_files(members):
    for tarinfo in members:
        if os.path.splitext(tarinfo.name)[1] == ".txt":
            yield tarinfo

tar = tarfile.open("sample.tar.gz")
tar.extractall(members=txt_files(tar))
tar.close()
