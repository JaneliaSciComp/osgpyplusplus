#!/usr/bin/env python
#
# This source file is part of the osgBoostPython library
# 
# Copyright (C) 2009-2010 Jean-Sebastien Guay
# 
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the Free Software
# Foundation; either version 3 of the License, or (at your option) any later
# version.
# 
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more details.
# http://www.gnu.org/copyleft/lesser.txt.
#

import sys
import math
import thread
from osgpypp import osg, osgDB, osgGA, osgViewer
# import osg
# import osgDB
# import osgGA
# import osgViewer

osg.Matrix = osg.Matrixd
osg.Vec3 = osg.Vec3f

# //
# // A simple demo demonstrating planar reflections using multiple renderings
# // of a subgraph, overriding of state attribures and use of the stencil buffer.
# //
# // The multipass system implemented here is a variation if Mark Kilgard's
# // paper "Improving Shadows and Reflections via the Stencil Buffer" which
# // can be found on the developer parts of the NVidia web site.
# //
# // The variations comes from the fact that the mirrors stencil values
# // are done on the first pass, rather than the second as in Mark's paper.
# // The second pass is now Mark's first pass - drawing the unreflected scene,
# // but also unsets the stencil buffer.  This variation stops the unreflected
# // world poking through the mirror to be seen in the final rendering and
# // also obscures the world correctly when on the reverse side of the mirror.
# // Although there is still some unresolved issue with the clip plane needing
# // to be flipped when looking at the reverse side of the mirror.  Niether
# // of these issues are mentioned in the Mark's paper, but trip us up when
# // we apply them.


def createMirrorTexturedState(filename):
    dstate = osg.StateSet();
    dstate.setMode(osg.GL_CULL_FACE,osg.StateAttribute.OFF|osg.StateAttribute.PROTECTED);

    #// set up the texture.
    image = osgDB.readImageFile(filename);
    if (image):
        texture = osg.Texture2D();
        texture.setImage(image);
        dstate.setTextureAttributeAndModes(0,texture,osg.StateAttribute.ON|osg.StateAttribute.PROTECTED);

    return dstate;

def createMirrorSurface(xMin,xMax,yMin,yMax,z):
    #// set up the drawstate.

    #// set up the Geometry.
    geom = osg.Geometry();

    coords = osg.Vec3Array();
    coords.append(osg.Vec3f(xMin,yMax,z))
    coords.append(osg.Vec3f(xMin,yMin,z))
    coords.append(osg.Vec3f(xMax,yMin,z))
    coords.append(osg.Vec3f(xMax,yMax,z))
    geom.setVertexArray(coords);

    norms = osg.Vec3Array();
    norms.append(osg.Vec3f(0.0,0.0,1.0))
    geom.setNormalArray(norms);
    geom.normalBinding = osg.Geometry.BIND_OVERALL

    tcoords = osg.Vec2Array()
    tcoords.append(osg.Vec2f(0.0,1.0))
    tcoords.append(osg.Vec2f(0.0,0.0))
    tcoords.append(osg.Vec2f(1.0,0.0))
    tcoords.append(osg.Vec2f(1.0,1.0))
    geom.setTexCoordArray(0,tcoords);

    colours = osg.Vec4Array();
    colours.append(osg.Vec4f(1.0,1.0,1.0,1.0))
    geom.setColorArray(colours);
    geom.colorBinding = osg.Geometry.BIND_OVERALL;

    geom.addPrimitiveSet(osg.DrawArrays(osg.PrimitiveSet.QUADS,0,4));

    return geom;

def toRad(degrees):
    return degrees*math.pi/180.0

def toDeg(rad):
    return rad/math.pi*180.0

def setupBin1(rootNode, mirror,z):
    #// set up the stencil ops so that the stencil buffer get set at
    #// the mirror plane
    stencil = osg.Stencil();
    stencil.setFunction(osg.Stencil.ALWAYS,1,4294967295)
    stencil.setOperation(osg.Stencil.KEEP, osg.Stencil.KEEP, osg.Stencil.REPLACE);

    #// switch off the writing to the color bit planes.
    colorMask = osg.ColorMask();
    colorMask.setMask(False,False,False,False);

    statesetBin1 = osg.StateSet()
    statesetBin1.setRenderBinDetails(1,"RenderBin");
    statesetBin1.setMode(osg.GL_CULL_FACE,osg.StateAttribute.OFF);
    statesetBin1.setAttributeAndModes(stencil,osg.StateAttribute.ON);
    statesetBin1.setAttribute(colorMask);

    #// set up the mirror geode.
    geode = osg.Geode();
    geode.addDrawable(mirror);
    geode.setStateSet(statesetBin1);

    rootNode.addChild(geode);

