#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgoscdevice"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osg
from osgpypp import osgDB
from osgpypp import osgFX
from osgpypp import osgGA
from osgpypp import osgText
from osgpypp import osgUtil
from osgpypp import osgViewer


# Translated from file 'osgoscdevice.cpp'

# OpenSceneGraph example, osgcubemap.
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
#include <osg/ValueObject>
#include <osg/FrontFace>
#include <osgDB/ReadFile>

#include <osgText/Text>

#include <osgGA/Device>
#include <osgGA/TrackballManipulator>
#include <osgGA/FlightManipulator>
#include <osgGA/StateSetManipulator>
#include <osgViewer/ViewerEventHandlers>

#include <osgViewer/CompositeViewer>

#include <osgFX/Scribe>

#include <osg/io_utils>


# class to handle events with a pick
class PickHandler (osgGA.GUIEventHandler) :

    PickHandler(osgGA.Device* device):
        _device(device) 

    ~PickHandler() 

    handle = bool( osgGA.GUIEventAdapter ea,osgGA.GUIActionAdapter aa)

    pick = virtual void(osgViewer.View* view,  osgGA.GUIEventAdapter ea)

    def setLabel(name, x, y):

        
        ea = osgGA.GUIEventAdapter()
        ea.setEventType(osgGA.GUIEventAdapter.USER)
        ea.setName("pick-result")
        ea.setUserValue("name", name)
        ea.setUserValue("x", x)
        ea.setUserValue("y", y)

        _device.sendEvent(*ea)

    _device = osgGA.Device()


bool PickHandler.handle( osgGA.GUIEventAdapter ea,osgGA.GUIActionAdapter aa)
    switch(ea.getEventType())
        case(osgGA.GUIEventAdapter.PUSH):
            view = dynamic_cast<osgViewer.View*>(aa)
            if view : pick(view,ea)
            return False

        case(osgGA.GUIEventAdapter.KEYUP):
            if ea.getKey() == 't' :
                user_event = osgGA.GUIEventAdapter()
                user_event.setEventType(osgGA.GUIEventAdapter.USER)
                user_event.setUserValue("vec2f", osg.Vec2f(1.0,2.0))
                user_event.setUserValue("vec3f", osg.Vec3f(1.0,2.0, 3.0))
                user_event.setUserValue("vec4f", osg.Vec4f(1.0,2.0, 3.0, 4.0))

                user_event.setUserValue("vec2d", osg.Vec2d(1.0,2.0))
                user_event.setUserValue("vec3d", osg.Vec3d(1.0,2.0, 3.0))
                user_event.setUserValue("vec4d", osg.Vec4d(1.0,2.0, 3.0, 4.0))

                user_event.setName("osc_test_1")

                _device.sendEvent(*user_event)


        default:
            return False

void PickHandler.pick(osgViewer.View* view,  osgGA.GUIEventAdapter ea)
    intersections = osgUtil.LineSegmentIntersector.Intersections()

    gdlist = ""
    x = ea.getX()
    y = ea.getY()
    if view.computeIntersections(ea, intersections) :
        for(osgUtil.LineSegmentIntersector.Intersections.iterator hitr = intersections.begin()
            hitr != intersections.end()
            ++hitr)
            os = std.ostringstream()
            if !hitr.nodePath.empty()  !(hitr.nodePath.back().getName().empty()) :
                # the geodes are identified by name.
                os, "Object \"", hitr.nodePath.back().getName(), "\""
            elif hitr.drawable.valid() :
                os, "Object \"", hitr.drawable.className(), "\""

            os, "        local coords vertex(", hitr.getLocalIntersectPoint(), ")", "  normal(", hitr.getLocalIntersectNormal(), ")"
            os, "        world coords vertex(", hitr.getWorldIntersectPoint(), ")", "  normal(", hitr.getWorldIntersectNormal(), ")"
            vil = hitr.indexList
            for(unsigned int i=0i<vil.size()++i)
                os, "        vertex indices [", i, "] = ", vil[i]

            gdlist += os.str()
    setLabel(gdlist, x, y)


class UserEventHandler (osgGA.GUIEventHandler) :

    UserEventHandler(osgText.Text* text) : osgGA.GUIEventHandler(), _text(text) 

    ~UserEventHandler() 

    handle = bool( osgGA.GUIEventAdapter ea,osgGA.GUIActionAdapter aa)
    _text = osgText.Text()



