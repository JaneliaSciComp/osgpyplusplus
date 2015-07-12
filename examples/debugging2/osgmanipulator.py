#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgmanipulator"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osg
from osgpypp import osgDB
from osgpypp import osgManipulator
from osgpypp import osgText
from osgpypp import osgUtil
from osgpypp import osgViewer
from osgpypp import osgGA


# Translated from file 'osgmanipulator.cpp'

# OpenSceneGraph example, osgmanipulator.
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


class PlaneConstraint(osgManipulator.Constraint):
    def __init__(self):
        osgManipulator.Constraint.__init__(self)

    def constrain(command):
        OSG_NOTICE, "PlaneConstraint TranslateInLineCommand ", command.getTranslation()
        return True

    def constrain(command):
        #command.setTranslation(osg.Vec3(0.0,0.0,0.0))
        OSG_NOTICE, "PlaneConstraint TranslateInPlaneCommand ", command.getTranslation()
        return True

    def constrain(command):
        #command.setScale(1.0)
        OSG_NOTICE, "PlaneConstraint Scale1DCommand", command.getScale()
        return True

    def constrain(command):
        #command.setScale(osg.Vec2d(1.0,1.0))
        OSG_NOTICE, "PlaneConstraint Scale2DCommand ", command.getScale()
        return True

    def constrain(command):
        OSG_NOTICE, "PlaneConstraint ScaleUniformCommand", command.getScale()
        return True            

def createDragger(name):
    dragger = 0
    if "TabPlaneDragger" == name :
        d = osgManipulator.TabPlaneDragger()
        d.setupDefaultGeometry()
        d.addConstraint(PlaneConstraint())
        dragger = d
    elif "TabPlaneTrackballDragger" == name :
        d = osgManipulator.TabPlaneTrackballDragger()
        d.setupDefaultGeometry()
        dragger = d
    elif "TabBoxTrackballDragger" == name :
        d = osgManipulator.TabBoxTrackballDragger()
        d.setupDefaultGeometry()
        dragger = d
    elif "TrackballDragger" == name :
        d = osgManipulator.TrackballDragger()
        d.setupDefaultGeometry()
        dragger = d
    elif "Translate1DDragger" == name :
        d = osgManipulator.Translate1DDragger()
        d.setupDefaultGeometry()
        dragger = d
    elif "Translate2DDragger" == name :
        d = osgManipulator.Translate2DDragger()
        d.setupDefaultGeometry()
        dragger = d
    elif "TranslateAxisDragger" == name :
        d = osgManipulator.TranslateAxisDragger()
        d.setupDefaultGeometry()
        dragger = d
    elif "TranslatePlaneDragger" == name :
        d = osgManipulator.TranslatePlaneDragger()
        d.setupDefaultGeometry()
        dragger = d
    elif "Scale1DDragger" == name :
        d = osgManipulator.Scale1DDragger()
        d.setupDefaultGeometry()
        dragger = d
    elif "Scale2DDragger" == name :
        d = osgManipulator.Scale2DDragger()
        d.setupDefaultGeometry()
        dragger = d
    elif "RotateCylinderDragger" == name :
        d = osgManipulator.RotateCylinderDragger()
        d.setupDefaultGeometry()
        dragger = d
    elif "RotateSphereDragger" == name :
        d = osgManipulator.RotateSphereDragger()
        d.setupDefaultGeometry()
        dragger = d
    else :
        d = osgManipulator.TabBoxDragger()
        d.setupDefaultGeometry()
        dragger = d
    return dragger


# The DraggerContainer node is used to fix the dragger's size on the screen
class DraggerContainer (osg.Group) :
    def __init__(self):
        self._dragger = osgManipulator.Dragger()
        self._draggerSize = 240.0
        self._active = True
    
    def setDragger(self, dragger):
        self._dragger = dragger
        if not containsNode(dragger): 
            addChild( dragger )
    
    def getDragger(self):
         return self._dragger
    
    def setDraggerSize(size):
         self._draggerSize = size

    def getDraggerSize():
         return self._draggerSize 
    
    def setActive(b):
         self._active = b 

    def getActive():
         return self._active 
    
    def traverse(nv):
        if  self._dragger.valid()  :
            if  self._active and nv.getVisitorType() == osg.NodeVisitor.CULL_VISITOR:
                cv = nv
                pixelSize = cv.pixelSize(self._dragger.getBound().center(), 0.48)
                if  pixelSize != self._draggerSize  :
                    pixelScale = self._draggerSize/pixelSize if pixelSize > 0.0 else 1.0
                    # pixelScale = pixelSize > 0.0 ? self._draggerSize/pixelSize : 1.0
                    scaleFactor = osg.Vec3d(pixelScale, pixelScale, pixelScale)
                    trans = self._dragger.getMatrix().getTrans()
                    self._dragger.setMatrix( osg.Matrix.scale(scaleFactor) * osg.Matrix.translate(trans) )
        osg.Group.traverse(nv)


