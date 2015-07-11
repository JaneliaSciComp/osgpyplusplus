#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgphotoalbum"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import OpenThreads
from osgpypp import osg
from osgpypp import osgDB
from osgpypp import osgText
from osgpypp import osgUtil
from osgpypp import osgViewer


# Translated from file 'ImageReaderWriter.cpp'

# OpenSceneGraph example, osgphotoalbum.
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


#include "ImageReaderWriter.h"

#include <osg/Texture2D>
#include <osg/Geometry>
#include <osg/Geode>

#include <sstream>


ImageReaderWriter.DataReference.DataReference():
    _fileName(),
    _resolutionX(256),
    _resolutionY(256),
    _center(0.625,0.0,0.0),
    _maximumWidth(1.25,0.0,0.0),
    _maximumHeight(0.0,0.0,1.0),
    _numPointsAcross(10),
    _numPointsUp(10),
    _backPage(False) 

ImageReaderWriter.DataReference.DataReference( str fileName, unsigned int res, float width, float height,bool backPage):
    _fileName(fileName),
    _resolutionX(res),
    _resolutionY(res),
    _center(width*0.5,0.0,height*0.5),
    _maximumWidth(width,0.0,0.0),
    _maximumHeight(0.0,0.0,height),
    _numPointsAcross(10),
    _numPointsUp(10),
    _backPage(backPage) 

ImageReaderWriter.DataReference.DataReference( DataReference rhs):
    _fileName(rhs._fileName),
    _resolutionX(rhs._resolutionX),
    _resolutionY(rhs._resolutionY),
    _center(rhs._center),
    _maximumWidth(rhs._maximumWidth),
    _maximumHeight(rhs._maximumHeight),
    _numPointsAcross(rhs._numPointsAcross),
    _numPointsUp(rhs._numPointsUp),
    _backPage(rhs._backPage) 



ImageReaderWriter.ImageReaderWriter()

str ImageReaderWriter.local_insertReference( str fileName, unsigned int res, float width, float height, bool backPage)
    ostr = strstream()
    ostr, "res_", res, "_", fileName

    myReference = ostr.str()
    _dataReferences[myReference] = DataReference(fileName,res,width,height,backPage)
    return myReference

osg.Image* ImageReaderWriter.readImage_Archive(DataReference dr, float s,float t)
    for(PhotoArchiveList.iterator itr=_photoArchiveList.begin()
        itr!=_photoArchiveList.end()
        ++itr)
        image = (*itr).readImage(dr._fileName,dr._resolutionX,dr._resolutionY,s,t)
        if image : return image
    return 0

osg.Image* ImageReaderWriter.readImage_DynamicSampling(DataReference dr, float s,float t)

    # record previous options.
    previousOptions = osgDB.Registry.instance().getOptions()

    options = osgDB.ImageOptions()
    options._destinationImageWindowMode = osgDB.ImageOptions.PIXEL_WINDOW
    options._destinationPixelWindow.set(0,0,dr._resolutionX,dr._resolutionY)

    osgDB.Registry.instance().setOptions(options.get())

    image = osgDB.readImageFile(dr._fileName)

    # restore previous options.
    osgDB.Registry.instance().setOptions(previousOptions.get())

    s = options.valid()?options._sourcePixelWindow.windowWidth:1.0
    t = options.valid()?options._sourcePixelWindow.windowHeight:1.0

    return image



osgDB.ReaderWriter.ReadResult ImageReaderWriter.local_readNode( str fileName,  Options*)
    itr = _dataReferences.find(fileName)
    if itr==_dataReferences.end() : return osgDB.ReaderWriter.ReadResult.FILE_NOT_HANDLED

    dr = itr.second

    image = 0
    s = 1.0,t=1.0

    # try to load photo from any loaded PhotoArchives
    if !_photoArchiveList.empty() :
        image = readImage_Archive(dr,s,t)

    # not loaded yet, so try to load it directly.
    if !image :
        image = readImage_DynamicSampling(dr,s,t)


    if image :


        photoWidth = 0.0
        photoHeight = 0.0
        maxWidth = dr._maximumWidth.length()
        maxHeight = dr._maximumHeight.length()


        if s/t :>(maxWidth/maxHeight) :
            # photo wider than tall relative to the required pictures size.
            # so need to clamp the width to the maximum width and then
            # set the height to keep the original photo aspect ratio.

            photoWidth = maxWidth
            photoHeight = photoWidth*(t/s)
        else :
            # photo tall than wide relative to the required pictures size.
            # so need to clamp the height to the maximum height and then
            # set the width to keep the original photo aspect ratio.

            photoHeight = maxHeight
            photoWidth = photoHeight*(s/t)

        photoWidth*=0.95
        photoHeight*=0.95

        halfWidthVector = osg.Vec3(dr._maximumWidth*(photoWidth*0.5/maxWidth))
        halfHeightVector = osg.Vec3(dr._maximumHeight*(photoHeight*0.5/maxHeight))


        # set up the texture.
        texture = osg.Texture2D()
        texture.setImage(image)
        texture.setResizeNonPowerOfTwoHint(False)
        texture.setFilter(osg.Texture.MIN_FILTER,osg.Texture.LINEAR)
        texture.setFilter(osg.Texture.MAG_FILTER,osg.Texture.LINEAR)

        # set up the drawstate.
        dstate = osg.StateSet()
        dstate.setMode(GL_LIGHTING,osg.StateAttribute.OFF)
        dstate.setTextureAttributeAndModes(0, texture,osg.StateAttribute.ON)

        # set up the geoset.
        geom = osg.Geometry()
        geom.setStateSet(dstate)

        coords = osg.Vec3Array(4)

        if !dr._backPage :
            (*coords)[0] = dr._center - halfWidthVector + halfHeightVector
            (*coords)[1] = dr._center - halfWidthVector - halfHeightVector
            (*coords)[2] = dr._center + halfWidthVector - halfHeightVector
            (*coords)[3] = dr._center + halfWidthVector + halfHeightVector
        else :
            (*coords)[3] = dr._center - halfWidthVector + halfHeightVector
            (*coords)[2] = dr._center - halfWidthVector - halfHeightVector
            (*coords)[1] = dr._center + halfWidthVector - halfHeightVector
            (*coords)[0] = dr._center + halfWidthVector + halfHeightVector
        geom.setVertexArray(coords)

        tcoords = osg.Vec2Array(4)
        (*tcoords)[0].set(0.0,1.0)
        (*tcoords)[1].set(0.0,0.0)
        (*tcoords)[2].set(1.0,0.0)
        (*tcoords)[3].set(1.0,1.0)
        geom.setTexCoordArray(0,tcoords)

        colours = osg.Vec4Array(1)
        (*colours)[0].set(1.0,1.0,1.0,1.0)
        geom.setColorArray(colours, osg.Array.BIND_OVERALL)

        geom.addPrimitiveSet(osg.DrawArrays(osg.PrimitiveSet.QUADS,0,4))

        # set up the geode.
        geode = osg.Geode()
        geode.addDrawable(geom)

        return geode

    else :
        return osgDB.ReaderWriter.ReadResult.FILE_NOT_HANDLED