class MyValueListVisitor (osg.ValueObject.GetValueVisitor) :
    def apply(value):
         _ss, value, " (bool)" 
    def apply(value):
         _ss, value, " (char)" 
    def apply(value):
         _ss, value, " (unsigned char)" 
    def apply(value):
         _ss, value, " (short)" 
    def apply(value):
         _ss, value, " (unsigned short)" 
    def apply(value):
         _ss, value, " (int)" 
    def apply(value):
         _ss, value, " (unsigned int)" 
    def apply(value):
         _ss, value, " (float)" 
    def apply(value):
         _ss, value, " (double)" 
    def apply(value):
         _ss, value, " (str)" 
    def apply(value):
         _ss, value, " (osg.Vec2f)" 
    def apply(value):
         _ss, value, " (osg.Vec3f)" 
    def apply(value):
         _ss, value, " (osg.Vec4f)" 
    def apply(value):
         _ss, value, " (osg.Vec2d)" 
    def apply(value):
         _ss, value, " (osg.Vec3d)" 
    def apply(value):
         _ss, value, " (osg.Vec4d)" 
    def apply(value):
         _ss, value, " (osg.Quat)" 
    def apply(value):
         _ss, value, " (osg.Plane)" 
    def apply(value):
         _ss, value, " (osg.Matrixf)" 
    def apply(value):
         _ss, value, " (osg.Matrixd)" 
    def value():
         return _ss.str() 
    def clear():
        _ss.clear() 
    _ss = std.ostringstream()


bool UserEventHandler.handle( osgGA.GUIEventAdapter ea,osgGA.GUIActionAdapter aa)
    if ea.getEventType() == osgGA.GUIEventAdapter.USER : 
        OSG_ALWAYS, "handle user-event: ", ea.getName()

        if ea.getName() == "/pick-result" :
            name = str("")
            float x(0), y(0)
            ea.getUserValue("name", name)
            ea.getUserValue("x", x)
            ea.getUserValue("y", y)
            ss = std.ostringstream()
            ss, "Name: ", name
            ss, "x: ", y, " y: ", y

            _text.setText(ss.str())
        elif ea.getName() == "/osgga" :
            rect = osg.Vec4()
            ea.getUserValue("resize", rect)
            view = dynamic_cast<osgViewer.View*>(aa)
            if view  (rect[2] > 0)  (rect[3] > 0) :
                OSG_ALWAYS, "resizing view to ", rect
                win = view.getCamera().getGraphicsContext() ? dynamic_cast<osgViewer.GraphicsWindow*>(view.getCamera().getGraphicsContext()) : NULL
                if win :
                    win.setWindowRectangle(rect[2] + 10 + rect[0], rect[1], rect[2], rect[3])
        else : 
            udc = ea.getUserDataContainer()
            if udc :
                OSG_ALWAYS, "contents of ", udc.getName(), ": "
                for(unsigned int i = 0 i < udc.getNumUserObjects() ++i)
                    vo = dynamic_cast< osg.ValueObject*>(udc.getUserObject(i))
                    OSG_ALWAYS, "  ", vo.getName(), ": "

                    vlv = MyValueListVisitor()
                    vo.get(vlv)
                    OSG_ALWAYS, vlv.value()
        return True

    return False