#// bin one - draw scene without mirror or reflection, unset
#// stencil values where scene is infront of mirror and hence
#// occludes the mirror.
def setupBin2(rootNode, model,z):
    stencil = osg.Stencil();
    stencil.setFunction(osg.Stencil.ALWAYS,0,4294967295);
    stencil.setOperation(osg.Stencil.KEEP, osg.Stencil.KEEP, osg.Stencil.REPLACE);

    statesetBin2 = osg.StateSet();
    statesetBin2.setRenderBinDetails(2,"RenderBin");
    statesetBin2.setAttributeAndModes(stencil,osg.StateAttribute.ON);

    groupBin2 = osg.Group();
    groupBin2.setStateSet(statesetBin2);
    groupBin2.addChild(model);

    rootNode.addChild(groupBin2);
    
#// bin3  - set up the depth to the furthest depth value
def setupBin3(rootNode, mirror,z):
    #// set up the stencil ops so that only operator on this mirrors stencil value.
    stencil = osg.Stencil()
    stencil.setFunction(osg.Stencil.EQUAL,1,4294967295);
    stencil.setOperation(osg.Stencil.KEEP, osg.Stencil.KEEP, osg.Stencil.KEEP);

    #// switch off the writing to the color bit planes.
    colorMask = osg.ColorMask();
    colorMask.setMask(False,False,False,False);

    #// set up depth so all writing to depth goes to maximum depth.
    depth = osg.Depth();
    depth.setFunction(osg.Depth.ALWAYS);
    depth.setRange(1.0,1.0);

    statesetBin3 = osg.StateSet();
    statesetBin3.setRenderBinDetails(3,"RenderBin");
    statesetBin3.setMode(osg.GL_CULL_FACE,osg.StateAttribute.OFF);
    statesetBin3.setAttributeAndModes(stencil,osg.StateAttribute.ON);
    statesetBin3.setAttribute(colorMask);
    statesetBin3.setAttribute(depth);

    #// set up the mirror geode.
    geode = osg.Geode();
    geode.addDrawable(mirror);
    geode.setStateSet(statesetBin3);

    rootNode.addChild(geode);

#// bin4  - draw the reflection.
def setupBin4(rootNode,model,z):
    #// now create the 'reflection' of the loaded model by applying
    #// create a Transform which flips the loaded model about the z axis
    #// relative to the mirror node, the loadedModel is added to the
    #// Transform so now appears twice in the scene, but is shared so there
    #// is negligable memory overhead.  Also use an osg.StateSet
    #// attached to the Transform to override the face culling on the subgraph
    #// to prevert an 'inside' out view of the reflected model.
    #// set up the stencil ops so that only operator on this mirrors stencil value.

    #// this clip plane removes any of the scene which when mirror would
    #// poke through the mirror.  However, this clip plane should really
    #// flip sides once the eye point goes to the back of the mirror...
    clipplane = osg.ClipPlane();
    clipplane.setClipPlane(0.0,0.0,-1.0,z); 
    clipplane.setClipPlaneNum(0);

    clipNode = osg.ClipNode();
    clipNode.addClipPlane(clipplane);

    dstate = clipNode.getOrCreateStateSet();
    dstate.setRenderBinDetails(4,"RenderBin");
    dstate.setMode(osg.GL_CULL_FACE,osg.StateAttribute.OVERRIDE|osg.StateAttribute.OFF);

    stencil = osg.Stencil();
    stencil.setFunction(osg.Stencil.EQUAL,1,4294967295);
    stencil.setOperation(osg.Stencil.KEEP, osg.Stencil.KEEP, osg.Stencil.KEEP);
    
    dstate.setAttributeAndModes(stencil,osg.StateAttribute.ON);

    reverseMatrix = osg.MatrixTransform();
    reverseMatrix.stateSet = dstate
    reverseMatrix.preMult(osg.Matrix.translate(0.0,0.0,-z)*
                 osg.Matrix.scale(1.0,1.0,-1.0)*
                 osg.Matrix.translate(0.0,0.0,z));

    reverseMatrix.addChild(model);

    clipNode.addChild(reverseMatrix);

    rootNode.addChild(clipNode);

