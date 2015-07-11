#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgsharedarray"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osg
from osgpypp import osgViewer


# Translated from file 'osgsharedarray.cpp'

# OpenSceneGraph example, osgsharedarray.
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

#include <osg/Array>
#include <osg/Geode>
#include <osg/Geometry>
#include <osgViewer/Viewer>

#* This class is an example of how to create your own subclass of osg.Array. This
#  * is useful if your application has data in its own form of storage and you don't
#  * want to make another copy into one of the predefined osg.Array classes.
#  *
#  * @note This is not really intended to be a useful subclass of osg.Array. It
#  * doesn't do anything smart about memory management. It is simply intended as
#  * an example you can follow to create your own subclasses of osg.Array for
#  * your application's storage requirements.
#  
class MyArray (osg.Array) :
    #* Default ctor. Creates an empty array. 
    MyArray() :
        osg.Array(osg.Array.Vec3ArrayType,3,GL_FLOAT),
        _numElements(0),
        _ptr(NULL) 

    #* "Normal" ctor.
#      *
#      * @param no The number of elements in the array.
#      * @param ptr Pointer to the data. This class just keeps that
#      * pointer. It doesn't manage the memory.
#      
    MyArray(unsigned int no, osg.Vec3* ptr) :
        osg.Array(osg.Array.Vec3ArrayType,3,GL_FLOAT),
        _numElements(no),
        _ptr(ptr) 

    #* Copy ctor. 
    MyArray( MyArray other,  osg.CopyOp copyop) :
        osg.Array(osg.Array.Vec3ArrayType,3,GL_FLOAT),
        _numElements(other._numElements),
        _ptr(other._ptr) 

    #* What type of object would clone return? 
    def cloneType():
        
        return MyArray()

    #* Create a copy of the object. 
    def clone(copyop):
        
        return MyArray(*this,copyop)

    #* Accept method for ArrayVisitors.
#      *
#      * @note This will end up in ArrayVisitor.apply(osg.Array).
#      
    def accept(av):
        
        av.apply(*this)

    #* Const accept method for ArrayVisitors.
#      *
#      * @note This will end up in ConstArrayVisitor.apply( osg.Array).
#      
    def accept(cav):
        
        cav.apply(*this)

    #* Accept method for ValueVisitors. 
    def accept(index, vv):
        
        vv.apply(_ptr[index])

    #* Const accept method for ValueVisitors. 
    def accept(index, cvv):
        
        cvv.apply(_ptr[index])

    #* Compare method.
#      * Return -1 if lhs element is less than rhs element, 0 if equal,
#      * 1 if lhs element is greater than rhs element.
#      
    def compare(lhs, rhs):
        
        elem_lhs = _ptr[lhs]
        elem_rhs = _ptr[rhs]
        if elem_lhs<elem_rhs : return -1
        if elem_rhs<elem_lhs : return  1
        return 0

    def getElementSize():

         sizeof = return(osg.Vec3) 

    #* Returns a pointer to the first element of the array. 
    def getDataPointer():
        
        return _ptr

    #* Returns the number of elements in the array. 
    def getNumElements():
        
        return _numElements

    #* Returns the number of bytes of storage required to hold
#      * all of the elements of the array.
#      
    def getTotalDataSize():
        
        return _numElements * sizeof(osg.Vec3)

    def reserveArray(num):

         OSG_NOTICE, "reserveArray() not supported" 
    def resizeArray(num):
         OSG_NOTICE, "resizeArray() not supported" 
    _numElements = unsigned int()
    _ptr = osg.Vec3*()


