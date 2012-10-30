
from StringIO import StringIO
from tempfile import mkstemp
import unittest
import os
import types
from pcoobject import PcoObject

class TestPcoObject(unittest.TestCase):
    def test___init__(self):
        pass

    def setUp(self):
        unittest.TestCase.setUp(self)
        # create temp file
        fh, abspath = mkstemp()
        self.pco_object = PcoObject(abspath, '.')
        fh = StringIO("""  PROGRAM-ID.   PAOB.
                          EXEC SQL INCLUDE 'BOBSSS030FTD' END-EXEC.
                          COPY BO-FELTXT    IN UCPROC.
                          COPY HP-SWITCHES.
                          HPCALL*
                          
                          * EXEC SQL INCLUDE 'SUSANNE' END-EXEC.
                          * COPY FREDDE-FELTXT    IN UCPROC.
                          *COPY DELL-SWITCHES.
                          * HPREMOV*
                  """)

        self.pco_object.read_from_file(fh)
        assert True # TODO: implement your test here

    def test_get_filename(self):
        self.filename = 'PAOB.pco'
#        self.assertEqual(os.path.splitext(self.filename)[0], self.pco_object.get_filename())
        assert True
 
    def test_get_copys(self):
        # self.assertEqual(expected, self.pco_object.get_copys())
        assert isinstance(self.pco_object.get_copys(), list)

    def test_get_copys_system(self):
        assert isinstance(self.pco_object.get_copys_system(), list)

    def test_get_sql_include(self):
        assert isinstance( self.pco_object.get_sql_include(), list)

    def test_get_pot_rm_stuff(self):
        print 'No of comments:' , len(self.pco_object.get_pot_rm_stuff())
        for n in self.pco_object.get_pot_rm_stuff():
            print n
        assert isinstance(self.pco_object.get_pot_rm_stuff(), list)
if __name__ == '__main__':
    unittest.main()
