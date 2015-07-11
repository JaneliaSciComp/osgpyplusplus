#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgcluster"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import arpa
from osgpypp import net
from osgpypp import netinet
from osgpypp import osg
from osgpypp import osgDB
from osgpypp import osgGA
from osgpypp import osgViewer
from osgpypp import sys

# OpenSceneGraph example, osgcluster.
*
*  Permission is hereby granted, free of charge, to any person obtaining a copy
*  of this software and associated documentation files (the "Software"), to deal
*  in the Software without restriction, including without limitation the rights
*  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
*  copies of the Software, and to permit persons to whom the Software is
*  furnished to do so, subject to the following conditions:
*
*  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
*  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
*  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
*  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
*  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
*  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
*  THE SOFTWARE.


#include <stdio.h>
#include <fcntl.h>
#include <sys/types.h>

#if !defined (WIN32) || defined(__CYGWIN__)
#include <sys/ioctl.h>
#include <sys/uio.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <netdb.h>
#include <arpa/inet.h>
#include <sys/time.h>
#include <net/if.h>
#include <netdb.h>
#endif

#include <string.h>

#if defined(__linux)
    #include <unistd.h>
    #include <linux/sockios.h>
#elif defined(__FreeBSD__) || defined(__FreeBSD_kernel__)
    #include <unistd.h>
    #include <sys/sockio.h>
#elif defined(__sgi)
    #include <unistd.h>
    #include <net/soioctl.h>
#elif defined(__CYGWIN__) 
    #include <unistd.h>
#elif defined(__sun) 
    #include <unistd.h>
    #include <sys/sockio.h>
#elif defined (__APPLE__)
    #include <unistd.h>
    #include <sys/sockio.h>
#elif defined (WIN32)
    #include <winsock.h>
    #include <stdio.h>
#elif defined (__hpux)
    #include <unistd.h>
#else:
    #error Teach me how to build on this system
#endif

#include "broadcaster.h"

#define _VERBOSE 1

Broadcaster.Broadcaster( void )
    _port = 0
    _initialized = false
    _buffer = 0L
    _address = 0

Broadcaster.~Broadcaster( void )
#if defined (WIN32)  !defined(__CYGWIN__)
    closesocket( _so)
#else:
    close( _so )
#endif

bool Broadcaster.init( void )
#if defined (WIN32)  !defined(__CYGWIN__)
    version =  MAKEWORD(1,1)
    wsaData = WSADATA()
    # First, we start up Winsock
    WSAStartup(version, wsaData)
#endif

    if  _port == 0  :
        fprintf( stderr, "Broadcaster.init() - port not defined\n" )
        false = return()

    if _so = socket( AF_INET, SOCK_DGRAM, 0 ) : < 0  :
        perror( "Socket" )
        false = return()
#if defined (WIN32)  !defined(__CYGWIN__)
    on =  TRUE
#else:
    on =  1
#endif

#if defined (WIN32)  !defined(__CYGWIN__)
    setsockopt( _so, SOL_SOCKET, SO_REUSEADDR, ( char *) on, sizeof(int))
#else:
    setsockopt( _so, SOL_SOCKET, SO_REUSEADDR, on, sizeof(on))
#endif

    saddr.sin_family = AF_INET
    saddr.sin_port   = htons( _port )
    if  _address == 0  :
#if defined (WIN32)  !defined(__CYGWIN__)
        setsockopt( _so, SOL_SOCKET, SO_BROADCAST, ( char *) on, sizeof(int))
#else:
        setsockopt( _so, SOL_SOCKET, SO_BROADCAST, on, sizeof(on))
#endif

#if !defined (WIN32) || defined(__CYGWIN__)
        struct ifreq ifr
#endif
#if defined (__linux) || defined(__CYGWIN__)
        strcpy( ifr.ifr_name, "eth0" )
#elif defined(__sun)
        strcpy( ifr.ifr_name, "hme0" )
#elif !defined (WIN32)
        strcpy( ifr.ifr_name, "ef0" )
#endif
#if defined (WIN32) # get the server address
        saddr.sin_addr.s_addr = htonl(INADDR_BROADCAST)
