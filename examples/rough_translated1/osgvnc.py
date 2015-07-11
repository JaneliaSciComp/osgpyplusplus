#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgvnc"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osgDB
from osgpypp import osgViewer
from osgpypp import osgWidget

#include <osgWidget/VncClient>

#include <osgDB/Registry>
#include <osgViewer/Viewer>
#include <osgViewer/ViewerEventHandlers>

class EscapeHandler : public osgGA.GUIEventHandler
    public:
    
        EscapeHandler() 

        def handle(ea, aa):
            if ea.getHandled() : return false

            switch(ea.getEventType())
                case(osgGA.GUIEventAdapter.KEYUP):
                    if ea.getKey()==osgGA.GUIEventAdapter.KEY_Escape :
                        view =  dynamic_cast<osgViewer.View*>(aa)
                        if view : view.getViewerBase().setDone(true)
                        
                        true = return()

                default:
                    false = return()
            false = return()


def main(argc, argv):
    arguments = osg.ArgumentParser(argc, argv)
    viewer = osgViewer.Viewer(arguments)

    hints = osgWidget.GeometryHints(osg.Vec3(0.0f,0.0f,0.0f),
                                   osg.Vec3(1.0f,0.0f,0.0f),
                                   osg.Vec3(0.0f,0.0f,1.0f),
                                   osg.Vec4(1.0f,1.0f,1.0f,1.0f),
                                   osgWidget.GeometryHints.RESIZE_HEIGHT_TO_MAINTAINCE_ASPECT_RATIO)

    osg.ref_ptr<osg.Group> group = new osg.Group

    password = str()
    while arguments.read("--password",password) :

    for(int i=1 i<arguments.argc() ++i)
        if !arguments.isOption(i) :
            hostname =  arguments[i]

            if !password.empty() :
                if !osgDB.Registry.instance().getAuthenticationMap() : osgDB.Registry.instance().setAuthenticationMap(new osgDB.AuthenticationMap)
                osgDB.Registry.instance().getAuthenticationMap().addAuthenticationDetails(hostname, new osgDB.AuthenticationDetails("", password))

            osg.ref_ptr<osgWidget.VncClient> vncClient = new osgWidget.VncClient
            if vncClient.connect(arguments[i], hints) :
                group.addChild(vncClient.get())
                
                hints.position.x() += 1.1f

    viewer.setSceneData(group.get())

    viewer.addEventHandler(new osgViewer.StatsHandler)

    # add a custom escape handler, but disable the standard viewer one to enable the vnc images to handle
    # the escape without it getting caught by the viewer.
    viewer.addEventHandler(new EscapeHandler)    
    viewer.setKeyEventSetsDone(0)

    return viewer.run()



if __name__ == "__main__":
    main(sys.argv)