# Translated from file 'ImageReaderWriter.h'

# -*-c++-*- 
#*
#*  OpenSceneGraph example, osgphotoalbum.
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

#ifndef IMAGEREADERWRITER_H
#define IMAGEREADERWRITER_H

#include <osgDB/ReadFile>
#include <osgDB/WriteFile>
#include <osgDB/ImageOptions>

#include <OpenThreads/ScopedLock>
#include <OpenThreads/ReentrantMutex>

#include "PhotoArchive.h"

#define SERIALIZER() OpenThreads.ScopedLock<OpenThreads.ReentrantMutex> lock(_serializerMutex)  

class ImageReaderWriter (osgDB.ReaderWriter) :
        
        ImageReaderWriter()
        
        def className():
        
             return "ImageReader" 

        def addPhotoArchive(archive):

             _photoArchiveList.push_back(archive) 

        def insertReference(fileName, res, width, height, backPage):

            
            SERIALIZER()
            return const_cast<ImageReaderWriter*>(this).local_insertReference(fileName, res, width, height, backPage)

        def readNode(fileName, options):

            
            SERIALIZER()
            return const_cast<ImageReaderWriter*>(this).local_readNode(fileName, options)

        local_insertReference = str( str fileName, unsigned int res, float width, float height, bool backPage)

        local_readNode = ReadResult( str fileName,  Options*)

        mutable OpenThreads.ReentrantMutex _serializerMutex

        class DataReference :
DataReference()
            DataReference( str fileName, unsigned int res, float width, float height,bool backPage)
            DataReference( DataReference rhs)

            _fileName = str()
            _resolutionX = unsigned int()
            _resolutionY = unsigned int()
            _center = osg.Vec3()
            _maximumWidth = osg.Vec3() 
            _maximumHeight = osg.Vec3()
            _numPointsAcross = unsigned int() 
            _numPointsUp = unsigned int()
            _backPage = bool()
        
        
        readImage_Archive = osg.Image*(DataReference dr, float s,float t)
        
        readImage_DynamicSampling = osg.Image*(DataReference dr, float s,float t)

        typedef std.map< str,DataReference > DataReferenceMap
        typedef std.vector< PhotoArchive > PhotoArchiveList

        _dataReferences = DataReferenceMap()
        _photoArchiveList = PhotoArchiveList()




#endif

# Translated from file 'osgphotoalbum.cpp'

# OpenSceneGraph example, osgphotoalbum.
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
#include <osg/MatrixTransform>
#include <osg/Switch>
#include <osg/PolygonOffset>
#include <osg/CullFace>

#include <osgUtil/Optimizer>

#include <osgDB/FileNameUtils>

#include <osgText/Text>

#include <osgViewer/Viewer>

#include "ImageReaderWriter.h"

#include <iostream>

using namespace osg

# now register with Registry to instantiate the above reader/writer,
# declaring in main so that the code to set up PagedLOD can get a handle
# to the ImageReaderWriter's
g_ImageReaderWriter = osgDB.RegisterReaderWriterProxy<ImageReaderWriter>()

Album = class()

