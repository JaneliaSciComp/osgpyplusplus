#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osganalysis"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osgDB
from osgpypp import osgGA
from osgpypp import osgUtil
from osgpypp import osgViewer


# Translated from file 'osganalysis.cpp'

# OpenSceneGraph example, osganalysis.
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


#include <osgViewer/Viewer>
#include <osgViewer/ViewerEventHandlers>

#include <osgDB/ReadFile>
#include <osgDB/WriteFile>
#include <osgDB/FileNameUtils>

#include <osgGA/TrackballManipulator>
#include <osgGA/StateSetManipulator>
#include <osgGA/TrackballManipulator>
#include <osgGA/FlightManipulator>
#include <osgGA/DriveManipulator>
#include <osgGA/KeySwitchMatrixManipulator>
#include <osgGA/AnimationPathManipulator>
#include <osgGA/TerrainManipulator>

#include <osgUtil/IncrementalCompileOperation>
#include <osgUtil/Simplifier>
#include <osgUtil/MeshOptimizers>

class StripStateVisitor (osg.NodeVisitor) :
    StripStateVisitor(bool useStateSets, bool useDisplayLists, bool useVBO):
        osg.NodeVisitor(osg.NodeVisitor.TRAVERSE_ALL_CHILDREN),
        _useStateSets(useStateSets),
        _useDisplayLists(useDisplayLists),
        _useVBO(useVBO) 

    _useStateSets = bool()
    _useDisplayLists = bool()
    _useVBO = bool()

    def apply(node):

        
        if !_useStateSets  node.getStateSet() : node.setStateSet(0)
        traverse(node)

    def apply(node):

        
        if !_useStateSets  node.getStateSet() : node.setStateSet(0)
        for(unsigned int i = 0 i<node.getNumDrawables() ++i)
            process(*node.getDrawable(i))

        traverse(node)

    def process(drawable):

        
        if !_useStateSets  drawable.getStateSet() :
            drawable.setStateSet(0)

        drawable.setUseDisplayList(_useDisplayLists)
        drawable.setUseVertexBufferObjects(_useVBO)


class OptimizeImageVisitor (osg.NodeVisitor) :
    OptimizeImageVisitor(osgDB.ImageProcessor* imageProcessor, bool compressImages, bool generateMipmaps):
        osg.NodeVisitor(osg.NodeVisitor.TRAVERSE_ALL_CHILDREN),
        _imageProcessor(imageProcessor),
        _compressImages(compressImages),
        _generateMipmaps(generateMipmaps) 

    _imageProcessor = osgDB.ImageProcessor()
    _compressImages = bool()
    _generateMipmaps = bool()

    def apply(node):

        
        processStateSet(node.getStateSet())
        traverse(node)

    def apply(node):

        
        processStateSet(node.getStateSet())
        for(unsigned int i = 0 i<node.getNumDrawables() ++i)
            processStateSet(node.getDrawable(i).getStateSet())

        traverse(node)

    def processStateSet(stateset):

        
        if !stateset : return

        for(unsigned int i=0 i<stateset.getNumTextureAttributeLists() ++i)
            sa = stateset.getTextureAttribute(i, osg.StateAttribute.TEXTURE)
            texture = dynamic_cast<osg.Texture*>(sa)
            if texture :
                for(unsigned int i=0 i<texture.getNumImages() ++i)
                    proccessImage(texture.getImage(i))
        


    def proccessImage(image):


        
        if !image : return

        if _imageProcessor.valid() :
            OSG_NOTICE, "Will be using ImageProcessor to process image ", image.getFileName()
        else :
            OSG_NOTICE, "No ImageProcessor to process image ", image.getFileName()
            OSG_NOTICE, "   compressImage ", _compressImages
            OSG_NOTICE, "   generateMipmaps ", _generateMipmaps




