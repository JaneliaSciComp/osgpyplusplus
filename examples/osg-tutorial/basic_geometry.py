#!/bin/env python

# Translated into python from C++ tutorial at
# http:#trac.openscenegraph.org/projects/osg/wiki/Support/Tutorials/BasicGeometry

from osgpypp import osg


def main():
    root = osg.Group()
    pyramidGeode = osg.Geode()
    pyramidGeometry = osg.Geometry()
    pyramidGeode.addDrawable(pyramidGeometry) 
    root.addChild(pyramidGeode)
    pyramidVertices = osg.Vec3Array()
    pyramidVertices.append( osg.Vec3( 0, 0, 0) ) # front left
    pyramidVertices.append( osg.Vec3(10, 0, 0) ) # front right
    pyramidVertices.append( osg.Vec3(10,10, 0) ) # back right 
    pyramidVertices.append( osg.Vec3( 0,10, 0) ) # back left 
    pyramidVertices.append( osg.Vec3( 5, 5,10) ) # peak
    pyramidGeometry.setVertexArray(pyramidVertices)


if __name__ == "__main__":
    main()

