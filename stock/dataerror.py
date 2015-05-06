''' Inherit Base class to be able to raise own defined exceptions '''
class DataError(Exception): pass

class NDataError(Exception):
    """
    Example for an own Exception with its own constructor and instance
    variables. It also has its own `__str__` and related methods to show
    details about the exception. Furthermore there is a `__cmp__` to sort
    multiple exceptions, in this case by file name and location.
    """
    def __init__(self, message, path, line=None, column=None):
        assert message is not None
        assert path is not None
        Exception.__init__(self, message)
        self._message = message
        self._path = path
        self._line = line
        self._column = column

    @property
    def path(self):
        return self._path

    @property
    def line(self):
        return self._line

    @property
    def column(self):
        return self._column

    def __str__(self):
        result = os.path.basename(self.path)
        if self.line is not None:
            result += ' (%d' % self.line
            if self.column is not None:
                result += ':%d' % self.column
            result += ')'
        result += ': %s' % self._message
        return result