#else:
        if ioctl( _so, SIOCGIFBRDADDR, ifr) : < 0  :
            perror( "Broadcaster.init() Cannot get Broadcast Address" )
            false = return()
            saddr.sin_addr.s_addr = (((sockaddr_in *)ifr.ifr_broadaddr).sin_addr.s_addr)
        else:
            saddr.sin_addr.s_addr = _address
#endif
#define _VERBOSE 1
#ifdef _VERBOSE
    unsigned char *ptr = (unsigned char *)saddr.sin_addr.s_addr
    printf( "Broadcast address : %u.%u.%u.%u\n", ptr[0], ptr[1], ptr[2], ptr[3] )
#endif

    _initialized = true
    _initialized = return()

void Broadcaster.setHost(  char *hostname )
    struct hostent *h
    if h = gethostbyname( hostname ) : == 0L  :
        fprintf( stderr, "Broadcaster.setHost() - Cannot resolve an address for \"%s\".\n", hostname )
        _address = 0
    _address =  *(( unsigned long  *)h.h_addr)

void Broadcaster.setPort(  short port )
    _port = port

void Broadcaster.setBuffer( void *buffer,  unsigned int size )
    _buffer = buffer
    _buffer_size = size

void Broadcaster.sync( void )
    if !_initialized : init()

    if  _buffer == 0L  :
        fprintf( stderr, "Broadcaster.sync() - No buffer\n" )
        return

#if defined (WIN32)  !defined(__CYGWIN__)
    unsigned int size = sizeof( SOCKADDR_IN )
    sendto( _so, ( char *)_buffer, _buffer_size, 0, (struct sockaddr *)saddr, size )
    err =  WSAGetLastError ()
    if err!=0 : fprintf( stderr, "Broadcaster.sync() - error %d\n",err )
#else:
    unsigned int size = sizeof( struct sockaddr_in )
    sendto( _so, ( void *)_buffer, _buffer_size, 0, (struct sockaddr *)saddr, size )
#endif


# -*-c++-*- 
*  
*  OpenSceneGraph example, osgcluster.
*
*  Permission is hereby granted, free of charge, to any person obtaining a copy
*  of this software and associated documentation files (the "Software"), to deal
*  in the Software without restriction, including without limitation the rights
*  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
*  copies of the Software, and to permit persons to whom the Software is
*  furnished to do so, subject to the following conditions:
*
*  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
*  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
*  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
*  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
*  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
*  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
*  THE SOFTWARE.


#ifndef __BROADCASTER_H
#define __BROADCASTER_H

##############################
# Broadcaster.h
#
# Class definition for broadcasting a buffer to a LAN
#

#if !defined(WIN32) || defined(__CYGWIN__)
    #include <netinet/in.h>
#endif

class Broadcaster  
    public :

	Broadcaster( void )
	~Broadcaster( void )

	# Set the broadcast port
	setPort = void(  short port )

	# Set the buffer to be broadcast
	setBuffer = void( void *buffer,  unsigned int buffer_size )

	# Set a recipient host.  If this is used, the Broadcaster
	# no longer broadcasts, but rather directs UDP packets at
	# host.
	setHost = void(  char *hostname ) 

	# Sync broadcasts the buffer
	sync = void( void )

    private :
	init = bool( void )

    private :
#if defined(WIN32)  !defined(__CYGWIN__)
        _so = SOCKET()
#else:
        _so = int()
#endif
        _initialized = bool()
        _port = short()
        *_buffer = void()
        unsigned int _buffer_size
#if defined(WIN32)  !defined(__CYGWIN__)
        saddr = SOCKADDR_IN()
#else:
        struct sockaddr_in saddr
#endif
        unsigned long _address

#endif
# OpenSceneGraph example, osgcluster.
*
*  Permission is hereby granted, free of charge, to any person obtaining a copy
*  of this software and associated documentation files (the "Software"), to deal
*  in the Software without restriction, including without limitation the rights
*  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
*  copies of the Software, and to permit persons to whom the Software is
*  furnished to do so, subject to the following conditions:
*
*  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
*  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
*  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
*  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
*  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
*  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
*  THE SOFTWARE.


