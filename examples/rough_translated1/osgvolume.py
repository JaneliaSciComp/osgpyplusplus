#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgvolume"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osg
from osgpypp import osgDB
from osgpypp import osgGA
from osgpypp import osgManipulator
from osgpypp import osgUtil
from osgpypp import osgViewer
from osgpypp import osgVolume


# Translated from file 'osgvolume.cpp'

# OpenSceneGraph example, osgvolume.
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

#include <osg/Node>
#include <osg/Geometry>
#include <osg/Notify>
#include <osg/Texture3D>
#include <osg/Texture1D>
#include <osg/ImageSequence>
#include <osg/TexGen>
#include <osg/Geode>
#include <osg/Billboard>
#include <osg/PositionAttitudeTransform>
#include <osg/ClipNode>
#include <osg/AlphaFunc>
#include <osg/TexGenNode>
#include <osg/TexEnv>
#include <osg/TexEnvCombine>
#include <osg/Material>
#include <osg/PrimitiveSet>
#include <osg/Endian>
#include <osg/BlendFunc>
#include <osg/BlendEquation>
#include <osg/TransferFunction>
#include <osg/MatrixTransform>

#include <osgDB/Registry>
#include <osgDB/ReadFile>
#include <osgDB/WriteFile>
#include <osgDB/FileUtils>
#include <osgDB/FileNameUtils>

#include <osgGA/EventVisitor>
#include <osgGA/TrackballManipulator>
#include <osgGA/FlightManipulator>
#include <osgGA/KeySwitchMatrixManipulator>

#include <osgUtil/CullVisitor>

#include <osgViewer/Viewer>
#include <osgViewer/ViewerEventHandlers>

#include <osgManipulator/TabBoxDragger>
#include <osgManipulator/TabPlaneTrackballDragger>
#include <osgManipulator/TrackballDragger>

#include <osg/io_utils>

#include <algorithm>
#include <iostream>

#include <osg/ImageUtils>
#include <osgVolume/Volume>
#include <osgVolume/VolumeTile>
#include <osgVolume/RayTracedTechnique>
#include <osgVolume/FixedFunctionTechnique>

enum ShadingModel
    Standard,
    Light,
    Isosurface,
    MaximumIntensityProjection



def createTexture3D(imageList, numComponentsDesired, s_maximumTextureSize, t_maximumTextureSize, r_maximumTextureSize, resizeToPowerOfTwo):


    

    if numComponentsDesired==0 :
        return osg.createImage3DWithAlpha(imageList,
                                        s_maximumTextureSize,
                                        t_maximumTextureSize,
                                        r_maximumTextureSize,
                                        resizeToPowerOfTwo)
    else:
        desiredPixelFormat = 0
        switch(numComponentsDesired)
            case(1) : desiredPixelFormat = GL_LUMINANCE break
            case(2) : desiredPixelFormat = GL_LUMINANCE_ALPHA break
            case(3) : desiredPixelFormat = GL_RGB break
            case(4) : desiredPixelFormat = GL_RGBA break

        return osg.createImage3D(imageList,
                                        desiredPixelFormat,
                                        s_maximumTextureSize,
                                        t_maximumTextureSize,
                                        r_maximumTextureSize,
                                        resizeToPowerOfTwo)

class ScaleOperator :
ScaleOperator():_scale(1.0) 
    ScaleOperator(float scale):_scale(scale) 
    ScaleOperator( ScaleOperator so):_scale(so._scale) 

    operator = ( ScaleOperator so)  _scale = so._scale return *this 

    _scale = float()

    inline void luminance(float l)   l*= _scale 
    inline void alpha(float a)   a*= _scale 
    inline void luminance_alpha(float l,float a)   l*= _scale a*= _scale  
    inline void rgb(float r,float g,float b)   r*= _scale g*=_scale b*=_scale 
    inline void rgba(float r,float g,float b,float a)   r*= _scale g*=_scale b*=_scale a*=_scale 


class RecordRowOperator :
RecordRowOperator(unsigned int num):_colours(num),_pos(0) 

    mutable std.vector<osg.Vec4>  _colours
    mutable unsigned int            _pos

    inline void luminance(float l)   rgba(l,l,l,1.0) 
    inline void alpha(float a)   rgba(1.0,1.0,1.0,a) 
    inline void luminance_alpha(float l,float a)   rgba(l,l,l,a)  
    inline void rgb(float r,float g,float b)   rgba(r,g,b,1.0) 
    inline void rgba(float r,float g,float b,float a)   _colours[_pos++].set(r,g,b,a) 


class WriteRowOperator :
WriteRowOperator():_pos(0) 
    WriteRowOperator(unsigned int num):_colours(num),_pos(0) 

    _colours = std.vector<osg.Vec4>()
    mutable unsigned int    _pos

    inline void luminance(float l)   l = _colours[_pos++].r() 
    inline void alpha(float a)   a = _colours[_pos++].a() 
    inline void luminance_alpha(float l,float a)   l = _colours[_pos].r() a = _colours[_pos++].a() 
    inline void rgb(float r,float g,float b)   r = _colours[_pos].r() g = _colours[_pos].g() b = _colours[_pos].b() 
    inline void rgba(float r,float g,float b,float a)    r = _colours[_pos].r() g = _colours[_pos].g() b = _colours[_pos].b() a = _colours[_pos++].a() 


