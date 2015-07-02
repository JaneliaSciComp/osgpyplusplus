#include "../default.h"

// TODO - wrap more classes
#include <osgDB/Archive>
#include <osgDB/DatabasePager>
#include <osgDB/fstream> // OK
#include <osgDB/ImagePager>
#include <osgDB/ReadFile> // OK this is a tricky one, needed for readNodeFile()
#include <osgDB/SharedStateManager> // NodeVisitor
#include <osgDB/Version> // OK