class Page (osg.Transform) :


    static Page* createPage(Album* album, unsigned int pageNo,  str frontFileName,  str backFileName, float width, float height)
        page = Page(album, pageNo, frontFileName, backFileName, width, height)
        if page.valid() : return page.release()
        else : return 0

    traverse = virtual void(osg.NodeVisitor nv)

    def setRotation(angle):

        
        _rotation = angle
        _targetRotation = angle
        dirtyBound()

    def getRotation():

         return _rotation 

    def rotateTo(angle, timeToRotateBy):

        
        _targetRotation = angle
        _targetTime = timeToRotateBy

    def rotating():

         return _targetRotation!=_rotation 

    def setPageVisible(frontVisible, backVisible):

        
        _switch.setValue(0,!frontVisible  !backVisible)
        _switch.setValue(1,frontVisible)
        _switch.setValue(2,backVisible)

    def getSwitch():

         return _switch.get() 
    def getSwitch():
         return _switch.get() 

    virtual bool computeLocalToWorldMatrix(osg.Matrix matrix,osg.NodeVisitor*) 
        if _referenceFrame==RELATIVE_RF :
            matrix.preMult(getMatrix())
        else : # absolute
            matrix = getMatrix()
        return True

    #* Get the transformation matrix which moves from world coords to local coords.
    virtual bool computeWorldToLocalMatrix(osg.Matrix matrix,osg.NodeVisitor*) 
        inverse = getInverseMatrix()

        if _referenceFrame==RELATIVE_RF :
            matrix.postMult(inverse)
        else : # absolute
            matrix = inverse
        return True

    def getMatrix():

         return _pageOffset*osg.Matrix.rotate(-_rotation,0.0,0.0,1.0) 
    def getInverseMatrix():
         return osg.Matrix.inverse(getMatrix()) 

    Page(Album* album, unsigned int pageNo,  str frontFileName,  str backFileName, float width, float height)

    _rotation = float()
    _pageOffset = osg.Matrix()

    _targetRotation = float()
    _targetTime = float()
    _lastTimeTraverse = float()

    _switch = osg.Switch()




class Album (osg.Referenced) :

    Album(osg.ArgumentParser ap, float width, float height)

    def getScene():

         return _group.get() 

    def getScene():

         return _group.get() 

    osg.Matrix getPageOffset(unsigned int pageNo) 

    def nextPage(timeToRotateBy):

         gotoPage = return(_currentPageNo+1,timeToRotateBy) 

    def previousPage(timeToRotateBy):

         return _currentPageNo>=1?gotoPage(_currentPageNo-1,timeToRotateBy):False 

    gotoPage = bool(unsigned int pageNo, float timeToRotateBy)

    def getBackgroundStateSet():

         return _backgroundStateSet.get() 

    setVisibility = void()

    typedef std.vector< Page > PageList

    _group = osg.Group()
    _pages = PageList()

    _backgroundStateSet = osg.StateSet()

    _currentPageNo = unsigned int()
    _radiusOfRings = float()
    _startAngleOfPages = float()
    _deltaAngleBetweenPages = float()




##############################################################