def clampToNearestValidPowerOfTwo(sizeX, sizeY, sizeZ, s_maximumTextureSize, t_maximumTextureSize, r_maximumTextureSize):

    
    # compute nearest powers of two for each axis.
    s_nearestPowerOfTwo = 1
    while s_nearestPowerOfTwo<sizeX  and  s_nearestPowerOfTwo<s_maximumTextureSize : s_nearestPowerOfTwo*=2

    t_nearestPowerOfTwo = 1
    while t_nearestPowerOfTwo<sizeY  and  t_nearestPowerOfTwo<t_maximumTextureSize : t_nearestPowerOfTwo*=2

    r_nearestPowerOfTwo = 1
    while r_nearestPowerOfTwo<sizeZ  and  r_nearestPowerOfTwo<r_maximumTextureSize : r_nearestPowerOfTwo*=2

    sizeX = s_nearestPowerOfTwo
    sizeY = t_nearestPowerOfTwo
    sizeZ = r_nearestPowerOfTwo

def readRaw(sizeX, sizeY, sizeZ, numberBytesPerComponent, numberOfComponents, endian, raw_filename):

    
    fin = osgDB.ifstream(raw_filename.c_str(), std.ifstream.binary)
    if  not fin : return 0

    pixelFormat = GLenum()
    switch(numberOfComponents)
        case 1 : pixelFormat = GL_LUMINANCE break
        case 2 : pixelFormat = GL_LUMINANCE_ALPHA break
        case 3 : pixelFormat = GL_RGB break
        case 4 : pixelFormat = GL_RGBA break
        default :
            osg.notify(osg.NOTICE), "Error: numberOfComponents=", numberOfComponents, " not supported, only 1,2,3 or 4 are supported."
            return 0


    dataType = GLenum()
    switch(numberBytesPerComponent)
        case 1 : dataType = GL_UNSIGNED_BYTE break
        case 2 : dataType = GL_UNSIGNED_SHORT break
        case 4 : dataType = GL_UNSIGNED_INT break
        default :
            osg.notify(osg.NOTICE), "Error: numberBytesPerComponent=", numberBytesPerComponent, " not supported, only 1,2 or 4 are supported."
            return 0

    s_maximumTextureSize = 256, t_maximumTextureSize=256, r_maximumTextureSize=256

    sizeS = sizeX
    sizeT = sizeY
    sizeR = sizeZ
    clampToNearestValidPowerOfTwo(sizeS, sizeT, sizeR, s_maximumTextureSize, t_maximumTextureSize, r_maximumTextureSize)

    image = osg.Image()
    image.allocateImage(sizeS, sizeT, sizeR, pixelFormat, dataType)


    endianSwap =  (endian not ="big") if ((osg.getCpuByteOrder()==osg.BigEndian)) else  (endian=="big")

    r_offset =  sizeR/2 - sizeZ/2 if ((sizeZ<sizeR)) else  0

    offset =  numberBytesPerComponent if (endianSwap) else  0
    delta =  -1 if (endianSwap) else  1
    for(int r=0r<sizeZ++r)
        for(int t=0t<sizeY++t)
            data = (char*) image.data(0,t,r+r_offset)
            for(int s=0s<sizeX++s)
                if  not fin : return 0

                for(int c=0c<numberOfComponents++c)
                    ptr = data+offset
                    for(int b=0b<numberBytesPerComponent++b)
                        fin.read((char*)ptr, 1)
                        ptr += delta
                    data += numberBytesPerComponent


    # normalise texture
        # compute range of values
        osg.Vec4 minValue, maxValue
        osg.computeMinMax(image, minValue, maxValue)
        osg.modifyImage(image,ScaleOperator(1.0/maxValue.r()))


    fin.close()

    if dataType not =GL_UNSIGNED_BYTE :
        # need to convert to ubyte

        new_image = osg.Image()
        new_image.allocateImage(sizeS, sizeT, sizeR, pixelFormat, GL_UNSIGNED_BYTE)

        readOp = RecordRowOperator(sizeS)
        writeOp = WriteRowOperator()

        for(int r=0r<sizeR++r)
            for(int t=0t<sizeT++t)
                # reset the indices to beginning
                readOp._pos = 0
                writeOp._pos = 0

                # read the pixels into readOp's _colour array
                osg.readRow(sizeS, pixelFormat, dataType, image.data(0,t,r), readOp)

                # pass readOp's _colour array contents over to writeOp (note this is just a pointer swap).
                writeOp._colours.swap(readOp._colours)

                osg.modifyRow(sizeS, pixelFormat, GL_UNSIGNED_BYTE, new_image.data(0,t,r), writeOp)

                # return readOp's _colour array contents back to its rightful owner.
                writeOp._colours.swap(readOp._colours)

        image = new_image

    return image.release()




