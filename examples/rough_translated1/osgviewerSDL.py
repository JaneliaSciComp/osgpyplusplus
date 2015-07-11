#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgviewerSDL"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osgDB
from osgpypp import osgGA
from osgpypp import osgViewer


# Translated from file 'osgviewerSDL.cpp'

# OpenSceneGraph example, osgviewerSDL.
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

# (C) 2005 Mike Weiblen http:#mew.cx/ released under the OSGPL.
# Simple example using GLUT to create an OpenGL window and OSG for rendering.
# Derived from osgGLUTsimple.cpp and osgkeyboardmouse.cpp

#include <osgViewer/Viewer>
#include <osgViewer/ViewerEventHandlers>
#include <osgGA/TrackballManipulator>
#include <osgDB/ReadFile>

#include "SDL.h"

#include <iostream>

def convertEvent(event, eventQueue):

    
    switch (event.type) 

        case SDL_MOUSEMOTION:
            eventQueue.mouseMotion(event.motion.x, event.motion.y)
            return True

        case SDL_MOUSEBUTTONDOWN:
            eventQueue.mouseButtonPress(event.button.x, event.button.y, event.button.button)
            return True

        case SDL_MOUSEBUTTONUP:
            eventQueue.mouseButtonRelease(event.button.x, event.button.y, event.button.button)
            return True

        case SDL_KEYUP:
            eventQueue.keyRelease( (osgGA.GUIEventAdapter.KeySymbol) event.key.keysym.unicode)
            return True

        case SDL_KEYDOWN:
            eventQueue.keyPress( (osgGA.GUIEventAdapter.KeySymbol) event.key.keysym.unicode)
            return True

        case SDL_VIDEORESIZE:
            eventQueue.windowResize(0, 0, event.resize.w, event.resize.h )
            return True

        default:
            break
    return False

def main(argc, argv):

    
    if argc<2 :
        print argv[0], ": requires filename argument."
        return 1

    # init SDL
    if  SDL_Init(SDL_INIT_VIDEO) < 0  :
        fprintf(stderr, "Unable to init SDL: %s\n", SDL_GetError())
        exit(1)
    atexit(SDL_Quit)
    

    # load the scene.
    loadedModel = osgDB.readNodeFile(argv[1])
    if !loadedModel :
        print argv[0], ": No data loaded."
        return 1

    # Starting with SDL 1.2.10, passing in 0 will use the system's current resolution.
    windowWidth = 0
    windowHeight = 0

    # Passing in 0 for bitdepth also uses the system's current bitdepth. This works before 1.2.10 too.
    bitDepth = 0

    # If not linked to SDL 1.2.10+, then we must use hardcoded values
    linked_version = SDL_Linked_Version()
    if linked_version.major == 1  linked_version.minor == 2 :
        if linked_version.patch < 10 :
            windowWidth = 1280
            windowHeight = 1024

    SDL_GL_SetAttribute( SDL_GL_RED_SIZE, 5 )
    SDL_GL_SetAttribute( SDL_GL_GREEN_SIZE, 5 )
    SDL_GL_SetAttribute( SDL_GL_BLUE_SIZE, 5 )
    SDL_GL_SetAttribute( SDL_GL_DEPTH_SIZE, 16 )
    SDL_GL_SetAttribute( SDL_GL_DOUBLEBUFFER, 1 )
    
    # set up the surface to render to
    screen = SDL_SetVideoMode(windowWidth, windowHeight, bitDepth, SDL_OPENGL | SDL_FULLSCREEN | SDL_RESIZABLE)
    if  screen == NULL  :
        std.cerr, "Unable to set ", windowWidth, "x", windowHeight, " video: %s\n", SDL_GetError()
        exit(1)

    SDL_EnableUNICODE(1)
    
    # If we used 0 to set the fields, query the values so we can pass it to osgViewer
    windowWidth = screen.w
    windowHeight = screen.h
    
    viewer = osgViewer.Viewer()
    gw = viewer.setUpViewerAsEmbeddedInWindow(0,0,windowWidth,windowHeight)
    viewer.setSceneData(loadedModel.get())
    viewer.setCameraManipulator(osgGA.TrackballManipulator)()
    viewer.addEventHandler(osgViewer.StatsHandler)()
    viewer.realize()

    done = False
    while  !done  :
        event = SDL_Event()

        while  SDL_PollEvent(event)  :
            # pass the SDL event into the viewers event queue
            convertEvent(event, *(gw.getEventQueue()))

            switch (event.type) 

                case SDL_VIDEORESIZE:
                    SDL_SetVideoMode(event.resize.w, event.resize.h, bitDepth, SDL_OPENGL | SDL_RESIZABLE)
                    gw.resized(0, 0, event.resize.w, event.resize.h )
                    break

                case SDL_KEYUP:

                    if event.key.keysym.sym==SDLK_ESCAPE : done = True
                    if event.key.keysym.sym=='f' : 
                        SDL_WM_ToggleFullScreen(screen)
                        gw.resized(0, 0, screen.w, screen.h )

                    break

                case SDL_QUIT:
                    done = True

        if done : continue


        # draw the frame
        viewer.frame()

        # Swap Buffers
        SDL_GL_SwapBuffers()
   
    return 0

#EOF

# Translated from file 'SDLMainForMacOSX.h'

# OpenSceneGraph example, osgviewerSDL.
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

#   SDLMain.m - main entry point for our Cocoa-ized SDL app
#       Initial Version: Darrell Walisser <dwaliss1@purdue.edu>
#       Non-NIB-Code  other changes: Max Horn <max@quendi.de>
#
#    Feel free to customize this file to suit your needs
#	
#	OSG users: This is the standard SDLMain (nibless) that 
#	comes with the SDL distribution. Only the file name has
#	been changed to avoid confusing non-Mac users.
#

#import <Cocoa/Cocoa.h>

@interface SDLMain : NSObject
@end


if __name__ == "__main__":
    main(sys.argv)