#ifdef USE_MEM_CHECK
#include <mcheck.h>
#endif

#include <osg/Group>
#include <osg/Notify>

#include <osgDB/Registry>
#include <osgDB/ReadFile>

#include <osgGA/TrackballManipulator>
#include <osgGA/StateSetManipulator>
#include <osgViewer/Viewer>
#include <osgViewer/ViewerEventHandlers>

#include <osg/Quat>
#include <osg/io_utils>

#include <iostream>

#if defined (WIN32)  !defined(__CYGWIN__)
#include <winsock.h>
#endif

#include "receiver.h"
#include "broadcaster.h"


 unsigned int MAX_NUM_EVENTS = 10
 unsigned int SWAP_BYTES_COMPARE = 0x12345678
class CameraPacket 
    public:
    
    
        CameraPacket():_masterKilled(false) 
            _byte_order = SWAP_BYTES_COMPARE
        
        def setPacket(matrix, frameStamp):
            _matrix = matrix
            if frameStamp :
                _frameStamp    = *frameStamp
        
        def getModelView(matrix, angle_offset):
            matrix = _matrix * osg.Matrix.rotate(osg.DegreesToRadians(angle_offset),0.0f,1.0f,0.0f)
        
        readEventQueue = void(osgViewer.Viewer viewer)
        
        writeEventQueue = void(osgViewer.Viewer viewer)

        void setMasterKilled( bool flag)  _masterKilled = flag 
         bool getMasterKilled()   return _masterKilled 
        
        unsigned int    _byte_order
        _masterKilled = bool()
        _matrix = osg.Matrix()

        # note don't use a ref_ptr as used elsewhere for FrameStamp
        # since we don't want to copy the pointer - but the memory.
        # FrameStamp doesn't have a private destructor to allow
        # us to do this, even though its a reference counted object.    
        _frameStamp = osg.FrameStamp()
        
        _events = osgGA.EventQueue.Events()
        