#// bin5  - draw the textured mirror and blend it with the reflection.
def setupBin5(rootNode, mirror,z):
    #// set up depth so all writing to depth goes to maximum depth.
    depth = osg.Depth();
    depth.setFunction(osg.Depth.ALWAYS);

    stencil = osg.Stencil();
    stencil.setFunction(osg.Stencil.EQUAL,1,4294967295);
    stencil.setOperation(osg.Stencil.KEEP, osg.Stencil.KEEP, osg.Stencil.ZERO);


    #// set up additive blending.
    trans = osg.BlendFunc();
    trans.setFunction(osg.BlendFunc.ONE,osg.BlendFunc.ONE);

    statesetBin5 = createMirrorTexturedState("Images/tank.rgb");

    statesetBin5.setRenderBinDetails(5,"RenderBin");
    statesetBin5.setMode(osg.GL_CULL_FACE,osg.StateAttribute.OFF);
    statesetBin5.setAttributeAndModes(stencil,osg.StateAttribute.ON);
    statesetBin5.setAttributeAndModes(trans,osg.StateAttribute.ON);
    statesetBin5.setAttribute(depth);

    #// set up the mirror geode.
    geode = osg.Geode();
    geode.addDrawable(mirror);
    geode.setStateSet(statesetBin5);

    rootNode.addChild(geode);



def createMirroredScene(model):
    #// calculate where to place the mirror according to the
    #// loaded models bounding sphere.
    bs = model.getBound();

    width_factor = 1.5;
    height_factor = 0.3;

    xMin = bs._center.x-bs._radius*width_factor;
    xMax = bs._center.x+bs._radius*width_factor;
    yMin = bs._center.y-bs._radius*width_factor;
    yMax = bs._center.y+bs._radius*width_factor;

    z = bs._center.z-bs._radius*height_factor;

    #// create a textured, transparent node at the appropriate place.
    mirror = createMirrorSurface(xMin,xMax,yMin,yMax,z);


    rootNode = osg.MatrixTransform();
    rootNode.setMatrix(osg.Matrix.rotate(toRad(45.0),1.0,0.0,0.0));

    #// make sure that the global color mask exists.
    rootColorMask = osg.ColorMask();
    rootColorMask.setMask(True,True,True,True);

    #// set up depth to be inherited by the rest of the scene unless
    #// overrideen. this is overridden in bin 3.
    rootDepth = osg.Depth()
    rootDepth.setFunction(osg.Depth.LESS);
    rootDepth.setRange(0.0,1.0);

    rootStateSet = osg.StateSet();
    rootStateSet.setAttribute(rootColorMask);
    rootStateSet.setAttribute(rootDepth);

    rootNode.setStateSet(rootStateSet)


    #// bin1  - set up the stencil values and depth for mirror.
    setupBin1(rootNode,mirror,z)
    setupBin2(rootNode,model,z)
    setupBin3(rootNode,mirror,z)
    setupBin4(rootNode,model,z)
    setupBin5(rootNode,mirror,z)

    return rootNode;


def main(argv):
    # use an ArgumentParser object to manage the program arguments.
    viewer = osgViewer.Viewer()
#    viewer.setThreadingModel(osgViewer.Viewer.SingleThreaded)

    # read the scene from the list of file specified commandline args.
    loadedModel = osgDB.readNodeFile("cessna.osg")
    if loadedModel == None:
        raise Exception('Could not load model file (is OSG_FILE_PATH set and correct?)')

    # create a transform to spin the model.
    loadedModelTransform = osg.MatrixTransform()
    loadedModelTransform.addChild(loadedModel)

    print loadedModelTransform.getBound()._center
#todo:    nc = osg.AnimationPathCallback(loadedModelTransform.getBound()._center,osg.Vec3(0.0,0.0,1.0),osg.inDegrees(45.0));
#    loadedModelTransform.setUpdateCallback(nc)

    rootNode = osg.Group()
    rootNode.stateSet.dataVariance = osg.Object.DYNAMIC
    rootNode.addChild(createMirroredScene(loadedModelTransform))

    viewer.addEventHandler(osgViewer.HelpHandler())
    viewer.addEventHandler(osgViewer.StatsHandler())
    viewer.addEventHandler(osgGA.StateSetManipulator(rootNode.stateSet))
    viewer.setSceneData(rootNode)
    print "set scene data"

    #hint to tell viewer to request stencil buffer when setting up windows
    osg.DisplaySettings().setMinimumNumStencilBits(8)
#    osg.DisplaySettings.instance().setMinimumNumStencilBits(8);

    osgDB.writeNodeFile(rootNode, "test_reflect.osg");

    viewer.run() #we need run, because that sets up a trackballmanipulator and so we have the correct "look" into the scene.
    return 0

if __name__ == "__main__":
    main(sys.argv)
