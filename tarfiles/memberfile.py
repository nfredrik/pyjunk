import hashlib
import tarfile

class MemberFile(object):

    def __init__(self, tarfile, file):
        self.fh = tarfile.extractfile(file)
#        self.hsh = hashlib.new('ripemd160')
        self.hsh = hashlib.md5()
        self.data = self.fh.read(100*1024)
        while self.data :
            self.hsh.update(self.data)
            self.data = self.fh.read(100*1024)

    def get_md5(self):
        return self.hsh.hexdigest()
