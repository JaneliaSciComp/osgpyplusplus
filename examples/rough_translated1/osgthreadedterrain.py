#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgthreadedterrain"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import OpenThreads
from osgpypp import osg
from osgpypp import osgDB
from osgpypp import osgGA
from osgpypp import osgTerrain
from osgpypp import osgText
from osgpypp import osgUtil
from osgpypp import osgViewer


# Translated from file 'osgthreadedterrain.cpp'

# OpenSceneGraph example, osgterrain.
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

#include <OpenThreads/Block>

#include <osg/Group>
#include <osg/Geode>
#include <osg/ShapeDrawable>
#include <osg/Texture2D>
#include <osg/PositionAttitudeTransform>
#include <osg/MatrixTransform>
#include <osg/CoordinateSystemNode>
#include <osg/ClusterCullingCallback>
#include <osg/ArgumentParser>


#include <osgDB/FileUtils>
#include <osgDB/fstream>
#include <osgDB/ReadFile>

#include <osgUtil/IncrementalCompileOperation>

#include <osgText/FadeText>

#include <osgViewer/Viewer>
#include <osgViewer/ViewerEventHandlers>

#include <osgGA/TrackballManipulator>
#include <osgGA/FlightManipulator>
#include <osgGA/DriveManipulator>
#include <osgGA/KeySwitchMatrixManipulator>
#include <osgGA/StateSetManipulator>
#include <osgGA/AnimationPathManipulator>
#include <osgGA/TerrainManipulator>

#include <osgTerrain/TerrainTile>
#include <osgTerrain/GeometryTechnique>
#include <osgTerrain/Layer>

#include <iostream>


typedef std.vector< osg.GraphicsThread > GraphicsThreads

class ReleaseBlockOnCompileCompleted (osgUtil.IncrementalCompileOperation.CompileCompletedCallback) :
ReleaseBlockOnCompileCompleted(osg.RefBlockCount* block):
        _block(block) 

    def compileCompleted(compileSet):

        
        if _block.valid() : _block.completed()
        
        # tell IncrementalCompileOperation that it's now safe to remove the compileSet
        
        osg.notify(osg.NOTICE), "compileCompleted(", compileSet, ")"
        
        return True

    _block = osg.RefBlockCount()



class LoadAndCompileOperation (osg.Operation) :

    LoadAndCompileOperation( str filename, osgUtil.IncrementalCompileOperation* ico , osg.RefBlockCount* block):
        Operation("Load and compile Operation", False),
        _filename(filename),
        _incrementalCompileOperation(ico),
        _block(block) 

    virtual void operator () (osg.Object* object)
        # osg.notify(osg.NOTICE), "LoadAndCompileOperation ", _filename

        _loadedModel = osgDB.readNodeFile(_filename)

        if _loadedModel.valid()  _incrementalCompileOperation.valid() :
            compileSet = osgUtil.IncrementalCompileOperation.CompileSet(_loadedModel.get())

            compileSet._compileCompletedCallback = ReleaseBlockOnCompileCompleted(_block.get())

            _incrementalCompileOperation.add(compileSet.get())
        else : 
            if _block.valid() : _block.completed()

        # osg.notify(osg.NOTICE), "done LoadAndCompileOperation ", _filename
    
    _filename = str()
    _loadedModel = osg.Node()
    _incrementalCompileOperation = osgUtil.IncrementalCompileOperation()
    _block = osg.RefBlockCount()



