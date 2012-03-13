import unittest
import os
import types
from pcoobject import PcoObject

class TestPcoObject(unittest.TestCase):
    def test___init__(self):
        pass

    def setUp(self):
        unittest.TestCase.setUp(self)
        self.pco_object = PcoObject('PAOB.pco')
        assert True # TODO: implement your test here

    def test_get_filename(self):
        self.filename = 'PAOB.pco'
        self.assertEqual(os.path.splitext(self.filename)[0], self.pco_object.get_filename())

    def test_get_copys(self):
        # self.assertEqual(expected, self.pco_object.get_copys())
        assert isinstance(self.pco_object.get_copys(), list)

    def test_get_copys_system(self):
        assert isinstance(self.pco_object.get_copys_system(), list)

    def test_get_sql_include(self):
        assert isinstance( self.pco_object.get_sql_include(), list)

    def test_get_pot_rm_stuff(self):
        print 'No of comments:' , len(self.pco_object.get_pot_rm_stuff())
        assert isinstance(self.pco_object.get_pot_rm_stuff(), list)
if __name__ == '__main__':
    unittest.main()
