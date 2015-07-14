#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgunittests"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import OpenThreads
from osgpypp import osg
from osgpypp import osgDB


# Translated from file 'FileNameUtils.cpp'

# -*-c++-*-
#*
#*  OpenSceneGraph example, osgunittests.
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

#include <osg/Notify>
#include <osg/ArgumentParser>
#include <osgDB/FileNameUtils>
#include <list>

void runFileNameUtilsTest(osg.ArgumentParser)
typedef std.list<str> Strings
    strings = Strings()
    strings.push_back(str(""))
    strings.push_back(str("myfile"))
    strings.push_back(str(".osgt"))
    strings.push_back(str("myfile.osgt"))
    strings.push_back(str("/myfile.osgt"))
    strings.push_back(str("home/robert/myfile.osgt"))
    strings.push_back(str("/home/robert/myfile.osgt"))
    strings.push_back(str("\\myfile.osgt"))
    strings.push_back(str("home\\robert\\myfile.osgt"))
    strings.push_back(str("\\home\\robert\\myfile.osgt"))
    strings.push_back(str("\\home/robert\\myfile.osgt"))
    strings.push_back(str("\\home\\robert/myfile.osgt"))
    strings.push_back(str("home/robert/"))
    strings.push_back(str("\\home\\robert\\"))
    strings.push_back(str("home/robert/myfile"))
    strings.push_back(str("\\home\\robert\\myfile"))
    strings.push_back(str("home/robert/.osgt"))
    strings.push_back(str("\\home\\robert\\.osgt"))
    strings.push_back(str("home/robert/myfile.ext.osgt"))
    strings.push_back(str("home\\robert\\myfile.ext.osgt"))

    for(Strings.iterator itr = strings.begin()
        not = strings.end()
        ++itr)
        str = *itr
        OSG_NOTICE, "string=", str
        OSG_NOTICE, "\n\tosgDB.getFilePath(str)=", osgDB.getFilePath(str)
        OSG_NOTICE, "\n\tosgDB.getSimpleFileName(str)=", osgDB.getSimpleFileName(str)
        OSG_NOTICE, "\n\tosgDB.getStrippedName(str)=", osgDB.getStrippedName(str)
        OSG_NOTICE, "\n\tosgDB.getFileExtension(str)=", osgDB.getFileExtension(str)
        OSG_NOTICE, "\n\tosgDB.getFileExtensionIncludingDot(str)=", osgDB.getFileExtensionIncludingDot(str)
        OSG_NOTICE, "\n\tosgDB.getNameLessExtension(str)=", osgDB.getNameLessExtension(str)
        OSG_NOTICE, "\n\tosgDB.getNameLessAllExtensions(str)=", osgDB.getNameLessAllExtensions(str)
        OSG_NOTICE

# Translated from file 'MultiThreadRead.cpp'

# OpenSceneGraph example, osgunittests.
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

#include <osg/Referenced>
#include <osgDB/ReadFile>
#include <osgDB/Registry>

#include <OpenThreads/Thread>
#include <OpenThreads/ScopedLock>

struct RefBarrier : public osg.Referenced, public OpenThreads.Barrier
    RefBarrier(int numThreads):
        OpenThreads.Barrier(numThreads) 


class ReadThread : public osg.Referenced, public OpenThreads.Thread

    ReadThread():
        _done(False)
    
    virtual ~ReadThread()
        _done = True
        
        while isRunning() : OpenThreads.Thread.YieldCurrentThread()
    
    def addFileName(filename):
    
        
        _fileNames.push_back(filename)
    
    def setStartBarrier(barrier):
    
         _startBarrier = barrier 
    def setEndBarrier(barrier):
         _endBarrier = barrier 

    def run():

        
        if _startBarrier.valid() : 
#if VERBOSE                
            print "Waiting on start block ", this
#endif
            _startBarrier.block()

#if VERBOSE                
        print "Starting ", this
#endif

        do
            if  not _fileNames.empty() :
                # take front filename
                filename = _fileNames.front()
                _fileNames.erase(_fileNames.begin())

#if VERBOSE                
                print "Reading ", filename
#endif
                node = osgDB.readNodeFile(filename)
#if VERBOSE                
                if node.valid() : print "..  OK"
                else print "..  FAILED"
#endif
            
         while  not testCancel()  and   not _fileNames.empty()  and   not _done :
        
        if _endBarrier.valid() : 
#if VERBOSE                
            print "Waiting on end block ", this
#endif
            _endBarrier.block()

#if VERBOSE                
        print "Completed", this
#endif
    
    typedef std.list<str> FileNames
    _fileNames = FileNames()
    _done = bool()
    _startBarrier = RefBarrier()
    _endBarrier = RefBarrier()




class SerializerReadFileCallback (osgDB.Registry.ReadFileCallback) :

    def openArchive(filename, status, indexBlockSizeHint, useObjectCache):

        
        lock = OpenThreads.ScopedLock<OpenThreads.Mutex>(_mutex)
        return osgDB.Registry.instance().openArchiveImplementation(filename, status, indexBlockSizeHint, useObjectCache)

    def readObject(filename, options):

        
        lock = OpenThreads.ScopedLock<OpenThreads.Mutex>(_mutex)
        return osgDB.Registry.instance().readObjectImplementation(filename,options)

    def readImage(filename, options):

        
        lock = OpenThreads.ScopedLock<OpenThreads.Mutex>(_mutex)
        return osgDB.Registry.instance().readImageImplementation(filename,options)

    def readHeightField(filename, options):

        
        lock = OpenThreads.ScopedLock<OpenThreads.Mutex>(_mutex)
        return osgDB.Registry.instance().readHeightFieldImplementation(filename,options)

    def readNode(filename, options):

        
        lock = OpenThreads.ScopedLock<OpenThreads.Mutex>(_mutex)
        return osgDB.Registry.instance().readNodeImplementation(filename,options)

    def readShader(filename, options):

        
        lock = OpenThreads.ScopedLock<OpenThreads.Mutex>(_mutex)
        return osgDB.Registry.instance().readShaderImplementation(filename,options)
       virtual ~SerializerReadFileCallback() 
       
       _mutex = OpenThreads.Mutex()




def runMultiThreadReadTests(numThreads, arguments):



    
#if VERBOSE                
    osg.notify(osg.NOTICE), "runMultiThreadReadTests() -- running"
#endif


    if arguments.read("preload") :
        osgDB.Registry.instance().loadLibrary(osgDB.Registry.instance().createLibraryNameForExtension("osg"))
        osgDB.Registry.instance().loadLibrary(osgDB.Registry.instance().createLibraryNameForExtension("rgb"))
        osgDB.Registry.instance().loadLibrary(osgDB.Registry.instance().createLibraryNameForExtension("jpeg"))
        osgDB.Registry.instance().loadLibrary(osgDB.Registry.instance().createLibraryNameForExtension("ive"))

    if arguments.read("serialize") :
        osgDB.Registry.instance().setReadFileCallback(SerializerReadFileCallback())

    startBarrier = RefBarrier(numThreads+1)
    endBarrier = RefBarrier(numThreads+1)

    typedef std.list< ReadThread > ReadThreads
    readThreads = ReadThreads()

    for(int i=0 i<numThreads ++i)
        readThread = ReadThread()

        readThread.setProcessorAffinity(numThreads % 4)

        readThread.setStartBarrier(startBarrier)
        readThread.setEndBarrier(endBarrier)

        readThread.addFileName("cessna.osgt")
        readThread.addFileName("glider.osgt")
        readThread.addFileName("town.ive")
        
        readThreads.push_back(readThread)

        readThread.start()
        

    startBarrier.block()
    endBarrier.block()

#if VERBOSE                
    osg.notify(osg.NOTICE), "runMultiThreadReadTests() -- completed."
#endif

# Translated from file 'MultiThreadRead.h'

# -*-c++-*- 
#*
#*  OpenSceneGraph example, osgunittests.
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

#ifndef MULTITHREADEDREAD_H
#define MULTITHREADEDREAD_H 1

#include <osg/ArgumentParser>

extern void runMultiThreadReadTests(int numThreads, osg.ArgumentParser arguments)

#endif

# Translated from file 'osgunittests.cpp'

# OpenSceneGraph example, osgunittests.
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

#include <osg/ArgumentParser>
#include <osg/ApplicationUsage>

#include <osg/Vec3>
#include <osg/Matrix>
#include <osg/Polytope>
#include <osg/Timer>
#include <osg/io_utils>

#include <OpenThreads/Thread>

#include "UnitTestFramework.h"
#include "performance.h"
#include "MultiThreadRead.h"

#include <iostream>

extern void runFileNameUtilsTest(osg.ArgumentParser arguments)