class MasterOperation (osg.Operation) :

    typedef std.set<str> Files
    typedef std.map<str, osg.Node >  FilenameNodeMap
    typedef std.vector< osg.Node >  Nodes


    MasterOperation( str filename, osgUtil.IncrementalCompileOperation* ico):
        Operation("Master reading operation",True),
        _filename(filename),
        _incrementalCompileOperation(ico)
    
    #* Set the OperationQueue that the MasterOperation can use to place tasks like file loading on for other processes to handle. 
    def setOperationQueue(oq):
         _operationQueue = oq 
    
    def getOperationQueue():
    
         return _operationQueue.get() 
    
    def readMasterFile(files):
    
        
        fin = osgDB.ifstream(_filename.c_str())
        if fin :
            fr = osgDB.Input()
            fr.attach(fin)

            readFilename = False

            while !fr.eof() :
                itrAdvanced = False
                if fr.matchSequence("file %s") || fr.matchSequence("file %w")  :
                    files.insert(fr[1].getStr())
                    fr += 2
                    itrAdvanced = True
                    readFilename = True

                if !itrAdvanced :
                    ++fr
            
            return readFilename
        return False
    
    def open(group):
    
        
        files = Files()
        readMasterFile(files)
        for(Files.iterator itr = files.begin()
            itr != files.end()
            ++itr)
            model = osgDB.readNodeFile(*itr)
            if model :
                osg.notify(osg.NOTICE), "open: Loaded file ", *itr
                group.addChild(model)
                _existingFilenameNodeMap[*itr] = model
        
        return True
    

    virtual void operator () (osg.Object* callingObject)
        # decided which method to call according to whole has called me.
        viewer = dynamic_cast<osgViewer.Viewer*>(callingObject)

        if viewer : update(viewer.getSceneData())
        load = else :()

    def load():

        
        #osg.notify(osg.NOTICE), "void load(Object)"
        filesA = Files()
        filesB = Files()
        
        readMasterFile(filesB)
        # osg.notify(osg.NOTICE), "First read ", filesA.size()

        # itererate until the master file is stable
        do
            OpenThreads.Thread.microSleep(100000)

            filesB.swap(filesA)
            filesB.clear()
            readMasterFile(filesB)

            # osg.notify(osg.NOTICE), "second read ", filesB.size()
            
         while filesA!=filesB :

        files = Files()
        files.swap(filesB)

        # osg.notify(osg.NOTICE), "Now equal ", files.size()


        newFiles = Files()
        removedFiles = Files()

        # find out which files are , and which ones have been removed.
            lock = OpenThreads.ScopedLock<OpenThreads.Mutex>(_mutex)

            for(Files.iterator fitr = files.begin()
                fitr != files.end()
                ++fitr)
                if _existingFilenameNodeMap.count(*fitr)==0 : newFiles.insert(*fitr)

            for(FilenameNodeMap.iterator litr = _existingFilenameNodeMap.begin()
                litr != _existingFilenameNodeMap.end()
                ++litr)
                if files.count(litr.first)==0 :
                    removedFiles.insert(litr.first)
        
#if 0
        if !newFiles.empty() || !removedFiles.empty() :
            osg.notify(osg.NOTICE), "void operator () files.size()=", files.size()
#endif

        # first load the files.
        nodesToAdd = FilenameNodeMap()
        if !newFiles.empty() :

            typedef std.vector< osg.GraphicsThread > GraphicsThreads
            threads = GraphicsThreads()
        
            for(unsigned int i=0 i<= osg.GraphicsContext.getMaxContextID() ++i)
                gc = osg.GraphicsContext.getCompileContext(i)
                gt = gc ? gc.getGraphicsThread() : 0
                if gt : threads.push_back(gt)

            if _operationQueue.valid() :
                # osg.notify(osg.NOTICE), "Using OperationQueue"

                _endOfLoadBlock = osg.RefBlockCount(newFiles.size())
                
                _endOfLoadBlock.reset()
     
                typedef std.list< LoadAndCompileOperation > LoadAndCompileList
                loadAndCompileList = LoadAndCompileList()
     
                for(Files.iterator nitr = newFiles.begin()
                    nitr != newFiles.end()
                    ++nitr)
                    # osg.notify(osg.NOTICE), "Adding LoadAndCompileOperation ", *nitr

                    loadAndCompile = LoadAndCompileOperation( *nitr, _incrementalCompileOperation.get(), _endOfLoadBlock.get() )
                    loadAndCompileList.push_back(loadAndCompile)
                    _operationQueue.add( loadAndCompile.get() )

#if 1
                operation = osg.Operation()
                while operation=_operationQueue.getNextOperation() :.valid() :
                    # osg.notify(osg.NOTICE), "Local running of operation"
                    (*operation)(0)
