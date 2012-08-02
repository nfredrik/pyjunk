import unittest
from splay import SplayTree

#
# coverage erase; coverage run test_splay.py; coverage html -i
#

class TestCase(unittest.TestCase):
    def setUp(self):
        self.keys = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.t = SplayTree()
        for key in self.keys:
            self.t.insert(key)

    def testInsert(self):
        for key in self.keys:
            self.assertEquals(key, self.t.find(key))
            
        # Forgot in first phase, insert an elem in tree already there
        self.t.insert(self.keys[0])    

    def testRemove(self):
        for key in self.keys:
            self.t.remove(key)
            self.assertEquals(self.t.find(key), None)
        # Forgot to remove elem not in tree
        self.t.remove(-13)    

    def testLargeInserts(self):
        t = SplayTree()
        nums = 40000
        gap = 307
        i = gap
        while i != 0:
            t.insert(i)
            i = (i + gap) % nums

    def testIsEmpty(self):
        self.assertFalse(self.t.isEmpty())
        t = SplayTree()
        self.assertTrue(t.isEmpty())

    def testMinMax(self):
        self.assertEquals(self.t.findMin(), 0)
        self.assertEquals(self.t.findMax(), 9)
        # Forgot in first phase, check when there no element in tree
        t = SplayTree()
        self.assertEquals(t.findMin(), None)
        self.assertEquals(t.findMax(), None)
        
    def TearDown(self):
        del self.t

if __name__ == "__main__":
    unittest.main()