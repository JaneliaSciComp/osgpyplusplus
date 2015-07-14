#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgparticleeffects"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osg
from osgpypp import osgDB
from osgpypp import osgParticle
from osgpypp import osgText
from osgpypp import osgUtil
from osgpypp import osgViewer


# Translated from file 'osgparticleeffects.cpp'

# OpenSceneGraph example, osgparticleeffects.
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

#include <osg/Group>
#include <osg/Geode>
#include <osg/ShapeDrawable>
#include <osg/Texture2D>
#include <osg/PositionAttitudeTransform>
#include <osg/MatrixTransform>
#include <osg/io_utils>

#include <osgUtil/Optimizer>

#include <osgDB/ReadFile>

#include <osgText/Text>

#include <osgParticle/ExplosionEffect>
#include <osgParticle/ExplosionDebrisEffect>
#include <osgParticle/SmokeEffect>
#include <osgParticle/SmokeTrailEffect>
#include <osgParticle/FireEffect>

# for the grid data..
#include "../osghangglide/terrain_coords.h"

wind = osg.Vec3(1.0,0.0,0.0)            

def createAnimationPath(center, radius, looptime):

    
    # set up the animation path 
    animationPath = osg.AnimationPath()
    animationPath.setLoopMode(osg.AnimationPath.LOOP)
    
    numSamples = 40
    yaw = 0.0
    yaw_delta = 2.0*osg.PI/((float)numSamples-1.0)
    roll = osg.inDegrees(30.0)
    
    time = 0.0
    time_delta = looptime/(double)numSamples
    for(int i=0i<numSamples++i)
        position = osg.Vec3(center+osg.Vec3(sinf(yaw)*radius,cosf(yaw)*radius,0.0))
        rotation = osg.Quat(osg.Quat(roll,osg.Vec3(0.0,1.0,0.0))*osg.Quat(-(yaw+osg.inDegrees(90.0)),osg.Vec3(0.0,0.0,1.0)))
        
        animationPath.insert(time,osg.AnimationPath.ControlPoint(position,rotation))

        yaw += yaw_delta
        time += time_delta

    return animationPath    

def createMovingModel(center, radius):

    
    animationLength = 10.0

    animationPath = createAnimationPath(center,radius,animationLength)

    model = osg.Group()

    glider = osgDB.readNodeFile("glider.osgt")
    if glider :
        bs = glider.getBound()
        size = radius/bs.radius()*0.15

        positioned = osg.MatrixTransform()
        positioned.setDataVariance(osg.Object.STATIC)
        positioned.setMatrix(osg.Matrix.translate(-bs.center())*
                                     osg.Matrix.scale(size,size,size)*
                                     osg.Matrix.rotate(osg.inDegrees(-90.0),0.0,0.0,1.0))
    
        positioned.addChild(glider)
    
        xform = osg.PositionAttitudeTransform()
        xform.setDataVariance(osg.Object.DYNAMIC)
        xform.getOrCreateStateSet().setMode(GL_NORMALIZE, osg.StateAttribute.ON)
        xform.setUpdateCallback(osg.AnimationPathCallback(animationPath,0.0,0.5))
        xform.addChild(positioned)

        model.addChild(xform)
 
    cessna = osgDB.readNodeFile("cessna.osgt")
    if cessna :
        bs = cessna.getBound()
        size = radius/bs.radius()*0.15

        positioned = osg.MatrixTransform()
        positioned.getOrCreateStateSet().setMode(GL_NORMALIZE, osg.StateAttribute.ON)
        positioned.setDataVariance(osg.Object.STATIC)
        positioned.setMatrix(osg.Matrix.translate(-bs.center())*
                                     osg.Matrix.scale(size,size,size)*
                                     osg.Matrix.rotate(osg.inDegrees(180.0),0.0,0.0,1.0))
    
        #positioned.addChild(cessna)
        positioned.addChild(cessna)
    
        xform = osg.MatrixTransform()
        xform.setDataVariance(osg.Object.DYNAMIC)
        xform.setUpdateCallback(osg.AnimationPathCallback(animationPath,0.0,1.0))
        xform.addChild(positioned)

        model.addChild(xform)
    
    return model


def computeTerrainIntersection(subgraph, x, y):


    
    bs = subgraph.getBound()
    zMax = bs.center().z()+bs.radius()
    zMin = bs.center().z()-bs.radius()
    
    intersector = osgUtil.LineSegmentIntersector(osg.Vec3(x,y,zMin),osg.Vec3(x,y,zMax))

    iv = osgUtil.IntersectionVisitor(intersector)

    subgraph.accept(iv)

    if intersector.containsIntersections() :
        return intersector.getFirstIntersection().getWorldIntersectPoint()

    return osg.Vec3(x,y,0.0)