def testFrustum(left, right, bottom, top, zNear, zFar):

    
    f = osg.Matrix()
    f.makeFrustum(left,right,bottom,top,zNear,zFar)

    c_left = 0
    c_right = 0
    c_top = 0
    c_bottom = 0
    c_zNear = 0
    c_zFar = 0
    
    
    print "testFrustum", f.getFrustum(c_left,c_right,c_bottom,c_top,c_zNear,c_zFar)
    print "  left = ", left, " compute ", c_left
    print "  right = ", right, " compute ", c_right

    print "  bottom = ", bottom, " compute ", c_bottom
    print "  top = ", top, " compute ", c_top

    print "  zNear = ", zNear, " compute ", c_zNear
    print "  zFar = ", zFar, " compute ", c_zFar
    
    print std.endl

def testOrtho(left, right, bottom, top, zNear, zFar):

    
    f = osg.Matrix()
    f.makeOrtho(left,right,bottom,top,zNear,zFar)

    c_left = 0
    c_right = 0
    c_top = 0
    c_bottom = 0
    c_zNear = 0
    c_zFar = 0

    print "testOrtho ", f.getOrtho(c_left,c_right,c_bottom,c_top,c_zNear,c_zFar)
    print "  left = ", left, " compute ", c_left
    print "  right = ", right, " compute ", c_right

    print "  bottom = ", bottom, " compute ", c_bottom
    print "  top = ", top, " compute ", c_top

    print "  zNear = ", zNear, " compute ", c_zNear
    print "  zFar = ", zFar, " compute ", c_zFar
    
    print std.endl

def testPerspective(fovy, aspect, zNear, zFar):

    
    f = osg.Matrix()
    f.makePerspective(fovy,aspect,zNear,zFar)

    c_fovy = 0
    c_aspect = 0
    c_zNear = 0
    c_zFar = 0

    print "testPerspective ", f.getPerspective(c_fovy,c_aspect,c_zNear,c_zFar)
    print "  fovy = ", fovy, " compute ", c_fovy
    print "  aspect = ", aspect, " compute ", c_aspect

    print "  zNear = ", zNear, " compute ", c_zNear
    print "  zFar = ", zFar, " compute ", c_zFar
    
    print std.endl

def testLookAt(eye, center, up):

    
    mv = osg.Matrix()
    mv.makeLookAt(eye,center,up)
    
    osg.Vec3 c_eye,c_center,c_up
    mv.getLookAt(c_eye,c_center,c_up)
    
    print "testLookAt"
    print "  eye ", eye, " compute ", c_eye
    print "  center ", center, " compute ", c_center
    print "  up ", up, " compute ", c_up
    
    print std.endl
    


def testMatrixInvert(matrix):


    
    #Invert it twice using the two inversion functions and view the results
    osg.notify(osg.NOTICE), "testMatrixInvert("
    osg.notify(osg.NOTICE), matrix
    osg.notify(osg.NOTICE), ")"

    invM1_0 = osg.Matrix()
    invM1_0.invert(matrix)
    osg.notify(osg.NOTICE), "Matrix.invert"
    osg.notify(osg.NOTICE), invM1_0
    default_result = matrix*invM1_0
    osg.notify(osg.NOTICE), "matrix * invert="
    osg.notify(osg.NOTICE), default_result


def sizeOfTest():

    
  print "sizeof(bool)==", sizeof(bool)
  print "sizeof(char)==", sizeof(char)
  print "sizeof(short)==", sizeof(short)
  print "sizeof(short int)==", sizeof(short int)
  print "sizeof(int)==", sizeof(int)
  print "sizeof(long)==", sizeof(long)
  print "sizeof(long int)==", sizeof(long int)

#if defined(_MSC_VER)
  # long long isn't supported on VS6.0...
  print "sizeof(__int64)==", sizeof(__int64)
#else:
  print "sizeof(long long)==", sizeof(long long)
#endif
  print "sizeof(float)==", sizeof(float)
  print "sizeof(double)==", sizeof(double)

  print "sizeof(std.istream.pos_type)==", sizeof(std.istream.pos_type)
  print "sizeof(std.istream.off_type)==", sizeof(std.istream.off_type)
  print "sizeof(OpenThreads.Mutex)==", sizeof(OpenThreads.Mutex)

  print "sizeof(str)==", sizeof(str)


#/ Exercise the Matrix.getRotate function.
#/ Compare the output of:
#/  q1 * q2 
#/ versus
#/  (mat(q1)*mat(q2)*scale).getRotate()
#/ for a range of rotations
def testGetQuatFromMatrix(scale):
    
    
    # Options
    
    # acceptable error range
    eps = 1e-6

    # scale matrix
    # To not test with scale, use 1,1,1
    # Not sure if 0's or negative values are acceptable
    scalemat = osg.Matrixd()
    scalemat.makeScale(scale)
    
    # range of rotations
#if 1
    # wide range
    rol1start = 0.0
    rol1stop = 360.0
    rol1step = 20.0

    pit1start = 0.0
    pit1stop = 90.0
    pit1step = 20.0

    yaw1start = 0.0
    yaw1stop = 360.0
    yaw1step = 20.0

    rol2start = 0.0
    rol2stop = 360.0
    rol2step = 20.0

    pit2start = 0.0
    pit2stop = 90.0
    pit2step = 20.0

    yaw2start = 0.0
    yaw2stop = 360.0
    yaw2step = 20.0
#else:
    # focussed range
    rol1start = 0.0
    rol1stop = 0.0
    rol1step = 0.1

    pit1start = 0.0
    pit1stop = 5.0
    pit1step = 5.0

    yaw1start = 89.0
    yaw1stop = 91.0
    yaw1step = 0.1

    rol2start = 0.0
    rol2stop = 0.0
    rol2step = 0.1

    pit2start = 0.0
    pit2stop = 0.0
    pit2step = 0.1

    yaw2start = 89.0
    yaw2stop = 91.0
    yaw2step = 0.1
#endif

    print std.endl, "Starting testGetQuatFromMatrix, it can take a while ..."

    osg.Timer_t tstart, tstop
    tstart = osg.Timer.instance().tick()
    count = 0
    for (double rol1 = rol1start rol1 <= rol1stop rol1 += rol1step) 
        for (double pit1 = pit1start pit1 <= pit1stop pit1 += pit1step) 
            for (double yaw1 = yaw1start yaw1 <= yaw1stop yaw1 += yaw1step) 
                for (double rol2 = rol2start rol2 <= rol2stop rol2 += rol2step) 
                    for (double pit2 = pit2start pit2 <= pit2stop pit2 += pit2step) 
                        for (double yaw2 = yaw2start yaw2 <= yaw2stop yaw2 += yaw2step)
                            count++
                            # create two quats based on the roll, pitch and yaw values
                            rot_quat1 = osg.Quat(osg.DegreesToRadians(rol1),osg.Vec3d(1,0,0),
                                  osg.DegreesToRadians(pit1),osg.Vec3d(0,1,0),
                                  osg.DegreesToRadians(yaw1),osg.Vec3d(0,0,1))

                            rot_quat2 = osg.Quat(osg.DegreesToRadians(rol2),osg.Vec3d(1,0,0),
                                  osg.DegreesToRadians(pit2),osg.Vec3d(0,1,0),
                                  osg.DegreesToRadians(yaw2),osg.Vec3d(0,0,1))

                            # create an output quat using quaternion math
                            out_quat1 = osg.Quat()
                            out_quat1 = rot_quat2 * rot_quat1

                            # create two matrices based on the input quats
                            osg.Matrixd mat1,mat2
                            mat1.makeRotate(rot_quat1)
                            mat2.makeRotate(rot_quat2)

                            # create an output quat by matrix multiplication and getRotate
                            out_mat = osg.Matrixd()
                            out_mat = mat2 * mat1
                            # add matrix scale for even more nastiness
                            out_mat = out_mat * scalemat
                            out_quat2 = osg.Quat()
                            out_quat2 = out_mat.getRotate()

                            # If the quaternion W is <0, then we should reflect
                            # to get it into the positive W.
                            # Unfortunately, when W is very small (close to 0), the sign
                            # does not really make sense because of precision problems
                            # and the reflection might not work.
                            if out_quat1.w()<0 : out_quat1 = out_quat1 * -1.0
                            if out_quat2.w()<0 : out_quat2 = out_quat2 * -1.0

                            # if the output quat length is not one 
                            # or if the components do not match,
                            # something is amiss

                            componentsOK = False
                            if ( ((fabs(out_quat1.x()-out_quat2.x())) < eps)  and 
                                 ((fabs(out_quat1.y()-out_quat2.y())) < eps)  and 
                                 ((fabs(out_quat1.z()-out_quat2.z())) < eps)  and 
                                 ((fabs(out_quat1.w()-out_quat2.w())) < eps) )
                                componentsOK = True
                            # We should also test for q = -q which is valid, so reflect
                            # one quat.
                            out_quat2 = out_quat2 * -1.0
                            if ( ((fabs(out_quat1.x()-out_quat2.x())) < eps)  and 
                                 ((fabs(out_quat1.y()-out_quat2.y())) < eps)  and 
                                 ((fabs(out_quat1.z()-out_quat2.z())) < eps)  and 
                                 ((fabs(out_quat1.w()-out_quat2.w())) < eps) )
                                componentsOK = True

                            lengthOK = False
                            if fabs(1.0-out_quat2.length()) < eps :
                                lengthOK = True

                            if  not lengthOK  or   not componentsOK :
                                print "testGetQuatFromMatrix problem at: \n", " r1=", rol1, " p1=", pit1, " y1=", yaw1, " r2=", rol2, " p2=", pit2, " y2=", yaw2, "\n"
                                print "quats:        ", out_quat1, " length: ", out_quat1.length(), "\n"
                                print "mats and get: ", out_quat2, " length: ", out_quat2.length(), "\n\n"
    tstop = osg.Timer.instance().tick()
    duration = osg.Timer.instance().delta_s(tstart,tstop)
    print "Time for testGetQuatFromMatrix with ", count, " iterations: ", duration

