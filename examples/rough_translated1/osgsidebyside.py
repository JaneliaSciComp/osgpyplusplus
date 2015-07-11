#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgsidebyside"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osg
from osgpypp import osgDB
from osgpypp import osgGA
from osgpypp import osgSim
from osgpypp import osgUtil
from osgpypp import osgViewer


# Translated from file 'osgsidebyside.cpp'

# OpenSceneGraph example, osgcamera.
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
#include <osgDB/WriteFile>
#include <osgViewer/Viewer>
#include <osgViewer/ViewerEventHandlers>
#include <osgGA/TrackballManipulator>
#include <osgGA/FlightManipulator>
#include <osgGA/AnimationPathManipulator>
#include <osgGA/GUIEventHandler>
#include <osgGA/StateSetManipulator>
#include <osg/PolygonMode>
#include <osgUtil/Optimizer>
#include <osg/Depth>
#include <iostream>
#include <osg/Switch>
#include <osgSim/MultiSwitch>
#include <osgSim/DOFTransform>

#include <osg/AlphaFunc>
#include <osg/BlendFunc>

using namespace osg
using namespace osgGA


class SwitchDOFVisitor : public osg.NodeVisitor, public osgGA.GUIEventHandler 
    SwitchDOFVisitor():
      osg.NodeVisitor(osg.NodeVisitor.TRAVERSE_ALL_CHILDREN)

    def apply(node):

        
        pMSwitch = dynamic_cast<osgSim.MultiSwitch*>(node)
        
        if pMSwitch :
            mSwitches.push_back(pMSwitch)

        osg.NodeVisitor.apply(node)
    
    def apply(node):
    
        
        pDof = dynamic_cast<osgSim.DOFTransform*>(node)
        
        if pDof :
            mDofs.push_back(pDof)
            pDof.setAnimationOn(True)

        osg.NodeVisitor.apply(node)

    def nextSwitch():

        
        for (size_t i=0 i < mSwitches.size() i++)
            if mSwitches[i].getSwitchSetList().size() > 1 :
                # Toggle through switchsets
                nextSwitchSet = mSwitches[i].getActiveSwitchSet()
                nextSwitchSet++
                if nextSwitchSet >= mSwitches[i].getSwitchSetList().size() :
                    nextSwitchSet = 0
                mSwitches[i].setActiveSwitchSet(nextSwitchSet)
            elif mSwitches[i].getSwitchSetList().size() == 1 :
                # If we have only one switchset, toggle values within this switchset
                values = mSwitches[i].getValueList(0)
                for (size_t j=0 j < values.size() j++)
                    if values[j] :
                        nextValue = j+1
                        if nextValue >= values.size() :
                            nextValue = 0
                        mSwitches[i].setSingleChildOn(0, nextValue)

    def multiplyAnimation(scale):

        
        for (size_t i=0 i < mDofs.size() i++)
            mDofs[i].setIncrementHPR(mDofs[i].getIncrementHPR() * scale)
            mDofs[i].setIncrementScale(mDofs[i].getIncrementScale() * scale)
            mDofs[i].setIncrementTranslate(mDofs[i].getIncrementTranslate() * scale)

    def handle(ea, aa):

        
        viewer = dynamic_cast<osgViewer.Viewer*>(aa)
        if !viewer : return False

        if ea.getHandled() : return False

        if ea.getEventType()==GUIEventAdapter.KEYDOWN :

            switch( ea.getKey() )
                case osgGA.GUIEventAdapter.KEY_Right:
                    # Toggle next switch
                    nextSwitch()
                    return True
                    break
                case osgGA.GUIEventAdapter.KEY_Up:
                    # Increase animation speed
                    multiplyAnimation(2)
                    return True
                    break
                case osgGA.GUIEventAdapter.KEY_Down:
                    # Decrease animation speed
                    multiplyAnimation(0.5)
                    return True
                    break
        return False
    mSwitches = std.vector<osgSim.MultiSwitch*>()
    mDofs = std.vector<osgSim.DOFTransform*>()