class SwapArrayVisitor (osg.ArrayVisitor) :
    SwapArrayVisitor(osg.Array* array):
        _array(array) 

    template <class ARRAY>
    def apply_imp(array):
        
        if array.getType()!=_array.getType() :
            OSG_NOTICE, "Arrays incompatible"
            return
        OSG_NOTICE, "Swapping Array"
        array.swap(*static_cast<ARRAY*>(_array))

    def apply(ba):

         apply_imp(ba) 
    def apply(ba):
         apply_imp(ba) 
    def apply(ba):
         apply_imp(ba) 
    def apply(ba):
         apply_imp(ba) 
    def apply(ba):
         apply_imp(ba) 
    def apply(ba):
         apply_imp(ba) 
    def apply(ba):
         apply_imp(ba) 
    def apply(ba):
         apply_imp(ba) 
    def apply(ba):
         apply_imp(ba) 
    def apply(ba):
         apply_imp(ba) 
    def apply(ba):
         apply_imp(ba) 

    _array = osg.Array*()


class MemoryVisitor (osg.NodeVisitor) :
     MemoryVisitor():
         osg.NodeVisitor(osg.NodeVisitor.TRAVERSE_ALL_CHILDREN) 


    def reset():


        
         _nodes.clear()
         _geometryMap.clear()
         _arrayMap.clear()
         _primitiveSetMap.clear()

    def apply(node):

        
        _nodes.insert(node)
        traverse(node)

    def apply(geode):

        
        _nodes.insert(geode)
        for(unsigned int i=0 i<geode.getNumDrawables() ++i)
            apply(geode, geode.getDrawable(i))

    def apply(geode, drawable):

        
        if !drawable : return

        geometry = drawable.asGeometry()
        if geometry :
            _geometryMap[geometry].insert(geode)

            apply(geometry, geometry.getVertexArray())
            apply(geometry, geometry.getNormalArray())
            apply(geometry, geometry.getColorArray())
            apply(geometry, geometry.getSecondaryColorArray())
            apply(geometry, geometry.getFogCoordArray())

            for(unsigned int i=0 i<geometry.getNumTexCoordArrays() ++i)
                apply(geometry, geometry.getTexCoordArray(i))
            for(unsigned int i=0 i<geometry.getNumVertexAttribArrays() ++i)
                apply(geometry, geometry.getVertexAttribArray(i))

            for(unsigned int i=0 i<geometry.getNumPrimitiveSets() ++i)
                apply(geometry, geometry.getPrimitiveSet(i))

    def apply(geometry, array):

        
        if !array : return
        _arrayMap[array].insert(geometry)

    def apply(geometry, primitiveSet):

        
        if !primitiveSet : return
        _primitiveSetMap[primitiveSet].insert(geometry)

    def report(out):

        
        out, "Nodes ", _nodes.size()
        out, "Geometries ", _geometryMap.size()
        out, "Arrays ", _arrayMap.size()
        out, "PrimitiveSets ", _primitiveSetMap.size()

    def reallocate():

        
        OSG_NOTICE, "Reallocating Arrays"

        typedef std.vector< osg.Array > ArrayVector
        typedef std.vector< osg.Geometry > GeometryVector
        newArrays = ArrayVector()
        newGeometries = GeometryVector()
        for(GeometryMap.iterator itr = _geometryMap.begin()
            itr != _geometryMap.end()
            ++itr)
            geometry = itr.first
            useVBO = geometry.getUseVertexBufferObjects()
            newGeometry = osg.clone(geometry, osg.CopyOp(osg.CopyOp.DEEP_COPY_ALL))
            newGeometry.setUseVertexBufferObjects(False)
            newGeometry.setUseVertexBufferObjects(useVBO)
            newGeometries.push_back(newGeometry)

        geom_itr = newGeometries.begin()
        for(GeometryMap.iterator itr = _geometryMap.begin()
            itr != _geometryMap.end()
            ++itr, ++geom_itr)
            geometry = itr.first
            geodes = itr.second
            for(Geodes.iterator gitr = geodes.begin()
                gitr != geodes.end()
                ++gitr)
                geode = const_cast<osg.Geode*>(*gitr)
                geode.replaceDrawable(geometry, geom_itr.get())

    typedef std.vector< osg.Geometry > GeometryVector
    typedef std.pair<osg.Array*, osg.Array*> ArrayPair
    typedef std.vector< ArrayPair > ArrayVector
    typedef std.pair<osg.PrimitiveSet*, osg.PrimitiveSet*> PrimitiveSetPair
    typedef std.vector< PrimitiveSetPair > PrimitiveSetVector

    def cloneArray(arrayVector, array):

        
        if !array : return 0
        newArray = static_cast<osg.Array*>(array.cloneType())
        arrayVector.push_back(ArrayPair(array,newArray))
        return newArray

    def clonePrimitiveSet(psVector, ps):

        
        if !ps : return 0
        newPS = static_cast<osg.PrimitiveSet*>(ps.cloneType())
        psVector.push_back(PrimitiveSetPair(ps,newPS))
        return newPS

    def reallocate2():

        
        OSG_NOTICE, "Reallocating Arrays"

        arrayVector = ArrayVector()
        primitiveSetVector = PrimitiveSetVector()
        newGeometries = GeometryVector()

        for(GeometryMap.iterator itr = _geometryMap.begin()
            itr != _geometryMap.end()
            ++itr)
            geometry = itr.first
            newGeometry = osg.clone(geometry, osg.CopyOp.SHALLOW_COPY)
            newGeometries.push_back(newGeometry.get())

            newGeometry.setVertexArray(cloneArray(arrayVector, geometry.getVertexArray()))
            newGeometry.setNormalArray(cloneArray(arrayVector, geometry.getNormalArray()))
            newGeometry.setColorArray(cloneArray(arrayVector, geometry.getColorArray()))
            newGeometry.setSecondaryColorArray(cloneArray(arrayVector, geometry.getSecondaryColorArray()))
            newGeometry.setFogCoordArray(cloneArray(arrayVector, geometry.getFogCoordArray()))
            for(unsigned int i=0 i<geometry.getNumTexCoordArrays() ++i)
                newGeometry.setTexCoordArray(i, cloneArray(arrayVector, geometry.getTexCoordArray(i)))
            for(unsigned int i=0 i<geometry.getNumVertexAttribArrays() ++i)
                newGeometry.setVertexAttribArray(i, cloneArray(arrayVector, geometry.getVertexAttribArray(i)))

            for(unsigned int i=0 i<geometry.getNumPrimitiveSets() ++i)
                newGeometry.setPrimitiveSet(i,clonePrimitiveSet(primitiveSetVector, geometry.getPrimitiveSet(i)))

        geom_itr = newGeometries.begin()
        for(GeometryMap.iterator itr = _geometryMap.begin()
            itr != _geometryMap.end()
            ++itr, ++geom_itr)
            geometry = itr.first
            geodes = itr.second
            for(Geodes.iterator gitr = geodes.begin()
                gitr != geodes.end()
                ++gitr)
                geode = const_cast<osg.Geode*>(*gitr)
                geode.replaceDrawable(geometry, geom_itr.get())

     typedef std.set<osg.Node*>  Nodes
     typedef std.set<osg.Geode*>  Geodes
     typedef std.set<osg.Geometry*>  Geometries
     typedef std.map<osg.Geometry*, Geodes> GeometryMap
     typedef std.map<osg.Array*, Geometries> ArrayMap
     typedef std.map<osg.PrimitiveSet*, Geometries> PrimitiveSetMap

     _nodes = Nodes()
     _geometryMap = GeometryMap()
     _arrayMap = ArrayMap()
     _primitiveSetMap = PrimitiveSetMap()