def readTransferFunctionFile(filename, colorScale):


    
    foundFile = osgDB.findDataFile(filename)
    if foundFile.empty() :
        print "Error: could not find transfer function file : ", filename
        return 0

    print "Reading transfer function ", filename

    colorMap = osg.TransferFunction1D.ColorMap()
    fin = osgDB.ifstream(foundFile.c_str())
    while fin :
        float value, red, green, blue, alpha
        fin >> value >> red >> green >> blue >> alpha
        if fin :
            print "value = ", value, " (", red, ", ", green, ", ", blue, ", ", alpha, ")"
            colorMap[value] = osg.Vec4(red*colorScale,green*colorScale,blue*colorScale,alpha*colorScale)

    if colorMap.empty() :
        print "Error: No values read from transfer function file: ", filename
        return 0

    tf = osg.TransferFunction1D()
    tf.assign(colorMap)

    return tf


class TestSupportOperation (osg.GraphicsOperation) :

    TestSupportOperation():
        osg.GraphicsOperation("TestSupportOperation",False),
        supported(True),
        errorMessage(),
        maximumTextureSize(256) 

    virtual void operator () (osg.GraphicsContext* gc)
        lock = OpenThreads.ScopedLock<OpenThreads.Mutex>(mutex)

        glGetIntegerv( GL_MAX_3D_TEXTURE_SIZE, maximumTextureSize )

        osg.notify(osg.NOTICE), "Max texture size=", maximumTextureSize

    mutex = OpenThreads.Mutex()
    supported = bool()
    errorMessage = str()
    maximumTextureSize = GLint()


class DraggerVolumeTileCallback (osgManipulator.DraggerCallback) :

    DraggerVolumeTileCallback(osgVolume.VolumeTile* volume, osgVolume.Locator* locator):
        _volume(volume),
        _locator(locator) 


    receive = virtual bool( osgManipulator.MotionCommand command)


    _volume = osg.observer_ptr<osgVolume.VolumeTile>()
    _locator = osgVolume.Locator()

    _startMotionMatrix = osg.Matrix()

    _localToWorld = osg.Matrix()
    _worldToLocal = osg.Matrix()



bool DraggerVolumeTileCallback.receive( osgManipulator.MotionCommand command)
    if  not _locator : return False

    switch (command.getStage())
        case osgManipulator.MotionCommand.START:
            # Save the current matrix
            _startMotionMatrix = _locator.getTransform()

            # Get the LocalToWorld and WorldToLocal matrix for this node.
            nodePathToRoot = osg.NodePath()
            osgManipulator.computeNodePathToRoot(*_volume,nodePathToRoot)
            _localToWorld = _startMotionMatrix * osg.computeLocalToWorld(nodePathToRoot)
            _worldToLocal = osg.Matrix.inverse(_localToWorld)

            return True
        case osgManipulator.MotionCommand.MOVE:
            # Transform the command's motion matrix into local motion matrix.
            localMotionMatrix = _localToWorld * command.getWorldToLocal()
                                            * command.getMotionMatrix()
                                            * command.getLocalToWorld() * _worldToLocal

            # Transform by the localMotionMatrix
            _locator.setTransform(localMotionMatrix * _startMotionMatrix)

            # osg.notify(osg.NOTICE), "New locator matrix ", _locator.getTransform()

            return True
        case osgManipulator.MotionCommand.FINISH:
            return True
        case osgManipulator.MotionCommand.NONE:
        default:
            return False