def createHUD():

    

    # create the hud. derived from osgHud.cpp
    # adds a set of quads, each in a separate Geode - which can be picked individually
    # eg to be used as a menuing/help system!
    # Can pick texts too!

    hudCamera = osg.Camera()
    hudCamera.setReferenceFrame(osg.Transform.ABSOLUTE_RF)
    hudCamera.setProjectionMatrixAsOrtho2D(0,1280,0,1024)
    hudCamera.setViewMatrix(osg.Matrix.identity())
    hudCamera.setRenderOrder(osg.Camera.POST_RENDER)
    hudCamera.setClearMask(GL_DEPTH_BUFFER_BIT)

    timesFont = str("fonts/times.ttf")

    # turn lighting off for the text and disable depth test to ensure its always ontop.
    position = osg.Vec3(150.0,800.0,0.0)
    delta = osg.Vec3(0.0,-60.0,0.0)

        geode = osg.Geode()
        stateset = geode.getOrCreateStateSet()
        stateset.setMode(GL_LIGHTING,osg.StateAttribute.OFF)
        stateset.setMode(GL_DEPTH_TEST,osg.StateAttribute.OFF)
        geode.setName("simple")
        hudCamera.addChild(geode)

        text = osgText.Text()
        geode.addDrawable( text )

        text.setFont(timesFont)
        text.setText("Picking in Head Up Displays is simple!")
        text.setPosition(position)

        position += delta


    for (int i=0 i<5 i++) 
        dy = osg.Vec3(0.0,-30.0,0.0)
        dx = osg.Vec3(120.0,0.0,0.0)
        geode = osg.Geode()
        stateset = geode.getOrCreateStateSet()
         char *opts[]="One", "Two", "Three", "January", "Feb", "2003"
        quad = osg.Geometry()
        stateset.setMode(GL_LIGHTING,osg.StateAttribute.OFF)
        stateset.setMode(GL_DEPTH_TEST,osg.StateAttribute.OFF)
        name = "subOption"
        name += " "
        name += str(opts[i])
        geode.setName(name)
        vertices = osg.Vec3Array(4) # 1 quad
        colors = osg.Vec4Array()
        colors = osg.Vec4Array()
        colors.push_back(osg.Vec4(0.8-0.1*i,0.1*i,0.2*i, 1.0))
        quad.setColorArray(colors, osg.Array.BIND_OVERALL)
        (*vertices)[0]=position
        (*vertices)[1]=position+dx
        (*vertices)[2]=position+dx+dy
        (*vertices)[3]=position+dy
        quad.setVertexArray(vertices)
        quad.addPrimitiveSet(osg.DrawArrays(osg.PrimitiveSet.QUADS,0,4))
        geode.addDrawable(quad)
        hudCamera.addChild(geode)

        position += delta



     # this displays what has been selected
        geode = osg.Geode()
        stateset = geode.getOrCreateStateSet()
        stateset.setMode(GL_LIGHTING,osg.StateAttribute.OFF)
        stateset.setMode(GL_DEPTH_TEST,osg.StateAttribute.OFF)
        geode.setName("The text label")
        hudCamera.addChild(geode)

        position += delta

    return hudCamera



class ForwardToDeviceEventHandler (osgGA.GUIEventHandler) :
    ForwardToDeviceEventHandler(osgGA.Device* device) : osgGA.GUIEventHandler(), _device(device) 

    virtual bool handle ( osgGA.GUIEventAdapter ea, osgGA.GUIActionAdapter aa, osg.Object *, osg.NodeVisitor *)
        _device.sendEvent(ea)
        return False
    _device = osgGA.Device()


class OscServiceDiscoveredEventHandler (ForwardToDeviceEventHandler) :
    OscServiceDiscoveredEventHandler() : ForwardToDeviceEventHandler(NULL) 

    def handle(ea, aa, o, nv):

        
        if _device.valid() :
            return ForwardToDeviceEventHandler.handle(ea, aa, o, nv)

        if ea.getEventType() == osgGA.GUIEventAdapter.USER :
            if ea.getName() == "/zeroconf/service-added" :
                host = str()
                port = unsigned int()
                ea.getUserValue("host", host)
                ea.getUserValue("port", port)

                OSG_ALWAYS, "osc-service discovered: ", host, ":", port()

                ss = std.ostringstream()
                ss, host, ":", port, ".sender.osc"
                _device = osgDB.readFile<osgGA.Device>(ss.str())

                view = dynamic_cast<osgViewer.View*>(aa)
                if view :
                    view.addEventHandler(PickHandler(_device.get()))
                return True
        return False