def testQuatRotate(from, to):

    
    q_nicolas = osg.Quat()
    q_nicolas.makeRotate(from,to)
    
    q_original = osg.Quat()
    q_original.makeRotate_original(from,to)
    
    print "osg.Quat.makeRotate(", from, ", ", to, ")"
    print "  q_nicolas = ", q_nicolas
    print "  q_original = ", q_original
    print "  from * M4x4(q_nicolas) = ", from * osg.Matrixd.rotate(q_nicolas)
    print "  from * M4x4(q_original) = ", from * osg.Matrixd.rotate(q_original)

def testQuat(quat_scale):

    
    q1 = osg.Quat()
    q1.makeRotate(osg.DegreesToRadians(30.0),0.0,0.0,1.0)

    q2 = osg.Quat()
    q2.makeRotate(osg.DegreesToRadians(133.0),0.0,1.0,1.0)

    q1_2 = q1*q2
    q2_1 = q2*q1

    m1 = osg.Matrix.rotate(q1)
    m2 = osg.Matrix.rotate(q2)
    
    m1_2 = m1*m2
    m2_1 = m2*m1
    
    qm1_2 = osg.Quat()
    qm1_2.set(m1_2)
    
    qm2_1 = osg.Quat()
    qm2_1.set(m2_1)
    
    print "q1*q2 = ", q1_2
    print "q2*q1 = ", q2_1
    print "m1*m2 = ", qm1_2
    print "m2*m1 = ", qm2_1


    testQuatRotate(osg.Vec3d(1.0,0.0,0.0),osg.Vec3d(0.0,1.0,0.0))
    testQuatRotate(osg.Vec3d(0.0,1.0,0.0),osg.Vec3d(1.0,0.0,0.0))
    testQuatRotate(osg.Vec3d(0.0,0.0,1.0),osg.Vec3d(0.0,1.0,0.0))
    testQuatRotate(osg.Vec3d(1.0,1.0,1.0),osg.Vec3d(1.0,0.0,0.0))
    testQuatRotate(osg.Vec3d(1.0,0.0,0.0),osg.Vec3d(1.0,0.0,0.0))
    testQuatRotate(osg.Vec3d(1.0,0.0,0.0),osg.Vec3d(-1.0,0.0,0.0))
    testQuatRotate(osg.Vec3d(-1.0,0.0,0.0),osg.Vec3d(1.0,0.0,0.0))
    testQuatRotate(osg.Vec3d(0.0,1.0,0.0),osg.Vec3d(0.0,-1.0,0.0))
    testQuatRotate(osg.Vec3d(0.0,-1.0,0.0),osg.Vec3d(0.0,1.0,0.0))
    testQuatRotate(osg.Vec3d(0.0,0.0,1.0),osg.Vec3d(0.0,0.0,-1.0))
    testQuatRotate(osg.Vec3d(0.0,0.0,-1.0),osg.Vec3d(0.0,0.0,1.0))

    # Test a range of rotations
    testGetQuatFromMatrix(quat_scale)

    # This is a specific test case for a matrix containing scale and rotation
    matrix = osg.Matrix(0.5, 0.0, 0.0, 0.0,
                       0.0, 0.5, 0.0, 0.0,
                       0.0, 0.0, 0.5, 0.0,
                       1.0, 1.0, 1.0, 1.0)
                       
    quat = osg.Quat()
    matrix.get(quat)
    
    osg.notify(osg.NOTICE), "Matrix = ", matrix, "rotation = ", quat, ", expected quat = (0,0,0,1)"

def testDecompose():

    
    angx = osg.DegreesToRadians(30.0)
    angy = osg.DegreesToRadians(30.0)
    angz = osg.DegreesToRadians(30.0)

    osg.Quat qx, qy, qz
    qx.makeRotate(angx, osg.Vec3f (1.0, 0.0, 0.0))
    qy.makeRotate(angy, osg.Vec3f (0.0, 1.0, 0.0))
    qz.makeRotate(angz, osg.Vec3f (0.0, 0.0, 1.0))

    rotation = qx * qy * qz

    matf = osg.Matrixf()
    matf.makeRotate(rotation)

    printf ("Test - Matrix.decompos(), input rotation  : %f %f %f %f\n", rotation._v[0], rotation._v[1], rotation._v[2], rotation._v[3])

    transf = osg.Vec3f()
    rotf = osg.Quat()
    sclf = osg.Vec3f()
    sof = osg.Quat()
    matf.decompose (transf, rotf, sclf, sof)
    printf ("Matrixf.decomposef\n")
    printf ("Translation      : %f %f %f\n", transf.x(), transf.y(), transf.z())
    printf ("Rotation         : %f %f %f %f\n", rotf._v[0], rotf._v[1], rotf._v[2], rotf._v[3])
    printf ("Scale            : %f %f %f\n", sclf.x(), sclf.y(), sclf.z())
    printf ("Scale Orientation: %f %f %f %f\n", sof._v[0], sof._v[1], sof._v[2], sof._v[3])

    matd = osg.Matrixd()
    matd.makeRotate(rotation)

    transd = osg.Vec3f()
    rotd = osg.Quat()
    scld = osg.Vec3f()
    sod = osg.Quat()
    matd.decompose (transd, rotd, scld, sod)
    printf ("Matrixd.decompose\n")
    printf ("Translation      : %f %f %f\n", transd.x(), transd.y(), transd.z())
    printf ("Rotation         : %f %f %f %f\n", rotd._v[0], rotd._v[1], rotd._v[2], rotd._v[3])
    printf ("Scale            : %f %f %f\n", scld.x(), scld.y(), scld.z())
    printf ("Scale Orientation: %f %f %f %f\n", sod._v[0], sod._v[1], sod._v[2], sod._v[3])

    osg.notify(osg.NOTICE)

class MyThread (OpenThreads.Thread) :
    void run(void)  


class NotifyThread (OpenThreads.Thread) :

    NotifyThread(osg.NotifySeverity level,  str message):
    _done(False),
    _level(level),
    _message(message) 

    ~NotifyThread()
        _done = True
        while isRunning() :
            OpenThreads.Thread.YieldCurrentThread()

    void run(void)
        print "Entering thread ...", _message

        count = 0

        while  not _done : 
            ++count
#if 1
            osg.notify(_level), _message, this, "\n"
#else:
            osg.notify(_level), _message, this
#endif

        print "Leaving thread ...", _message, " count=", count

    _done = bool()
    _level = osg.NotifySeverity()
    _message = str()
  


def testThreadInitAndExit():

    
    print "******   Running thread start and delete test   ****** "

        thread = MyThread()
        thread.startThread()
    
    # add a sleep to allow the thread start to fall over it its going to.
    OpenThreads.Thread.microSleep(500000)
    
    print "pass    thread start and delete test"


    print "******   Running notify thread test   ****** "

        thread1 = NotifyThread(osg.INFO,"thread one:")
        thread2 = NotifyThread(osg.INFO,"thread two:")
        thread3 = NotifyThread(osg.INFO,"thread three:")
        thread4 = NotifyThread(osg.INFO,"thread four:")
        thread1.startThread()
        thread2.startThread()
        thread3.startThread()
        thread4.startThread()

        # add a sleep to allow the thread start to fall over it its going to.
        OpenThreads.Thread.microSleep(5000000)

    print "pass    noitfy thread test."

def testPolytope():

    
    pt = osg.Polytope()
    pt.setToBoundingBox(osg.BoundingBox(-1000, -1000, -1000, 1000, 1000, 1000))
    bContains = pt.contains(osg.Vec3(0, 0, 0))
    if bContains :
        print "Polytope pt.contains(osg.Vec3(0, 0, 0)) has succeeded."
    else:
        print "Polytope pt.contains(osg.Vec3(0, 0, 0)) has failed."