def main(argv):

    
    # use an ArgumentParser object to manage the program arguments.
    arguments = osg.ArgumentParser(argv)

    # set up the usage document, in case we need to print out how to use this program.
    arguments.getApplicationUsage().setDescription(arguments.getApplicationName()+" is the example which demonstrates use of 3D textures.")
    arguments.getApplicationUsage().setCommandLineUsage(arguments.getApplicationName()+" [options] filename ...")
    arguments.getApplicationUsage().addCommandLineOption("-h or --help","Display this information")
    arguments.getApplicationUsage().addCommandLineOption("--images [filenames]","Specify a stack of 2d images to build the 3d volume from.")
    arguments.getApplicationUsage().addCommandLineOption("--shader","Use OpenGL Shading Language. (default)")
    arguments.getApplicationUsage().addCommandLineOption("--no-shader","Disable use of OpenGL Shading Language.")
    arguments.getApplicationUsage().addCommandLineOption("--gpu-tf","Aply the transfer function on the GPU. (default)")
    arguments.getApplicationUsage().addCommandLineOption("--cpu-tf","Apply the transfer function on the CPU.")
    arguments.getApplicationUsage().addCommandLineOption("--mip","Use Maximum Intensity Projection (MIP) filtering.")
    arguments.getApplicationUsage().addCommandLineOption("--isosurface","Use Iso surface render.")
    arguments.getApplicationUsage().addCommandLineOption("--light","Use normals computed on the GPU to render a lit volume.")
    arguments.getApplicationUsage().addCommandLineOption("-n","Use normals computed on the GPU to render a lit volume.")
    arguments.getApplicationUsage().addCommandLineOption("--xSize <size>","Relative width of rendered brick.")
    arguments.getApplicationUsage().addCommandLineOption("--ySize <size>","Relative length of rendered brick.")
    arguments.getApplicationUsage().addCommandLineOption("--zSize <size>","Relative height of rendered brick.")
    arguments.getApplicationUsage().addCommandLineOption("--maxTextureSize <size>","Set the texture maximum resolution in the s,t,r (x,y,z) dimensions.")
    arguments.getApplicationUsage().addCommandLineOption("--s_maxTextureSize <size>","Set the texture maximum resolution in the s (x) dimension.")
    arguments.getApplicationUsage().addCommandLineOption("--t_maxTextureSize <size>","Set the texture maximum resolution in the t (y) dimension.")
    arguments.getApplicationUsage().addCommandLineOption("--r_maxTextureSize <size>","Set the texture maximum resolution in the r (z) dimension.")
    arguments.getApplicationUsage().addCommandLineOption("--modulate-alpha-by-luminance","For each pixel multiply the alpha value by the luminance.")
    arguments.getApplicationUsage().addCommandLineOption("--replace-alpha-with-luminance","For each pixel set the alpha value to the luminance.")
    arguments.getApplicationUsage().addCommandLineOption("--replace-rgb-with-luminance","For each rgb pixel convert to the luminance.")
    arguments.getApplicationUsage().addCommandLineOption("--num-components <num>","Set the number of components to in he target image.")
    arguments.getApplicationUsage().addCommandLineOption("--no-rescale","Disable the rescaling of the pixel data to 0.0 to 1.0 range")
    arguments.getApplicationUsage().addCommandLineOption("--rescale","Enable the rescale of the pixel data to 0.0 to 1.0 range (default).")
    arguments.getApplicationUsage().addCommandLineOption("--shift-min-to-zero","Shift the pixel data so min value is 0.0.")
    arguments.getApplicationUsage().addCommandLineOption("--sequence-length <num>","Set the length of time that a sequence of images with run for.")
    arguments.getApplicationUsage().addCommandLineOption("--sd <num>","Short hand for --sequence-length")
    arguments.getApplicationUsage().addCommandLineOption("--sdwm <num>","Set the SampleDensityWhenMovingProperty to specified value")
    arguments.getApplicationUsage().addCommandLineOption("--lod","Enable techniques to reduce the level of detail when moving.")