def singleWindowSideBySideCameras(viewer):

    
    wsi = osg.GraphicsContext.getWindowingSystemInterface()
    if !wsi : 
        osg.notify(osg.NOTICE), "Error, no WindowSystemInterface available, cannot create windows."
        return
    
    unsigned int width, height
    wsi.getScreenResolution(osg.GraphicsContext.ScreenIdentifier(0), width, height)



    # Not fullscreen
    width /= 2
    height /= 2

    traits = osg.GraphicsContext.Traits()
    traits.x = 100
    traits.y = 100
    traits.width = width
    traits.height = height
    traits.windowDecoration = True
    traits.doubleBuffer = True
    traits.sharedContext = 0

    gc = osg.GraphicsContext.createGraphicsContext(traits.get())
    if gc.valid() :
        osg.notify(osg.INFO), "  GraphicsWindow has been created successfully."

        # need to ensure that the window is cleared make sure that the complete window is set the correct colour
        # rather than just the parts of the window that are under the camera's viewports
        gc.setClearColor(osg.Vec4f(0.2,0.2,0.6,1.0))
        gc.setClearMask(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    else :
        osg.notify(osg.NOTICE), "  GraphicsWindow has not been created successfully."


    master = viewer.getCamera()

    # get the default settings for the camera
    double fovy, aspectRatio, zNear, zFar
    master.getProjectionMatrixAsPerspective(fovy, aspectRatio, zNear, zFar)

    # reset this for the actual apsect ratio of out created window
    windowAspectRatio = double(width)/double(height)
    master.setProjectionMatrixAsPerspective(fovy, windowAspectRatio, 1.0, 10000.0)

    master.setName("MasterCam")

    camera = osg.Camera()
    camera.setCullMask(1)
    camera.setName("Left")
    camera.setGraphicsContext(gc.get())
    camera.setViewport(osg.Viewport(0, 0, width/2, height))
    buffer = traits.doubleBuffer ? GL_BACK : GL_FRONT
    camera.setDrawBuffer(buffer)
    camera.setReadBuffer(buffer)
    viewer.addSlave(camera.get(), osg.Matrixd.scale(1.0,0.5,1.0), osg.Matrixd())

    camera = osg.Camera()
    camera.setCullMask(2)
    camera.setName("Right")
    camera.setGraphicsContext(gc.get())
    camera.setViewport(osg.Viewport(width/2, 0, width/2, height))
    buffer = traits.doubleBuffer ? GL_BACK : GL_FRONT
    camera.setDrawBuffer(buffer)
    camera.setReadBuffer(buffer)
    viewer.addSlave(camera.get(), osg.Matrixd.scale(1.0,0.5,1.0), osg.Matrixd())

def main(argc, argv):

    
    # use an ArgumentParser object to manage the program arguments.
    arguments = osg.ArgumentParser(argc,argv)

    if argc<2 : 
        print argv[0], ": requires filename argument."
        return 1

    viewer = osgViewer.Viewer(arguments)
    
    outputfile = str("output.osgt")
    while arguments.read("-o",outputfile) : 

    while arguments.read("-s") :  viewer.setThreadingModel(osgViewer.Viewer.SingleThreaded) 
    while arguments.read("-g") :  viewer.setThreadingModel(osgViewer.Viewer.CullDrawThreadPerContext) 
    while arguments.read("-d") :  viewer.setThreadingModel(osgViewer.Viewer.DrawThreadPerContext) 
    while arguments.read("-c") :  viewer.setThreadingModel(osgViewer.Viewer.CullThreadPerCameraDrawThreadPerContext) 
    
    singleWindowSideBySideCameras(viewer)

    viewer.setCameraManipulator( osgGA.TrackballManipulator() )
    viewer.addEventHandler(osgViewer.StatsHandler)()
    viewer.addEventHandler(osgViewer.ThreadingHandler)()
    viewer.addEventHandler(osgViewer.WindowSizeHandler())
    viewer.addEventHandler(osgViewer.LODScaleHandler())
    viewer.addEventHandler(osgGA.StateSetManipulator())

    visit = SwitchDOFVisitor()
    viewer.addEventHandler(visit)
    
    loadedModel = osg.Node()
    # load the scene.
    loadedModel = osgDB.readNodeFiles(arguments)

    if !loadedModel : 
        print argv[0], ": No data loaded."
        return 1

    group = osg.Group()
    
    group1 = osg.Group()
    group1.addChild(loadedModel.get())
    group1.setNodeMask(1)

    # Uncomment these lines if you like to compare the loaded model to the resulting model in a merge/diff tool
    #osgDB.writeNodeFile(*loadedModel.get(), "dummy1.osgt")

    osgDB.writeNodeFile(*loadedModel.get(), outputfile)
    convertedModel = osgDB.readNodeFile(outputfile)

    #osgDB.writeNodeFile(*convertedModel.get(), "dummy2.osgt")

    group2 = osg.Group()
    group2.addChild(convertedModel.get())
    group2.setNodeMask(2)

    # Activate DOF animations and collect switches
    loadedModel.accept(*visit)
    convertedModel.accept(*visit)

    group.addChild(group1)
    group.addChild(group2)

    viewer.setSceneData(group)

    viewer.setThreadingModel(osgViewer.Viewer.DrawThreadPerContext)
    viewer.realize()

    viewer.run()

    return 0



if __name__ == "__main__":
    main(sys.argv)