Page.Page(Album* album, unsigned int pageNo,  str frontFileName,  str backFileName, float width, float height)
    # set up transform parts.
    _rotation = 0
    _targetRotation = 0
    _targetTime = 0
    _lastTimeTraverse = 0

    _pageOffset = album.getPageOffset(pageNo)

    setNumChildrenRequiringUpdateTraversal(1)


    # set up subgraph
    readerWriter = osgDB.Registry.instance().getReaderWriterForExtension("gdal")
    if !readerWriter :
        print "Error: GDAL plugin not available, cannot preceed with database creation"

    _switch = osg.Switch()

    rw = g_ImageReaderWriter.get()


    # set up non visible page.
    non_visible_page = osg.Group()
    _switch.addChild(non_visible_page)
        geom = osg.Geometry()
        geom.setStateSet(album.getBackgroundStateSet())

        coords = osg.Vec3Array(8)
        (*coords)[0].set(0.0,0.0,0.0)
        (*coords)[1].set(0.0,0.0,height)
        (*coords)[2].set(0.0,0.0,height)
        (*coords)[3].set(width,0.0,height)
        (*coords)[4].set(width,0.0,height)
        (*coords)[5].set(width,0.0,0.0)
        (*coords)[6].set(width,0.0,0.0)
        (*coords)[7].set(0.0,0.0,0.0)
        geom.setVertexArray(coords)


        normals = osg.Vec3Array(8)
        (*normals)[0].set(-1.0,0.0,0.0)
        (*normals)[1].set(-1.0,0.0,0.0)
        (*normals)[2].set(0.0,0.0,-1.0)
        (*normals)[3].set(0.0,0.0,-1.0)
        (*normals)[4].set(1.0,0.0,0.0)
        (*normals)[5].set(1.0,0.0,0.0)
        (*normals)[6].set(0.0,0.0,1.0)
        (*normals)[7].set(0.0,0.0,1.0)
        geom.setNormalArray(normals, osg.Array.BIND_PER_VERTEX)

        tcoords = osg.Vec2Array(8)
        (*tcoords)[0].set(0.0,0.0)
        (*tcoords)[1].set(0.0,1.0)
        (*tcoords)[2].set(0.0,1.0)
        (*tcoords)[3].set(1.0,1.0)
        (*tcoords)[4].set(1.0,1.0)
        (*tcoords)[5].set(0.0,1.0)
        (*tcoords)[6].set(0.0,1.0)
        (*tcoords)[7].set(0.0,0.0)
        geom.setTexCoordArray(0,tcoords)

        colours = osg.Vec4Array(1)
        (*colours)[0].set(1.0,1.0,1.0,1.0)
        geom.setColorArray(colours, osg.Array.BIND_OVERALL)

        geom.addPrimitiveSet(osg.DrawArrays(osg.PrimitiveSet.LINES,0,8))

        # set up the geode.
        geode = osg.Geode()
        geode.addDrawable(geom)


        non_visible_page.addChild(geode)


    # set up visible page.
    front_page = osg.Group()
    _switch.addChild(front_page)


        geom = osg.Geometry()
        geom.setStateSet(album.getBackgroundStateSet())

        coords = osg.Vec3Array(4)
        (*coords)[0].set(0.0,0.0,height)
        (*coords)[1].set(0.0,0.0,0)
        (*coords)[2].set(width,0.0,0)
        (*coords)[3].set(width,0.0,height)
        geom.setVertexArray(coords)

        normals = osg.Vec3Array(1)
        (*normals)[0].set(0.0,-1.0,0.0)
        geom.setNormalArray(normals, osg.Array.BIND_OVERALL)

        tcoords = osg.Vec2Array(4)
        (*tcoords)[0].set(0.0,1.0)
        (*tcoords)[1].set(0.0,0.0)
        (*tcoords)[2].set(1.0,0.0)
        (*tcoords)[3].set(1.0,1.0)
        geom.setTexCoordArray(0,tcoords)

        colours = osg.Vec4Array(1)
        (*colours)[0].set(1.0,1.0,1.0,1.0)
        geom.setColorArray(colours, osg.Array.BIND_OVERALL)

        geom.addPrimitiveSet(osg.DrawArrays(osg.PrimitiveSet.QUADS,0,4))

        # set up the geode.
        geode = osg.Geode()
        geode.addDrawable(geom)


        front_page.addChild(geode)

    if !frontFileName.empty() :
        cut_off_distance = 8.0
        max_visible_distance = 300.0

        center = osg.Vec3(width*0.5,0.0,height*0.5)

        text = osgText.Text()
        text.setFont("fonts/arial.ttf")
        text.setPosition(center)
        text.setCharacterSize(height/20.0)
        text.setAlignment(osgText.Text.CENTER_CENTER)
        text.setAxisAlignment(osgText.Text.XZ_PLANE)
        text.setColor(osg.Vec4(1.0,1.0,0.0,1.0))
        text.setText(str("Loading ")+frontFileName)

        geode = osg.Geode()
        geode.addDrawable(text)

        pagedlod = osg.PagedLOD()
        pagedlod.setCenter(center)
        pagedlod.setRadius(1.6)
        pagedlod.setNumChildrenThatCannotBeExpired(2)

        pagedlod.setRange(0,max_visible_distance,1e7)
        pagedlod.addChild(geode)

        pagedlod.setRange(1,cut_off_distance,max_visible_distance)
        pagedlod.setFileName(1,rw.insertReference(frontFileName,256,width,height,False))

        pagedlod.setRange(2,0.0,cut_off_distance)
        pagedlod.setFileName(2,rw.insertReference(frontFileName,1024,width,height,False))

        front_page.addChild(pagedlod)


    # set up back of page.
    back_page = osg.Group()
    _switch.addChild(back_page)


        geom = osg.Geometry()
        geom.setStateSet(album.getBackgroundStateSet())

        coords = osg.Vec3Array(4)
        (*coords)[0].set(width,0.0,height)
        (*coords)[1].set(width,0.0,0)
        (*coords)[2].set(0.0,0.0,0)
        (*coords)[3].set(0.0,0.0,height)
        geom.setVertexArray(coords)

        normals = osg.Vec3Array(1)
        (*normals)[0].set(0.0,1.0,0.0)
        geom.setNormalArray(normals, osg.Array.BIND_OVERALL)

        tcoords = osg.Vec2Array(4)
        (*tcoords)[0].set(1.0,1.0)
        (*tcoords)[1].set(1.0,0.0)
        (*tcoords)[2].set(0.0,0.0)
        (*tcoords)[3].set(0.0,1.0)
        geom.setTexCoordArray(0,tcoords)

        colours = osg.Vec4Array(1)
        (*colours)[0].set(1.0,1.0,1.0,1.0)
        geom.setColorArray(colours, osg.Array.BIND_OVERALL)

        geom.addPrimitiveSet(osg.DrawArrays(osg.PrimitiveSet.QUADS,0,4))

        # set up the geode.
        geode = osg.Geode()
        geode.addDrawable(geom)


        back_page.addChild(geode)

    if !backFileName.empty() :
        cut_off_distance = 8.0
        max_visible_distance = 300.0

        center = osg.Vec3(width*0.5,0.0,height*0.5)

        text = osgText.Text()
        text.setFont("fonts/arial.ttf")
        text.setPosition(center)
        text.setCharacterSize(height/20.0)
        text.setAlignment(osgText.Text.CENTER_CENTER)
        text.setAxisAlignment(osgText.Text.REVERSED_XZ_PLANE)
        text.setColor(osg.Vec4(1.0,1.0,0.0,1.0))
        text.setText(str("Loading ")+backFileName)

        geode = osg.Geode()
        geode.addDrawable(text)

        pagedlod = osg.PagedLOD()
        pagedlod.setCenter(center)
        pagedlod.setRadius(1.6)
        pagedlod.setNumChildrenThatCannotBeExpired(2)

        pagedlod.setRange(0,max_visible_distance,1e7)
        pagedlod.addChild(geode)

        pagedlod.setRange(1,cut_off_distance,max_visible_distance)
        pagedlod.setFileName(1,rw.insertReference(backFileName,256,width,height,True))

        pagedlod.setRange(2,0.0,cut_off_distance)
        pagedlod.setFileName(2,rw.insertReference(backFileName,1024,width,height,True))

        back_page.addChild(pagedlod)

    addChild(_switch.get())

