#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osglightpoint"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osg
from osgpypp import osgDB
from osgpypp import osgSim
from osgpypp import osgUtil
from osgpypp import osgViewer

# OpenSceneGraph example, osglightpoint.
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


#include <osg/GL>
#include <osgViewer/Viewer>

#include <osg/MatrixTransform>
#include <osg/Billboard>
#include <osg/Geode>
#include <osg/Group>
#include <osg/ShapeDrawable>
#include <osg/Notify>
#include <osg/PointSprite>
#include <osg/Texture2D>
#include <osg/BlendFunc>

#include <osgDB/Registry>
#include <osgDB/ReadFile>

#include <osgUtil/Optimizer>

#include <osgSim/LightPointNode>

#include <iostream>

#define INTERPOLATE(member) lp.member = start.member*rstart + end.member*rend

void addToLightPointNode(osgSim.LightPointNode lpn,osgSim.LightPoint start,osgSim.LightPoint end,unsigned int noSteps)
    if noSteps<=1 :
        lpn.addLightPoint(start)
        return
    
    rend =  0.0f
    rdelta =  1.0f/((float)noSteps-1.0f)
    
    lpn.getLightPointList().reserve(noSteps)
    
    for(unsigned int i=0i<noSteps++i,rend+=rdelta)
        rstart =  1.0f-rend
        lp = osgSim.LightPoint(start)
        INTERPOLATE(_position)
        INTERPOLATE(_intensity)
        INTERPOLATE(_color)
        INTERPOLATE(_radius)

        lpn.addLightPoint(lp)
        

#undef INTERPOLATE

usePointSprites = bool()

def createLightPointsDatabase():
    start = osgSim.LightPoint()
    end = osgSim.LightPoint()

    start._position.set(-500.0f,-500.0f,0.0f)
    start._color.set(1.0f,0.0f,0.0f,1.0f)
    
    end._position.set(500.0f,-500.0f,0.0f)
    end._color.set(1.0f,1.0f,1.0f,1.0f)
    
    transform =  new osg.MatrixTransform
    
    transform.setDataVariance(osg.Object.STATIC)
    transform.setMatrix(osg.Matrix.scale(0.1,0.1,0.1))

    start_delta = osg.Vec3(0.0f,10.0f,0.0f)
    end_delta = osg.Vec3(0.0f,10.0f,1.0f)

    noStepsX =  100
    noStepsY =  100

#     osgSim.BlinkSequence* bs = new osgSim.BlinkSequence
#     bs.addPulse(1.0,osg.Vec4(1.0f,0.0f,0.0f,1.0f))
#     bs.addPulse(0.5,osg.Vec4(0.0f,0.0f,0.0f,0.0f)) # off
#     bs.addPulse(1.5,osg.Vec4(1.0f,1.0f,0.0f,1.0f))
#     bs.addPulse(0.5,osg.Vec4(0.0f,0.0f,0.0f,0.0f)) # off
#     bs.addPulse(1.0,osg.Vec4(1.0f,1.0f,1.0f,1.0f))
#     bs.addPulse(0.5,osg.Vec4(0.0f,0.0f,0.0f,0.0f)) # off
    

#    osgSim.Sector* sector = new osgSim.ConeSector(osg.Vec3(0.0f,0.0f,1.0f),osg.inDegrees(45.0),osg.inDegrees(45.0))
#    osgSim.Sector* sector = new osgSim.ElevationSector(-osg.inDegrees(45.0),osg.inDegrees(45.0),osg.inDegrees(45.0))
#    osgSim.Sector* sector = new osgSim.AzimSector(-osg.inDegrees(45.0),osg.inDegrees(45.0),osg.inDegrees(90.0))
#     osgSim.Sector* sector = new osgSim.AzimElevationSector(osg.inDegrees(180),osg.inDegrees(90), # azim range
#                                                                 osg.inDegrees(0.0),osg.inDegrees(90.0), # elevation range
#                                                                 osg.inDegrees(5.0))

    for(int i=0i<noStepsY++i)

#         osgSim.BlinkSequence* local_bs = new osgSim.BlinkSequence(*bs)
#         local_bs.setSequenceGroup(new osgSim.BlinkSequence.SequenceGroup((double)i*0.1))        
#         start._blinkSequence = local_bs