def main(argv):


    
    arguments = osg.ArgumentParser(argv)

    # set up the usage document, in case we need to print out how to use this program.
    arguments.getApplicationUsage().setDescription(arguments.getApplicationName()+" is the example which runs units tests.")
    arguments.getApplicationUsage().setCommandLineUsage(arguments.getApplicationName()+" [options]")
    arguments.getApplicationUsage().addCommandLineOption("-h or --help","Display this information")
    arguments.getApplicationUsage().addCommandLineOption("qt","Display qualified tests.")
    arguments.getApplicationUsage().addCommandLineOption("quat","Display extended quaternion tests.")
    arguments.getApplicationUsage().addCommandLineOption("quat_scaled sx sy sz","Display extended quaternion tests of pre scaled matrix.")
    arguments.getApplicationUsage().addCommandLineOption("sizeof","Display sizeof tests.")
    arguments.getApplicationUsage().addCommandLineOption("matrix","Display qualified tests.")
    arguments.getApplicationUsage().addCommandLineOption("performance","Display qualified tests.")
    arguments.getApplicationUsage().addCommandLineOption("read-threads <numthreads>","Run multi-thread reading test.")
 

    if arguments.argc()<=1 :
        arguments.getApplicationUsage().write(std.cout,osg.ApplicationUsage.COMMAND_LINE_OPTION)
        return 1

    printQualifiedTest = False 
    while arguments.read("qt") : printQualifiedTest = True 

    printMatrixTest = False 
    while arguments.read("matrix") : printMatrixTest = True 

    printSizeOfTest = False 
    while arguments.read("sizeof") : printSizeOfTest = True

    printFileNameUtilsTests = False
    while arguments.read("filenames") : printFileNameUtilsTests = True

    printQuatTest = False 
    while arguments.read("quat") : printQuatTest = True

    numReadThreads = 0 
    while arguments.read("read-threads", numReadThreads) : 

    printPolytopeTest = False 
    while arguments.read("polytope") : printPolytopeTest = True
    
    doTestThreadInitAndExit = False
    while arguments.read("thread") : doTestThreadInitAndExit = True

    quat_scale = osg.Vec3d(1.0,1.0,1.0) 
    while arguments.read("quat_scaled", quat_scale.x(), quat_scale.y(), quat_scale.z() ) : printQuatTest = True 

    performanceTest = False 
    while arguments.read("p")  or  arguments.read("performance") : performanceTest = True 

    # if user request help write it out to cout.
    if arguments.read("-h")  or  arguments.read("--help") :
        print arguments.getApplicationUsage().getCommandLineUsage()
        arguments.getApplicationUsage().write(std.cout,arguments.getApplicationUsage().getCommandLineOptions())
        return 1

    # any option left unread are converted into errors to write out later.
    arguments.reportRemainingOptionsAsUnrecognized()

    # report any errors if they have occurred when parsing the program arguments.
    if arguments.errors() :
        arguments.writeErrorMessages(std.cout)
        return 1
    
    if printQuatTest :
        testQuat(quat_scale)

    if printMatrixTest :
        print "******   Running matrix tests   ******"

        testFrustum(-1,1,-1,1,1,1000)
        testFrustum(0,1,1,2,2.5,100000)

        testOrtho(0,1,1,2,2.1,1000)
        testOrtho(-1,10,1,20,2.5,100000)

        testPerspective(20,1,1,1000)
        testPerspective(90,2,1,1000)

        testLookAt(osg.Vec3(10.0,4.0,2.0),osg.Vec3(10.0,4.0,2.0)+osg.Vec3(0.0,1.0,0.0),osg.Vec3(0.0,0.0,1.0))
        testLookAt(osg.Vec3(10.0,4.0,2.0),osg.Vec3(10.0,4.0,2.0)+osg.Vec3(1.0,1.0,0.0),osg.Vec3(0.0,0.0,1.0))
        
        testMatrixInvert(osg.Matrix(0.999848,  -0.002700,  0.017242, -0.1715,
                                     0,         0.987960,   0.154710,  0.207295,
                                     -0.017452, -0.154687,  0.987809, -0.98239,
                                     0,         0,          0,         1))

        testMatrixInvert(osg.Matrix(0.999848,  -0.002700,  0.017242,   0.0,
                                     0.0,        0.987960,   0.154710,   0.0,
                                     -0.017452, -0.154687,  0.987809,   0.0,
                                     -0.1715,    0.207295,  -0.98239,   1.0))

        testDecompose()

    
    if printSizeOfTest :
        print "**** sizeof() tests  ******"
        
        sizeOfTest()

        print std.endl


    if performanceTest :
        print "**** performance tests  ******"
        
        runPerformanceTests()

    if numReadThreads>0 :
        runMultiThreadReadTests(numReadThreads, arguments)
        return 0


    if printPolytopeTest :
        testPolytope()


    if printQualifiedTest : 
         print "*****   Qualified Tests  ******"

         printer = osgUtx.QualifiedTestPrinter()
         osgUtx.TestGraph.instance().root().accept( printer )    
         print std.endl

    if printFileNameUtilsTests :
        runFileNameUtilsTest(arguments)


    if doTestThreadInitAndExit :
        testThreadInitAndExit()

    print "******   Running tests   ******"

    # Global Data or Context
    ctx = osgUtx.TestContext()
    runner = osgUtx.TestRunner( ctx )
    runner.specify("root")

    osgUtx.TestGraph.instance().root().accept( runner )

    return 0

# Translated from file 'performance.cpp'

# OpenSceneGraph example, osgunittests.
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

#include "performance.h"

#include <osg/Timer>
#include <iostream>

#include <osg/NodeVisitor>
#include <osg/ref_ptr>
#include <osg/MatrixTransform>
#include <osg/Group>

class Benchmark :
Benchmark()
        calibrate()
    
        _beginTick = _timer.tick()
        _endTick = _timer.tick()
    
    def calibrate(numLoops):
    
        
        beginTick = _timer.tick()
        for(unsigned int i=0i<numLoops++i)
            begin()
            end()
        endTick = _timer.tick()
        _averageDelay = _timer.delta_s(beginTick,endTick)/(double)numLoops
    
    inline void begin()
        _beginTick = _timer.tick()

    inline void end()
        _endTick = _timer.tick()

    inline double time()
        t = _timer.delta_s(_beginTick,_endTick) - _averageDelay
        return  0.0 if (t<0.0) else  t

    inline void output( char* str, double numIterations=1.0)
        print str, "\t"
        s = time()/numIterations
        if s>=1.0 : print s, " s"
        elif s>=0.001 : print s*1000.0, " ms (10 ^ -3)"
        elif s>=0.000001 : print s*1000000.0, " ns (10 ^ -6)"
        else print s*1000000000.0, " ps (10 ^ -9)"

    _timer = osg.Timer()
    _beginTick = osg.Timer_t()
    _endTick = osg.Timer_t()
    _averageDelay = double()


#define RUN(A,B,D)  A.begin() for(unsigned int i=0i<D++i) B A.end() A.output(#B,D) 


static int v = 0
#define OPERATION  v=v+1 

inline void inline_increment()  OPERATION 
def function_increment():
     OPERATION 

typedef void ( * IncrementProc) ()
s_functionIncrement = function_increment
inline void functionPointer_increment()  s_functionIncrement() 


InlineMethod = struct()
Method = struct()
VirtualMethod = struct()
VirtualMethod2 = struct()

class Visitor :
apply = virtual void(InlineMethod m)
    apply = virtual void(Method m)
    apply = virtual void(VirtualMethod m)
    apply = virtual void(VirtualMethod2 m)
    virtual ~Visitor() 



class InlineMethod :
def method():
     OPERATION 
    def accept(visitor):
         visitor.apply(*this) 
    virtual ~InlineMethod() 


class Method :
def accept(visitor):
     visitor.apply(*this) 
    method = void()
    virtual ~Method() 


void Method.method()  OPERATION 
 
class VirtualMethod :
def accept(visitor):
     visitor.apply(*this) 
    method = virtual void()
    virtual ~VirtualMethod() 


void VirtualMethod.method()  OPERATION 

class VirtualMethod2 (VirtualMethod) :
VirtualMethod2()  

    def accept(visitor):

         visitor.apply(*this) 
    method = virtual void()
    virtual ~VirtualMethod2()  
    
    char a[100]


void VirtualMethod2.method()  OPERATION 

void Visitor.apply(Method m)  m.method() 
void Visitor.apply(VirtualMethod m)  m.method() 
void Visitor.apply(InlineMethod m)  m.method() 
void Visitor.apply(VirtualMethod2 m)  m.method() 

class CustomVisitor :
def apply(m):
     m.method() 
    def apply(m):
         m.method() 
    def apply(m):
         m.method() 
    def apply(m):
         m.method() 
    virtual ~CustomVisitor() 


class CustomNodeVisitor (osg.NodeVisitor) :
    void apply(osg.Node)  
    void apply(osg.Group)  
    void apply(osg.Transform)  



