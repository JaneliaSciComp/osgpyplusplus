#include <windows.h>

// TODO - wrap more classes
#include <osgDB/ReadFile> // TODO - this is a tricky one, needed for readNodeFile()
#include <osgDB/fstream>
#include <osgDB/Version>

static int SHALLOW_COPY = osg::CopyOp::SHALLOW_COPY;
