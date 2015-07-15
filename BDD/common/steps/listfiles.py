
# Implementor
class ListAPI:
    def list(self, includeHiddenFiles):
        raise Exception


# ConcreteImplementor 1/2
class ListAPILinux(ListAPI):
    def list(self, includeHiddenFiles):
        pass  # use popen to list files, take of hidden files too..

# ConcreteImplementor 1/2
class ListAPIWindows(ListAPI):
    def list(self, includeHiddenFiles):
        pass  # use popen to list files, take of hidden files too..


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
    def __init__(self, listAPI):
        self.__listAPI = listAPI
        self._includeHiddenFiles = False

    # low-level i.e. Implementation specific
    def list(self):
        self.__listAPI.list(self)

    # high-level i.e. Abstraction specific
    def includeHiddenFiles(self, pct):
        self._includeHiddenFiles = True