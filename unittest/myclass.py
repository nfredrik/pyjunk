


class MyClass(object):
    def __init__(self):
        self.data = None

    def readData(self, source):
        self.data = source.read()
        source.close()

    def synchronise(self):
        source = self.getDataSource()
        self.readData(source)
        self.store()
