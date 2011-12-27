import unittest
from mock import Mock, sentinel

from myclass import MyClass

class TestMyClass(unittest.TestCase):

    def testSynchronise(self):
        myclass = MyClass()

        # put the monkey patching in place
        myclass.getDataSource = Mock()
        myclass.getDataSource.return_value = sentinel.DataSource

        myclass.readData = Mock()
        myclass.store = Mock()

        # make the call
        myclass.synchronise()

        # assertions
        self.assertTrue(myclass.getDataSource.called)
        myclass.readData.assert_called_with(sentinel.DataSource)
        self.assertTrue(myclass.store.called)

if __name__ == '__main__':
    unittest.main()
