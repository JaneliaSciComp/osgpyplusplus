#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgcompositeviewer"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osg
from osgpypp import osgDB
from osgpypp import osgFX
from osgpypp import osgGA
from osgpypp import osgText
from osgpypp import osgUtil
from osgpypp import osgViewer


# Translated from file 'osgcompositeviewer.cpp'

# OpenSceneGraph example, osgcompositeviewer.
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

#include <iostream>

#include <osgUtil/Optimizer>
#include <osgDB/ReadFile>

#include <osg/Material>
#include <osg/Geode>
#include <osg/BlendFunc>
#include <osg/Depth>
#include <osg/Projection>
#include <osg/PolygonOffset>
#include <osg/MatrixTransform>
#include <osg/Camera>
#include <osg/FrontFace>

#include <osgText/Text>

#include <osgGA/TrackballManipulator>
#include <osgGA/FlightManipulator>
#include <osgGA/StateSetManipulator>
#include <osgViewer/ViewerEventHandlers>

#include <osgViewer/CompositeViewer>

#include <osgFX/Scribe>

#include <osg/io_utils>

# class to handle events with a pick
class PickHandler (osgGA.GUIEventHandler) :

    PickHandler():
        _mx(0.0),
        _my(0.0) 

    ~PickHandler() 

    def handle(ea, aa):

        
        view = dynamic_cast<osgViewer.View*>(aa)
        if  not view : return False

        switch(ea.getEventType())
            case(osgGA.GUIEventAdapter.PUSH):
                _mx = ea.getX()
                _my = ea.getY()
                break
            case(osgGA.GUIEventAdapter.RELEASE):
                if _mx==ea.getX()  and  _my==ea.getY() :
                    pick(view, ea)
                break
            default:
                break
        return False

    def pick(view, event):

        
        node = 0
        parent = 0

        intersections = osgUtil.LineSegmentIntersector.Intersections()
        if view.computeIntersections(event, intersections) :
            intersection = *intersections.begin()
            nodePath = intersection.nodePath
            node =  nodePath[nodePath.size()-1] if ((nodePath.size()>=1)) else 0
            parent =  dynamic_cast<osg.Group*>(nodePath[nodePath.size()-2]) if ((nodePath.size()>=2)) else 0

        # now we try to decorate the hit node by the osgFX.Scribe to show that its been "picked"
        if parent  and  node :
            parentAsScribe = dynamic_cast<osgFX.Scribe*>(parent)
            if  not parentAsScribe :
                # node not already picked, so highlight it with an osgFX.Scribe
                scribe = osgFX.Scribe()
                scribe.addChild(node)
                parent.replaceChild(node,scribe)
            else:
                # node already picked so we want to remove scribe to unpick it.
                parentList = parentAsScribe.getParents()
                for(osg.Node.ParentList.iterator itr=parentList.begin()
                    not = parentList.end()
                    ++itr)
                    (*itr).replaceChild(parentAsScribe,node)


    float _mx, _my




