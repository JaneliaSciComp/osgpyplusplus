#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osguserdata"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osg
from osgpypp import osgDB
from osgpypp import osgViewer


# Translated from file 'osguserdata.cpp'

# OpenSceneGraph example, osguserdata.
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


#include <osgViewer/Viewer>

#include <osgDB/ReadFile>
#include <osgDB/WriteFile>

#include <osg/io_utils>
#include <osg/ArgumentParser>
#include <osg/UserDataContainer>

#include <osg/ValueObject>

namespace MyNamespace

#* Provide an simple example of customizing the default UserDataContainer.
class MyUserDataContainer (osg.DefaultUserDataContainer) :
        MyUserDataContainer() 
        MyUserDataContainer( MyUserDataContainer udc,  osg.CopyOp copyop=osg.CopyOp.SHALLOW_COPY):
            DefaultUserDataContainer(udc, copyop) 

        META_Object(MyNamespace, MyUserDataContainer)

        def getUserObject(i):

            
            OSG_NOTICE, "MyUserDataContainer.getUserObject(", i, ")"
            return  osg.DefaultUserDataContainer.getUserObject(i)

        def getUserObject(i):

            
            OSG_NOTICE, "MyUserDataContainer.getUserObject(", i, ") "
            return osg.DefaultUserDataContainer.getUserObject(i)
        virtual ~MyUserDataContainer() 



#* Provide basic example of providing serialization support for the MyUserDataContainer.
REGISTER_OBJECT_WRAPPER( MyUserDataContainer,
                         MyNamespace.MyUserDataContainer,
                         MyNamespace.MyUserDataContainer,
                         "osg.Object osg.UserDataContainer osg.DefaultUserDataContainer MyNamespace.MyUserDataContainer" )

class MyGetValueVisitor (osg.ValueObject.GetValueVisitor) :
        def apply(value):
             OSG_NOTICE, " bool ", value 
        def apply(value):
             OSG_NOTICE, " char ", value 
        def apply(value):
             OSG_NOTICE, " uchar ", value 
        def apply(value):
             OSG_NOTICE, " short ", value 
        def apply(value):
             OSG_NOTICE, " ushort ", value 
        def apply(value):
             OSG_NOTICE, " int ", value 
        def apply(value):
             OSG_NOTICE, " uint ", value 
        def apply(value):
             OSG_NOTICE, " float ", value 
        def apply(value):
             OSG_NOTICE, " double ", value 
        def apply(value):
             OSG_NOTICE, " string ", value 
        def apply(value):
             OSG_NOTICE, " Vec2f ", value 
        def apply(value):
             OSG_NOTICE, " Vec3f ", value 
        def apply(value):
             OSG_NOTICE, " Vec4f ", value 
        def apply(value):
             OSG_NOTICE, " Vec2d ", value 
        def apply(value):
             OSG_NOTICE, " Vec3d ", value 
        def apply(value):
             OSG_NOTICE, " Vec4d ", value 
        def apply(value):
             OSG_NOTICE, " Quat ", value 
        def apply(value):
             OSG_NOTICE, " Plane ", value 
        def apply(value):
             OSG_NOTICE, " Matrixf ", value 
        def apply(value):
             OSG_NOTICE, " Matrixd ", value 


template<typename T>
class GetNumeric (osg.ValueObject.GetValueVisitor) :

        GetNumeric():
            _set(False),
            _value(0) 
        
        def apply(value):
        
             _value = value _set = True 
        def apply(value):
             _value = value _set = True  
        def apply(value):
             _value = value _set = True  
        def apply(value):
             _value = value _set = True  
        def apply(value):
             _value = value _set = True  
        def apply(value):
             _value = value _set = True  
        def apply(value):
             _value = value _set = True  
        def apply(value):
             _value = value _set = True  
        def apply(value):
             _value = value _set = True 

        _set = bool()
        _value = T()


template<typename T>
def getNumeric(object):
    
    bvo = dynamic_cast<osg.ValueObject*>(object)
    if bvo :
        gn = GetNumeric<T>()
        if bvo.get(gn)  and  gn._set : return gn._value
    T = return(0)

def testResults(node):

    
    j = 0
    if node.getUserValue("Int value",j) :
        OSG_NOTICE, "Int value=", j
    else:
        OSG_NOTICE, "Int value not found"

    readString = str()
    if node.getUserValue("Status",readString) :
        OSG_NOTICE, "Status=", readString
    else:
        OSG_NOTICE, "Status not found"

    height = 0.0
    if node.getUserValue("Height",height) :
        OSG_NOTICE, "Height=", height
    else:
        OSG_NOTICE, "Height not found"

    udc = node.getUserDataContainer()
    if udc :
        OSG_NOTICE, "udc.getNumUserObjects()=", udc.getNumUserObjects()
        for(unsigned int i=0 i<udc.getNumUserObjects() ++i)
            mgvv = MyGetValueVisitor()
            userObject = udc.getUserObject(i)
            valueObject = dynamic_cast<osg.ValueObject*>(userObject)
            OSG_NOTICE, "userObject=", userObject, ", className=", userObject.className(), ", getName()=", userObject.getName(), " valueObject=", valueObject, " getNumeric ", getNumeric<float>(userObject), " "
            if valueObject : valueObject.get(mgvv)
            OSG_NOTICE
    
    OSG_NOTICE


def main(argv):


    
    arguments = osg.ArgumentParser(argv)
    
    node = osg.Group()

    if arguments.read("--MyUserDataContainer")  or  arguments.read("--mydc") :
        node.setUserDataContainer(MyNamespace.MyUserDataContainer)()
    
    i = 10
    node.setUserValue("Int value",i)

    testString = str("All seems fine")
    node.setUserValue("Status",testString)

    node.setUserValue("Height",float(1.4))

    drawable = osg.Geometry()
    drawable.setName("myDrawable")
    node.getOrCreateUserDataContainer().addUserObject(drawable)

    node.setUserValue("fred",12)
    node.setUserValue("john",1.1)
    node.setUserValue("david",1.9)
    node.setUserValue("char",char(65))
    node.setUserValue("matrixd",osg.Matrixd.translate(1.0,2.0,3.0))
    node.setUserValue("flag-on",True)
    node.setUserValue("flag-off",False)

    OSG_NOTICE, "Testing results for values set directly on scene graph"
    testResults(node)

        osgDB.writeNodeFile(*node, "results.osgt")

        from_osgt = osgDB.readNodeFile("results.osgt")
        if from_osgt.valid() :
            OSG_NOTICE, "Testing results for values from scene graph read from .osgt file"
            testResults(from_osgt)
    
        osgDB.writeNodeFile(*node, "results.osgb")

        from_osgb = osgDB.readNodeFile("results.osgb")
        if from_osgb.valid() :
            OSG_NOTICE, "Testing results for values from scene graph read from .osgb file"
            testResults(from_osgb)

        osgDB.writeNodeFile(*node, "results.osgx")

        from_osgx = osgDB.readNodeFile("results.osgx")
        if from_osgx.valid() :
            OSG_NOTICE, "Testing results for values from scene graph read from .osgx file"
            testResults(from_osgx)
    return 0


if __name__ == "__main__":
    main(sys.argv)