def addDraggerToScene(scene, name, fixedSizeInScreen):
    scene.getOrCreateStateSet().setMode(osg.GL_NORMALIZE, osg.StateAttribute.ON)
    transform = osg.MatrixTransform()
    transform.addChild(scene)
    dragger = createDragger(name)
    root = osg.Group()
    root.addChild(transform)
    if  fixedSizeInScreen:
        draggerContainer = DraggerContainer()
        draggerContainer.setDragger( dragger )
        root.addChild(draggerContainer)
    else :
        root.addChild(dragger)
    scale = scene.getBound().radius() * 1.6
    dragger.setMatrix(osg.Matrix.scale(scale, scale, scale) * osg.Matrix.translate(scene.getBound().center()))

    if dragger is not None:
        dragger.addTransformUpdating(transform, osgManipulator.DraggerTransformCallback.HANDLE_TRANSLATE_IN_LINE)
    else:
        dragger.addTransformUpdating(transform)
    # we want the dragger to handle it's own events automatically
    dragger.setHandleEvents(True)
    # if we don't set an activation key or mod mask then any mouse click on
    # the dragger will activate it, however if do define either of ActivationModKeyMask or
    # and ActivationKeyEvent then you'll have to press either than mod key or the specified key to
    # be able to activate the dragger when you mouse click on it.  Please note the follow allows
    # activation if either the ctrl key or the 'a' key is pressed and held down.
    dragger.setActivationModKeyMask(osgGA.GUIEventAdapter.MODKEY_CTRL)
    dragger.setActivationKeyEvent(ord('a'))
    return root

def createDemoScene(fixedSizeInScreen):
    root = osg.Group()
    geode_1 = osg.Geode()
    transform_1 = osg.MatrixTransform()
    geode_2 = osg.Geode()
    transform_2 = osg.MatrixTransform()
    geode_3 = osg.Geode()
    transform_3 = osg.MatrixTransform()
    geode_4 = osg.Geode()
    transform_4 = osg.MatrixTransform()
    geode_5 = osg.Geode()
    transform_5 = osg.MatrixTransform()
    geode_6 = osg.Geode()
    transform_6 = osg.MatrixTransform()
    geode_7 = osg.Geode()
    transform_7 = osg.MatrixTransform()

    radius = 0.8
    height = 1.0
    hints = osg.TessellationHints()
    hints.setDetailRatio(2.0)
    shape = osg.ShapeDrawable()

    shape = osg.ShapeDrawable(osg.Box(osg.Vec3(0.0, 0.0, -2.0), 10, 10.0, 0.1), hints)
    shape.setColor(osg.Vec4(0.5, 0.5, 0.7, 1.0))
    geode_1.addDrawable(shape)

    shape = osg.ShapeDrawable(osg.Cylinder(osg.Vec3(0.0, 0.0, 0.0), radius * 2,radius), hints)
    shape.setColor(osg.Vec4(0.8, 0.8, 0.8, 1.0))
    geode_2.addDrawable(shape)

    shape = osg.ShapeDrawable(osg.Cylinder(osg.Vec3(-3.0, 0.0, 0.0), radius,radius), hints)
    shape.setColor(osg.Vec4(0.6, 0.8, 0.8, 1.0))
    geode_3.addDrawable(shape)

    shape = osg.ShapeDrawable(osg.Cone(osg.Vec3(3.0, 0.0, 0.0), 2 * radius,radius), hints)
    shape.setColor(osg.Vec4(0.4, 0.9, 0.3, 1.0))
    geode_4.addDrawable(shape)

    shape = osg.ShapeDrawable(osg.Cone(osg.Vec3(0.0, -3.0, 0.0), radius, height), hints)
    shape.setColor(osg.Vec4(0.2, 0.5, 0.7, 1.0))
    geode_5.addDrawable(shape)

    shape = osg.ShapeDrawable(osg.Cylinder(osg.Vec3(0.0, 3.0, 0.0), radius, height), hints)
    shape.setColor(osg.Vec4(1.0, 0.3, 0.3, 1.0))
    geode_6.addDrawable(shape)

    shape = osg.ShapeDrawable(osg.Cone(osg.Vec3(0.0, 0.0, 3.0), 2.0, 2.0), hints)
    shape.setColor(osg.Vec4(0.8, 0.8, 0.4, 1.0))
    geode_7.addDrawable(shape)

    # material
    matirial = osg.Material()
    matirial.setColorMode(osg.Material.DIFFUSE)
    matirial.setAmbient(osg.Material.FRONT_AND_BACK, osg.Vec4(0, 0, 0, 1))
    matirial.setSpecular(osg.Material.FRONT_AND_BACK, osg.Vec4(1, 1, 1, 1))
    matirial.setShininess(osg.Material.FRONT_AND_BACK, 64.0)
    root.getOrCreateStateSet().setAttributeAndModes(matirial, osg.StateAttribute.ON)

    transform_1.addChild(addDraggerToScene(geode_1,"TabBoxDragger",fixedSizeInScreen))
    transform_2.addChild(addDraggerToScene(geode_2,"TabPlaneDragger",fixedSizeInScreen))
    transform_3.addChild(addDraggerToScene(geode_3,"TabBoxTrackballDragger",fixedSizeInScreen))
    transform_4.addChild(addDraggerToScene(geode_4,"TrackballDragger",fixedSizeInScreen))
    transform_5.addChild(addDraggerToScene(geode_5,"Translate1DDragger",fixedSizeInScreen))
    transform_6.addChild(addDraggerToScene(geode_6,"Translate2DDragger",fixedSizeInScreen))
    transform_7.addChild(addDraggerToScene(geode_7,"TranslateAxisDragger",fixedSizeInScreen))

    root.addChild(transform_1)
    root.addChild(transform_2)
    root.addChild(transform_3)
    root.addChild(transform_4)
    root.addChild(transform_5)
    root.addChild(transform_6)
    root.addChild(transform_7)
    return root