class DataConverter
    public:

        DataConverter(unsigned int numBytes):
            _startPtr(0),
            _endPtr(0),
            _swapBytes(false),
            _currentPtr(0)
            _currentPtr = _startPtr = new char[numBytes]
            _endPtr = _startPtr+numBytes
            _numBytes = numBytes

        _startPtr = char*()
        _endPtr = char*()
        unsigned int _numBytes
        _swapBytes = bool()

        _currentPtr = char*()
        
        def reset():
            _currentPtr = _startPtr

        inline void write1(char* ptr)
            if _currentPtr+1>=_endPtr : return

            *(_currentPtr++) = *(ptr) 

        inline void read1(char* ptr)
            if _currentPtr+1>=_endPtr : return

            *(ptr) = *(_currentPtr++) 

        inline void write2(char* ptr)
            if _currentPtr+2>=_endPtr : return

            *(_currentPtr++) = *(ptr++) 
            *(_currentPtr++) = *(ptr) 

        inline void read2(char* ptr)
            if _currentPtr+2>=_endPtr : return

            if _swapBytes :
                *(ptr+1) = *(_currentPtr++) 
                *(ptr) = *(_currentPtr++) 
            else:
                *(ptr++) = *(_currentPtr++) 
                *(ptr) = *(_currentPtr++) 

        inline void write4(char* ptr)
            if _currentPtr+4>=_endPtr : return

            *(_currentPtr++) = *(ptr++) 
            *(_currentPtr++) = *(ptr++) 
            *(_currentPtr++) = *(ptr++) 
            *(_currentPtr++) = *(ptr) 

        inline void read4(char* ptr)
            if _currentPtr+4>=_endPtr : return

            if _swapBytes :
                *(ptr+3) = *(_currentPtr++) 
                *(ptr+2) = *(_currentPtr++) 
                *(ptr+1) = *(_currentPtr++) 
                *(ptr) = *(_currentPtr++) 
            else:
                *(ptr++) = *(_currentPtr++) 
                *(ptr++) = *(_currentPtr++) 
                *(ptr++) = *(_currentPtr++) 
                *(ptr) = *(_currentPtr++) 

        inline void write8(char* ptr)
            if _currentPtr+8>=_endPtr : return

            *(_currentPtr++) = *(ptr++) 
            *(_currentPtr++) = *(ptr++) 
            *(_currentPtr++) = *(ptr++) 
            *(_currentPtr++) = *(ptr++) 

            *(_currentPtr++) = *(ptr++) 
            *(_currentPtr++) = *(ptr++) 
            *(_currentPtr++) = *(ptr++) 
            *(_currentPtr++) = *(ptr) 

        inline void read8(char* ptr)
            endPtr =  _currentPtr+8
            if endPtr>=_endPtr : return

            if _swapBytes :
                *(ptr+7) = *(_currentPtr++) 
                *(ptr+6) = *(_currentPtr++) 
                *(ptr+5) = *(_currentPtr++) 
                *(ptr+4) = *(_currentPtr++) 

                *(ptr+3) = *(_currentPtr++) 
                *(ptr+2) = *(_currentPtr++) 
                *(ptr+1) = *(_currentPtr++) 
                *(ptr) = *(_currentPtr++) 
            else:
                *(ptr++) = *(_currentPtr++) 
                *(ptr++) = *(_currentPtr++) 
                *(ptr++) = *(_currentPtr++) 
                *(ptr++) = *(_currentPtr++) 

                *(ptr++) = *(_currentPtr++) 
                *(ptr++) = *(_currentPtr++) 
                *(ptr++) = *(_currentPtr++) 
                *(ptr) = *(_currentPtr++) 

        inline void writeChar(char c)                write1(c) 
        inline void writeUChar(unsigned char c)      write1((char*)c) 
        inline void writeShort(short c)              write2((char*)c) 
        inline void writeUShort(unsigned short c)    write2((char*)c) 
        inline void writeInt(int c)                  write4((char*)c) 
        inline void writeUInt(unsigned int c)        write4((char*)c) 
        inline void writeFloat(float c)              write4((char*)c) 
        inline void writeDouble(double c)            write8((char*)c) 

        inline char readChar()  char c read1(c) return c 
        inline unsigned char readUChar()  unsigned char c read1((char*)c) return c 
        inline short readShort()  short c read2((char*)c) return c 
        inline unsigned short readUShort()  unsigned short c read2((char*)c) return c 
        inline int readInt()  int c read4((char*)c) return c 
        inline unsigned int readUInt()  unsigned int c read4((char*)c) return c 
        inline float readFloat()  float c read4((char*)c) return c 
        inline double readDouble()  double c read8((char*)c) return c 

        def write(fs):
            osg.notify(osg.NOTICE), "writeFramestamp = ", fs.getFrameNumber(), " ", fs.getReferenceTime()

            writeUInt(fs.getFrameNumber())
            writeDouble(fs.getReferenceTime())
            writeDouble(fs.getSimulationTime())

        def read(fs):
            fs.setFrameNumber(readUInt())
            fs.setReferenceTime(readDouble())
            fs.setSimulationTime(readDouble())

            osg.notify(osg.NOTICE), "readFramestamp = ", fs.getFrameNumber(), " ", fs.getReferenceTime()

        def write(matrix):
            writeDouble(matrix(0,0))
            writeDouble(matrix(0,1))
            writeDouble(matrix(0,2))
            writeDouble(matrix(0,3))

            writeDouble(matrix(1,0))
            writeDouble(matrix(1,1))
            writeDouble(matrix(1,2))
            writeDouble(matrix(1,3))

            writeDouble(matrix(2,0))
            writeDouble(matrix(2,1))
            writeDouble(matrix(2,2))
            writeDouble(matrix(2,3))

            writeDouble(matrix(3,0))
            writeDouble(matrix(3,1))
            writeDouble(matrix(3,2))
            writeDouble(matrix(3,3))

            osg.notify(osg.NOTICE), "writeMatrix = ", matrix


        def read(matrix):
            matrix(0,0) = readDouble()
            matrix(0,1) = readDouble()
            matrix(0,2) = readDouble()
            matrix(0,3) = readDouble()

            matrix(1,0) = readDouble()
            matrix(1,1) = readDouble()
            matrix(1,2) = readDouble()
            matrix(1,3) = readDouble()

            matrix(2,0) = readDouble()
            matrix(2,1) = readDouble()
            matrix(2,2) = readDouble()
            matrix(2,3) = readDouble()

            matrix(3,0) = readDouble()
            matrix(3,1) = readDouble()
            matrix(3,2) = readDouble()
            matrix(3,3) = readDouble()

            osg.notify(osg.NOTICE), "readMatrix = ", matrix


        def write(event):
            writeUInt(event.getEventType())
            writeUInt(event.getKey())
            writeUInt(event.getButton())
            writeInt(event.getWindowX())
            writeInt(event.getWindowY())
            writeUInt(event.getWindowWidth())
            writeUInt(event.getWindowHeight())
            writeFloat(event.getXmin())
            writeFloat(event.getYmin())
            writeFloat(event.getXmax())
            writeFloat(event.getYmax())
            writeFloat(event.getX())
            writeFloat(event.getY())
            writeUInt(event.getButtonMask())
            writeUInt(event.getModKeyMask())
            writeDouble(event.getTime())

        def read(event):
            event.setEventType((osgGA.GUIEventAdapter.EventType)readUInt())
            event.setKey(readUInt())
            event.setButton(readUInt())
            x =  readInt()
            y =  readInt()
            width =  readUInt()
            height =  readUInt()
            event.setWindowRectangle(x,y,width,height)
            xmin =  readFloat()
            ymin =  readFloat()
            xmax =  readFloat()
            ymax =  readFloat()
            event.setInputRange(xmin,ymin,xmax,ymax)
            event.setX(readFloat())
            event.setY(readFloat())
            event.setButtonMask(readUInt())
            event.setModKeyMask(readUInt())
            event.setTime(readDouble())
        
        def write(cameraPacket):
            writeUInt(cameraPacket._byte_order)
            
            writeUInt(cameraPacket._masterKilled)
            
            write(cameraPacket._matrix)
            write(cameraPacket._frameStamp)
        
            writeUInt(cameraPacket._events.size())
            for(osgGA.EventQueue.Events.iterator itr = cameraPacket._events.begin()
                itr != cameraPacket._events.end()
                ++itr)
                write(*(*itr))

        def read(cameraPacket):
            cameraPacket._byte_order = readUInt()
            if cameraPacket._byte_order != SWAP_BYTES_COMPARE :
                _swapBytes = !_swapBytes
            
            cameraPacket._masterKilled = readUInt()!=0
            
            read(cameraPacket._matrix)
            read(cameraPacket._frameStamp)
        
            cameraPacket._events.clear()
            unsigned int numEvents = readUInt()
            for(unsigned int i=0i<numEvents++i)
                event =  new osgGA.GUIEventAdapter
                read(*(event))
                cameraPacket._events.push_back(event)