class SceneGraphProcessor (osg.Referenced) :
    SceneGraphProcessor()
        _init()

    SceneGraphProcessor(osg.ArgumentParser arguments)
        _init()

        while arguments.read("--vbo") :  modifyDrawableSettings = True useVBO = True  
        while arguments.read("--dl") :  modifyDrawableSettings = True useDisplayLists = True  

        while arguments.read("-s", simplificatioRatio) : 
        while arguments.read("--tristripper") :  useTriStripVisitor=True 
        while arguments.read("--no-tristripper") :  useTriStripVisitor=False 
        while arguments.read("--smoother") :   useSmoothingVisitor=True 
        while arguments.read("--no-smoother") :   useSmoothingVisitor=False 

        while arguments.read("--remove-duplicate-vertices") || arguments.read("--rdv") : removeDuplicateVertices = True
        while arguments.read("--optimize-vertex-cache") || arguments.read("--ovc") : optimizeVertexCache = True
        while arguments.read("--optimize-vertex-order") || arguments.read("--ovo") : optimizeVertexOrder = True

        while arguments.read("--build-mipmaps") :  modifyTextureSettings = True buildImageMipmaps = True 
        while arguments.read("--compress") :  modifyTextureSettings = True compressImages = True 
        while arguments.read("--disable-mipmaps") :  modifyTextureSettings = True disableMipmaps = True 

        while arguments.read("--reallocate") || arguments.read("--ra")  :  reallocateMemory = True 

        OSG_NOTICE, "simplificatioRatio=", simplificatioRatio

    def process(node):

        
        if !node :
            OSG_NOTICE, "SceneGraphProcessor.process(Node*) : error cannot process NULL Node."
            return 0

        OSG_NOTICE, "SceneGraphProcessor.process(", node, ") : ", node.getName()

        if simplificatioRatio < 1.0 :
            OSG_NOTICE, "Running simplifier with simplification ratio=", simplificatioRatio
            maxError = 4.0
            simplifier = osgUtil.Simplifier(simplificatioRatio, maxError)
            simplifier.setDoTriStrip(useTriStripVisitor)
            simplifier.setSmoothing(useSmoothingVisitor)
            node.accept(simplifier)


        if modifyTextureSettings :
            oiv = OptimizeImageVisitor(osgDB.Registry.instance().getImageProcessor(), compressImages, buildImageMipmaps)
            node.accept(oiv)


        if removeDuplicateVertices :
            OSG_NOTICE, "Running osgUtil.IndexMeshVisitor"
            imv = osgUtil.IndexMeshVisitor()
            node.accept(imv)
            imv.makeMesh()

        if optimizeVertexCache :
            OSG_NOTICE, "Running osgUtil.VertexCacheVisitor"
            vcv = osgUtil.VertexCacheVisitor()
            node.accept(vcv)
            vcv.optimizeVertices()

        if optimizeVertexOrder :
            OSG_NOTICE, "Running osgUtil.VertexAccessOrderVisitor"
            vaov = osgUtil.VertexAccessOrderVisitor()
            node.accept(vaov)
            vaov.optimizeOrder()

        if modifyDrawableSettings :
            OSG_NOTICE, "Running StripStateVisitor"
            ssv = StripStateVisitor(True, useDisplayLists, useVBO)
            node.accept(ssv)

        mv = MemoryVisitor()
        node.accept(mv)
        mv.report(osg.notify(osg.NOTICE))

        if reallocateMemory :
            OSG_NOTICE, "Running Reallocation of scene graph memory"
            mv.reallocate()

        mv.reset()
        node.accept(mv)
        mv.report(osg.notify(osg.NOTICE))

        return node

    def _init():

        
        modifyDrawableSettings = False
        useVBO = False
        useDisplayLists = False

        simplificatioRatio = 1.0
        useTriStripVisitor = False
        useSmoothingVisitor = False

        removeDuplicateVertices = False
        optimizeVertexCache = False
        optimizeVertexOrder = False

        reallocateMemory = False
        
        modifyTextureSettings = False
        buildImageMipmaps = False
        compressImages = False
        disableMipmaps = False

    modifyDrawableSettings = bool()
    useVBO = bool()
    useDisplayLists = bool()

    simplificatioRatio = float()
    useTriStripVisitor = bool()
    useSmoothingVisitor = bool()

    removeDuplicateVertices = bool()
    optimizeVertexCache = bool()
    optimizeVertexOrder = bool()

    reallocateMemory = bool()
    
    modifyTextureSettings = bool()
    buildImageMipmaps = bool()
    compressImages = bool()
    disableMipmaps = bool()