void Page.traverse(osg.NodeVisitor nv)
    # if app traversal update the frame count.
    if nv.getVisitorType()==osg.NodeVisitor.UPDATE_VISITOR :
        framestamp = nv.getFrameStamp()
        if framestamp :
            t = framestamp.getSimulationTime()

            if _rotation!=_targetRotation :
                if t>=_targetTime : _rotation = _targetRotation
                else : _rotation += (_targetRotation-_rotation)*(t-_lastTimeTraverse)/(_targetTime-_lastTimeTraverse)

                dirtyBound()

            _lastTimeTraverse = t

    Transform.traverse(nv)


##############################################################

Album.Album(osg.ArgumentParser arguments, float width, float height)


    typedef std.vector<str> FileList
    fileList = FileList()

    for(int pos=1pos<arguments.argc()++pos)
        if arguments.isString(pos) :
            filename = str(arguments[pos])
            if osgDB.getLowerCaseFileExtension(filename)=="album" :
                photoArchive = PhotoArchive.open(filename)
                if photoArchive :
                    g_ImageReaderWriter.get().addPhotoArchive(photoArchive)
                    photoArchive.getImageFileNameList(fileList)

            else :
                fileList.push_back(arguments[pos])

    _radiusOfRings = 0.02
    _startAngleOfPages = 0.0
    _deltaAngleBetweenPages = osg.PI/(float)fileList.size()

    _group = osg.Group()
    _group.getOrCreateStateSet().setAttributeAndModes(osg.CullFace,osg.StateAttribute.ON)()

    _backgroundStateSet = osg.StateSet()
    _backgroundStateSet.setAttributeAndModes(osg.PolygonOffset(1.0,1.0),osg.StateAttribute.ON)

    # load the images.
    i = unsigned int()
    for(i=0i<fileList.size()i+=2)
        page = i+1<fileList.size()?
                     Page.createPage(this,_pages.size(),fileList[i],fileList[i+1], width, height):
                     Page.createPage(this,_pages.size(),fileList[i],"", width, height)
        if page :
            _pages.push_back(page)
            _group.addChild(page)

    setVisibility()


osg.Matrix Album.getPageOffset(unsigned int pageNo) 
    angleForPage = _startAngleOfPages+_deltaAngleBetweenPages*(float)pageNo
    delta = osg.Vec3(_radiusOfRings*sinf(angleForPage),-_radiusOfRings*cosf(angleForPage),0.0)
    return osg.Matrix.translate(delta)

bool Album.gotoPage(unsigned int pageNo, float timeToRotateBy)
    if pageNo>=_pages.size() : return False

    if pageNo>_currentPageNo :
        for(unsigned int i=_currentPageNoi<pageNo++i)
            _pages[i].rotateTo(osg.PI,timeToRotateBy)
        _currentPageNo = pageNo

        return True
    elif pageNo<_currentPageNo :
        for(unsigned int i=pageNoi<_currentPageNo++i)
            _pages[i].rotateTo(0,timeToRotateBy)
        _currentPageNo = pageNo

        return True

    return False

void Album.setVisibility()
    for(unsigned int i=0i<_pages.size()++i)
        front_visible = _pages[i].rotating() ||
                             (i>0?_pages[i-1].rotating():False) ||
                             i==_currentPageNo ||
                             i==0

        back_visible = _pages[i].rotating() ||
                            ((i+1)<_pages.size()?_pages[i+1].rotating():False) ||
                            i==_currentPageNo-1 ||
                            i==_pages.size()-1

        _pages[i].setPageVisible(front_visible,back_visible)



##############################################################


class SlideEventHandler (osgGA.GUIEventHandler) :

    SlideEventHandler()

    META_Object(osgStereImageApp,SlideEventHandler)

    set = void(Album* album, float timePerSlide, bool autoSteppingActive)

    handle = virtual bool( osgGA.GUIEventAdapter ea,osgGA.GUIActionAdapter)

    virtual void getUsage(osg.ApplicationUsage usage) 

    ~SlideEventHandler() 
    SlideEventHandler( SlideEventHandler, osg.CopyOp) 

    _album = Album()
    _firstTraversal = bool()
    _previousTime = double()
    _timePerSlide = double()
    _autoSteppingActive = bool()


SlideEventHandler.SlideEventHandler():
    _album(0),
    _firstTraversal(True),
    _previousTime(-1.0),
    _timePerSlide(5.0),
    _autoSteppingActive(False)

void SlideEventHandler.set(Album* album, float timePerSlide, bool autoSteppingActive)
    _album = album

    _timePerSlide = timePerSlide
    _autoSteppingActive = autoSteppingActive


bool SlideEventHandler.handle( osgGA.GUIEventAdapter ea,osgGA.GUIActionAdapter)
    switch(ea.getEventType())
        case(osgGA.GUIEventAdapter.KEYDOWN):
            if ea.getKey()=='a' :
                _autoSteppingActive = !_autoSteppingActive
                _previousTime = ea.getTime()
                return True
            elif ea.getKey()=='n' :
                _album.nextPage(ea.getTime()+1.0)
                return True
            elif ea.getKey()=='p' :
                _album.previousPage(ea.getTime()+1.0)
                return True
            return False
        case(osgGA.GUIEventAdapter.FRAME):
            if _autoSteppingActive :
                if _firstTraversal :
                    _firstTraversal = False
                    _previousTime = ea.getTime()
                elif ea.getTime()-_previousTime>_timePerSlide :
                    _previousTime = ea.getTime()

                    _album.nextPage(ea.getTime()+1.0)

            _album.setVisibility()


        default:
            return False