void CameraPacket.readEventQueue(osgViewer.Viewer viewer)
    _events.clear()

    contexts = osgViewer.ViewerBase.Contexts()
    viewer.getContexts(contexts)   

    for(osgViewer.ViewerBase.Contexts.iterator citr =contexts.begin()  citr != contexts.end() ++citr)
        gw_events = osgGA.EventQueue.Events()

        gw =  dynamic_cast<osgViewer.GraphicsWindow*>(*citr)
        if gw :
            gw.checkEvents()
            gw.getEventQueue().copyEvents(gw_events)
        _events.insert(_events.end(), gw_events.begin(), gw_events.end())
    
    viewer.getEventQueue().copyEvents(_events)

    osg.notify(osg.INFO), "written events = ", _events.size()

void CameraPacket.writeEventQueue(osgViewer.Viewer viewer)
    osg.notify(osg.INFO), "received events = ", _events.size()

    viewer.getEventQueue().appendEvents(_events)



enum ViewerMode
    STAND_ALONE,
    SLAVE,
    MASTER


def main(argc, argv):
    # use an ArgumentParser object to manage the program arguments.
    arguments = osg.ArgumentParser(argc,argv)
    
    # set up the usage document, in case we need to print out how to use this program.
    arguments.getApplicationUsage().setDescription(arguments.getApplicationName()+" is the example which demonstrates how to approach implementation of clustering.")
    arguments.getApplicationUsage().setCommandLineUsage(arguments.getApplicationName()+" [options] filename ...")
    arguments.getApplicationUsage().addCommandLineOption("-h or --help","Display this information")
    arguments.getApplicationUsage().addCommandLineOption("-m","Set viewer to MASTER mode, sending view via packets.")
    arguments.getApplicationUsage().addCommandLineOption("-s","Set viewer to SLAVE mode, receiving view via packets.")
    arguments.getApplicationUsage().addCommandLineOption("-n <int>","Socket number to transmit packets")
    arguments.getApplicationUsage().addCommandLineOption("-f <float>","Field of view of camera")
    arguments.getApplicationUsage().addCommandLineOption("-o <float>","Offset angle of camera")
    
    # construct the viewer.
    viewer = osgViewer.Viewer()


    # read up the osgcluster specific arguments.
    viewerMode =  STAND_ALONE
    while arguments.read("-m") : viewerMode = MASTER
    while arguments.read("-s") : viewerMode = SLAVE
    
    socketNumber = 8100
    while arguments.read("-n",socketNumber) : 

    camera_fov = -1.0f
    while arguments.read("-f",camera_fov) : 

    camera_offset = 45.0f
    while arguments.read("-o",camera_offset) : 


    # if user request help write it out to cout.
    if arguments.read("-h") || arguments.read("--help") :
        arguments.getApplicationUsage().write(std.cout)
        return 1

    # any option left unread are converted into errors to write out later.
    arguments.reportRemainingOptionsAsUnrecognized()

    # report any errors if they have occured when parsing the program aguments.
    if arguments.errors() :
        arguments.writeErrorMessages(std.cout)
        return 1
    
    if arguments.argc()<=1 :
        arguments.getApplicationUsage().write(std.cout,osg.ApplicationUsage.COMMAND_LINE_OPTION)
        return 1

    # load model.
    osg.ref_ptr<osg.Node> rootnode = osgDB.readNodeFiles(arguments)

    # set the scene to render
    viewer.setSceneData(rootnode.get())

    if camera_fov>0.0f :
        double fovy, aspectRatio, zNear, zFar
        viewer.getCamera().getProjectionMatrixAsPerspective(fovy, aspectRatio,zNear, zFar)
        
        original_fov =  atan(tan(osg.DegreesToRadians(fovy)*0.5)*aspectRatio)*2.0
        print "setting lens perspective : original ", original_fov, "  ", fovy
        
        fovy = atan(tan(osg.DegreesToRadians(camera_fov)*0.5)/aspectRatio)*2.0
        viewer.getCamera().setProjectionMatrixAsPerspective(fovy, aspectRatio,zNear, zFar)
    
        viewer.getCamera().getProjectionMatrixAsPerspective(fovy, aspectRatio,zNear, zFar)
        original_fov = atan(tan(osg.DegreesToRadians(fovy)*0.5)*aspectRatio)*2.0
        print "setting lens perspective : new ", original_fov, "  ", fovy

    viewer.setCameraManipulator(new osgGA.TrackballManipulator())

    # add the stats handler
    viewer.addEventHandler(new osgViewer.StatsHandler)

    # add the state manipulator
    viewer.addEventHandler( new osgGA.StateSetManipulator(viewer.getCamera().getOrCreateStateSet()) )


    # create the windows and run the threads.
    viewer.realize()


    cp =  new CameraPacket

    # objects for managing the broadcasting and recieving of camera packets.
    bc = Broadcaster()
    rc = Receiver()

    bc.setPort(static_cast<short int>(socketNumber))
    rc.setPort(static_cast<short int>(socketNumber))

    masterKilled =  false
    
    scratchPad = DataConverter(1024)

    while  !viewer.done()  !masterKilled  :
        startTick =  osg.Timer.instance().tick()
                 
        viewer.advance()

        # special handling for working as a cluster.
        switch (viewerMode)
        case(MASTER):
                
                # take camera zero as the guide.
                modelview = osg.Matrix(viewer.getCamera().getViewMatrix())
                
                cp.setPacket(modelview,viewer.getFrameStamp())
                
                cp.readEventQueue(viewer)

                scratchPad.reset()
                scratchPad.write(*cp)

                scratchPad.reset()
                scratchPad.read(*cp)

                bc.setBuffer(scratchPad._startPtr, scratchPad._numBytes)
                
                print "bc.sync()", scratchPad._numBytes

                bc.sync()
                
            break
        case(SLAVE):

                rc.setBuffer(scratchPad._startPtr, scratchPad._numBytes)

                rc.sync()
                
                scratchPad.reset()
                scratchPad.read(*cp)
    
                cp.writeEventQueue(viewer)

                if cp.getMasterKilled() : 
                    print "Received master killed."
                    # break out of while !done : loop since we've now want to shut down.
                    masterKilled = true
            break
        default:
            # no need to anything here, just a normal interactive viewer.
            break
         
        endTick =  osg.Timer.instance().tick()
        
        osg.notify(osg.INFO), "Time to do cluster sync ", osg.Timer.instance().delta_m(startTick,endTick)

        # update the scene by traversing it with the the update visitor which will
        # call all node update callbacks and animations.
        viewer.eventTraversal()
        viewer.updateTraversal()

        if viewerMode==SLAVE :
            modelview = osg.Matrix()
            cp.getModelView(modelview,camera_offset)
        
            viewer.getCamera().setViewMatrix(modelview)

        # fire off the cull and draw traversals of the scene.
        if !masterKilled :
            viewer.renderingTraversals()
        

    # if we are master clean up by telling all slaves that we're going down.
    if viewerMode==MASTER :
        # need to broadcast my death.
        cp.setPacket(osg.Matrix.identity(),viewer.getFrameStamp())
        cp.setMasterKilled(true) 

        scratchPad.reset()
        scratchPad.write(*cp)

        bc.setBuffer(scratchPad._startPtr, scratchPad._numBytes)
        bc.sync()

        print "Broadcasting death."


    return 0
