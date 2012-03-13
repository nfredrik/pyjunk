import unittest
from infoobject import InfoObject

class TestInfoObject(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)
        self.info_object = InfoObject('JANNE', ['hej', 'hopp'])
        assert True # TODO: implement your test here

    def test_add_copys(self):
        # info_object = InfoObject(filename)
        self.info_object.add_copys('PRUTT', 'BAJS')
        assert True # TODO: implement your test here

    def test_add_sql_includes(self):
        # info_object = InfoObject(filename)
#        self.info_object.add_copys('BAJA')
#        self.info_object.add_copys('BAJA')
        self.info_object.add_sql_includes('SKIT')
        assert True # TODO: implement your test here

    def test_pelle(self):
        self.info_object = InfoObject('PELLE', ['hej', 'hopp'])
        self.info_object.add_copys('FIS','BAJS')
        self.info_object.add_copys_system('GUL')
        self.info_object.add_sql_includes('SKIT')
        assert True

if __name__ == '__main__':
    unittest.main()