#        start._sector = sector

        lpn =  new osgSim.LightPointNode

        #
        set =  lpn.getOrCreateStateSet()

        if usePointSprites :
            lpn.setPointSprite()

            # Set point sprite texture in LightPointNode StateSet.
            tex =  new osg.Texture2D()
            tex.setImage(osgDB.readImageFile("Images/particle.rgb"))
            set.setTextureAttributeAndModes(0, tex, osg.StateAttribute.ON)

        #set.setMode(GL_BLEND, osg.StateAttribute.ON)
        #osg.BlendFunc *fn = new osg.BlendFunc()
        #fn.setFunction(osg.BlendFunc.SRC_ALPHA, osg.BlendFunc.DST_ALPHA)
        #set.setAttributeAndModes(fn, osg.StateAttribute.ON)
        #

        addToLightPointNode(*lpn,start,end,noStepsX)
        
        start._position += start_delta
        end._position += end_delta
        
        transform.addChild(lpn)    
        
    group =  new osg.Group
    group.addChild(transform)
    
    
    group = return()

static osg.Node* CreateBlinkSequenceLightNode()
   lightPointNode =  new osgSim.LightPointNode

   lpList = osgSim.LightPointNode.LightPointList()

   osg.ref_ptr<osgSim.SequenceGroup>   seq_0
   seq_0 = new osgSim.SequenceGroup
   seq_0._baseTime = 0.0

   osg.ref_ptr<osgSim.SequenceGroup>   seq_1
   seq_1 = new osgSim.SequenceGroup
   seq_1._baseTime = 0.5

   max_points =  32
   for( int i = 0 i < max_points ++i )
      lp = osgSim.LightPoint()
      x =  cos( (2.0*osg.PI*i)/max_points )
      z =  sin( (2.0*osg.PI*i)/max_points )
      lp._position.set( x, 0.0f, z + 30.0f )
      lp._blinkSequence = new osgSim.BlinkSequence
      for( int j = 10 j > 0 --j )
         intensity =  j/10.0f
         lp._blinkSequence.addPulse( 1.0/max_points,
                                     osg.Vec4( intensity, intensity, intensity, intensity ) )
      if  max_points > 10  :
         lp._blinkSequence.addPulse( 1.0 - 10.0/max_points,
                                     osg.Vec4( 0.0f, 0.0f, 0.0f, 0.0f ) )

      if  i  1  :
         lp._blinkSequence.setSequenceGroup( seq_1.get() )
      else:
         lp._blinkSequence.setSequenceGroup( seq_0.get() )
      lp._blinkSequence.setPhaseShift( i/(static_cast<double>(max_points)) )
      lpList.push_back( lp )

   lightPointNode.setLightPointList( lpList )

   lightPointNode = return()

def main(argc, argv):
    # use an ArgumentParser object to manage the program arguments.
    arguments = osg.ArgumentParser(argc,argv)

    # set up the usage document, in case we need to print out how to use this program.
    arguments.getApplicationUsage().setDescription(arguments.getApplicationName()+" is the example which demonstrates use high quality light point, typically used for naviagional lights.")
    arguments.getApplicationUsage().setCommandLineUsage(arguments.getApplicationName()+" [options] filename ...")
    arguments.getApplicationUsage().addCommandLineOption("-h or --help","Display this information")
    arguments.getApplicationUsage().addCommandLineOption("--sprites","Point sprites.")

    # construct the viewer.
    viewer = osgViewer.Viewer()

    # if user request help write it out to cout.
    if arguments.read("-h") || arguments.read("--help") :
        arguments.getApplicationUsage().write(std.cout)
        return 1

    usePointSprites = false
    while arguments.read("--sprites") :  usePointSprites = true 

    rootnode =  new osg.Group

    # load the nodes from the commandline arguments.
    rootnode.addChild(osgDB.readNodeFiles(arguments))
    rootnode.addChild(createLightPointsDatabase())
    rootnode.addChild(CreateBlinkSequenceLightNode())
    
    # run optimization over the scene graph
    optimzer = osgUtil.Optimizer()
    optimzer.optimize(rootnode)
     
    # add a viewport to the viewer and attach the scene graph.
    viewer.setSceneData( rootnode )
    
    return viewer.run()


if __name__ == "__main__":
    main(sys.argv)