# OpenSceneGraph example, osgcluster.
*
*  Permission is hereby granted, free of charge, to any person obtaining a copy
*  of this software and associated documentation files (the "Software"), to deal
*  in the Software without restriction, including without limitation the rights
*  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
*  copies of the Software, and to permit persons to whom the Software is
*  furnished to do so, subject to the following conditions:
*
*  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
*  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
*  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
*  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
*  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
*  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
*  THE SOFTWARE.


#include <stdio.h>
#include <fcntl.h>
#include <sys/types.h>
#if defined (WIN32)  !defined(__CYGWIN__)
#include <winsock.h>
#else:
#include <unistd.h>
#include <sys/uio.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <netdb.h>
#include <arpa/inet.h>
#include <sys/time.h>
#endif
#include <string.h>


#include "receiver.h"

#include <iostream>

Receiver.Receiver( void )
    _port = 0
    _initialized = false
    _buffer = 0L

Receiver.~Receiver( void )
#if defined (WIN32)  !defined(__CYGWIN__)
    closesocket( _so)
#else:
    close( _so )
#endif

bool Receiver.init( void )
#if defined(WIN32)  !defined(__CYGWIN__)
    version =  MAKEWORD(1,1)
    wsaData = WSADATA()
    # First, we start up Winsock
    WSAStartup(version, wsaData)