void SlideEventHandler.getUsage(osg.ApplicationUsage usage) 
    usage.addKeyboardMouseBinding("Space","Reset the image position to center")
    usage.addKeyboardMouseBinding("a","Toggle on/off the automatic advancement for image to image")
    usage.addKeyboardMouseBinding("n","Advance to next image")
    usage.addKeyboardMouseBinding("p","Move to previous image")

def main(argc, argv):

    

    # use an ArgumentParser object to manage the program arguments.
    arguments = osg.ArgumentParser(argc,argv)

    # set up the usage document, in case we need to print out how to use this program.
    arguments.getApplicationUsage().setDescription(arguments.getApplicationName()+" is the example which demonstrates use node masks to create stereo images.")
    arguments.getApplicationUsage().setCommandLineUsage(arguments.getApplicationName()+" [options] image_file [image_file]")
    arguments.getApplicationUsage().addCommandLineOption("-d <float>","Time delay in seconds between the display of successive image pairs when in auto advance mode.")
    arguments.getApplicationUsage().addCommandLineOption("-a","Enter auto advance of image pairs on start up.")
    arguments.getApplicationUsage().addCommandLineOption("-h or --help","Display this information")
    arguments.getApplicationUsage().addCommandLineOption("--create <filename>","Create an photo archive of specified files")


    # construct the viewer.
    viewer = osgViewer.Viewer(arguments)

    viewer.setThreadingModel(osgViewer.Viewer.SingleThreaded)

    # register the handler to add keyboard and mouse handling.
    seh = SlideEventHandler()
    viewer.addEventHandler(seh)

    # read any time delay argument.
    timeDelayBetweenSlides = 5.0
    while arguments.read("-d",timeDelayBetweenSlides) : 

    autoSteppingActive = False
    while arguments.read("-a") : autoSteppingActive = True

    # if user request help write it out to cout.
    if arguments.read("-h") || arguments.read("--help") :
        arguments.getApplicationUsage().write(std.cout)
        return 1

    archiveName = str()
    while arguments.read("--create",archiveName) : 

    # any option left unread are converted into errors to write out later.
    arguments.reportRemainingOptionsAsUnrecognized()

    # report any errors if they have occurred when parsing the program arguments.
    if arguments.errors() :
        arguments.writeErrorMessages(std.cout)
        return 1

    if arguments.argc()<=1 :
        arguments.getApplicationUsage().write(std.cout,osg.ApplicationUsage.COMMAND_LINE_OPTION)
        return 1


    if !archiveName.empty() :
        # archive name set to create
        fileNameList = PhotoArchive.FileNameList()
        for(int i=1i<arguments.argc()++i)
            if arguments.isString(i) : fileNameList.push_back(str(arguments[i]))

        PhotoArchive.buildArchive(archiveName,fileNameList)

        return 0


    # now the windows have been realized we switch off the cursor to prevent it
    # distracting the people seeing the stereo images.
    double fovy, aspectRatio, zNear, zFar
    viewer.getCamera().getProjectionMatrixAsPerspective(fovy, aspectRatio, zNear, zFar)

    fovy = osg.DegreesToRadians(fovy)
    fovx = atan(tan(fovy*0.5)*aspectRatio)*2.0

    radius = 1.0
    width = 2*radius*tan(fovx*0.5)
    height = 2*radius*tan(fovy*0.5)

    album = Album(arguments,width,height)

    # creat the scene from the file list.
    rootNode = album.getScene()

    if !rootNode : return 0


    #osgDB.writeNodeFile(*rootNode,"test.osgt")

    # set the scene to render
    viewer.setSceneData(album.getScene())

    # set up the SlideEventHandler.
    seh.set(album.get(),timeDelayBetweenSlides,autoSteppingActive)

    viewer.realize()

    # switch off the cursor
    windows = osgViewer.Viewer.Windows()
    viewer.getWindows(windows)
    for(osgViewer.Viewer.Windows.iterator itr = windows.begin()
        itr != windows.end()
        ++itr)
        (*itr).useCursor(False)


    return viewer.run()


# Translated from file 'PhotoArchive.cpp'

# OpenSceneGraph example, osgphotoalbum.
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

#include "PhotoArchive.h"

#include <osg/GLU>
#include <osg/Notify>
#include <osgDB/ReadFile>
#include <osgDB/fstream>

#include <osg/GraphicsContext>

#include <iostream>
#include <string.h>

FILE_IDENTIFER =  str("osgphotoalbum photo archive")

PhotoArchive.PhotoArchive( str filename)
    readPhotoIndex(filename)

bool PhotoArchive.readPhotoIndex( str filename)
    in = osgDB.ifstream(filename.c_str())
    
    fileIndentifier = char [FILE_IDENTIFER.size()]
    in.read(fileIndentifier,FILE_IDENTIFER.size())
    if FILE_IDENTIFER!=fileIndentifier :
        delete [] fileIndentifier
        return False
    delete [] fileIndentifier
    
    numPhotos = unsigned int()
    in.read((char*)numPhotos,sizeof(numPhotos))

    _photoIndex.resize(numPhotos)

    in.read((char*)_photoIndex.front(),sizeof(PhotoHeader)*numPhotos)
    
    # success record filename.
    _archiveFileName = filename
    
    return True

