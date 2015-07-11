#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgkdtree"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osg
from osgpypp import osgDB
from osgpypp import osgSim
from osgpypp import osgUtil
from osgpypp import osgViewer

# OpenSceneGraph example, osgintersection.
*
*  Permission is hereby granted, free of charge, to any person obtaining a copy
*  of this software and associated documentation files (the "Software"), to deal
*  in the Software without restriction, including without limitation the rights
*  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
*  copies of the Software, and to permit persons to whom the Software is
*  furnished to do so, subject to the following conditions:
*
*  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
*  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
*  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
*  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
*  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
*  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
*  THE SOFTWARE.


  
#include <osgDB/ReadFile>

#include <osg/ArgumentParser>
#include <osg/ApplicationUsage>
#include <osg/Timer>
#include <osg/CoordinateSystemNode>
#include <osg/Notify>
#include <osg/io_utils>
#include <osg/Geometry>
#include <osg/TriangleIndexFunctor>


#include <osgUtil/IntersectionVisitor>
#include <osgUtil/LineSegmentIntersector>
#include <osgUtil/UpdateVisitor>

#include <osgSim/LineOfSight>
#include <osgSim/HeightAboveTerrain>
#include <osgSim/ElevationSlice>

#include <osgViewer/Viewer>

#include <osg/KdTree>

#include <iostream>

def main(argc, argv):
    # use an ArgumentParser object to manage the program arguments.
    arguments = osg.ArgumentParser(argc,argv)
    
    maxNumLevels =  16
    targetNumIndicesPerLeaf =  16

    while arguments.read("--max", maxNumLevels) : 
    while arguments.read("--leaf", targetNumIndicesPerLeaf) : 
    
    osgDB.Registry.instance().setBuildKdTreesHint(osgDB.ReaderWriter.Options.BUILD_KDTREES)
    
    osg.ref_ptr<osg.Node> scene = osgDB.readNodeFiles(arguments)
    
    if !scene : 
        print "No model loaded, please specify a valid model on the command line."
        return 0

    viewer = osgViewer.Viewer()
    viewer.setSceneData(scene.get())
    return viewer.run()


if __name__ == "__main__":
    main(sys.argv)
