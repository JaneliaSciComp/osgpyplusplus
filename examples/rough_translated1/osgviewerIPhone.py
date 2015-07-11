#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgviewerIPhone"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osg
from osgpypp import osgDB
from osgpypp import osgText
from osgpypp import osgViewer


# Translated from file 'iphoneViewerAppDelegate.h'

#Created by Thomas Hogarth 2009

#force the link to our desired osgPlugins
#include "osgPlugins.h"

#include <osgDB/ReadFile>
#include <osg/MatrixTransform>
#include <osgText/Text>
#include <osgViewer/Viewer>


#import <UIKit/UIKit.h>


@interface iphoneViewerAppDelegate : NSObject <UIApplicationDelegate, UIAccelerometerDelegate> 
    
    _window = UIWindow*() #main application window
    
    _displayLink = CADisplayLink*()
    
    _viewer = osgViewer.Viewer()
    _root = osg.MatrixTransform()
    

@property (nonatomic, retain) #IBOutlet UIWindow *_window

- (void)updateScene

@end


# Translated from file 'osgPlugins.h'

#pragma once 

#include <osgViewer/GraphicsWindow>
#include <osgDB/Registry>

#windowing system
USE_GRAPICSWINDOW_IMPLEMENTATION(IOS)


#plugins

#USE_OSGPLUGIN(obj)
#USE_OSGPLUGIN(ive)
USE_OSGPLUGIN(osg)

USE_OSGPLUGIN(imageio)
USE_OSGPLUGIN(avfoundation)
#USE_OSGPLUGIN(freetype)



if __name__ == "__main__":
    main(sys.argv)