#endif                                
                # osg.notify(osg.NOTICE), "Waiting for completion of LoadAndCompile operations"
                _endOfLoadBlock.block()
                # osg.notify(osg.NOTICE), "done ... Waiting for completion of LoadAndCompile operations"
                
                for(LoadAndCompileList.iterator litr = loadAndCompileList.begin()
                    litr != loadAndCompileList.end()
                    ++litr)
                    if *litr :._loadedModel.valid() :
                        nodesToAdd[(*litr)._filename] = (*litr)._loadedModel

            
            else :

                _endOfLoadBlock = osg.RefBlockCount(newFiles.size())
                
                _endOfLoadBlock.reset()

                for(Files.iterator nitr = newFiles.begin()
                    nitr != newFiles.end()
                    ++nitr)
                    loadedModel = osgDB.readNodeFile(*nitr)

                    if loadedModel.get() :
                        nodesToAdd[*nitr] = loadedModel

                        if _incrementalCompileOperation.valid() :
                            compileSet = osgUtil.IncrementalCompileOperation.CompileSet(loadedModel.get())

                            compileSet._compileCompletedCallback = ReleaseBlockOnCompileCompleted(_endOfLoadBlock.get())

                            _incrementalCompileOperation.add(compileSet.get())
                        else :
                            _endOfLoadBlock.completed()
                    else :
                        _endOfLoadBlock.completed()

                _endOfLoadBlock.block()

                        
        
        requiresBlock = False
        
        # pass the locally peppared data to MasterOperations shared data
        # so that updated thread can merge these changes with the main scene 
        # graph.  This merge is carried out via the update(..) method.
        if !removedFiles.empty() || !nodesToAdd.empty() :        
            lock = OpenThreads.ScopedLock<OpenThreads.Mutex>(_mutex)
            _nodesToRemove.swap(removedFiles)
            _nodesToAdd.swap(nodesToAdd)
            requiresBlock = True

        # now block so we don't try to load anything till the data has been merged
        # otherwise _existingFilenameNodeMap will get out of sync.
        if requiresBlock :
            _updatesMergedBlock.block()
        else :
            OpenThreads.Thread.YieldCurrentThread()

    
    # merge the changes with the main scene graph.
    def update(scene):
        
        # osg.notify(osg.NOTICE), "void update(Node*)"

        group = dynamic_cast<osg.Group*>(scene)
        if !group :
            osg.notify(osg.NOTICE), "Error, MasterOperation.update(Node*) can only work with a Group as Viewer.getSceneData()."
            return
    
        lock = OpenThreads.ScopedLock<OpenThreads.Mutex>(_mutex)
        
        if !_nodesToRemove.empty() || !_nodesToAdd.empty() :
            osg.notify(osg.NOTICE), "update().................. "

        if !_nodesToRemove.empty() :
            for(Files.iterator itr = _nodesToRemove.begin()
                itr != _nodesToRemove.end()
                ++itr)
                fnmItr = _existingFilenameNodeMap.find(*itr)
                if fnmItr != _existingFilenameNodeMap.end() :
                    osg.notify(osg.NOTICE), "  update():removing ", *itr
                
                    group.removeChild(fnmItr.second.get())
                    _existingFilenameNodeMap.erase(fnmItr)

            _nodesToRemove.clear()
        
        if !_nodesToAdd.empty() :
            for(FilenameNodeMap.iterator itr = _nodesToAdd.begin()
                itr != _nodesToAdd.end()
                ++itr)
                osg.notify(osg.NOTICE), "  update():inserting ", itr.first
                group.addChild(itr.second.get())
                _existingFilenameNodeMap[itr.first] = itr.second
            
            _nodesToAdd.clear()

        _updatesMergedBlock.release()

    
    # add release implementation so that any thread cancellation can
    # work even when blocks and barriers are used.
    def release():
        
        if _operationQueue.valid() : _operationQueue.removeAllOperations()

        _updatesMergedBlock.release()
        if _endOfCompilebarrier.valid() : _endOfCompilebarrier.release()
        if _endOfLoadBlock.valid() : _endOfLoadBlock.release()

    
    _filename = str()
    
    _mutex = OpenThreads.Mutex()
    _existingFilenameNodeMap = FilenameNodeMap()
    _nodesToRemove = Files()
    _nodesToAdd = FilenameNodeMap()
    _updatesMergedBlock = OpenThreads.Block()

    _incrementalCompileOperation = osgUtil.IncrementalCompileOperation()
    _endOfCompilebarrier = osg.BarrierOperation()
    _endOfLoadBlock = osg.RefBlockCount()
    
    _operationQueue = osg.OperationQueue()


