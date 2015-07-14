#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgintersection"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osg
from osgpypp import osgDB
from osgpypp import osgSim
from osgpypp import osgUtil


# Translated from file 'osgintersection.cpp'

# OpenSceneGraph example, osgintersection.
#*
#*  Permission is hereby granted, free of charge, to any person obtaining a copy
#*  of this software and associated documentation files (the "Software"), to deal
#*  in the Software without restriction, including without limitation the rights
#*  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#*  copies of the Software, and to permit persons to whom the Software is
#*  furnished to do so, subject to the following conditions:
#*
#*  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#*  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#*  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#*  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#*  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#*  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#*  THE SOFTWARE.
#

#include <osg/ArgumentParser>
#include <osg/ApplicationUsage>
#include <osg/Timer>
#include <osg/CoordinateSystemNode>
#include <osg/Notify>
#include <osg/io_utils>

#include <osgDB/ReadFile>

#include <osgUtil/IntersectionVisitor>
#include <osgUtil/LineSegmentIntersector>

#include <osgSim/LineOfSight>
#include <osgSim/HeightAboveTerrain>
#include <osgSim/ElevationSlice>

#include <iostream>

class MyReadCallback (osgUtil.IntersectionVisitor.ReadCallback) :
def readNodeFile(filename):
    
        return osgDB.readNodeFile(filename)



def main(argv):


    
    # use an ArgumentParser object to manage the program arguments.
    arguments = osg.ArgumentParser(argv)
    
    scene = osgDB.readNodeFiles(arguments)
    
    if  not scene : 
        print "No model loaded, please specify a valid model on the command line."
        return 0
    
    print "Intersection "
    
    
    bs = scene.getBound()


    useIntersectorGroup = True
    useLineOfSight = True
    
    #osg.CoordinateSystemNode* csn = dynamic_cast<osg.CoordinateSystemNode*>(scene)
    #osg.EllipsoidModel* em =  csn.getEllipsoidModel() if (csn) else  0

    if useLineOfSight :
    
        start = bs.center() + osg.Vec3d(0.0,bs.radius(),0.0)
        end = bs.center() - osg.Vec3d(0.0, bs.radius(),0.0)
        deltaRow = osg.Vec3d( 0.0, 0.0, bs.radius()*0.01)
        deltaColumn = osg.Vec3d( bs.radius()*0.01, 0.0, 0.0)

        los = osgSim.LineOfSight()
        
#if 1
        numRows = 20
        numColumns = 20
        hat = osgSim.HeightAboveTerrain()
        hat.setDatabaseCacheReadCallback(los.getDatabaseCacheReadCallback())

        for(unsigned int r=0 r<numRows ++r)
            for(unsigned int c=0 c<numColumns ++c)
                s = start + deltaColumn * double(c) + deltaRow * double(r)
                e = end + deltaColumn * double(c) + deltaRow * double(r)
                los.addLOS(s,e)
                hat.addPoint(s)


            print "Computing LineOfSight"

            startTick = osg.Timer.instance().tick()

            los.computeIntersections(scene)

            endTick = osg.Timer.instance().tick()

            print "Completed in ", osg.Timer.instance().delta_s(startTick,endTick)

            for(unsigned int i=0 i<los.getNumLOS() i++)
                intersections = los.getIntersections(i)
                for(osgSim.LineOfSight.Intersections.const_iterator itr = intersections.begin()
                    not = intersections.end()
                    ++itr)
                     print "  point ", *itr
        
            # now do a second traversal to test performance of cache.
            startTick = osg.Timer.instance().tick()

            print "Computing HeightAboveTerrain"

            hat.computeIntersections(scene)

            endTick = osg.Timer.instance().tick()

            for(unsigned int i=0 i<hat.getNumPoints() i++)
                 print "  point = ", hat.getPoint(i), " hat = ", hat.getHeightAboveTerrain(i)


            print "Completed in ", osg.Timer.instance().delta_s(startTick,endTick)