#* The data values for the example. Simply defines a cube with
#  * per-face colors and normals.
#  

 osg.Vec3 myVertices[] =  osg.Vec3(-1.,-1., 1.),
                                 osg.Vec3( 1.,-1., 1.),
                                 osg.Vec3( 1., 1., 1.),
                                 osg.Vec3(-1., 1., 1.),

                                 osg.Vec3( 1.,-1., 1.),
                                 osg.Vec3( 1.,-1.,-1.),
                                 osg.Vec3( 1., 1.,-1.),
                                 osg.Vec3( 1., 1., 1.),

                                 osg.Vec3( 1.,-1.,-1.),
                                 osg.Vec3(-1.,-1.,-1.),
                                 osg.Vec3(-1., 1.,-1.),
                                 osg.Vec3( 1., 1.,-1.),

                                 osg.Vec3(-1.,-1.,-1.),
                                 osg.Vec3(-1.,-1., 1.),
                                 osg.Vec3(-1., 1., 1.),
                                 osg.Vec3(-1., 1.,-1.),

                                 osg.Vec3(-1., 1., 1.),
                                 osg.Vec3( 1., 1., 1.),
                                 osg.Vec3( 1., 1.,-1.),
                                 osg.Vec3(-1., 1.,-1.),

                                 osg.Vec3(-1.,-1.,-1.),
                                 osg.Vec3( 1.,-1.,-1.),
                                 osg.Vec3( 1.,-1., 1.),
                                 osg.Vec3(-1.,-1., 1.),
                               


 osg.Vec3 myNormals[] =  osg.Vec3( 0., 0., 1.),
                                osg.Vec3( 0., 0., 1.),
                                osg.Vec3( 0., 0., 1.),
                                osg.Vec3( 0., 0., 1.),

                                osg.Vec3( 1., 0., 0.),
                                osg.Vec3( 1., 0., 0.),
                                osg.Vec3( 1., 0., 0.),
                                osg.Vec3( 1., 0., 0.),

                                osg.Vec3( 0., 0.,-1.),
                                osg.Vec3( 0., 0.,-1.),
                                osg.Vec3( 0., 0.,-1.),
                                osg.Vec3( 0., 0.,-1.),

                                osg.Vec3(-1., 0., 0.),
                                osg.Vec3(-1., 0., 0.),
                                osg.Vec3(-1., 0., 0.),
                                osg.Vec3(-1., 0., 0.),

                                osg.Vec3( 0., 1., 0.),
                                osg.Vec3( 0., 1., 0.),
                                osg.Vec3( 0., 1., 0.),
                                osg.Vec3( 0., 1., 0.),

                                osg.Vec3( 0.,-1., 0.),
                                osg.Vec3( 0.,-1., 0.),
                                osg.Vec3( 0.,-1., 0.),
                                osg.Vec3( 0.,-1., 0.)
                              

 osg.Vec4 myColors[] =  osg.Vec4( 1., 0., 0., 1.),
                               osg.Vec4( 1., 0., 0., 1.),
                               osg.Vec4( 1., 0., 0., 1.),
                               osg.Vec4( 1., 0., 0., 1.),

                               osg.Vec4( 0., 1., 0., 1.),
                               osg.Vec4( 0., 1., 0., 1.),
                               osg.Vec4( 0., 1., 0., 1.),
                               osg.Vec4( 0., 1., 0., 1.),

                               osg.Vec4( 1., 1., 0., 1.),
                               osg.Vec4( 1., 1., 0., 1.),
                               osg.Vec4( 1., 1., 0., 1.),
                               osg.Vec4( 1., 1., 0., 1.),

                               osg.Vec4( 0., 0., 1., 1.),
                               osg.Vec4( 0., 0., 1., 1.),
                               osg.Vec4( 0., 0., 1., 1.),
                               osg.Vec4( 0., 0., 1., 1.),

                               osg.Vec4( 1., 0., 1., 1.),
                               osg.Vec4( 1., 0., 1., 1.),
                               osg.Vec4( 1., 0., 1., 1.),
                               osg.Vec4( 1., 0., 1., 1.),

                               osg.Vec4( 0., 1., 1., 1.),
                               osg.Vec4( 0., 1., 1., 1.),
                               osg.Vec4( 0., 1., 1., 1.),
                               osg.Vec4( 0., 1., 1., 1.)
                             

#* Create a Geode that describes a cube using our own
#  * subclass of osg.Array for the vertices. It uses
#  * the "regular" array classes for all of the other
#  * arrays.
#  *
#  * Creating your own Array class isn't really very
#  * useful for a tiny amount of data like this. You
#  * could just go ahead and copy the data into one of
#  * the "regular" Array classes like this does for
#  * normals and colors. The point of creating your
#  * own subclass of Array is for use with datasets
#  * that are much larger than anything you could
#  * create a simple example from. In that case, you
#  * might not want to create a copy of the data in
#  * one of the Array classes that comes with OSG, but
#  * instead reuse the copy your application already
#  * has and wrap it up in a subclass of osg.Array
#  * that presents the right interface for use with
#  * OpenSceneGraph.
#  *
#  * Note that I'm only using the shared array for the
#  * vertices. You could do something similar for any
#  * of the Geometry node's data arrays.
#  
def createGeometry():
    
    geode = osg.Geode()

    # create Geometry
    geom = osg.Geometry(osg.Geometry())

    # add vertices using MyArray class
    numVertices = sizeof(myVertices)/sizeof(myVertices[0])
    geom.setVertexArray(MyArray(numVertices,const_cast<osg.Vec3*>(myVertices[0])))

    # add normals
    numNormals = sizeof(myNormals)/sizeof(myNormals[0])
    geom.setNormalArray(osg.Vec3Array(numNormals,const_cast<osg.Vec3*>(myNormals[0])), osg.Array.BIND_PER_VERTEX)

    # add colors
    numColors = sizeof(myColors)/sizeof(myColors[0])
    normal_array = osg.Vec4Array(numColors,const_cast<osg.Vec4*>(myColors[0]))
    geom.setColorArray(normal_array, osg.Array.BIND_PER_VERTEX)

    # add PrimitiveSet
    geom.addPrimitiveSet(osg.DrawArrays(osg.PrimitiveSet.QUADS, 0, numVertices))

    # Changing these flags will tickle different cases in
    # Geometry.drawImplementation. They should all work fine
    # with the shared array.
    geom.setUseVertexBufferObjects(False)
    geom.setUseDisplayList(False)

    geode.addDrawable( geom.get() )

    return geode

int main(int , char **)
    # construct the viewer.
    viewer = osgViewer.Viewer()

    # add model to viewer.
    viewer.setSceneData( createGeometry() )

    # create the windows and run the threads.
    return viewer.run()


if __name__ == "__main__":
    main(sys.argv)