#    arguments.getApplicationUsage().addCommandLineOption("--raw <sizeX> <sizeY> <sizeZ> <numberBytesPerComponent> <numberOfComponents> <endian> <filename>","read a raw image data")

    # construct the viewer.
    viewer = osgViewer.Viewer(arguments)

    # add the window size toggle handler
    viewer.addEventHandler(osgViewer.WindowSizeHandler)()

        keyswitchManipulator = osgGA.KeySwitchMatrixManipulator()

        keyswitchManipulator.addMatrixManipulator( ord("1"), "Trackball", osgGA.TrackballManipulator() )

        flightManipulator = osgGA.FlightManipulator()
        flightManipulator.setYawControlMode(osgGA.FlightManipulator.NO_AUTOMATIC_YAW)
        keyswitchManipulator.addMatrixManipulator( ord("2"), "Flight", flightManipulator )

        viewer.setCameraManipulator( keyswitchManipulator )

    # add the stats handler
    viewer.addEventHandler(osgViewer.StatsHandler)()

    viewer.getCamera().setClearColor(osg.Vec4(0.0,0.0,0.0,0.0))

    # if user request help write it out to cout.
    if arguments.read("-h")  or  arguments.read("--help") :
        arguments.getApplicationUsage().write(std.cout)
        return 1

    outputFile = str()
    while arguments.read("-o",outputFile) : 



    transferFunction = osg.TransferFunction1D()
    tranferFunctionFile = str()
    while arguments.read("--tf",tranferFunctionFile) :
        transferFunction = readTransferFunctionFile(tranferFunctionFile)
    while arguments.read("--tf-255",tranferFunctionFile) :
        transferFunction = readTransferFunctionFile(tranferFunctionFile,1.0/255.0)

    while arguments.read("--test") :
        transferFunction = osg.TransferFunction1D()
        transferFunction.setColor(0.0, osg.Vec4(1.0,0.0,0.0,0.0))
        transferFunction.setColor(0.5, osg.Vec4(1.0,1.0,0.0,0.5))
        transferFunction.setColor(1.0, osg.Vec4(0.0,0.0,1.0,1.0))

    while arguments.read("--test2") :
        transferFunction = osg.TransferFunction1D()
        transferFunction.setColor(0.0, osg.Vec4(1.0,0.0,0.0,0.0))
        transferFunction.setColor(0.5, osg.Vec4(1.0,1.0,0.0,0.5))
        transferFunction.setColor(1.0, osg.Vec4(0.0,0.0,1.0,1.0))
        transferFunction.assign(transferFunction.getColorMap())

        # deprecated options

        invalidOption = False

        numSlices = 500
        while arguments.read("-s",numSlices) :  OSG_NOTICE, "Warning: -s option no longer supported." invalidOption = True 

        sliceEnd = 1.0
        while arguments.read("--clip",sliceEnd) :  OSG_NOTICE, "Warning: --clip option no longer supported." invalidOption = True 


        if invalidOption : return 1

    xMultiplier = 1.0
    while arguments.read("--xMultiplier",xMultiplier) : 

    yMultiplier = 1.0
    while arguments.read("--yMultiplier",yMultiplier) : 

    zMultiplier = 1.0
    while arguments.read("--zMultiplier",zMultiplier) : 


    alphaFunc = 0.02
    while arguments.read("--alphaFunc",alphaFunc) : 



    shadingModel = Standard
    while arguments.read("--mip") : shadingModel =  MaximumIntensityProjection

    while arguments.read("--isosurface")  or  arguments.read("--iso-surface") : shadingModel = Isosurface

    while arguments.read("--light")  or  arguments.read("-n") : shadingModel = Light

    xSize = 0.0, ySize=0.0, zSize=0.0
    while arguments.read("--xSize",xSize) : 
    while arguments.read("--ySize",ySize) : 
    while arguments.read("--zSize",zSize) : 

    testSupportOperation = TestSupportOperation()
    viewer.setRealizeOperation(testSupportOperation)

    viewer.realize()

    maximumTextureSize = testSupportOperation.maximumTextureSize
    s_maximumTextureSize = maximumTextureSize
    t_maximumTextureSize = maximumTextureSize
    r_maximumTextureSize = maximumTextureSize
    while arguments.read("--maxTextureSize",maximumTextureSize) :
        s_maximumTextureSize = maximumTextureSize
        t_maximumTextureSize = maximumTextureSize
        r_maximumTextureSize = maximumTextureSize
    while arguments.read("--s_maxTextureSize",s_maximumTextureSize) : 
    while arguments.read("--t_maxTextureSize",t_maximumTextureSize) : 
    while arguments.read("--r_maxTextureSize",r_maximumTextureSize) : 

    # set up colour space operation.
    colourSpaceOperation = osg.NO_COLOR_SPACE_OPERATION
    colourModulate = osg.Vec4(0.25,0.25,0.25,0.25)
    while arguments.read("--modulate-alpha-by-luminance") :  colourSpaceOperation = osg.MODULATE_ALPHA_BY_LUMINANCE 
    while arguments.read("--modulate-alpha-by-colour", colourModulate.x(),colourModulate.y(),colourModulate.z(),colourModulate.w() ) :  colourSpaceOperation = osg.MODULATE_ALPHA_BY_COLOR 
    while arguments.read("--replace-alpha-with-luminance") :  colourSpaceOperation = osg.REPLACE_ALPHA_WITH_LUMINANCE 
    while arguments.read("--replace-rgb-with-luminance") :  colourSpaceOperation = osg.REPLACE_RGB_WITH_LUMINANCE 


    enum RescaleOperation
        NO_RESCALE,
        RESCALE_TO_ZERO_TO_ONE_RANGE,
        SHIFT_MIN_TO_ZERO
    

    rescaleOperation = RESCALE_TO_ZERO_TO_ONE_RANGE
    while arguments.read("--no-rescale") : rescaleOperation = NO_RESCALE
    while arguments.read("--rescale") : rescaleOperation = RESCALE_TO_ZERO_TO_ONE_RANGE
    while arguments.read("--shift-min-to-zero") : rescaleOperation = SHIFT_MIN_TO_ZERO


    resizeToPowerOfTwo = False

    numComponentsDesired = 0
    while arguments.read("--num-components", numComponentsDesired) : 

    useManipulator = False
    while arguments.read("--manipulator")  or  arguments.read("-m") :  useManipulator = True 


    useShader = True
    while arguments.read("--shader") :  useShader = True 
    while arguments.read("--no-shader") :  useShader = False 

    gpuTransferFunction = True
    while arguments.read("--gpu-tf") :  gpuTransferFunction = True 
    while arguments.read("--cpu-tf") :  gpuTransferFunction = False 

    sampleDensityWhenMoving = 0.0
    while arguments.read("--sdwm", sampleDensityWhenMoving) : 

    while arguments.read("--lod") :  sampleDensityWhenMoving = 0.02 

    sequenceLength = 10.0
    while arguments.read("--sequence-duration", sequenceLength)  or 
          arguments.read("--sd", sequenceLength) : 

    typedef std.list< osg.Image > Images
    images = Images()


    vh_filename = str()
    while arguments.read("--vh", vh_filename) :
        str raw_filename, transfer_filename
        int xdim(0), ydim(0), zdim(0)

        header = osgDB.ifstream(vh_filename.c_str())
        if header :
            header >> raw_filename >> transfer_filename >> xdim >> ydim >> zdim >> xSize >> ySize >> zSize

        if xdim*ydim*zdim==0 :
            print "Error in reading volume header ", vh_filename
            return 1

        if  not raw_filename.empty() :
            images.push_back(readRaw(xdim, ydim, zdim, 1, 1, "little", raw_filename))

        if  not transfer_filename.empty() :
            fin = osgDB.ifstream(transfer_filename.c_str())
            if fin :
                colorMap = osg.TransferFunction1D.ColorMap()
                value = 0.0
                while fin  and  value<=1.0 :
                    float red, green, blue, alpha
                    fin >> red >> green >> blue >> alpha
                    if fin :
                        colorMap[value] = osg.Vec4(red/255.0,green/255.0,blue/255.0,alpha/255.0)
                        print "value = ", value, " (", red, ", ", green, ", ", blue, ", ", alpha, ")"
                        print "  (", colorMap[value], ")"
                    value += 1/255.0

                if colorMap.empty() :
                    print "Error: No values read from transfer function file: ", transfer_filename
                    return 0

                transferFunction = osg.TransferFunction1D()
                transferFunction.assign(colorMap)



    int sizeX, sizeY, sizeZ, numberBytesPerComponent, numberOfComponents
    str endian, raw_filename
    while arguments.read("--raw", sizeX, sizeY, sizeZ, numberBytesPerComponent, numberOfComponents, endian, raw_filename) :
        images.push_back(readRaw(sizeX, sizeY, sizeZ, numberBytesPerComponent, numberOfComponents, endian, raw_filename))

    images_pos = arguments.find("--images")
    if images_pos>=0 :
        imageList = osg.ImageList()
        pos = images_pos+1
        for(pos<arguments.argc()  and   not arguments.isOption(pos)++pos)
            arg = str(arguments[pos])
            if arg.find(ord("*"))  not = str.npos :
                contents = osgDB.expandWildcardsInFilename(arg)
                for (unsigned int i = 0 i < contents.size() ++i)
                    image = osgDB.readImageFile( contents[i] )

                    if image :
                        OSG_NOTICE, "Read osg.Image FileName.", image.getFileName(), ", pixelFormat=0x", std.hex, image.getPixelFormat(), std.dec, ", s=", image.s(), ", t=", image.t(), ", r=", image.r()
                        imageList.push_back(image)
            else:
                # not an option so assume string is a filename.
                image = osgDB.readImageFile( arguments[pos] )

                if image :
                    OSG_NOTICE, "Read osg.Image FileName.", image.getFileName(), ", pixelFormat=0x", std.hex, image.getPixelFormat(), std.dec, ", s=", image.s(), ", t=", image.t(), ", r=", image.r()
                    imageList.push_back(image)

        arguments.remove(images_pos, pos-images_pos)

        # pack the textures into a single texture.
        image = createTexture3D(imageList, numComponentsDesired, s_maximumTextureSize, t_maximumTextureSize, r_maximumTextureSize, resizeToPowerOfTwo)
        if image :
            images.push_back(image)
        else:
            OSG_NOTICE, "Unable to create 3D image from source files."


    # any option left unread are converted into errors to write out later.
    arguments.reportRemainingOptionsAsUnrecognized()

    # report any errors if they have occurred when parsing the program arguments.
    if arguments.errors() :
        arguments.writeErrorMessages(std.cout)
        return 1


    # assume remaining arguments are file names of textures.
    for(int pos=1pos<arguments.argc()++pos)
        if  not arguments.isOption(pos) :
            filename = arguments[pos]
            if osgDB.getLowerCaseFileExtension(filename)=="dicom" :
                # not an option so assume string is a filename.
                image = osgDB.readImageFile(filename)
                if image :
                    images.push_back(image)
            else:
                fileType = osgDB.fileType(filename)
                if fileType == osgDB.FILE_NOT_FOUND :
                    filename = osgDB.findDataFile(filename)
                    fileType = osgDB.fileType(filename)

                if fileType == osgDB.DIRECTORY :
                    image = osgDB.readImageFile(filename+".dicom")
                    if image : images.push_back(image)
                elif fileType == osgDB.REGULAR_FILE :
                    # not an option so assume string is a filename.
                    image = osgDB.readImageFile( filename )
                    if image : images.push_back(image)
                else:
                    osg.notify(osg.NOTICE), "Error: could not find file: ", filename
                    return 1

    if images.empty() :
        print "No model loaded, please specify a volumetric image file on the command line."
        return 1


    sizeItr = images.begin()
    image_s = (*sizeItr).s()
    image_t = (*sizeItr).t()
    image_r = (*sizeItr).r()
    ++sizeItr

    for(sizeItr  not = images.end() ++sizeItr)
        if *sizeItr :.s()  not = image_s  or 
            (*sizeItr).t()  not = image_t  or 
            (*sizeItr).r()  not = image_r :
            print "Images in sequence are not of the same dimensions."
            return 1


    details = dynamic_cast<osgVolume.ImageDetails*>(images.front().getUserData())
    matrix =  details.getMatrix() : dynamic_cast<osg: if (details) else RefMatrix*>(images.front().getUserData())

    if  not matrix :
        if xSize==0.0 : xSize = static_cast<float>(image_s)
        if ySize==0.0 : ySize = static_cast<float>(image_t)
        if zSize==0.0 : zSize = static_cast<float>(image_r)

        matrix = osg.RefMatrix(xSize, 0.0,   0.0,   0.0,
                                    0.0,   ySize, 0.0,   0.0,
                                    0.0,   0.0,   zSize, 0.0,
                                    0.0,   0.0,   0.0,   1.0)


    if xMultiplier not =1.0  or  yMultiplier not =1.0  or  zMultiplier not =1.0 :
        matrix.postMultScale(osg.Vec3d(fabs(xMultiplier), fabs(yMultiplier), fabs(zMultiplier)))

    minValue = osg.Vec4(FLT_MAX, FLT_MAX, FLT_MAX, FLT_MAX)
    maxValue = osg.Vec4(-FLT_MAX, -FLT_MAX, -FLT_MAX, -FLT_MAX)
    computeMinMax = False
    for(Images.iterator itr = images.begin()
        not = images.end()
        ++itr)
        osg.Vec4 localMinValue, localMaxValue
        if osg.computeMinMax(itr, localMinValue, localMaxValue) :
            if localMinValue.r()<minValue.r() : minValue.r() = localMinValue.r()
            if localMinValue.g()<minValue.g() : minValue.g() = localMinValue.g()
            if localMinValue.b()<minValue.b() : minValue.b() = localMinValue.b()
            if localMinValue.a()<minValue.a() : minValue.a() = localMinValue.a()

            if localMaxValue.r()>maxValue.r() : maxValue.r() = localMaxValue.r()
            if localMaxValue.g()>maxValue.g() : maxValue.g() = localMaxValue.g()
            if localMaxValue.b()>maxValue.b() : maxValue.b() = localMaxValue.b()
            if localMaxValue.a()>maxValue.a() : maxValue.a() = localMaxValue.a()

            osg.notify(osg.NOTICE), "  (", localMinValue, ") (", localMaxValue, ") ", (*itr).getFileName()

            computeMinMax = True

    if computeMinMax :
        osg.notify(osg.NOTICE), "Min value ", minValue
        osg.notify(osg.NOTICE), "Max value ", maxValue

        minComponent = minValue[0]
        minComponent = osg.minimum(minComponent,minValue[1])
        minComponent = osg.minimum(minComponent,minValue[2])
        minComponent = osg.minimum(minComponent,minValue[3])

        maxComponent = maxValue[0]
        maxComponent = osg.maximum(maxComponent,maxValue[1])
        maxComponent = osg.maximum(maxComponent,maxValue[2])
        maxComponent = osg.maximum(maxComponent,maxValue[3])