# 
def main(argv):
    # use an ArgumentParser object to manage the program arguments.
    arguments = osg.ArgumentParser(argv)
    # set up the usage document, in case we need to print out how to use this program.
    arguments.getApplicationUsage().setApplicationName(arguments.getApplicationName())
    arguments.getApplicationUsage().setCommandLineUsage(arguments.getApplicationName()+" [options] filename ...")
    arguments.getApplicationUsage().addCommandLineOption("--image <filename>","Load an image and render it on a quad")
    arguments.getApplicationUsage().addCommandLineOption("--dem <filename>","Load an image/DEM and render it on a HeightField")
    arguments.getApplicationUsage().addCommandLineOption("-h or --help","Display command line parameters")
    arguments.getApplicationUsage().addCommandLineOption("--help-env","Display environmental variables available")
    arguments.getApplicationUsage().addCommandLineOption("--help-keys","Display keyboard  mouse bindings available")
    arguments.getApplicationUsage().addCommandLineOption("--help-all","Display all command line, env vars and keyboard  mouse bindings.")
    arguments.getApplicationUsage().addCommandLineOption("--dragger <draggername>","Use the specified dragger for manipulation [TabPlaneDragger, TabPlaneTrackballDragger, TrackballDragger, Translate1DDragger, Translate2DDragger, TranslateAxisDragger, TabBoxDragger, TranslatePlaneDragger, Scale1DDragger, Scale2DDragger, RotateCylinderDragger, RotateSphereDragger]")
    arguments.getApplicationUsage().addCommandLineOption("--fixedDraggerSize","Fix the size of the dragger geometry in the screen space")
    fixedSizeInScreen = False
    while arguments.read("--fixedDraggerSize") :  fixedSizeInScreen = True 
    # construct the viewer.
    viewer = osgViewer.Viewer()
    # get details on keyboard and mouse bindings used by the viewer.
    viewer.getUsage(arguments.getApplicationUsage())
    # if user request help write it out to cout.
    helpAll = arguments.read("--help-all")
    helpType = (( osg.ApplicationUsage.COMMAND_LINE_OPTION if (helpAll or arguments.read("-h") or arguments.read("--help")) else 0 ) |
                        (osg.ApplicationUsage.ENVIRONMENTAL_VARIABLE if (helpAll or  arguments.read("--help-env")) else 0 ) |
                        (osg.ApplicationUsage.KEYBOARD_MOUSE_BINDING if (helpAll or  arguments.read("--help-keys")) else 0 ))
    if helpType :
        arguments.getApplicationUsage().write(std.cout, helpType)
        return 1
    # report any errors if they have occurred when parsing the program arguments.
    if arguments.errors() :
        arguments.writeErrorMessages(std.cout)
        return 1
    dragger_name = "TabBoxDragger"
    arguments.read("--dragger", dragger_name)
    start_tick = osg.Timer.instance().tick()
    # read the scene from the list of file specified command line args.
    loadedModel = osgDB.readNodeFiles(arguments)
    # if no model has been successfully loaded report failure.
    tragger2Scene = bool(True)
    if not loadedModel : 
        #print arguments.getApplicationName(), ": No data loaded"
        #return 1
        loadedModel = createDemoScene(fixedSizeInScreen)
        tragger2Scene=False
    # any option left unread are converted into errors to write out later.
    arguments.reportRemainingOptionsAsUnrecognized()
    # report any errors if they have occurred when parsing the program arguments.
    if arguments.errors() :
        arguments.writeErrorMessages(std.cout)
    end_tick = osg.Timer.instance().tick()
    print "Time to load = ", osg.Timer.instance().delta_s(start_tick,end_tick)
    # optimize the scene graph, remove redundant nodes and state etc.
    optimizer = osgUtil.Optimizer()
    optimizer.optimize(loadedModel)
    # pass the loaded scene graph to the viewer.
    if  tragger2Scene:
        viewer.setSceneData(addDraggerToScene(loadedModel, dragger_name, fixedSizeInScreen))
    else:
        viewer.setSceneData(loadedModel)
    return viewer.run()


if __name__ == "__main__":
    main(sys.argv)
