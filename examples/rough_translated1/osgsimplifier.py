#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgsimplifier"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osgDB
from osgpypp import osgGA
from osgpypp import osgUtil
from osgpypp import osgViewer


# Translated from file 'osgsimplifier.cpp'

# OpenSceneGraph example, osgsimplifier.
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

#include <osgDB/ReadFile>
#include <osgUtil/Optimizer>
#include <osgUtil/Simplifier>
#include <osgViewer/Viewer>
#include <osgGA/TrackballManipulator>
#include <iostream>

class KeyboardEventHandler (osgGA.GUIEventHandler) :
    
    KeyboardEventHandler(unsigned int flag) : _flag(flag)
    
    
    virtual bool handle( osgGA.GUIEventAdapter ea,osgGA.GUIActionAdapter)
        switch(ea.getEventType())
            case(osgGA.GUIEventAdapter.KEYDOWN):
                if ea.getKey()=='n' :
                    _flag = 1
                    return True
                if ea.getKey()=='p' :
                    _flag = 2
                    return True
                break
            default:
                break
        return False

    _flag = unsigned int()



def main(argc, argv):


    

    # use an ArgumentParser object to manage the program arguments.
    arguments = osg.ArgumentParser(argc,argv)
    
    # set up the usage document, in case we need to print out how to use this program.
    arguments.getApplicationUsage().setApplicationName(arguments.getApplicationName())
    arguments.getApplicationUsage().setDescription(arguments.getApplicationName()+" examples illustrates simplification of triangle meshes.")
    arguments.getApplicationUsage().setCommandLineUsage(arguments.getApplicationName()+" [options] filename ...")
    arguments.getApplicationUsage().addCommandLineOption("-h or --help","Display this information")
    arguments.getApplicationUsage().addCommandLineOption("--ratio <ratio>","Specify the sample ratio","0.5]")
    arguments.getApplicationUsage().addCommandLineOption("--max-error <error>","Specify the maximum error","4.0")
    

    sampleRatio = 0.5
    maxError = 4.0

    # construct the viewer.
    viewer = osgViewer.Viewer()

    # read the sample ratio if one is supplied
    while arguments.read("--ratio",sampleRatio) : 
    while arguments.read("--max-error",maxError) : 

    # if user request help write it out to cout.
    if arguments.read("-h") || arguments.read("--help") :
        arguments.getApplicationUsage().write(std.cout)
        return 1

    if arguments.argc()<=1 :
        arguments.getApplicationUsage().write(std.cout,osg.ApplicationUsage.COMMAND_LINE_OPTION)
        return 1

    # read the scene from the list of file specified commandline args.
    loadedModel = osgDB.readNodeFiles(arguments)
  
    # if not loaded assume no arguments passed in, try use default mode instead.
    if !loadedModel : loadedModel = osgDB.readNodeFile("dumptruck.osgt")
    
    # if no model has been successfully loaded report failure.
    if !loadedModel : 
        print arguments.getApplicationName(), ": No data loaded"
        return 1
    
    #loadedModel.accept(simplifier)

    keyFlag = 0
    viewer.addEventHandler(KeyboardEventHandler(keyFlag))

    # set the scene to render
    viewer.setSceneData(loadedModel.get())

    viewer.setCameraManipulator(osgGA.TrackballManipulator())

    # create the windows and run the threads.
    viewer.realize()

    multiplier = 0.8
    minRatio = 0.001
    ratio = sampleRatio


    while  !viewer.done()  :
        # fire off the cull and draw traversals of the scene.
        viewer.frame()
    
        if keyFlag == 1 || keyFlag == 2 :
            if keyFlag == 1 : ratio *= multiplier
            if keyFlag == 2 : ratio /= multiplier
            if ratio<minRatio : ratio=minRatio
            
            simplifier = osgUtil.Simplifier(ratio, maxError)

            print "Runing osgUtil.Simplifier with SampleRatio=", ratio, " maxError=", maxError, " ..."
            std.cout.flush()
            
            root = (osg.Node*)loadedModel.clone(osg.CopyOp.DEEP_COPY_ALL)

            root.accept(simplifier)
            
            print "done"
            
            viewer.setSceneData(root.get())
            keyFlag = 0
    
    return 0



if __name__ == "__main__":
    main(sys.argv)
