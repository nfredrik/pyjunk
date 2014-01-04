
# The Context Management Protocol

class TraceBlock:
    def message(self, arg):
        print('running ' + arg)
        
    # The context managers' is called first in block. Value, in this case 'self', 
    # return to the variable in the 'as' clause    
    def __enter__(self):
        print('starting with block')
        return self
    
    # Returns None if normal else return False to raise and exception!
    def __exit__(self, exc_type, exc_value, exc_tb):
        if exc_type is None:
            print('exited normally\n')
        else:
            print('raise an exception! ' + str(exc_type))
            return False    # Propagate

if __name__ == '__main__':
    with TraceBlock() as action:  
        action.message('test 1')
        print('reached end test 1')
        action.message('test 1.5')
        print('reached test 1.5')

    with TraceBlock() as action:
        action.message('test 2')
        raise TypeError
        print('not reached')