#######################################
# MAIN SCENE GRAPH BUILDING FUNCTION
#######################################

def build_world(root):

    

    terrainGeode = osg.Geode()
    # create terrain
        stateset = osg.StateSet()
        image = osgDB.readImageFile("Images/lz.rgb")
        if image :
            texture = osg.Texture2D()
            texture.setImage(image)
            stateset.setTextureAttributeAndModes(0,texture,osg.StateAttribute.ON)

        terrainGeode.setStateSet( stateset )

        size = 1000 # 10km
        scale = size/39.0 # 10km
        z_scale = scale*3.0

        grid = osg.HeightField()
        grid.allocate(38,39)
        grid.setXInterval(scale)
        grid.setYInterval(scale)

        for(unsigned int r=0r<39++r)
            for(unsigned int c=0c<38++c)
                grid.setHeight(c,r,z_scale*vertex[r+c*39][2])
        terrainGeode.addDrawable(osg.ShapeDrawable(grid))
        
        root.addChild(terrainGeode)


    # create particle effects
        position = computeTerrainIntersection(terrainGeode,100.0,100.0)

        explosion = osgParticle.ExplosionEffect(position, 10.0)
        explosionDebri = osgParticle.ExplosionDebrisEffect(position, 10.0)
        smoke = osgParticle.SmokeEffect(position, 10.0)
        fire = osgParticle.FireEffect(position, 10.0)

        explosion.setWind(wind)
        explosionDebri.setWind(wind)
        smoke.setWind(wind)
        fire.setWind(wind)

        root.addChild(explosion)
        root.addChild(explosionDebri)
        root.addChild(smoke)
        root.addChild(fire)
    
    # create particle effects
        position = computeTerrainIntersection(terrainGeode,200.0,100.0)

        explosion = osgParticle.ExplosionEffect(position, 1.0)
        explosionDebri = osgParticle.ExplosionDebrisEffect(position, 1.0)
        smoke = osgParticle.SmokeEffect(position, 1.0)
        fire = osgParticle.FireEffect(position, 1.0)

        explosion.setWind(wind)
        explosionDebri.setWind(wind)
        smoke.setWind(wind)
        fire.setWind(wind)

        root.addChild(explosion)
        root.addChild(explosionDebri)
        root.addChild(smoke)
        root.addChild(fire)

    # create the moving models.
        root.addChild(createMovingModel(osg.Vec3(500.0,500.0,500.0),300.0))


