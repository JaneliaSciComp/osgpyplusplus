from osgpypp import osg, osgDB
import unittest

class TestOsgStateSet(unittest.TestCase):
    def test_classAvailable(self):
        g = osg.GraphicsCostEstimator()
       
    def test_resultTypes(self):
        g = osg.GraphicsCostEstimator()
        node = osg.Node()
        g.estimateCompileCost(node)

if __name__ == '__main__':
    unittest.main()
