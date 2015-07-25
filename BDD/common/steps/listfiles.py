import os
import platform
import subprocess


''' TODO: 
          - Return result as list? or?...
          - set and get current working directory
'''

# Implementor
class ListAPI:
    def list_impl(self, includeHiddenFiles):
        raise NotImplementedError

    def ip_config_impl(self):
        raise NotImplementedError

    def set_cwd(self):
        raise NotImplementedError

    def get_cwd(self):
        raise NotImplementedError

# ConcreteImplementor 1/2
class ListAPILinux(ListAPI):
    def list_impl(self, includeHiddenFiles):

        if includeHiddenFiles:
            print('Linux list files included hidden ones')
        else:
            print('Linux list files')
            print(os.listdir())

    def ip_config_impl(self):
        print('Linux showing some ip config stuff...')
    def __str__(self):
        return 'Linux'

# ConcreteImplementor 2/2
class ListAPIWindows(ListAPI):
    def list_impl(self, includeHiddenFiles):
        if includeHiddenFiles:
            print('Windows list files included hidden ones')
            print (os.listdir())            
            return os.listdir()   # return a list of files.
        else:
            print('Windows list files')
            visible = [f for f in os.listdir() if not f.startswith('.')]
            print (visible)
            return visible   # return a list of files.

            #nn = subprocess.call(["dir"], shell=True)   # Successful execution with exit code 0
            # ll = subprocess.check_output(['dir'], shell=True)
            # print ('Have %d bytes in output' % len(ll))

    def ip_config_impl(self):
        print('Windows showing some ip config stuff...')
        from uuid import getnode as get_mac
        mac = get_mac()



class Platform(object):
    '''Make it possible to decide what operating system we are using'''

    operativ = {'Linux':ListAPILinux(), 'Darwin':ListAPILinux(), 'Windows':ListAPIWindows()}

    def __init__(self):
        self._os = self.operativ.get(platform.system(), None)
    def __call__(self):
        return self._os

# Abstraction
class List:
    # low-level
    def list(self):
        raise NotImplementedError

    # high-level
    def includeHiddenFiles(self):
        raise NotImplementedError


# Refined Abstraction
class ListFiles(List):
    def __init__(self):
        self._listAPI = Platform()
        self._includeHiddenFiles = False

    # low-level i.e. Implementation specific
    @property
    def list(self):
        self._listAPI().list_impl(self._includeHiddenFiles)

    @property 
    def ip_config(self):
        self._listAPI().ip_config_impl()

    # high-level i.e. Abstraction specific
    @property
    def includeHiddenFiles(self):
        self._includeHiddenFiles = True




if __name__ == '__main__':

    listFiles = ListFiles()
    listFiles.list

    listFiles.includeHiddenFiles
    listFiles.list

    listFiles.ip_config

