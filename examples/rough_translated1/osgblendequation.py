#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgblendequation"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osg
from osgpypp import osgDB
from osgpypp import osgUtil
from osgpypp import osgViewer


# Translated from file 'osgblendequation.cpp'

# OpenSceneGraph example, osgblendequation.
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

#include <osg/Geode>
#include <osg/Group>
#include <osg/Notify>
#include <osg/BlendEquation>

#include <osgDB/Registry>
#include <osgDB/ReadFile>

#include <osgUtil/Optimizer>

#include <osgViewer/Viewer>

#include <iostream>

_eq_nb = 8
 osg.BlendEquation.Equation _equations[_eq_nb]=
    osg.BlendEquation.FUNC_ADD,
    osg.BlendEquation.FUNC_SUBTRACT,
    osg.BlendEquation.FUNC_REVERSE_SUBTRACT,
    osg.BlendEquation.RGBA_MIN,
    osg.BlendEquation.RGBA_MAX,
    osg.BlendEquation.ALPHA_MIN,
    osg.BlendEquation.ALPHA_MAX,
    osg.BlendEquation.LOGIC_OP


 char* _equations_name[_eq_nb]=
    "osg.BlendEquation.FUNC_ADD",
    "osg.BlendEquation.FUNC_SUBTRACT",
    "osg.BlendEquation.FUNC_REVERSE_SUBTRACT",
    "osg.BlendEquation.RGBA_MIN",
    "osg.BlendEquation.RGBA_MAX",
    "osg.BlendEquation.ALPHA_MIN",
    "osg.BlendEquation.ALPHA_MAX",
    "osg.BlendEquation.LOGIC_OP"



class TechniqueEventHandler (osgGA.GUIEventHandler) :

    TechniqueEventHandler(osg.BlendEquation* blendEq)  _blendEq=blendEq _eq_index=0
    TechniqueEventHandler()  std.cerr, "Error, can't initialize it not "

    META_Object(osgBlendEquationApp,TechniqueEventHandler)

    handle = virtual bool( osgGA.GUIEventAdapter ea,osgGA.GUIActionAdapter)

    virtual void getUsage(osg.ApplicationUsage usage) 

    ~TechniqueEventHandler() 

    TechniqueEventHandler( TechniqueEventHandler, osg.CopyOp) 

    _blendEq = osg.BlendEquation*()

    _eq_index = int()




    
bool TechniqueEventHandler.handle( osgGA.GUIEventAdapter ea,osgGA.GUIActionAdapter)
    switch(ea.getEventType())
        case(osgGA.GUIEventAdapter.KEYDOWN):
            if ea.getKey()==osgGA.GUIEventAdapter.KEY_Right  or 
                ea.getKey()==osgGA.GUIEventAdapter.KEY_KP_Right :
                _eq_index++
                if _eq_index>=_eq_nb : _eq_index=0
                _blendEq.setEquation(_equations[_eq_index])
                print "Equation name = ", _equations_name[_eq_index]
                return True
            elif ea.getKey()==osgGA.GUIEventAdapter.KEY_Left  or 
                     ea.getKey()==osgGA.GUIEventAdapter.KEY_KP_Left :
                _eq_index--
                if _eq_index<0 : _eq_index=_eq_nb-1
                _blendEq.setEquation(_equations[_eq_index])
                print "Operation name = ", _equations_name[_eq_index]
                return True
            return False

        default:
            return False

void TechniqueEventHandler.getUsage(osg.ApplicationUsage usage) 
    usage.addKeyboardMouseBinding("Left Arrow","Advance to next equation")
    usage.addKeyboardMouseBinding("Right Array","Move to previous equation")




def main(argv):




    

    # use an ArgumentParser object to manage the program arguments.
    arguments = osg.ArgumentParser(argv)

    # set up the usage document, in case we need to print out how to use this program.
    arguments.getApplicationUsage().setDescription(arguments.getApplicationName()+" is the example which demonstrates how to use glBlendEquation for mixing rendered scene and the frame-buffer.")
    arguments.getApplicationUsage().setCommandLineUsage(arguments.getApplicationName()+" [options] filename ...")
    arguments.getApplicationUsage().addCommandLineOption("-h or --help","Display this information")
   
    # construct the viewer.
    viewer = osgViewer.Viewer()

    # load the nodes from the commandline arguments.
    loadedModel = osgDB.readNodeFiles(arguments)

    # if not loaded assume no arguments passed in, try use default mode instead.
    if  not loadedModel : loadedModel = osgDB.readNodeFile("cessnafire.osgt")
  
    if  not loadedModel :
        print arguments.getApplicationName(), ": No data loaded"
        return 1

    root = osg.Group()
    root.addChild(loadedModel)
    
    
    stateset = osg.StateSet()
    stateset.setDataVariance(osg.Object.DYNAMIC)
    
    blendEquation = osg.BlendEquation(osg.BlendEquation.FUNC_ADD)
    blendEquation.setDataVariance(osg.Object.DYNAMIC)
    
    stateset.setAttributeAndModes(blendEquation,osg.StateAttribute.OVERRIDE|osg.StateAttribute.ON)
            
    #tell to sort the mesh before displaying it
    stateset.setRenderingHint(osg.StateSet.TRANSPARENT_BIN)           

    loadedModel.setStateSet(stateset)

    viewer.addEventHandler(TechniqueEventHandler(blendEquation))

    # add a viewport to the viewer and attach the scene graph.
    viewer.setSceneData( root )
    
    return viewer.run()


if __name__ == "__main__":
    main(sys.argv)