# 
class DatabasePagingOperation : public osg.Operation, public osgUtil.IncrementalCompileOperation.CompileCompletedCallback

    DatabasePagingOperation( str filename,
                             str outputFilename,
                             SceneGraphProcessor* sceneGraphProcessor, 
                             osgUtil.IncrementalCompileOperation* ico):
        Operation("DatabasePaging Operation", False),
        _filename(filename),
        _outputFilename(outputFilename),
        _modelReadyToMerge(False),
        _sceneGraphProcessor(sceneGraphProcessor),
        _incrementalCompileOperation(ico)

    virtual void operator () (osg.Object* object)
        osg.notify(osg.NOTICE), "LoadAndCompileOperation ", _filename

        _modelReadyToMerge = False
        _loadedModel = osgDB.readNodeFile(_filename)

        if _loadedModel.valid() :
            if _sceneGraphProcessor.valid() :
                _loadedModel = _sceneGraphProcessor.process(_loadedModel.get())

        if _loadedModel.valid() :
            if !_outputFilename.empty() :
                OSG_NOTICE, "Writing out file ", _outputFilename
                
                osgDB.writeNodeFile(*_loadedModel, _outputFilename)

            if _incrementalCompileOperation.valid() :
                OSG_NOTICE, "Registering with ICO ", _outputFilename

                compileSet = osgUtil.IncrementalCompileOperation.CompileSet(_loadedModel.get())

                compileSet._compileCompletedCallback = this

                _incrementalCompileOperation.add(compileSet.get())
            else :
                _modelReadyToMerge = True

        osg.notify(osg.NOTICE), "done LoadAndCompileOperation ", _filename

    def compileCompleted(compileSet):

        
        OSG_NOTICE, "compileCompleted"
        _modelReadyToMerge = True
        return True

    _filename = str()
    _outputFilename = str()
    _loadedModel = osg.Node()
    _modelReadyToMerge = bool()
    _sceneGraphProcessor = SceneGraphProcessor()
    _incrementalCompileOperation = osgUtil.IncrementalCompileOperation()