void PhotoArchive.getImageFileNameList(FileNameList filenameList)
    for(PhotoIndexList.const_iterator itr=_photoIndex.begin()
        itr!=_photoIndex.end()
        ++itr)
        filenameList.push_back(str(itr.filename))
                        

osg.Image* PhotoArchive.readImage( str filename,
                                    unsigned int target_s, unsigned target_t,
                                    float original_s, float original_t)
    for(PhotoIndexList.const_iterator itr=_photoIndex.begin()
        itr!=_photoIndex.end()
        ++itr)
        if filename==itr.filename :
            photoHeader = *itr
        
            if target_s <= photoHeader.thumbnail_s 
                 target_t <= photoHeader.thumbnail_t 
                 photoHeader.thumbnail_position != 0 :
                in = osgDB.ifstream(_archiveFileName.c_str(),std.ios.in | std.ios.binary)
                
                # find image
                in.seekg(photoHeader.thumbnail_position)
                
                # read image header
                imageHeader = ImageHeader()
                in.read((char*)imageHeader,sizeof(ImageHeader))
                data = unsigned char[imageHeader.size]()
                in.read((char*)data,imageHeader.size)
                
                image = osg.Image()
                image.setImage(photoHeader.thumbnail_s,photoHeader.thumbnail_t,1,
                                imageHeader.pixelFormat,imageHeader.pixelFormat,imageHeader.type,
                                data,osg.Image.USE_NEW_DELETE)
                                
                original_s =  photoHeader.original_s
                original_t =  photoHeader.original_t
                
                return image
                 
            if photoHeader.fullsize_s 
                 photoHeader.fullsize_t 
                 photoHeader.fullsize_position != 0 :
                in = osgDB.ifstream(_archiveFileName.c_str(),std.ios.in | std.ios.binary)
                
                # find image
                in.seekg(photoHeader.fullsize_position)
                
                # read image header
                imageHeader = ImageHeader()
                in.read((char*)imageHeader,sizeof(ImageHeader))
                data = unsigned char[imageHeader.size]()
                in.read((char*)data,imageHeader.size)
                
                image = osg.Image()
                image.setImage(photoHeader.fullsize_s,photoHeader.fullsize_t,1,
                                imageHeader.pixelFormat,imageHeader.pixelFormat,imageHeader.type,
                                data,osg.Image.USE_NEW_DELETE)
                                
                original_s =  photoHeader.original_s
                original_t =  photoHeader.original_t
                
                return image


    return NULL

