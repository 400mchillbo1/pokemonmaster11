import unittest
from game import kin_count
class test(unittest.TestCase):
    def testcount1(self):
        rv=kin_count()
        self.assertGreaterEqual(rv,0)
    def testcontnone(self):
        rev=kin_count()
        self.assertIsNotNone(rev)
    def testcount2(self):
        rtv=kin_count()
        self.assertLessEqual(rtv,8)
    if __name__ == '__main__':
        unittest.main()