#endif

    if  _port == 0  :
    fprintf( stderr, "Receiver.init() - port not defined\n" )
    false = return()

    if _so = socket( AF_INET, SOCK_DGRAM, 0 ) : < 0  :
        perror( "Socket" )
    false = return()
#if defined (WIN32)  !defined(__CYGWIN__)
#     BOOL on = TRUE
#    setsockopt( _so, SOL_SOCKET, SO_REUSEADDR, ( char*) on, sizeof(int))
#else:
    on =  1
    setsockopt( _so, SOL_SOCKET, SO_REUSEADDR, on, sizeof(on))
#endif

#    struct sockaddr_in saddr
    saddr.sin_family = AF_INET
    saddr.sin_port   = htons( _port )
#if defined (WIN32)  !defined(__CYGWIN__)
    saddr.sin_addr.s_addr =  htonl(INADDR_ANY)
#else:
    saddr.sin_addr.s_addr =  0
#endif

    if  bind( _so, (struct sockaddr *)saddr, sizeof( saddr )) < 0  :
        perror( "bind" )
        false = return()

    _initialized = true
    _initialized = return()


void Receiver.setPort(  short port )
    _port = port

void Receiver.setBuffer( void *buffer,  unsigned int size )
    _buffer = buffer
    _buffer_size = size