class TexturePoolHandler (osgGA.GUIEventHandler) :
    def handle(ea, aa):
        
        if ea.getEventType() == osgGA.GUIEventAdapter.KEYUP :
            if ea.getKey()=='r' :
                osg.Texture.getTextureObjectManager(0).reportStats(osg.notify(osg.NOTICE))
                osg.GLBufferObjectManager.getGLBufferObjectManager(0).reportStats(osg.notify(osg.NOTICE))
        return False


class ReportStatsAnimationCompletedCallback (osgGA.AnimationPathManipulator.AnimationCompletedCallback) :
virtual void completed( osgGA.AnimationPathManipulator*)
        OSG_NOTICE, "Animation completed"
        osg.Texture.getTextureObjectManager(0).reportStats(osg.notify(osg.NOTICE))
        osg.GLBufferObjectManager.getGLBufferObjectManager(0).reportStats(osg.notify(osg.NOTICE))


def main(argc, argv):

    
    arguments = osg.ArgumentParser(argc, argv)

    # construct the viewer.
    viewer = osgViewer.Viewer(arguments)

    # set up camera manipulators
        keyswitchManipulator = osgGA.KeySwitchMatrixManipulator()

        keyswitchManipulator.addMatrixManipulator( '1', "Trackball", osgGA.TrackballManipulator() )
        keyswitchManipulator.addMatrixManipulator( '2', "Flight", osgGA.FlightManipulator() )
        keyswitchManipulator.addMatrixManipulator( '3', "Drive", osgGA.DriveManipulator() )
        keyswitchManipulator.addMatrixManipulator( '4', "Terrain", osgGA.TerrainManipulator() )

        keyForAnimationPath = '8'
        animationSpeed = 1.0
        while arguments.read("--speed",animationSpeed)  : 

        pathfile = str()
        while arguments.read("-p",pathfile) :
            apm = osgGA.AnimationPathManipulator(pathfile)
            if apm || !apm.valid() :
                apm.setTimeScale(animationSpeed)
                apm.setAnimationCompletedCallback(ReportStatsAnimationCompletedCallback())
                
                num = keyswitchManipulator.getNumMatrixManipulators()
                keyswitchManipulator.addMatrixManipulator( keyForAnimationPath, "Path", apm )
                keyswitchManipulator.selectMatrixManipulator(num)
                ++keyForAnimationPath

        viewer.setCameraManipulator( keyswitchManipulator.get() )

    # set up event handlers 
        viewer.addEventHandler( osgViewer.StatsHandler())
        viewer.addEventHandler( osgViewer.WindowSizeHandler() )
        viewer.addEventHandler( osgGA.StateSetManipulator(viewer.getCamera().getOrCreateStateSet()) )
        viewer.addEventHandler( TexturePoolHandler() )

    ########################################/
    #
    # IncrementalCompileOperation settings
    #
    incrementalCompile = osgUtil.IncrementalCompileOperation()
    viewer.setIncrementalCompileOperation(incrementalCompile.get())

    if arguments.read("--force") || arguments.read("-f") :
        incrementalCompile.assignForceTextureDownloadGeometry()

    if arguments.read("-a") :
        incrementalCompile.setMinimumTimeAvailableForGLCompileAndDeletePerFrame(1)
        incrementalCompile.setConservativeTimeRatio(1)
        incrementalCompile.setMaximumNumOfObjectsToCompilePerFrame(100)
    elif arguments.read("-c") :
        incrementalCompile.setMinimumTimeAvailableForGLCompileAndDeletePerFrame(0.0001)
        incrementalCompile.setConservativeTimeRatio(0.01)
        incrementalCompile.setMaximumNumOfObjectsToCompilePerFrame(1)

    ########################################/
    #
    # SceneGraph processing setup
    #
    sceneGraphProcessor = SceneGraphProcessor(arguments)

    ########################################/
    #
    # Database settings
    #
    timeBetweenMerges = 2.0
    while arguments.read("--interval",timeBetweenMerges) : 

    outputPostfix = str()
    while arguments.read("-o",outputPostfix) :  OSG_NOTICE, "Set ouputPostfix to ", outputPostfix 


    typedef std.vector< str > FileNames
    fileNames = FileNames()
    for(int pos=1pos<arguments.argc()++pos)
        if !arguments.isOption(pos) :
            fileNames.push_back(arguments[pos])

    if fileNames.empty() :
        OSG_NOTICE, "No files loaded, please specify files on commandline."
        return 1

    # load the models using a paging thread and use the incremental compile operation to
    # manage the compilation of GL objects without breaking frame.

    modelIndex = 0

    databasePagingThread = osg.OperationThread()
    databasePagingOperation = DatabasePagingOperation()

    databasePagingThread = osg.OperationThread()
    databasePagingThread.startThread()


    group = osg.Group()
    viewer.setSceneData(group.get())

    viewer.realize()

    filename = fileNames[modelIndex++]
    outputFilename = outputPostfix.empty() ? str() : osgDB.getStrippedName(filename)+outputPostfix

    databasePagingOperation = DatabasePagingOperation(
        filename,
        outputFilename,
        sceneGraphProcessor.get(),
        incrementalCompile.get())

    databasePagingThread.add(databasePagingOperation.get())


    timeOfLastMerge = viewer.getFrameStamp().getReferenceTime()

    while !viewer.done() :
        viewer.frame()

        currentTime = viewer.getFrameStamp().getReferenceTime()

        if !databasePagingOperation 
            modelIndex<fileNames.size() 
            (currentTime-timeOfLastMerge)>timeBetweenMerges :
            filename = fileNames[modelIndex++]
            outputFilename = outputPostfix.empty() ? str() : osgDB.getStrippedName(filename)+outputPostfix

            databasePagingOperation = DatabasePagingOperation(
                filename,
                outputFilename,
                sceneGraphProcessor.get(),
                incrementalCompile.get())

            databasePagingThread.add(databasePagingOperation.get())

        if databasePagingOperation.get()  databasePagingOperation._modelReadyToMerge :
            OSG_NOTICE, "Merging subgraph"
            
            timeOfLastMerge = currentTime

            group.removeChildren(0,group.getNumChildren())

            group.addChild(databasePagingOperation._loadedModel.get())

            viewer.home()

            # we no longer need the paging operation as it's done it's job.
            databasePagingOperation = 0

            viewer.home()

    return 0


if __name__ == "__main__":
    main(sys.argv)