def runPerformanceTests():


    
    benchmark = Benchmark()
    
    iterations = 10000000

    RUN(benchmark,  , iterations)

    v = 0
    RUN(benchmark, OPERATION , iterations)
    RUN(benchmark, functionPointer_increment() , iterations)
    RUN(benchmark, inline_increment() , iterations)
    RUN(benchmark, function_increment() , iterations)

    m4 = VirtualMethod2()
    RUN(benchmark, m4.method() , iterations)

    m1 = InlineMethod()
    RUN(benchmark, m1.method() , iterations)

    m2 = Method()
    RUN(benchmark, m2.method() , iterations)

    m3 = VirtualMethod()
    RUN(benchmark, m3.method() , iterations)
    RUN(benchmark, m3.method() , iterations)

    visitor = Visitor()
    RUN(benchmark, m4.accept(visitor), iterations)
    RUN(benchmark, m1.accept(visitor), iterations)
    RUN(benchmark, m2.accept(visitor), iterations)
    RUN(benchmark, m3.accept(visitor), iterations)
    RUN(benchmark, m4.accept(visitor), iterations)

    vm4 = m4

    RUN(benchmark, (dynamic_cast<VirtualMethod2*>(vm4)).method(), iterations)
    RUN(benchmark, (static_cast<VirtualMethod2*>(vm4)).method(), iterations)
    RUN(benchmark,  VirtualMethod mm mm.method() , iterations)
    RUN(benchmark,  VirtualMethod2 mm mm.method() , iterations)


    group = osg.Group()
    mt = osg.MatrixTransform()
    m = mt
    cnv = CustomNodeVisitor()
    RUN(benchmark,  osg.MatrixTransform* mtl = dynamic_cast<osg.MatrixTransform*>(m) if mtl : cnv.apply(*mtl) , 1000)
    RUN(benchmark,  m.accept(cnv) , 10000)
    

# Translated from file 'performance.h'

# -*-c++-*- 
#*
#*  OpenSceneGraph example, osgunittests.
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

#ifndef PERFORMANCE_H
#define PERFORMANCE_H 1

extern void runPerformanceTests()

#endif

# Translated from file 'UnitTestFramework.cpp'

# OpenSceneGraph example, osgunittests.
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

#include "UnitTestFramework.h"

#include <algorithm>

namespace osgUtx

#######################################

TestContext.TestContext()

void TestContext.setTraceLevel(TraceLevel tl)
    _tout.setTraceLevel(tl)

TestContext.TraceLevel TestContext.getTraceLevel() 
    return _tout.getTraceLevel()

std.ostream TestContext.tout(TraceLevel tl) 
    return _tout.stream(tl)

#######################################


TestContext.TraceStream.TraceStream(std.ostream o, TraceLevel tl):
    _traceLevel(tl),
    _outputStreamPtr(o),
#if defined(WIN32)  and   not (defined(__CYGWIN__)  or  defined(__MINGW32__))
    _nullStream("nul")
#else:
    _nullStream("/dev/null")
#endif

TestContext.TraceStream.~TraceStream()
    _nullStream.close()

void TestContext.TraceStream.setTraceLevel(TraceLevel tl)
    _traceLevel = tl

TestContext.TraceLevel TestContext.TraceStream.getTraceLevel() 
    return _traceLevel

std.ostream TestContext.TraceStream.stream(TestContext.TraceLevel tl)
    if _traceLevel >= tl :
        return *_outputStreamPtr
    return _nullStream

#######################################

TestGraph TestGraph.instance()
    static TestGraph instance_
    return instance_

TestSuite* TestGraph.root()
    return root_

TestSuite* TestGraph.suite( str path, TestSuite* tsuite, bool createIfNecessary)
    using namespace std

    pathComponents = list<string>()

    it1 = path.begin()
    it2 = it1

    # Dissect the path into it's constituent components
    do

        while  it2  not = path.end()  and  *it2  not = ord(".")  : ++it2

        # Consider a check for "" empty  pathComponents.push_back( std: if (strings) else string(it1,it2) )

        if  it2  not = path.end() : ++it2

        it1 = it2

    while  it2  not = path.end() :

    suite = return(pathComponents.begin(), pathComponents.end(),
            tsuite, createIfNecessary)


TestSuite* TestGraph.suite(
        std.list<str>.iterator it,
        std.list<str>.iterator end,
        TestSuite* tsuite, bool createIfNecessary)
    using namespace std

    if   not  tsuite : tsuite = root()

    # Make sure these tie up
    if *it  not = tsuite.name() : return 0

    ++it
    if it == end : return tsuite

    child = tsuite.findChild(*it)

    if child :

        # We've found a child with the right name. But is it a 
        # test  if TestSuite* childSuite = dynamic_cast<TestSuite*>(child) if (suite) else 
            suite = return(it, end, childSuite, createIfNecessary)

        # We could return 0 here, to indicate that someone is
        # trying to add a TestSuite named 'xxx' to a suite with a
        # Test already named 'xxx'. But we don't enforce uniqueness
        # the other way round, so we don't do it this way round
        # either. Carry on as normal, and create a TestSuite of
        # the same name if createIfNecessary is True.


    if createIfNecessary :

        childSuite = TestSuite(*it)
        tsuite.add(childSuite)
        suite = return(it, end, childSuite, createIfNecessary)

    return 0

TestGraph.TestGraph(): root_(TestSuite("root"))


#######################################

bool TestQualifier.visitEnter( TestSuite* pSuite )
    _path.append( pSuite.name() )
    _path += SEPCHAR 
    return True

# Leaving a composite: Pop its name from the Path
bool TestQualifier.visitLeave( TestSuite* pSuite )
#    assert( _path.rfind( pSuite.name() + static_cast< char>(SEPCHAR))
#                == _path.size() - pSuite.name().size()  - 1)

    _path.erase( _path.size() - pSuite.name().size() -1 )
    return True

# Provide read-only access to the current qualifier
 str TestQualifier.currentPath() 
    return _path

#######################################

osg.Timer TestRecord.timer_

void TestRecord.start()
    start_ = timer_.tick()

void TestRecord.stop()
    stop_ = timer_.tick()

void TestRecord.log( TestFailureX e)
    stop()
    result_ = Failure
    problem_ = e.what()

void TestRecord.log( TestErrorX e)
    stop()
    result_ = Error
    problem_ = e.what()

void TestRecord.log( std.exception e)
    stop()
    result_ = Error
    problem_ = e.what()

void TestRecord.log( str s)
    stop()
    result_ = Error
    problem_ = s

TestRecord.TestRecord( str name):
    name_(name),
    start_(0),
    stop_(0),
    result_(Success),
    problem_("No problem")

std.ostream operator, (std.ostream o, TestRecord tr)
    if tr.result_ == TestRecord.Success :         o, "pass"
    elif tr.result_ == TestRecord.Failure :    o, "fail"
    else                                          o, "error"

    o, "\t", tr.name_


    #o, tr.start_, '\t', tr.stop_, '\t', TestRecord.timer_.delta_s(tr.start_,tr.stop_)

    # Just print out the duration
    o, '\t', TestRecord.timer_.delta_s(tr.start_,tr.stop_), ord("s")

    if tr.result_  not = TestRecord.Success :
        o, '\t', tr.problem_

    return o

#######################################

TestRunner.TestRunner( TestContext ctx ) : _ctx( ctx )

void TestRunner.specify(  str sQualifiedName )
    _tests.push_back( sQualifiedName )

bool TestRunner.visitEnter( TestSuite* pSuite )
    TestQualifier.visitEnter( pSuite )
    return  not _ctx.shouldStop()

#ifndef DOXYGEN_SHOULD_SKIP_THIS

namespace osgUtx

class isSpecified :
pTestName_ =  str()

    isSpecified( str s): pTestName_(s) 

    bool operator()( str specifiedTest)
        return pTestName_.find(specifiedTest) == 0

    operator = ( isSpecified)  return *this 



#endif # DOXYGEN_SHOULD_SKIP_THIS 

bool TestRunner.visit( TestCase* pTest )
    if  std.find_if _tests.begin(),_tests.end(),
                      osgUtx.isSpecified(currentPath() + pTest.name() )  :  not = _tests.end() : perform( pTest )

    return  not _ctx.shouldStop()

bool TestRunner.visitLeave( TestSuite* pSuite )
    TestQualifier.visitLeave( pSuite )
    return  not _ctx.shouldStop()

void TestRunner.perform( TestCase* pTest )
    record = _db.createRecord( currentPath() + pTest.name() )

    try
        record.start()
        pTest.run( _ctx )
        record.stop()

    catch (  TestFailureX e )
        record.log( e )
    catch (  TestErrorX e )
        record.log( e )
    catch (  std.exception e )
        record.log( e )
    catch ( ... )
        record.log( str("Unknown") )


    _ctx.tout(TestContext.Results), record

#######################################

TestSuite.TestSuite(  str name ) : Test( name )

void TestSuite.add( Test* pTest )
    _tests.push_back( pTest )

Test* TestSuite.findChild( str name)
    for(Tests.iterator it = _tests.begin()
        not = _tests.end()
        ++it)

        if *it :.name() == name : return (*it)

    return 0

bool TestSuite.accept( Test.Visitor v )
    if  v.visitEnter( this )  :
        end = _tests.end()
        for ( Tests.iterator at = _tests.begin() at  not = end ++at )
            if   not (*at).accept( v )  :
                break

    return v.visitLeave( this )   # continue with siblings?