class FilterHandler (osgGA.GUIEventHandler) : 

    FilterHandler(osgTerrain.GeometryTechnique* gt):
        _gt(gt) 

    def handle(ea, aa):

        
        if !_gt : return False

        switch(ea.getEventType())
        case(osgGA.GUIEventAdapter.KEYDOWN):
                if ea.getKey() == 'g' :
                    osg.notify(osg.NOTICE), "Gaussian"
                    _gt.setFilterMatrixAs(osgTerrain.GeometryTechnique.GAUSSIAN)
                    return True
                elif ea.getKey() == 's' :
                    osg.notify(osg.NOTICE), "Smooth"
                    _gt.setFilterMatrixAs(osgTerrain.GeometryTechnique.SMOOTH)
                    return True
                elif ea.getKey() == 'S' :
                    osg.notify(osg.NOTICE), "Sharpen"
                    _gt.setFilterMatrixAs(osgTerrain.GeometryTechnique.SHARPEN)
                    return True
                elif ea.getKey() == '+' :
                    _gt.setFilterWidth(_gt.getFilterWidth()*1.1)
                    osg.notify(osg.NOTICE), "Filter width = ", _gt.getFilterWidth()
                    return True
                elif ea.getKey() == '-' :
                    _gt.setFilterWidth(_gt.getFilterWidth()/1.1)
                    osg.notify(osg.NOTICE), "Filter width = ", _gt.getFilterWidth()
                    return True
                elif ea.getKey() == '>' :
                    _gt.setFilterBias(_gt.getFilterBias()+0.1)
                    osg.notify(osg.NOTICE), "Filter bias = ", _gt.getFilterBias()
                    return True
                elif ea.getKey() == '<' :
                    _gt.setFilterBias(_gt.getFilterBias()-0.1)
                    osg.notify(osg.NOTICE), "Filter bias = ", _gt.getFilterBias()
                    return True
                break
        default:
            break
        return False


    _gt = osg.observer_ptr<osgTerrain.GeometryTechnique>()





class LayerHandler (osgGA.GUIEventHandler) : 

    LayerHandler(osgTerrain.Layer* layer):
        _layer(layer) 

    def handle(ea, aa):

        
        if !_layer : return False

        scale = 1.2

        switch(ea.getEventType())
        case(osgGA.GUIEventAdapter.KEYDOWN):
                if ea.getKey() == 'q' :
                    _layer.transform(0.0, scale)
                    return True
                elif ea.getKey() == 'a' :
                    _layer.transform(0.0, 1.0/scale)
                    return True
                break
        default:
            break
        return False


    _layer = osg.observer_ptr<osgTerrain.Layer>()


