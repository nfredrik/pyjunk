import platform


# Implementor
class ListAPI:
    def list(self, includeHiddenFiles):
        raise NotImplementedError

    def ip_config(self):
        raise NotImplementedError

# ConcreteImplementor 1/2
class ListAPILinux(ListAPI):
    def list(self, includeHiddenFiles):

        if includeHiddenFiles:
            print('Linux list files included hidden ones')
        else:
            print('Linux list files')
        # use popen to list files, take of hidden files too..

    def ip_config(self):
        print('Linux showing some ip config stuff...')
    def __str__(self):
        return 'Linux'

# ConcreteImplementor 2/2
class ListAPIWindows(ListAPI):
    def list(self, includeHiddenFiles):
        raise NotImplementedError  # use popen to list files, take of hidden files too..



class Platform(object):
    '''# Make it possible to decide what operating system we are using'''

    operativ = {'Linux':ListAPILinux(), 'Darwin':ListAPILinux(), 'Windows':ListAPIWindows()}

    def __init__(self):
        self._os = self.operativ.get(platform.system(), None)
    def __call__(self):
        return self._os

# Abstraction
class List:
    # low-level
    def list(self):
        raise Exception

    # high-level
    def includeHiddenFiles(self):
        raise Exception



# Refined Abstraction
class ListFiles(List):
    def __init__(self):
        self._listAPI = Platform()
        self._includeHiddenFiles = False

    # low-level i.e. Implementation specific
    @property
    def list(self):
        self._listAPI().list(self._includeHiddenFiles)

    @property 
    def ip_config(self):
        self._listAPI().ip_config()

    # high-level i.e. Abstraction specific
    @property
    def includeHiddenFiles(self):
        self._includeHiddenFiles = True






#nisse = Platform()

#print(str(nisse))

listFiles = ListFiles()
listFiles.includeHiddenFiles
listFiles.list
listFiles.ip_config

