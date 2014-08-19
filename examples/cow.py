from osgpyplusplus import osg, osgDB

print osg.osgGetVersion()
print osgDB.osgDBGetVersion()
scene = osgDB.readNodeFile("cow.osg")

from osgpyplusplus import osgViewer
print osgViewer.osgViewerGetVersion()

viewer = osgViewer.Viewer()
viewer.setSceneData(scene)
viewer.setUpViewInWindow(100, 100, 500, 500, 0)
viewer.run()