#######################################

bool QualifiedTestPrinter.visit( TestCase* pTest )
    osg.notify(osg.NOTICE), currentPath() + pTest.name()
    return True

#######################################



# Translated from file 'UnitTestFramework.h'

# -*-c++-*- 
#*
#*  OpenSceneGraph example, osgunittests.
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

#ifndef OSG_UNITTESTFRAMEWORK
#define OSG_UNITTESTFRAMEWORK 1

#include <osg/Export>
#include <osg/Referenced>
#include <osg/ref_ptr>
#include <osg/Timer>
#include <osg/Notify>

#include <osgDB/fstream>

#include <string>
#include <vector>
#include <list>

#*
#
#\namespace osgUtx
#
#The osgUtx is a unit test framework.
#

namespace osgUtx

TestVisitor = class()


#*
#Test, an abstract base class, is the Composite pattern's \em component
#class for our graph of test cases, and defines the basic interface
#for all Test components. It is a referent, and may be pointed
#to by an osg.ref_ptr.
#
class Test (osg.Referenced) :

    typedef TestVisitor Visitor    # Test is redundant

    Test(  str sName ) : _name( sName ) 

    def name():

         return _name 

    virtual bool accept( Visitor ) = 0

        virtual ~Test() 

    _name = str()



#*
#TestContext wraps up information which is passed to tests as they are run,
#and may contain test-specific information or 'global' test objects, such
#as an output stream for verbose output during the running of tests.
#
#\todo Improve the output stream code by providing a filtering stream.
#
class TestContext :

    TestContext()

    def shouldStop():

         return False 
    def isVerbose():
         return True 

    enum TraceLevel
        Off,        #/< All tracing turned off
        Results,    #/< Output results only
        Full        #/< Full test diagnostic output
    

    setTraceLevel = void(TraceLevel tl)
    TraceLevel getTraceLevel() 

    std.ostream tout(TraceLevel tl=Full) 

    TestContext( TestContext)
    operator = ( TestContext)

#ifndef DOXYGEN_SHOULD_SKIP_THIS

    class TraceStream :
        TraceStream(std.ostream o=osg.notify(osg.NOTICE), TraceLevel tl=Results)
        ~TraceStream()

        setTraceLevel = void(TraceLevel tl)
        TraceLevel getTraceLevel() 

        stream = std.ostream(TraceLevel tl)

        _traceLevel = TraceLevel()
        _outputStreamPtr = std.ostream*()
        _nullStream = osgDB.ofstream()
    

#endif # DOXYGEN_SHOULD_SKIP_THIS 

    mutable TraceStream _tout




TestSuite = class()
TestCase = class()

#*
#Visits while maintaining the current hierarchical context. Also allows
#the traversal to be short-circuited at any point during the visitation.
#
class TestVisitor :

    #..Should we enter this node and its children?
    virtual bool visitEnter( TestSuite* )  return True 

    #..Returns True to continue to next Leaf
    virtual bool visit( TestCase* ) = 0

    #..Returns True to continue to next Composite
    virtual bool visitLeave( TestSuite* )  return True 

    TestVisitor() 
    TestVisitor(  TestVisitor ) 
    virtual ~TestVisitor()    


#*
#TestCase, supplies the interface for a Composite pattern's
#\em leaf class, though it is not a leaf in itself.
#
class TestCase (Test) :

    typedef TestContext Context # Test in TestContext? is redundant

    TestCase(  str sName ) : Test( sName ) 

    def accept(v):

         return v.visit( this ) 

    virtual void run(  Context ) = 0  # Subclass OSGUTX_EXPORT Responsibility

        virtual ~TestCase() 


#*
#Base class catchable for the exceptions which may be thrown to
#indicate problems during the run of a TestCase.
#
class TestX :

    TestX( str s):_what(s)    
    virtual ~TestX() 

    def what():

         return _what 
    _what = str()


#*
#A TestFailureX indicates a failure in the tested component.
#
class TestFailureX (TestX) :
    TestFailureX( str s):TestX(s)    


#*
#A TestErrorX indicates an error while testing a component,
#which prevents the test from being run. It does not indicate
#a problem with the component, but rather a problem during the
#run which prevents the component from being tested.
#
class TestErrorX (TestX) :
    TestErrorX( str s):TestX(s)    


#*
#TestCase_ is a class template for a leaf TestCase, which allows TestFixture
#classes to be easily collected into the tree of tests, and have their public
#test methods called. It is worth noting that, for a given TestCase_, an
#instance of the test fixture class will be constructed prior to the
#test method being called, and destructed afterwards. This prevents 'leakage'
#of information from one test case to the next.
#
template< typename FixtureT >
class TestCase_ (TestCase) :
typedef void (FixtureT.*TestMethodPtr)(  Context )

    # Constructor adds the TestMethod pointer
    TestCase_(  str sName, TestMethodPtr pTestMethod ) :
            TestCase( sName ),
            _pTestMethod( pTestMethod )

    # Create a TestFixture instance and invoke  def run(ctx) if (TestMethod) else 
        
        ( FixtureT().*_pTestMethod )( ctx )

        virtual ~TestCase_() 

    _pTestMethod = TestMethodPtr()


#*
#A TestSuite is the \em composite component of the Composite pattern,
#and allows aggregation of Tests into hierarchies.
#
class TestSuite (Test) :

    TestSuite(  str name )

    #* Adds a Test to the suite. 
    add = void( Test* pTest )

    #*
#    @returns    The immediate child denoted by name, or 0 if not found.
#    
    findChild = Test*( str name)

    accept = virtual bool( Test.Visitor v )

        virtual ~TestSuite() 

    typedef std.vector< Test > Tests
    _tests = Tests()  # Collection of Suites and/or Cases


#*
#TestGraph is a singleton providing central access to the tree of tests
#primarily, it provides access to the root suite.
#
class TestGraph :

    static TestGraph instance()

    #*
#        @return a pointer to the root TestSuite.
#    
    root = TestSuite*()

    #*
#        A utility function for accessing an arbitrary suite by pathname, relative to
#        the suite 'tsuite' (defaults to root if null), and with the option of creating
#        the \em TestSuite designated by \em path, if it does not already exist.
#
#        This method may return 0 if the suite either cannot be found (and createIfNecssary
#        is 0), or the first component of \em path is not the same as the name of the
#        TestSuite \em tsuite.
#
#        This was written to aid the auto-registration of tests at specific points in
#        the test tree, where the tests' AutoRegistrationAgents may be distributed across
#        several files, and cannot be guaranteed to run in a given order. E.g. You cannot
#        register a test "root.osg.MyTest" unless you know that the the suite "root.osg"
#        already exists.
#        
#
#        @param path                    The name of the TestSuite to return.
#        @param tsuite                The suite to 'start from'. Path is relative to this
#                                    suite (defaults to root suite).
#        @param createIfNecessary    Optionally create the TestSuite(s) denoted by path if
#                                    they do not exist.
#    
    suite = TestSuite*( str path, TestSuite* tsuite = 0,bool createIfNecessary = False)

    #*
#        Does the same job as the version of suite listed above, but the path
#        is passed in as components in a list, represented by the iterator parameters.
#    
    suite = TestSuite*(
        std.list<str>.iterator it,
        std.list<str>.iterator end,
        TestSuite* tsuite, bool createIfNecessary)

    TestGraph()

    TestGraph( TestGraph)
    operator = ( TestGraph)

    root_ = TestSuite()




#*
#Maintains a string that when accessed in the "visit" member, returns the
#current qualified TestSuite path.
#
class TestQualifier (TestVisitor) :
enum  SEPCHAR = ord(".") 

    # Entering a composite: Push its name on the Path
    visitEnter = virtual bool( TestSuite* pSuite )

    # Leaving a composite: Pop its name from the Path
    visitLeave = virtual bool( TestSuite* pSuite )

    # Provide read-only access to the current qualifier
     str currentPath() 

    _path = str()    # Current qualifier


#*
#QualifiedTestPrinter prints to standard output a list of fully
#qualified tests.
#
class QualifiedTestPrinter (TestQualifier) :


    visit = virtual bool( TestCase* pTest )


#*
#A TestRecord records the output of a given test case, i.e. its start/stop time,
#its result, and a textual description of any problems.
#
#\todo    Consider adding accessor methods if necessary, to get the details
#        stored in the TestRecord.
#
class TestRecord :
    
        TestRecord() 
        
        TestRecord( TestRecord rhs):
            name_(rhs.name_),
            start_(rhs.start_),
            stop_(rhs.stop_),
            result_(rhs.result_),
            problem_(rhs.problem_)
        
        
        operator = ( TestRecord rhs)
            if rhs==this : return *this

            name_ = rhs.name_
            start_ = rhs.start_
            stop_ = rhs.stop_
            result_ = rhs.result_
            problem_ = rhs.problem_

            return *this

        start = void()
        stop = void()
        log = void( TestFailureX e)
        log = void( TestErrorX e)
        log = void( std.exception e)
        log = void( str s)

        # FIXME: Add accessors?

        # Onlye a TestReport can create a TestRecord
        friend class TestReport
        TestRecord( str name)

        enum Result
            Success,Failure,Error
        

        friend std.ostream operator, (std.ostream o, TestRecord tr)

        static osg.Timer    timer_    # To time tests

        name_ = str()
        start_ = osg.Timer_t()
        stop_ = osg.Timer_t()
        result_ = Result()
        problem_ = str()