# class to handle events with a pick
class PickHandler (osgGA.GUIEventHandler) : 

    PickHandler()         
    
    def handle(ea, aa):
    
        
        switch(ea.getEventType())
            case(osgGA.GUIEventAdapter.PUSH):
                viewer = dynamic_cast<osgViewer.Viewer*>(aa)
                pick(viewer,ea)
            return False

        default:
            return False

    def pick(viewer, ea):

        
        root = dynamic_cast<osg.Group*>(viewer.getSceneData())       
        if  not root : return
        
        intersections = osgUtil.LineSegmentIntersector.Intersections()
        if viewer.computeIntersections(ea,intersections) :
            hit = *intersections.begin()

            handleMovingModels = False
            nodePath = hit.nodePath
            for(osg.NodePath.const_iterator nitr=nodePath.begin()
                not = nodePath.end()
                ++nitr)
                transform = dynamic_cast< osg.Transform*>(*nitr)
                if transform :
                    if transform.getDataVariance()==osg.Object.DYNAMIC : handleMovingModels=True
            
            position =  hit.getLocalIntersectPoint() if (handleMovingModels) else  hit.getWorldIntersectPoint()
            scale = 10.0 * ((float)rand() / (float)RAND_MAX)
            intensity = 1.0

            explosion = osgParticle.ExplosionEffect(position, scale, intensity)
            explosionDebri = osgParticle.ExplosionDebrisEffect(position, scale, intensity)
            fire = osgParticle.FireEffect(position, scale, intensity)
            smoke = 0
            if handleMovingModels :
                smoke =  osgParticle.SmokeTrailEffect(position, scale, intensity)
            smoke = osgParticle.SmokeEffect(position, scale, intensity)
            
            explosion.setWind(wind)
            explosionDebri.setWind(wind)
            smoke.setWind(wind)
            fire.setWind(wind)

            effectsGroup = osg.Group()
            effectsGroup.addChild(explosion)
            effectsGroup.addChild(explosionDebri)
            effectsGroup.addChild(smoke)
            effectsGroup.addChild(fire)
            

            if handleMovingModels :
                # insert particle effects alongside the hit node, therefore able to track that nodes movement,
                # however, this does require us to insert the ParticleSystem itself into the root of the scene graph
                # separately from the the main particle effects group which contains the emitters and programs.
                # the follow code block implements this, note the path for handling particle effects which arn't attached to 
                # moving models is easy - just a single line of code not 
            
                # tell the effects not to attach to the particle system locally for rendering, as we'll handle add it into the 
                # scene graph ourselves.
                explosion.setUseLocalParticleSystem(False)
                explosionDebri.setUseLocalParticleSystem(False)
                smoke.setUseLocalParticleSystem(False)
                fire.setUseLocalParticleSystem(False)

                # find a place to insert the particle effects group alongside the hit node.
                # there are two possible ways that this can be done, either insert it into
                # a pre-existing group along side the hit node, or if no pre existing group
                # is found then this needs to be inserted above the hit node, and then the
                # particle effect can be inserted into this.
                hitNode = hit.nodePath.back()
                parents = hitNode.getParents()                
                insertGroup = 0
                numGroupsFound = 0
                for(osg.Node.ParentList.iterator itr=parents.begin()
                    not = parents.end()
                    ++itr)
                    if typeid(*(*itr))==typeid(osg.Group) :
                        ++numGroupsFound
                        insertGroup = *itr
                if numGroupsFound==parents.size()  and  numGroupsFound==1  and  insertGroup :
                    osg.notify(osg.INFO), "PickHandler.pick(,) hit node's parent is a single osg.Group so we can simple the insert the particle effects group here."

                    # just reuse the existing group.
                    insertGroup.addChild(effectsGroup)
                else:
                    osg.notify(osg.INFO), "PickHandler.pick(,) hit node doesn't have an appropriate osg.Group node to insert particle effects into, inserting a osg.Group."()
                    insertGroup = osg.Group()
                    for(osg.Node.ParentList.iterator itr=parents.begin()
                        not = parents.end()
                        ++itr)
                        (*itr).replaceChild(hit.nodePath.back(),insertGroup)
                    insertGroup.addChild(hitNode)
                    insertGroup.addChild(effectsGroup)

                # finally insert the particle systems into a Geode and attach to the root of the scene graph so the particle system
                # can be rendered.
                geode = osg.Geode()
                geode.addDrawable(explosion.getParticleSystem())
                geode.addDrawable(explosionDebri.getParticleSystem())
                geode.addDrawable(smoke.getParticleSystem())
                geode.addDrawable(fire.getParticleSystem())
                
                root.addChild(geode)

            else:
                # when we don't have moving models we can simple insert the particle effect into the root of the scene graph
                osg.notify(osg.INFO), "PickHandler.pick(,) adding particle effects to root node."
                root.addChild(effectsGroup)

#if 0            
            geode = osg.Geode()
            geode.addDrawable(osg.ShapeDrawable(osg.Sphere(position,scale)))
            group.addChild(geode)
#endif
 
    virtual ~PickHandler() 


# function used in debugging
def insertParticle(root, center, radius):
    
    handleMovingModels = False

    position = center + 
               osg.Vec3( radius * (((float)rand() / (float)RAND_MAX)-0.5)*2.0,
                          radius * (((float)rand() / (float)RAND_MAX)-0.5)*2.0,
                          0.0)

    scale = 10.0 * ((float)rand() / (float)RAND_MAX)
    intensity = 1.0

    explosion = osgParticle.ExplosionEffect(position, scale, intensity)
    explosionDebri = osgParticle.ExplosionDebrisEffect(position, scale, intensity)
    fire = osgParticle.FireEffect(position, scale, intensity)
    smoke = 0
    if handleMovingModels :
        smoke =  osgParticle.SmokeTrailEffect(position, scale, intensity)
    smoke = osgParticle.SmokeEffect(position, scale, intensity)

    explosion.setWind(wind)
    explosionDebri.setWind(wind)
    smoke.setWind(wind)
    fire.setWind(wind)

    effectsGroup = osg.Group()
    effectsGroup.addChild(explosion)
    effectsGroup.addChild(explosionDebri)
    effectsGroup.addChild(smoke)
    effectsGroup.addChild(fire)

    root.addChild(effectsGroup)

#######################################
# main()
#######################################

int main(int, char **)
    # construct the viewer.
    viewer = osgViewer.Viewer()

    # register the pick handler
    viewer.addEventHandler(PickHandler())
    
    root = osg.Group()
    build_world(root)

    optimizer = osgUtil.Optimizer()
    optimizer.optimize(root)
   
    # add a viewport to the viewer and attach the scene graph.
    viewer.setSceneData(root)
        
    return viewer.run()


if __name__ == "__main__":
    main(sys.argv)