void PhotoArchive.buildArchive( str filename,  FileNameList imageList, unsigned int thumbnailSize, unsigned int maximumSize, bool #compressed)

    photoIndex = PhotoIndexList()
    photoIndex.reserve(imageList.size())
    for(FileNameList.const_iterator fitr=imageList.begin()
        fitr!=imageList.end()
        ++fitr)
        header = PhotoHeader()
        
        # set name
        strncpy(header.filename,fitr.c_str(),255)
        header.filename[255]=0
        
        header.thumbnail_s = thumbnailSize
        header.thumbnail_t = thumbnailSize
        header.thumbnail_position = 0
        
        header.fullsize_s = thumbnailSize
        header.fullsize_t = thumbnailSize
        header.fullsize_position = 0

        photoIndex.push_back(header)
        

    print "Building photo archive containing ", photoIndex.size(), " pictures"

    # open up the archive for writing to
    out = osgDB.ofstream(filename.c_str(), std.ios.out | std.ios.binary)

    # write out file indentifier.
    out.write(FILE_IDENTIFER.c_str(),FILE_IDENTIFER.size())

    numPhotos = photoIndex.size()
    out.write((char*)numPhotos,sizeof(unsigned int))

    # write the photo index to ensure we can the correct amount of space
    # available.
    startOfPhotoIndex = out.tellp()
    out.write((char*)photoIndex.front(),sizeof(PhotoHeader)*photoIndex.size())

    photoCount = 1    
    for(PhotoIndexList.iterator pitr=photoIndex.begin()
        pitr!=photoIndex.end()
        ++pitr,++photoCount)
        photoHeader = *pitr
        
        
        print "Processing image ", photoCount, " of ", photoIndex.size(), " filename=", photoHeader.filename
        print "    reading image..."std.cout.flush()
        
        image = osgDB.readImageFile(photoHeader.filename)
        
        print "done."
        
        photoHeader.original_s = image.s()
        photoHeader.original_t = image.t()


            print "    creating thumbnail image..."
            # first need to rescale image to the require thumbnail size
            newTotalSize = image.computeRowWidthInBytes(thumbnailSize,image.getPixelFormat(),image.getDataType(),image.getPacking())*
                thumbnailSize

            # need to sort out what size to really use...
            newData = unsigned char [newTotalSize]()
            if !newData :
                # should we throw an exception???  Just return for time being.
                osg.notify(osg.FATAL), "Error scaleImage() did not succeed : out of memory.", newTotalSize
                return

            psm = osg.PixelStorageModes()
            psm.pack_alignment = image.getPacking()
            psm.pack_row_length = image.getRowLength()
            psm.unpack_alignment = image.getPacking()

            status = osg.gluScaleImage(psm, image.getPixelFormat(),
                image.s(),
                image.t(),
                image.getDataType(),
                image.data(),
                thumbnailSize,
                thumbnailSize,
                image.getDataType(),
                newData)

            if status!=0 :
                delete [] newData
                osg.notify(osg.WARN), "Error scaleImage() did not succeed : errorString = ", osg.gluErrorString((GLenum)status)
                return
    
            # now set up the photo header.
            photoHeader.thumbnail_s = thumbnailSize
            photoHeader.thumbnail_t = thumbnailSize
            photoHeader.thumbnail_position = (unsigned int)out.tellp()

            # set up image header
            imageHeader = ImageHeader()
            imageHeader.s = thumbnailSize
            imageHeader.t = thumbnailSize
            imageHeader.internalTextureformat = image.getInternalTextureFormat()
            imageHeader.pixelFormat = image.getPixelFormat()
            imageHeader.type = image.getDataType()
            imageHeader.size = newTotalSize

            # write out image header and image data.
            out.write((char*)imageHeader,sizeof(ImageHeader))
            out.write((char*)newData,imageHeader.size)
            
            delete [] newData

            print "done."

        
            print "    creating fullsize image..."std.cout.flush()


            photoHeader.fullsize_s = osg.minimum((unsigned int)image.s(),maximumSize)
            photoHeader.fullsize_t = osg.minimum((unsigned int)image.t(),maximumSize)
            photoHeader.fullsize_position = (unsigned int)out.tellp()

            # first need to rescale image to the require thumbnail size
            newTotalSize = image.computeRowWidthInBytes(photoHeader.fullsize_s,image.getPixelFormat(),image.getDataType(),image.getPacking())*
                photoHeader.fullsize_t

            # need to sort out what size to really use...
            newData = unsigned char [newTotalSize]()
            if !newData :
                # should we throw an exception???  Just return for time being.
                osg.notify(osg.FATAL), "Error scaleImage() did not succeed : out of memory.", newTotalSize
                return

            psm = osg.PixelStorageModes()
            psm.pack_alignment = image.getPacking()
            psm.pack_row_length = image.getRowLength()
            psm.unpack_alignment = image.getPacking()

            status = osg.gluScaleImage(psm, image.getPixelFormat(),
                image.s(),
                image.t(),
                image.getDataType(),
                image.data(),
                photoHeader.fullsize_s,
                photoHeader.fullsize_t,
                image.getDataType(),
                newData)

            if status!=0 :
                delete [] newData
                osg.notify(osg.WARN), "Error scaleImage() did not succeed : errorString = ", osg.gluErrorString((GLenum)status)
                return

            imageHeader = ImageHeader()
            imageHeader.s = photoHeader.fullsize_s
            imageHeader.t = photoHeader.fullsize_t
            imageHeader.internalTextureformat = image.getInternalTextureFormat()
            imageHeader.pixelFormat = image.getPixelFormat()
            imageHeader.type = image.getDataType()
            imageHeader.size = newTotalSize

            out.write((char*)imageHeader,sizeof(ImageHeader))
            out.write((char*)newData,imageHeader.size)
            #out.write((char*)image.data(),imageHeader.size)

            delete [] newData

            print "done."
        

    # rewrite photo index now it has the correct sizes set
    out.seekp(startOfPhotoIndex)
    out.write((char*)photoIndex.front(),sizeof(PhotoHeader)*photoIndex.size())


# Translated from file 'PhotoArchive.h'

# -*-c++-*- 
#*
#*  OpenSceneGraph example, osgphotoalbum.
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

#ifndef PHOTOARCHIVE_H
#define PHOTOARCHIVE_H

#include <osg/Image>

class PhotoArchive (osg.Referenced) :

    static PhotoArchive* open( str filename)
        archive = PhotoArchive(filename)
        if !archive.empty() : return archive.release()
        else : return 0

    typedef std.vector<str> FileNameList
    
    def empty():
    
         return _photoIndex.empty() 

    getImageFileNameList = void(FileNameList filenameList)
    
    static void buildArchive( str filename,  FileNameList imageList, unsigned int thumbnailSize=256, unsigned int maximumSize=1024, bool compressed=True)

    readImage = osg.Image*( str filename,
                          unsigned int target_s, unsigned target_t,
                          float original_s, float original_t)

    PhotoArchive( str filename)

    virtual ~PhotoArchive() 

    readPhotoIndex = bool( str filename)
    
    class PhotoHeader :
PhotoHeader():
            original_s(0),
            original_t(0),
            thumbnail_s(0),
            thumbnail_t(0),
            thumbnail_position(0),
            fullsize_s(0),
            fullsize_t(0),
            fullsize_position(0)
            filename[0]='\0'
    
        char filename[256]
        original_s = unsigned int()
        original_t = unsigned int()

        thumbnail_s = unsigned int()
        thumbnail_t = unsigned int()
        thumbnail_position = unsigned int()

        fullsize_s = unsigned int()
        fullsize_t = unsigned int()
        fullsize_position = unsigned int()
    

    
    class ImageHeader :
ImageHeader():
            s(0),
            t(0),
            internalTextureformat(0),
            pixelFormat(0),
            type(0),
            size(0) 
    
        s = unsigned int()
        t = unsigned int()
        internalTextureformat = GLint()
        pixelFormat = GLenum()
        type = GLenum()
        size = unsigned int()
    


    typedef std.vector<PhotoHeader> PhotoIndexList

    _archiveFileName = str()
    _photoIndex = PhotoIndexList()    



#endif


if __name__ == "__main__":
    main(sys.argv)
