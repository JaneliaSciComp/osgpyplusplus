from osgpyplusplus import osg
import unittest

class TestVec3(unittest.TestCase):
    def test_version(self):
        version = osg.osgGetVersion()
        self.assertTrue(len(version) > 0)

if __name__ == '__main__':
    unittest.main()