def main(argc, argv):

    

    # use an ArgumentParser object to manage the program arguments.
    arguments = osg.ArgumentParser(argc,argv)

    arguments.getApplicationUsage().addCommandLineOption("--zeroconf","uses zeroconf to advertise the osc-plugin and to discover it")
    arguments.getApplicationUsage().addCommandLineOption("--sender","create a view which sends its events via osc")
    arguments.getApplicationUsage().addCommandLineOption("--recevier","create a view which receive its events via osc")



    # read the scene from the list of file specified commandline args.
    scene = osgDB.readNodeFiles(arguments)

    if !scene :
        print argv[0], ": requires filename argument."
        return 1

    use_zeroconf = bool(False)
    use_sender = bool(False)
    use_receiver = bool(False)
    if arguments.find("--zeroconf") > 0 :  use_zeroconf = True 
    if arguments.find("--sender") > 0 :  use_sender = True 
    if arguments.find("--receiver") > 0 :  use_receiver = True 
    # construct the viewer.
    viewer = osgViewer.CompositeViewer(arguments)

    # receiver view
    if use_receiver : 
        traits = osg.GraphicsContext.Traits()
        traits.x = 600
        traits.y = 100
        traits.width = 400
        traits.height = 400
        traits.windowDecoration = True
        traits.doubleBuffer = True
        traits.sharedContext = 0
        traits.windowName = "Receiver / view two"

        gc = osg.GraphicsContext.createGraphicsContext(traits.get())

        view = osgViewer.View()
        view.setName("View two")
        viewer.addView(view)

        group = osg.Group()
        group.addChild(scene.get())
        geode = osg.Geode()
        group.addChild(geode)

        text = osgText.Text()
        geode.addDrawable( text )

        text.setFont("Arial.ttf")
        text.setText("Waiting for data")
        text.setPosition(osg.Vec3(-50,0,30))
        text.setAxisAlignment(osgText.TextBase.SCREEN)
        text.setDataVariance(osg.Object.DYNAMIC)
        text.setCharacterSize(2.0)
        view.setSceneData(group)
        view.getCamera().setName("Cam two")
        view.getCamera().setViewport(osg.Viewport(0,0, traits.width, traits.height))
        view.getCamera().setGraphicsContext(gc.get())

        view.addEventHandler( osgViewer.StatsHandler )()
        view.addEventHandler( UserEventHandler(text) )

        device = osgDB.readFile<osgGA.Device>("0.0.0.0:9000.receiver.osc")
        if device.valid()  (device.getCapabilities()  osgGA.Device.RECEIVE_EVENTS) :
            view.addDevice(device.get())

            # add a zeroconf device, advertising the osc-device
            if use_zeroconf :
                zeroconf_device = osgDB.readFile<osgGA.Device>("_osc._udp:9000.advertise.zeroconf")
                if zeroconf_device :
                    view.addDevice(zeroconf_device)
        else : 
            OSG_WARN, "could not open osc-device, receiving will not work"

    # sender view
    if use_sender : 
        traits = osg.GraphicsContext.Traits()
        traits.x = 100
        traits.y = 100
        traits.width = 400
        traits.height = 400
        traits.windowDecoration = True
        traits.doubleBuffer = True
        traits.sharedContext = 0
        traits.windowName = "Sender / view one"

        gc = osg.GraphicsContext.createGraphicsContext(traits.get())


        view = osgViewer.View()
        view.setName("View one")
        viewer.addView(view)

        g = osg.Group()
        g.addChild(scene.get())
        g.addChild(createHUD())
        view.setSceneData(g)
        view.getCamera().setName("Cam one")
        view.getCamera().setViewport(osg.Viewport(0,0, traits.width, traits.height))
        view.getCamera().setGraphicsContext(gc.get())
        view.setCameraManipulator(osgGA.TrackballManipulator)()

        # add the state manipulator
        statesetManipulator = osgGA.StateSetManipulator()
        statesetManipulator.setStateSet(view.getCamera().getOrCreateStateSet())

        view.addEventHandler( statesetManipulator.get() )
        view.addEventHandler( osgViewer.StatsHandler )()

        if use_zeroconf :
            zeroconf_device = osgDB.readFile<osgGA.Device>("_osc._udp.discover.zeroconf")
            if zeroconf_device : 
                view.addDevice(zeroconf_device)
                view.getEventHandlers().push_front(OscServiceDiscoveredEventHandler())

        else :
            device = osgDB.readFile<osgGA.Device>("localhost:9000.sender.osc")
            if device.valid()  (device.getCapabilities()  osgGA.Device.SEND_EVENTS) :
                # add as first event handler, so it gets ALL events ...
                view.getEventHandlers().push_front(ForwardToDeviceEventHandler(device.get()))

                # add the demo-pick-event-handler
                view.addEventHandler(PickHandler(device.get()))
            else : 
                OSG_WARN, "could not open osc-device, sending will not work"




    while arguments.read("-s") :  viewer.setThreadingModel(osgViewer.CompositeViewer.SingleThreaded) 
    while arguments.read("-g") :  viewer.setThreadingModel(osgViewer.CompositeViewer.CullDrawThreadPerContext) 
    while arguments.read("-c") :  viewer.setThreadingModel(osgViewer.CompositeViewer.CullThreadPerCameraDrawThreadPerContext) 

     # run the viewer's main frame loop
     return viewer.run()


if __name__ == "__main__":
    main(sys.argv)
