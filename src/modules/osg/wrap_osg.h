#include <windows.h>

// TODO wrap more classes
#include <osg/Quat> // OK
#include <osg/Vec2f> // OK

#include <osg/Object>
#include <osg/CopyOp>
#include <osg/UserDataContainer>

#include <osg/Notify> // OK
#include <osg/Stats> // OK excluded getAttribute methods
#include <osg/Referenced> // OK excluded copy methods
#include <osg/Observer> // OK
#include <osg/DeleteHandler> // OK
#include <osg/Export> // OK
#include <osg/Version> // OK

int SHALLOW_COPY = osg::CopyOp::SHALLOW_COPY;

// #include <osg/Matrixf>