def main(argc, argv):

    
    arguments = osg.ArgumentParser(argc, argv)

    # construct the viewer.
    viewer = osgViewer.Viewer(arguments)

    # set up the camera manipulators.
        keyswitchManipulator = osgGA.KeySwitchMatrixManipulator()

        keyswitchManipulator.addMatrixManipulator( '1', "Trackball", osgGA.TrackballManipulator() )
        keyswitchManipulator.addMatrixManipulator( '2', "Flight", osgGA.FlightManipulator() )
        keyswitchManipulator.addMatrixManipulator( '3', "Drive", osgGA.DriveManipulator() )
        keyswitchManipulator.addMatrixManipulator( '4', "Terrain", osgGA.TerrainManipulator() )

        pathfile = str()
        keyForAnimationPath = '5'
        while arguments.read("-p",pathfile) :
            apm = osgGA.AnimationPathManipulator(pathfile)
            if apm || !apm.valid() : 
                num = keyswitchManipulator.getNumMatrixManipulators()
                keyswitchManipulator.addMatrixManipulator( keyForAnimationPath, "Path", apm )
                keyswitchManipulator.selectMatrixManipulator(num)
                ++keyForAnimationPath

        viewer.setCameraManipulator( keyswitchManipulator.get() )


    # add the state manipulator
    viewer.addEventHandler( osgGA.StateSetManipulator(viewer.getCamera().getOrCreateStateSet()) )

    # add the stats handler
    viewer.addEventHandler(osgViewer.StatsHandler)()

    # add the record camera path handler
    viewer.addEventHandler(osgViewer.RecordCameraPathHandler)()

    # attach an IncrementaCompileOperation to allow the master loading 
    # to be handled with an incremental compile to avoid frame drops when large objects are added.
    viewer.setIncrementalCompileOperation(osgUtil.IncrementalCompileOperation())

    x = 0.0
    y = 0.0
    w = 1.0
    h = 1.0

    numLoadThreads = 1
    while arguments.read("--load-threads",numLoadThreads) :  

    masterOperation = MasterOperation()
    masterFilename = str()
    while arguments.read("-m",masterFilename) :
        masterOperation = MasterOperation(masterFilename, viewer.getIncrementalCompileOperation())
    

    terrainTile = osgTerrain.TerrainTile()
    locator = osgTerrain.Locator()
    validDataOperator = osgTerrain.NoDataValue(0.0)
    lastAppliedLayer = osgTerrain.Layer()

    locator.setCoordinateSystemType(osgTerrain.Locator.GEOCENTRIC)
    locator.setTransformAsExtents(-osg.PI, -osg.PI*0.5, osg.PI, osg.PI*0.5)

    layerNum = 0

    filterName = str()

    filter = osg.Texture.LINEAR

    float minValue, maxValue
    scale = 1.0
    offset = 0.0

    pos = 1
    while pos<arguments.argc() :
        filename = str()
        
        if arguments.read(pos, "--layer",layerNum) : 
            osg.notify(osg.NOTICE), "Set layer number to ", layerNum

        elif arguments.read(pos, "-b") :
            terrainTile.setTreatBoundariesToValidDataAsDefaultValue(True)
        
        elif arguments.read(pos, "-e",x,y,w,h) :
            # define the extents.
            locator.setCoordinateSystemType(osgTerrain.Locator.GEOCENTRIC)
            locator.setTransformAsExtents(x,y,x+w,y+h)

        elif arguments.read(pos, "--transform",offset, scale) || arguments.read(pos, "-t",offset, scale) :
            # define the extents.

        elif arguments.read(pos, "--cartesian",x,y,w,h) :
            # define the extents.
            locator.setCoordinateSystemType(osgTerrain.Locator.PROJECTED)
            locator.setTransformAsExtents(x,y,x+w,y+h)

        elif arguments.read(pos, "--hf",filename) :
            osg.notify(osg.NOTICE), "--hf ", filename

            hf = osgDB.readHeightFieldFile(filename)
            if hf.valid() :
                hfl = osgTerrain.HeightFieldLayer()
                hfl.setHeightField(hf.get())
                
                hfl.setLocator(locator.get())
                hfl.setValidDataOperator(validDataOperator.get())
                hfl.setMagFilter(filter)
                
                if offset!=0.0 || scale!=1.0 :
                    hfl.transform(offset,scale)
                
                terrainTile.setElevationLayer(hfl.get())
                
                lastAppliedLayer = hfl.get()
                
                osg.notify(osg.NOTICE), "created osgTerrain.HeightFieldLayer"
            else :
                osg.notify(osg.NOTICE), "failed to create osgTerrain.HeightFieldLayer"
            
            scale = 1.0
            offset = 0.0
            

        elif arguments.read(pos, "-d",filename) || arguments.read(pos, "--elevation-image",filename) :
            osg.notify(osg.NOTICE), "--elevation-image ", filename

            image = osgDB.readImageFile(filename)
            if image.valid() :
                imageLayer = osgTerrain.ImageLayer()
                imageLayer.setImage(image.get())
                imageLayer.setLocator(locator.get())
                imageLayer.setValidDataOperator(validDataOperator.get())
                imageLayer.setMagFilter(filter)
                
                if offset!=0.0 || scale!=1.0 :
                    imageLayer.transform(offset,scale)
                
                terrainTile.setElevationLayer(imageLayer.get())
                
                lastAppliedLayer = imageLayer.get()

                osg.notify(osg.NOTICE), "created Elevation osgTerrain.ImageLayer"
            else :
                osg.notify(osg.NOTICE), "failed to create osgTerrain.ImageLayer"

            scale = 1.0
            offset = 0.0
            
        
        elif arguments.read(pos, "-c",filename) || arguments.read(pos, "--image",filename) :
            osg.notify(osg.NOTICE), "--image ", filename, " x=", x, " y=", y, " w=", w, " h=", h

            image = osgDB.readImageFile(filename)
            if image.valid() :
                imageLayer = osgTerrain.ImageLayer()
                imageLayer.setImage(image.get())
                imageLayer.setLocator(locator.get())
                imageLayer.setValidDataOperator(validDataOperator.get())
                imageLayer.setMagFilter(filter)
                
                if offset!=0.0 || scale!=1.0 :
                    imageLayer.transform(offset,scale)

                terrainTile.setColorLayer(layerNum, imageLayer.get())

                lastAppliedLayer = imageLayer.get()

                osg.notify(osg.NOTICE), "created Color osgTerrain.ImageLayer"
            else :
                osg.notify(osg.NOTICE), "failed to create osgTerrain.ImageLayer"

            scale = 1.0
            offset = 0.0
            

        elif arguments.read(pos, "--filter",filterName) :
            if filterName=="NEAREST" :
                osg.notify(osg.NOTICE), "--filter ", filterName
                filter = osg.Texture.NEAREST
            elif filterName=="LINEAR" : 
                filter = osg.Texture.LINEAR
                osg.notify(osg.NOTICE), "--filter ", filterName
            else :
                osg.notify(osg.NOTICE), "--filter ", filterName, " unrecognized filter name, please use LINEAER or NEAREST."

            if terrainTile.getColorLayer(layerNum) :
                terrainTile.getColorLayer(layerNum).setMagFilter(filter)
            

        elif arguments.read(pos, "--tf",minValue, maxValue) :
            tf = osg.TransferFunction1D()
            
            numCells = 6
            delta = (maxValue-minValue)/float(numCells-1)
            v = minValue
            
            tf.allocate(6)
            tf.setColor(v, osg.Vec4(1.0,1.0,1.0,1.0)) v += delta
            tf.setColor(v, osg.Vec4(1.0,0.0,1.0,1.0)) v += delta
            tf.setColor(v, osg.Vec4(1.0,0.0,0.0,1.0)) v += delta
            tf.setColor(v, osg.Vec4(1.0,1.0,0.0,1.0)) v += delta
            tf.setColor(v, osg.Vec4(0.0,1.0,1.0,1.0)) v += delta
            tf.setColor(v, osg.Vec4(0.0,1.0,0.0,1.0))
            
            osg.notify(osg.NOTICE), "--tf ", minValue, " ", maxValue

            terrainTile.setColorLayer(layerNum, osgTerrain.ContourLayer(tf.get()))
        else :
            ++pos

    

    scene = osg.Group()

    if terrainTile.valid()  (terrainTile.getElevationLayer() || terrainTile.getColorLayer(0)) :
        osg.notify(osg.NOTICE), "Terrain created"
    
        scene.addChild(terrainTile.get())

        geometryTechnique = osgTerrain.GeometryTechnique()
        terrainTile.setTerrainTechnique(geometryTechnique.get())
        viewer.addEventHandler(FilterHandler(geometryTechnique.get()))
        viewer.addEventHandler(LayerHandler(lastAppliedLayer.get()))

    if masterOperation.valid() :
        osg.notify(osg.NOTICE), "Master operation created"

        masterOperation.open(scene.get())
    
    if scene.getNumChildren()==0 :
        osg.notify(osg.NOTICE), "No model created, please specify terrain or master file on command line."
        return 0
    
    viewer.setSceneData(scene.get())


    # start operation thread if a master file has been used.
    masterOperationThread = osg.OperationThread()
    
    typedef std.list< osg.OperationThread > OperationThreadList
    generalThreadList = OperationThreadList()
    
    if masterOperation.valid() : 
        masterOperationThread = osg.OperationThread()
        masterOperationThread.startThread()
        
        masterOperationThread.add(masterOperation.get())

#        if numLoadThreads>0 :
            operationQueue = osg.OperationQueue()
            masterOperation.setOperationQueue(operationQueue.get())

            for(unsigned int i=0 i<numLoadThreads ++i)
                thread = osg.OperationThread()
                thread.setOperationQueue(operationQueue.get())
                thread.startThread()
                generalThreadList.push_back(thread)
        
        viewer.addUpdateOperation(masterOperation.get())
    
    viewer.setThreadingModel(osgViewer.Viewer.SingleThreaded)
    
    # enable the use of compile contexts and associated threads.
    # osg.DisplaySettings.instance().setCompileContextsHint(True)

    # realize the graphics windows.
    viewer.realize()

    # run the viewers main loop
    return viewer.run()



if __name__ == "__main__":
    main(sys.argv)
