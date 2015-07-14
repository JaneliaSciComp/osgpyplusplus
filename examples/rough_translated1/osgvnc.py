#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgvnc"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osgDB
from osgpypp import osgViewer
from osgpypp import osgWidget


# Translated from file 'osgvnc.cpp'

#include <osgWidget/VncClient>

#include <osgDB/Registry>
#include <osgViewer/Viewer>
#include <osgViewer/ViewerEventHandlers>

class EscapeHandler (osgGA.GUIEventHandler) :
    
        EscapeHandler() 

        def handle(ea, aa):

            
            if ea.getHandled() : return False

            switch(ea.getEventType())
                case(osgGA.GUIEventAdapter.KEYUP):
                    if ea.getKey()==osgGA.GUIEventAdapter.KEY_Escape :
                        view = dynamic_cast<osgViewer.View*>(aa)
                        if view : view.getViewerBase().setDone(True)
                        
                        return True

                default:
                    return False
            return False


def main(argv):

    
    arguments = osg.ArgumentParser(argv)
    viewer = osgViewer.Viewer(arguments)

    hints = osgWidget.GeometryHints(osg.Vec3(0.0,0.0,0.0),
                                   osg.Vec3(1.0,0.0,0.0),
                                   osg.Vec3(0.0,0.0,1.0),
                                   osg.Vec4(1.0,1.0,1.0,1.0),
                                   osgWidget.GeometryHints.RESIZE_HEIGHT_TO_MAINTAINCE_ASPECT_RATIO)

    group = osg.Group()

    password = str()
    while arguments.read("--password",password) :

    for(int i=1 i<arguments.argc() ++i)
        if  not arguments.isOption(i) :
            hostname = arguments[i]

            if  not password.empty() :
                if  not osgDB.Registry.instance().getAuthenticationMap() : osgDB.Registry.instance().setAuthenticationMap(osgDB.AuthenticationMap)()
                osgDB.Registry.instance().getAuthenticationMap().addAuthenticationDetails(hostname, osgDB.AuthenticationDetails("", password))

            vncClient = osgWidget.VncClient()
            if vncClient.connect(arguments[i], hints) :
                group.addChild(vncClient)
                
                hints.position.x() += 1.1

    viewer.setSceneData(group)

    viewer.addEventHandler(osgViewer.StatsHandler)()

    # add a custom escape handler, but disable the standard viewer one to enable the vnc images to handle
    # the escape without it getting caught by the viewer.
    viewer.addEventHandler(EscapeHandler)()    
    viewer.setKeyEventSetsDone(0)

    return viewer.run()



if __name__ == "__main__":
    main(sys.argv)