#endif

            # now do a second traversal to test performance of cache.
            startTick = osg.Timer.instance().tick()

            print "Computing ElevationSlice"
            es = osgSim.ElevationSlice()
            es.setDatabaseCacheReadCallback(los.getDatabaseCacheReadCallback())

            es.setStartPoint(bs.center()+osg.Vec3d(bs.radius(),0.0,0.0) )
            es.setEndPoint(bs.center()+osg.Vec3d(0.0,0.0, bs.radius()) )

            es.computeIntersections(scene)

            endTick = osg.Timer.instance().tick()

            print "Completed in ", osg.Timer.instance().delta_s(startTick,endTick)

            typedef osgSim.ElevationSlice.DistanceHeightList DistanceHeightList
            dhl = es.getDistanceHeightIntersections()
            print "Number of intersections =", dhl.size()
            for(DistanceHeightList.const_iterator dhitr = dhl.begin()
                not = dhl.end()
                ++dhitr)
                 std.cout.precision(10)
                 print "  ", dhitr.first, " ", dhitr.second


    elif useIntersectorGroup :
        startTick = osg.Timer.instance().tick()
    
        start = bs.center() + osg.Vec3d(0.0,bs.radius(),0.0)
        end = bs.center()# - osg.Vec3d(0.0, bs.radius(),0.0)
        deltaRow = osg.Vec3d( 0.0, 0.0, bs.radius()*0.01)
        deltaColumn = osg.Vec3d( bs.radius()*0.01, 0.0, 0.0)
        numRows = 20
        numColumns = 20

        intersectorGroup = osgUtil.IntersectorGroup()

        for(unsigned int r=0 r<numRows ++r)
            for(unsigned int c=0 c<numColumns ++c)
                s = start + deltaColumn * double(c) + deltaRow * double(r)
                e = end + deltaColumn * double(c) + deltaRow * double(r)
                intersector = osgUtil.LineSegmentIntersector(s, e)
                intersectorGroup.addIntersector( intersector )

        
        intersectVisitor = osgUtil.IntersectionVisitor( intersectorGroup, MyReadCallback )()
        scene.accept(intersectVisitor)

        endTick = osg.Timer.instance().tick()

        print "Completed in ", osg.Timer.instance().delta_s(startTick,endTick)

        if  intersectorGroup.containsIntersections()  :
            print "Found intersections "

            intersectors = intersectorGroup.getIntersectors()
            for(osgUtil.IntersectorGroup.Intersectors.iterator intersector_itr = intersectors.begin()
                not = intersectors.end()
                ++intersector_itr)
                lsi = dynamic_cast<osgUtil.LineSegmentIntersector*>(intersector_itr)
                if lsi :
                    intersections = lsi.getIntersections()
                    for(osgUtil.LineSegmentIntersector.Intersections.iterator itr = intersections.begin()
                        not = intersections.end()
                        ++itr)
                        intersection = *itr
                        print "  ratio ", intersection.ratio
                        print "  point ", intersection.localIntersectionPoint
                        print "  normal ", intersection.localIntersectionNormal
                        print "  indices ", intersection.indexList.size()
                        print "  primitiveIndex ", intersection.primitiveIndex
                        print std.endl
        

    else:
        startTick = osg.Timer.instance().tick()

    #if 1
        start = bs.center() + osg.Vec3d(0.0,bs.radius(),0.0)
        end = bs.center() - osg.Vec3d(0.0, bs.radius(),0.0)
    #else:
        start = bs.center() + osg.Vec3d(0.0,0.0, bs.radius())
        end = bs.center() - osg.Vec3d(0.0, 0.0, bs.radius())
    #endif

        intersector = osgUtil.LineSegmentIntersector(start, end)

        intersectVisitor = osgUtil.IntersectionVisitor( intersector, MyReadCallback )()

        scene.accept(intersectVisitor)

        endTick = osg.Timer.instance().tick()

        print "Completed in ", osg.Timer.instance().delta_s(startTick,endTick)

        if  intersector.containsIntersections()  :
            intersections = intersector.getIntersections()
            for(osgUtil.LineSegmentIntersector.Intersections.iterator itr = intersections.begin()
                not = intersections.end()
                ++itr)
                intersection = *itr
                print "  ratio ", intersection.ratio
                print "  point ", intersection.localIntersectionPoint
                print "  normal ", intersection.localIntersectionNormal
                print "  indices ", intersection.indexList.size()
                print "  primitiveIndex ", intersection.primitiveIndex
                print std.endl
    
    return 0


if __name__ == "__main__":
    main(sys.argv)
