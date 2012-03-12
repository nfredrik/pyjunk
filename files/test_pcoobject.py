import unittest
from pcoobject import PcoObject

class TestPcoObject(unittest.TestCase):
    def test___init__(self):
        pass

    def setUp(self):
        unittest.TestCase.setUp(self)
        self.pco_object = PcoObject('PAOB.pco')
        assert True # TODO: implement your test here

    def test_get_filename(self):
        # pco_object = PcoObject(filename)
        # self.assertEqual(expected, pco_object.get_filename())
#        pco_object = PcoObject('PAOB.pco')
        print 'Hurra:', self.pco_object.get_filename()
        assert False # TODO: implement your test here

    def test_get_copys(self):
        # self.assertEqual(expected, pco_object.get_copys())
        print 'COPYS:' + '-' * 40
        print self.pco_object.get_copys()
        assert True # TODO: implement your test here

    def test_get_copys_system(self):
        print 'COPYS SYSTEM:' + '-' * 40
        print self.pco_object.get_copys_system()
        assert True # TODO: implement your test here

    def test_get_number_of_rows(self):
        # pco_object = PcoObject(filename)
        # self.assertEqual(expected, pco_object.get_number_of_rows())
        assert True # TODO: implement your test here

    def test_get_sql_include(self):
        # pco_object = PcoObject(filename)
        print 'INCLUDES:' + '-' * 40
        print self.pco_object.get_sql_include()
        assert True # TODO: implement your test here

if __name__ == '__main__':
    unittest.main()
