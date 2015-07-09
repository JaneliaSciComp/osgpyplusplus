from osgpypp import osgUtil
import unittest

class TestOsgAddRangeOperator(unittest.TestCase):
    def test_classAvailable(self):
        s = osgUtil.AddRangeOperator()

if __name__ == '__main__':
    unittest.main()