#*
#A TestReport represents the complete set of results (TestRecords) for a
#given test run.
#
#\todo    Add support for printing the test report in various formats:
#        e.g. text, XML, CSV
#
class TestReport :

    def createRecord(s):

        
        _records.push_back(TestRecord(s))
        return _records.back()
    _records = std.list<TestRecord>()









#*
#A TestRunner is a visitor which will run specified tests as it traverses the
#test graph.
#
#\todo    Consider an accessor method to get at the TestReport if necessary.
#
class TestRunner (TestQualifier) :

    TestRunner( TestContext ctx )

    #*
#        Tests may be specified by partial names. E.g. specifiying "root"
#        will run all tests below root, i.e. all tests.
#        Specifiying    "root.osg" will run all tests below \em root.osg.
#        Specifying "root.osg.de" will run all tests (and suites) below
#        \em root.osg with names beginning with the \em de.
#    
    specify = void(  str sQualifiedName )

    visitEnter = bool( TestSuite* pSuite )
    visit = bool( TestCase* pTest )
    visitLeave = bool( TestSuite* pSuite )

    perform = void( TestCase* pTest )

    operator = ( TestRunner)  return *this 

    _db = TestReport()            # Results
    _ctx = TestContext()            # The Global Testing Context
    _tests = std.vector<str>()          # Specified Tests