#if 0
        switch(rescaleOperation)
            case(NO_RESCALE):
                break

            case(RESCALE_TO_ZERO_TO_ONE_RANGE):
                scale = 0.99/(maxComponent-minComponent)
                offset = -minComponent * scale

                for(Images.iterator itr = images.begin()
                    not = images.end()
                    ++itr)
                    osg.offsetAndScaleImage(itr,
                        osg.Vec4(offset, offset, offset, offset),
                        osg.Vec4(scale, scale, scale, scale))
                break
            case(SHIFT_MIN_TO_ZERO):
                offset = -minComponent

                for(Images.iterator itr = images.begin()
                    not = images.end()
                    ++itr)
                    osg.offsetAndScaleImage(itr,
                        osg.Vec4(offset, offset, offset, offset),
                        osg.Vec4(1.0, 1.0, 1.0, 1.0))
                break
        
#endif


    if colourSpaceOperation not =osg.NO_COLOR_SPACE_OPERATION :
        for(Images.iterator itr = images.begin()
            not = images.end()
            ++itr)
            (*itr) = osg.colorSpaceConversion(colourSpaceOperation, itr, colourModulate)

    if  not gpuTransferFunction  and  transferFunction.valid() :
        for(Images.iterator itr = images.begin()
            not = images.end()
            ++itr)
            *itr = osgVolume.applyTransferFunction(itr, transferFunction)

    image_3d = 0

    if images.size()==1 :
        osg.notify(osg.NOTICE), "Single image ", images.size(), " volumes."
        image_3d = images.front()
    else:
        osg.notify(osg.NOTICE), "Creating sequence of ", images.size(), " volumes."

        imageSequence = osg.ImageSequence()
        imageSequence.setLength(sequenceLength)
        image_3d = imageSequence
        for(Images.iterator itr = images.begin()
            not = images.end()
            ++itr)
            imageSequence.addImage(itr)
        imageSequence.play()

    volume = osgVolume.Volume()
    tile = osgVolume.VolumeTile()
    volume.addChild(tile)

    layer = osgVolume.ImageLayer(image_3d)

    if details :
        layer.setTexelOffset(details.getTexelOffset())
        layer.setTexelScale(details.getTexelScale())

    switch(rescaleOperation)
        case(NO_RESCALE):
            break

        case(RESCALE_TO_ZERO_TO_ONE_RANGE):
            layer.rescaleToZeroToOneRange()
            break
        case(SHIFT_MIN_TO_ZERO):
            layer.translateMinToZero()
            break
    

    if xMultiplier<0.0  or  yMultiplier<0.0  or  zMultiplier<0.0 :
        layer.setLocator(osgVolume.Locator(
             -1.0 : 0.0, yMultiplier<0.0 ? -1.0 : 0.0, zMultiplier<0.0 ? -1.0 if (osg.Matrix.translate(xMultiplier<0.0) else  0.0) *
             -1.0 : 1.0, yMultiplier<0.0 ? -1.0 : 1.0, zMultiplier<0.0 ? -1.0 if (osg.Matrix.scale(xMultiplier<0.0) else  1.0) *
            (*matrix)
            ))
    else:
        layer.setLocator(osgVolume.Locator(*matrix))
    tile.setLocator(osgVolume.Locator(*matrix))

    tile.setLayer(layer)

    tile.setEventCallback(osgVolume.PropertyAdjustmentCallback())

    if useShader :

        sp = osgVolume.SwitchProperty()
        sp.setActiveProperty(0)

        ap = osgVolume.AlphaFuncProperty(alphaFunc)
        sd = osgVolume.SampleDensityProperty(0.005)
        sdwm = sampleDensityWhenMoving not  osgVolume.SampleDensityWhenMovingProperty(sampleDensityWhenMoving) if (=0.0) else  0
        tp = osgVolume.TransparencyProperty(1.0)
        tfp =  osgVolume.TransferFunctionProperty(transferFunction) if (transferFunction.valid()) else  0

            # Standard
            cp = osgVolume.CompositeProperty()
            cp.addProperty(ap)
            cp.addProperty(sd)
            cp.addProperty(tp)
            if sdwm : cp.addProperty(sdwm)
            if tfp : cp.addProperty(tfp)

            sp.addProperty(cp)

            # Light
            cp = osgVolume.CompositeProperty()
            cp.addProperty(ap)
            cp.addProperty(sd)
            cp.addProperty(tp)
            cp.addProperty(osgVolume.LightingProperty)()
            if sdwm : cp.addProperty(sdwm)
            if tfp : cp.addProperty(tfp)

            sp.addProperty(cp)

            # Isosurface
            cp = osgVolume.CompositeProperty()
            cp.addProperty(sd)
            cp.addProperty(tp)
            cp.addProperty(osgVolume.IsoSurfaceProperty(alphaFunc))
            if sdwm : cp.addProperty(sdwm)
            if tfp : cp.addProperty(tfp)

            sp.addProperty(cp)

            # MaximumIntensityProjection
            cp = osgVolume.CompositeProperty()
            cp.addProperty(ap)
            cp.addProperty(sd)
            cp.addProperty(tp)
            cp.addProperty(osgVolume.MaximumIntensityProjectionProperty)()
            if sdwm : cp.addProperty(sdwm)
            if tfp : cp.addProperty(tfp)

            sp.addProperty(cp)

        switch(shadingModel)
            case(Standard):                     sp.setActiveProperty(0) break
            case(Light):                        sp.setActiveProperty(1) break
            case(Isosurface):                   sp.setActiveProperty(2) break
            case(MaximumIntensityProjection):   sp.setActiveProperty(3) break
        layer.addProperty(sp)


        tile.setVolumeTechnique(osgVolume.RayTracedTechnique)()
    else:
        layer.addProperty(osgVolume.AlphaFuncProperty(alphaFunc))
        tile.setVolumeTechnique(osgVolume.FixedFunctionTechnique)()

    if  not outputFile.empty() :
        ext = osgDB.getFileExtension(outputFile)
        name_no_ext = osgDB.getNameLessExtension(outputFile)
        if ext=="osg"  or  ext=="osgt"  or  ext=="osgx"  :
            if image_3d.valid() :
                image_3d.setFileName(name_no_ext + ".dds")
                options = osgDB.Options("ddsNoAutoFlipWrite")
                osgDB.writeImageFile(*image_3d, image_3d.getFileName(), options)
            osgDB.writeNodeFile(*volume, outputFile)
        elif ext=="ive"  or  ext=="osgb"  :
            osgDB.writeNodeFile(*volume, outputFile)
        elif ext=="dds" :
            osgDB.writeImageFile(*image_3d, outputFile)
        else:
            print "Extension not support for file output, not file written."

        return 0

    if volume.valid() :

        loadedModel = volume

        if useManipulator :
            group = osg.Group()

#if 1
            dragger = osgManipulator.TabBoxDragger()
#else:
            dragger = osgManipulator.TrackballDragger()
#endif
            dragger.setupDefaultGeometry()
            dragger.setHandleEvents(True)
            dragger.setActivationModKeyMask(osgGA.GUIEventAdapter.MODKEY_SHIFT)
            dragger.addDraggerCallback(DraggerVolumeTileCallback(tile, tile.getLocator()))
            dragger.setMatrix(osg.Matrix.translate(0.5,0.5,0.5)*tile.getLocator().getTransform())


            group.addChild(dragger)

            #dragger.addChild(volume)

            group.addChild(volume)

            loadedModel = group


        # set the scene to render
        viewer.setSceneData(loadedModel)

        # the the viewers main frame loop
        viewer.run()

    return 0


if __name__ == "__main__":
    main(sys.argv)