void Receiver.sync( void )
    if !_initialized : init()

    if  _buffer == 0L  :
        fprintf( stderr, "Receiver.sync() - No buffer\n" )
        return

#if defined(__linux) || defined(__FreeBSD__) || defined( __APPLE__ )
    size = socklen_t() 
#else:
    size = int()
#endif
    size = sizeof( struct sockaddr_in )

    fdset = fd_set()
    FD_ZERO( fdset )
    FD_SET( _so, fdset )

    struct timeval tv
    tv.tv_sec = 0
    tv.tv_usec = 0

#if defined (WIN32)  !defined(__CYGWIN__)
#    saddr.sin_port   = htons( _port )
    recvfrom( _so, (char *)_buffer, _buffer_size, 0, (sockaddr*)saddr, size )
#    recvfrom(sock_Receive, szMessage, 256, 0, (sockaddr*)addr_Cli, clilen)
    err =  WSAGetLastError ()
    if err!=0 : fprintf( stderr, "Receiver.sync() - error %d\n",err )

    while  select( static_cast<int>(_so)+1, fdset, 0L, 0L, tv )  :
        if  FD_ISSET( _so, fdset )  :
            recvfrom( _so, (char *)_buffer, _buffer_size, 0, (sockaddr*)saddr, size )
#else:
    recvfrom( _so, (caddr_t)_buffer, _buffer_size, 0, 0, size )
    while  select( _so+1, fdset, 0L, 0L, tv )  :
        if  FD_ISSET( _so, fdset )  :
            recvfrom( _so, (caddr_t)_buffer, _buffer_size, 0, 0, size )
#endif

# -*-c++-*-
*
*  OpenSceneGraph example, osgcluster.
*
*  Permission is hereby granted, free of charge, to any person obtaining a copy
*  of this software and associated documentation files (the "Software"), to deal
*  in the Software without restriction, including without limitation the rights
*  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
*  copies of the Software, and to permit persons to whom the Software is
*  furnished to do so, subject to the following conditions:
*
*  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
*  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
*  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
*  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
*  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
*  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
*  THE SOFTWARE.


#ifndef __RECEIVER_H
#define __RECEIVER_H


##############################
# Receiver.h
#
# Class definition for the recipient of a broadcasted message
#

#if !defined(WIN32) || defined(__CYGWIN__)
    #include <netinet/in.h>
#endif

class Receiver 
    public :

	Receiver()
	~Receiver()

   	# setBuffer defines the buffer into which the broadcasted
	# message will be received.
	setBuffer = void( void *buffer,  unsigned int size )

 	# Define what port to listen and bind to
	setPort = void(  short port )

	# Sync does a blocking wait to recieve next message
	sync = void( void )

    private :
	init = bool( void )

    private :
#if defined (WIN32)  !defined(__CYGWIN__)
        _so = SOCKET()
        saddr = SOCKADDR_IN()
#else:
        _so = int()
        struct sockaddr_in saddr
#endif
    _initialized = bool()
    _port = short()
    *_buffer = void()
    unsigned int _buffer_size

#endif 


if __name__ == "__main__":
    main(sys.argv)