#*
#Starts a TestSuite singleton function
#@see OSGUTX_ADD_TESTCASE, OSGUTX_END_TESTSUITE
#
#define OSGUTX_BEGIN_TESTSUITE( tsuite ) \
    osgUtx.TestSuite* tsuite##_TestSuite() \
     \
        static osgUtx.TestSuite s_suite = 0 \
        if  s_suite == 0  :  \
            s_suite = osgUtx.TestSuite( #tsuite )



#*
#Adds a test case to a suite object being created in a TestSuite singleton function.
#@see OSGUTX_BEGIN_TESTSUITE, OSGUTX_END_TESTSUITE
#
#define OSGUTX_ADD_TESTCASE( tfixture, tmethod ) \
            s_suite.add( osgUtx.TestCase_<tfixture>(  \
                                #tmethod, tfixture.tmethod ) )

#*
#Ends a TestSuite singleton function
#@see OSGUTX_BEGIN_TESTSUITE, OSGUTX_ADD_TESTCASE
#
#define OSGUTX_END_TESTSUITE \
         \
        return s_suite \

#* Define a TestSuite accessor 
#define OSGUTX_TESTSUITE( tsuite ) \
    tsuite##_TestSuite()


#*
#Adds a suite to a suite - allows composition of test suites.
#@see OSGUTX_BEGIN_TESTSUITE, OSGUTX_END_TESTSUITE
#
#define OSGUTX_ADD_TESTSUITE( childSuite ) \
    s_suite.add( childSuite##_TestSuite() )


#* Autoregister a testsuite with the root suite at startup 
#define OSGUTX_AUTOREGISTER_TESTSUITE( tsuite ) \
    static osgUtx.TestSuiteAutoRegistrationAgent tsuite##_autoRegistrationObj__( tsuite##_TestSuite() )

#* Auto register a testsuite with at designated point in the suite graph at startup 
#define OSGUTX_AUTOREGISTER_TESTSUITE_AT( tsuite , path ) \
    static osgUtx.TestSuiteAutoRegistrationAgent tsuite##_autoRegistrationObj__( tsuite##_TestSuite(), #path )

namespace osgUtx

#*
#A helper struct to perform automatic registration at program startup not for
#direct use, it should be used via the following macros. (It's a secret agent :-)
#
#@see OSGUTX_AUTOREGISTER_TESTSUITE, OSGUTX_AUTOREGISTER_TESTSUITE_AT
#
class TestSuiteAutoRegistrationAgent :
TestSuiteAutoRegistrationAgent(TestSuite* tsuite,  char* path = 0)
        if   not  path  : path = "root"

        # Find the suite named in 'path', create it if necessary
        regSuite = osgUtx.TestGraph.instance().suite( path, 0, True )

        if  not regSuite :
            osg.notify(osg.WARN), "Warning, unable to register test suite named \"", tsuite.name(), "\" at ", path, ", falling back to root suite."
            regSuite = osgUtx.TestGraph.instance().root()

        regSuite.add(tsuite)



#*
#OSGUTX_TEST_F is a convenience macro, analogous to assert(), which will
#throw an osgUtx.TestFailureX if \em expr evaluates to False this should be
#used to test for failure in a given test, as opposed to an actual error
#in the test owing to some other reason than the tested code being faulty.
#
#The exception will indicate the file and line number of the failed expression,
#along with expression itself.
#
#define OSGUTX_TEST_F( expr ) \
    if   not (expr)  : \
        ss = strstream() \
        ss, #expr, " failure: ", __FILE__, ", line ", __LINE__, std.ends \
        throw osgUtx.TestFailureX(ss.str()) \

#*
#OSGUTX_TEST_E is a convenience macro, analogous to assert(), which will
#throw an osgUtx.TestErrorX if \em expr evaluates to False this should be
#used to test for an error in a given test, as opposed to a failure
#in the tested code.
#
#The exception will indicate the file and line number of the failed expression,
#along with expression itself.
#
#define OSGUTX_TEST_E( expr ) \
    if   not (expr)  : \
        ss = strstream() \
        ss, #expr, " error: ", __FILE__, ", line ", __LINE__, std.ends \
        throw osgUtx.TestErrorX(ss.str()) \


#endif # OSG_UNITTESTFRAMEWORK

# Translated from file 'UnitTests_osg.cpp'

# OpenSceneGraph example, osgunittests.
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

#include "UnitTestFramework.h"

#include <osg/Matrixd>
#include <osg/Matrixf>
#include <osg/Vec3d>
#include <osg/Vec3>
#include <sstream>

namespace osg


#######################################/
# 
#  Vec3 Tests
#
class Vec3TestFixture :

    Vec3TestFixture()

    testAddition = void( osgUtx.TestContext ctx)
    testSubtraction = void( osgUtx.TestContext ctx)
    testScalarMultiplication = void( osgUtx.TestContext ctx)
    testDotProduct = void( osgUtx.TestContext ctx)

    # Some convenience variables for use in the tests
    Vec3 v1_, v2_, v3_



Vec3TestFixture.Vec3TestFixture():
    v1_(1.0, 1.0, 1.0),
    v2_(2.0, 2.0, 2.0),
    v3_(3.0, 3.0, 3.0)

void Vec3TestFixture.testAddition( osgUtx.TestContext)
    OSGUTX_TEST_F( v1_ + v2_ == v3_ )

void Vec3TestFixture.testSubtraction( osgUtx.TestContext)
    OSGUTX_TEST_F( v3_ - v1_ == v2_ )

void Vec3TestFixture.testScalarMultiplication( osgUtx.TestContext)
    OSGUTX_TEST_F( v1_ * 3 == v3_ )

void Vec3TestFixture.testDotProduct( osgUtx.TestContext)
    

OSGUTX_BEGIN_TESTSUITE(Vec3)
    OSGUTX_ADD_TESTCASE(Vec3TestFixture, testAddition)
    OSGUTX_ADD_TESTCASE(Vec3TestFixture, testSubtraction)
    OSGUTX_ADD_TESTCASE(Vec3TestFixture, testScalarMultiplication)
    OSGUTX_ADD_TESTCASE(Vec3TestFixture, testDotProduct)
OSGUTX_END_TESTSUITE

OSGUTX_AUTOREGISTER_TESTSUITE_AT(Vec3, root.osg)

#######################################/
# 
#  Matrix Tests
#
class MatrixTestFixture :

    MatrixTestFixture()

    testPreMultTranslate = void( osgUtx.TestContext ctx)
    testPostMultTranslate = void( osgUtx.TestContext ctx)
    testPreMultScale = void( osgUtx.TestContext ctx)
    testPostMultScale = void( osgUtx.TestContext ctx)
    testPreMultRotate = void( osgUtx.TestContext ctx)
    testPostMultRotate = void( osgUtx.TestContext ctx)

    # Some convenience variables for use in the tests
    _md = Matrixd()
    _mf = Matrixf()
    _v3d = Vec3d()
    _v3 = Vec3()
    _q1 = Quat()
    _q2 = Quat()
    _q3 = Quat()
    _q4 = Quat()



MatrixTestFixture.MatrixTestFixture():
    _md(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16),
    _mf(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16),
    _v3d(1, 2, 3),
    _v3(1, 2, 3),
    _q1(1, 0, 0, 0),
    _q2(0, 1, 0, 0),
    _q3(0, 0, 1, 0),
    _q4(0, 0, 0, 1)

void MatrixTestFixture.testPreMultTranslate( osgUtx.TestContext)
    tdo = osg.Matrixd()
    tdn = osg.Matrixd()
    tfo = osg.Matrixf()
    tfn = osg.Matrixf()

    tdo = _md
    tdn = _md
    tdo.preMult(osg.Matrixd.translate(_v3d))
    tdn.preMultTranslate(_v3d)
    OSGUTX_TEST_F( tdo == tdn )

    tdo = _md
    tdn = _md
    tdo.preMult(osg.Matrixd.translate(_v3))
    tdn.preMultTranslate(_v3)
    OSGUTX_TEST_F( tdo == tdn )

    tfo = _mf
    tfn = _mf
    tfo.preMult(osg.Matrixf.translate(_v3d))
    tfn.preMultTranslate(_v3d)
    OSGUTX_TEST_F( tfo == tfn )

    tfo = _mf
    tfn = _mf
    tfo.preMult(osg.Matrixf.translate(_v3))
    tfn.preMultTranslate(_v3)
    OSGUTX_TEST_F( tfo == tfn )

void MatrixTestFixture.testPostMultTranslate( osgUtx.TestContext)
    tdo = osg.Matrixd()
    tdn = osg.Matrixd()
    tfo = osg.Matrixf()
    tfn = osg.Matrixf()

    tdo = _md
    tdn = _md
    tdo.postMult(osg.Matrixd.translate(_v3d))
    tdn.postMultTranslate(_v3d)
    OSGUTX_TEST_F( tdo == tdn )

    tdo = _md
    tdn = _md
    tdo.postMult(osg.Matrixd.translate(_v3))
    tdn.postMultTranslate(_v3)
    OSGUTX_TEST_F( tdo == tdn )

    tfo = _mf
    tfn = _mf
    tfo.postMult(osg.Matrixf.translate(_v3d))
    tfn.postMultTranslate(_v3d)
    OSGUTX_TEST_F( tfo == tfn )

    tfo = _mf
    tfn = _mf
    tfo.postMult(osg.Matrixf.translate(_v3))
    tfn.postMultTranslate(_v3)
    OSGUTX_TEST_F( tfo == tfn )

void MatrixTestFixture.testPreMultScale( osgUtx.TestContext)
    tdo = osg.Matrixd()
    tdn = osg.Matrixd()
    tfo = osg.Matrixf()
    tfn = osg.Matrixf()

    tdo = _md
    tdn = _md
    tdo.preMult(osg.Matrixd.scale(_v3d))
    tdn.preMultScale(_v3d)
    OSGUTX_TEST_F( tdo == tdn )

    tdo = _md
    tdn = _md
    tdo.preMult(osg.Matrixd.scale(_v3))
    tdn.preMultScale(_v3)
    OSGUTX_TEST_F( tdo == tdn )

    tfo = _mf
    tfn = _mf
    tfo.preMult(osg.Matrixf.scale(_v3d))
    tfn.preMultScale(_v3d)
    OSGUTX_TEST_F( tfo == tfn )

    tfo = _mf
    tfn = _mf
    tfo.preMult(osg.Matrixf.scale(_v3))
    tfn.preMultScale(_v3)
    OSGUTX_TEST_F( tfo == tfn )

void MatrixTestFixture.testPostMultScale( osgUtx.TestContext)
    tdo = osg.Matrixd()
    tdn = osg.Matrixd()
    tfo = osg.Matrixf()
    tfn = osg.Matrixf()

    tdo = _md
    tdn = _md
    tdo.postMult(osg.Matrixd.scale(_v3d))
    tdn.postMultScale(_v3d)
    OSGUTX_TEST_F( tdo == tdn )

    tdo = _md
    tdn = _md
    tdo.postMult(osg.Matrixd.scale(_v3))
    tdn.postMultScale(_v3)
    OSGUTX_TEST_F( tdo == tdn )

    tfo = _mf
    tfn = _mf
    tfo.postMult(osg.Matrixf.scale(_v3d))
    tfn.postMultScale(_v3d)
    OSGUTX_TEST_F( tfo == tfn )

    tfo = _mf
    tfn = _mf
    tfo.postMult(osg.Matrixf.scale(_v3))
    tfn.postMultScale(_v3)
    OSGUTX_TEST_F( tfo == tfn )

void MatrixTestFixture.testPreMultRotate( osgUtx.TestContext)
    tdo = osg.Matrixd()
    tdn = osg.Matrixd()
    tfo = osg.Matrixf()
    tfn = osg.Matrixf()

    tdo = _md
    tdn = _md
    tdo.preMult(osg.Matrixd.rotate(_q1))
    tdn.preMultRotate(_q1)
    OSGUTX_TEST_F( tdo == tdn )

    tdo = _md
    tdn = _md
    tdo.preMult(osg.Matrixd.rotate(_q2))
    tdn.preMultRotate(_q2)
    OSGUTX_TEST_F( tdo == tdn )

    tdo = _md
    tdn = _md
    tdo.preMult(osg.Matrixd.rotate(_q3))
    tdn.preMultRotate(_q3)
    OSGUTX_TEST_F( tdo == tdn )

    tdo = _md
    tdn = _md
    tdo.preMult(osg.Matrixd.rotate(_q4))
    tdn.preMultRotate(_q4)
    OSGUTX_TEST_F( tdo == tdn )

    tfo = _mf
    tfn = _mf
    tfo.preMult(osg.Matrixf.rotate(_q1))
    tfn.preMultRotate(_q1)
    OSGUTX_TEST_F( tfo == tfn )

    tfo = _mf
    tfn = _mf
    tfo.preMult(osg.Matrixf.rotate(_q2))
    tfn.preMultRotate(_q2)
    OSGUTX_TEST_F( tfo == tfn )

    tfo = _mf
    tfn = _mf
    tfo.preMult(osg.Matrixf.rotate(_q3))
    tfn.preMultRotate(_q3)
    OSGUTX_TEST_F( tfo == tfn )

    tfo = _mf
    tfn = _mf
    tfo.preMult(osg.Matrixf.rotate(_q4))
    tfn.preMultRotate(_q4)
    OSGUTX_TEST_F( tfo == tfn )

void MatrixTestFixture.testPostMultRotate( osgUtx.TestContext)
    tdo = osg.Matrixd()
    tdn = osg.Matrixd()
    tfo = osg.Matrixf()
    tfn = osg.Matrixf()

    tdo = _md
    tdn = _md
    tdo.postMult(osg.Matrixd.rotate(_q1))
    tdn.postMultRotate(_q1)
    OSGUTX_TEST_F( tdo == tdn )

    tdo = _md
    tdn = _md
    tdo.postMult(osg.Matrixd.rotate(_q2))
    tdn.postMultRotate(_q2)
    OSGUTX_TEST_F( tdo == tdn )

    tdo = _md
    tdn = _md
    tdo.postMult(osg.Matrixd.rotate(_q3))
    tdn.postMultRotate(_q3)
    OSGUTX_TEST_F( tdo == tdn )

    tdo = _md
    tdn = _md
    tdo.postMult(osg.Matrixd.rotate(_q4))
    tdn.postMultRotate(_q4)
    OSGUTX_TEST_F( tdo == tdn )

    tfo = _mf
    tfn = _mf
    tfo.postMult(osg.Matrixf.rotate(_q1))
    tfn.postMultRotate(_q1)
    OSGUTX_TEST_F( tfo == tfn )

    tfo = _mf
    tfn = _mf
    tfo.postMult(osg.Matrixf.rotate(_q2))
    tfn.postMultRotate(_q2)
    OSGUTX_TEST_F( tfo == tfn )

    tfo = _mf
    tfn = _mf
    tfo.postMult(osg.Matrixf.rotate(_q3))
    tfn.postMultRotate(_q3)
    OSGUTX_TEST_F( tfo == tfn )

    tfo = _mf
    tfn = _mf
    tfo.postMult(osg.Matrixf.rotate(_q4))
    tfn.postMultRotate(_q4)
    OSGUTX_TEST_F( tfo == tfn )

OSGUTX_BEGIN_TESTSUITE(Matrix)
    OSGUTX_ADD_TESTCASE(MatrixTestFixture, testPreMultTranslate)
    OSGUTX_ADD_TESTCASE(MatrixTestFixture, testPostMultTranslate)
    OSGUTX_ADD_TESTCASE(MatrixTestFixture, testPreMultScale)
    OSGUTX_ADD_TESTCASE(MatrixTestFixture, testPostMultScale)
    OSGUTX_ADD_TESTCASE(MatrixTestFixture, testPreMultRotate)
    OSGUTX_ADD_TESTCASE(MatrixTestFixture, testPostMultRotate)
OSGUTX_END_TESTSUITE

OSGUTX_AUTOREGISTER_TESTSUITE_AT(Matrix, root.osg)




if __name__ == "__main__":
    main(sys.argv)