def main(argv):


    

    # use an ArgumentParser object to manage the program arguments.
    arguments = osg.ArgumentParser(argv)

    # read the scene from the list of file specified commandline args.
    scene = osgDB.readNodeFiles(arguments)

    if  not scene :
        print argv[0], ": requires filename argument."
        return 1

    # construct the viewer.
    viewer = osgViewer.CompositeViewer(arguments)

    if arguments.read("-1") :
            view = osgViewer.View()
            view.setName("Single view")
            view.setSceneData(osgDB.readNodeFile("fountain.osgt"))

            view.addEventHandler( osgViewer.StatsHandler )()

            view.setUpViewAcrossAllScreens()
            view.setCameraManipulator(osgGA.TrackballManipulator)()
            viewer.addView(view)

    if arguments.read("-2") :

        # view one
            view = osgViewer.View()
            view.setName("View one")
            viewer.addView(view)

            view.setUpViewOnSingleScreen(0)
            view.setSceneData(scene)
            view.setCameraManipulator(osgGA.TrackballManipulator)()

            # add the state manipulator
            statesetManipulator = osgGA.StateSetManipulator()
            statesetManipulator.setStateSet(view.getCamera().getOrCreateStateSet())

            view.addEventHandler( statesetManipulator )

        # view two
            view = osgViewer.View()
            view.setName("View two")
            viewer.addView(view)

            view.setUpViewOnSingleScreen(1)
            view.setSceneData(scene)
            view.setCameraManipulator(osgGA.TrackballManipulator)()

            view.addEventHandler( osgViewer.StatsHandler )()


            # add the handler for doing the picking
            view.addEventHandler(PickHandler())


    if arguments.read("-3")  or  viewer.getNumViews()==0 :

        wsi = osg.GraphicsContext.getWindowingSystemInterface()
        if  not wsi :
            osg.notify(osg.NOTICE), "Error, no WindowSystemInterface available, cannot create windows."
            return 1

        unsigned int width, height
        wsi.getScreenResolution(osg.GraphicsContext.ScreenIdentifier(0), width, height)

        traits = osg.GraphicsContext.Traits()
        traits.x = 100
        traits.y = 100
        traits.width = 1000
        traits.height = 800
        traits.windowDecoration = True
        traits.doubleBuffer = True
        traits.sharedContext = 0

        gc = osg.GraphicsContext.createGraphicsContext(traits)
        if gc.valid() :
            osg.notify(osg.INFO), "  GraphicsWindow has been created successfully."

            # need to ensure that the window is cleared make sure that the complete window is set the correct colour
            # rather than just the parts of the window that are under the camera's viewports
            gc.setClearColor(osg.Vec4f(0.2,0.2,0.6,1.0))
            gc.setClearMask(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        else:
            osg.notify(osg.NOTICE), "  GraphicsWindow has not been created successfully."

        # view one
            view = osgViewer.View()
            view.setName("View one")
            viewer.addView(view)

            view.setSceneData(scene)
            view.getCamera().setName("Cam one")
            view.getCamera().setViewport(osg.Viewport(0,0, traits.width/2, traits.height/2))
            view.getCamera().setGraphicsContext(gc)
            view.setCameraManipulator(osgGA.TrackballManipulator)()

            # add the state manipulator
            statesetManipulator = osgGA.StateSetManipulator()
            statesetManipulator.setStateSet(view.getCamera().getOrCreateStateSet())

            view.addEventHandler( statesetManipulator )

            view.addEventHandler( osgViewer.StatsHandler )()
            view.addEventHandler( osgViewer.HelpHandler )()
            view.addEventHandler( osgViewer.WindowSizeHandler )()
            view.addEventHandler( osgViewer.ThreadingHandler )()
            view.addEventHandler( osgViewer.RecordCameraPathHandler )()

        # view two
            view = osgViewer.View()
            view.setName("View two")
            viewer.addView(view)

            view.setSceneData(scene)
            view.getCamera().setName("Cam two")
            view.getCamera().setViewport(osg.Viewport(traits.width/2,0, traits.width/2, traits.height/2))
            view.getCamera().setGraphicsContext(gc)
            view.setCameraManipulator(osgGA.TrackballManipulator)()

            # add the handler for doing the picking
            view.addEventHandler(PickHandler())


        # view three
            view = osgViewer.View()
            view.setName("View three")
            viewer.addView(view)

            view.setSceneData(osgDB.readNodeFile("cessnafire.osgt"))

            view.getCamera().setName("Cam three")
            view.getCamera().setProjectionMatrixAsPerspective(30.0, double(traits.width) / double(traits.height/2), 1.0, 1000.0)
            view.getCamera().setViewport(osg.Viewport(0, traits.height/2, traits.width, traits.height/2))
            view.getCamera().setGraphicsContext(gc)
            view.setCameraManipulator(osgGA.TrackballManipulator)()



    while arguments.read("-s") :  viewer.setThreadingModel(osgViewer.CompositeViewer.SingleThreaded) 
    while arguments.read("-g") :  viewer.setThreadingModel(osgViewer.CompositeViewer.CullDrawThreadPerContext) 
    while arguments.read("-c") :  viewer.setThreadingModel(osgViewer.CompositeViewer.CullThreadPerCameraDrawThreadPerContext) 

     # run the viewer's main frame loop
     return viewer.run()



if __name__ == "__main__":
    main(sys.argv)
