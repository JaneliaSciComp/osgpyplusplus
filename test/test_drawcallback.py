from osgpypp import osg
import unittest

class TestDrawCallback(unittest.TestCase):
    def test_classAvailable(self):
        # Create derived class to test abstract base class DrawCallback
        class Foo(osg.Camera.DrawCallback):
            pass

if __name__ == '__main__':
    unittest.main()
