from osgpypp import osg
import unittest

class TestOsgStateSet(unittest.TestCase):
    def test_classAvailable(self):
        s = osg.StateSet()

    def test_enumsAvailable_partial(self):
        #Functions
        osg.StateSet.INHERIT_RENDERBIN_DETAILS
        osg.StateSet.USE_RENDERBIN_DETAILS
        osg.StateSet.OVERRIDE_RENDERBIN_DETAILS
       
    def test_methodsAvailable(self):
        #todo
        s = osg.StateSet()
        s.setRenderBinDetails(1, 'test')

if __name__ == '__main__':
    unittest.main()
