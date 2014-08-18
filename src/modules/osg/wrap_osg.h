#include <windows.h>

// TODO wrap more classes
#include <osg/Quat> // OK
#include <osg/Vec2f> // OK

#include <osg/Object>
#include <osg/CopyOp>
#include <osg/UserDataContainer>
// #include <osg/StateAttributeCallback>
// #include <osg/StateAttribute>
// #include <osg/NodeVisitor>
// #include <osg/Node>
// #include <osg/Drawable>

#include <osg/Notify> // OK
#include <osg/Stats> // OK excluded getAttribute methods
#include <osg/Referenced> // OK excluded copy methods
#include <osg/Observer> // OK
#include <osg/DeleteHandler> // OK
#include <osg/Export> // OK
#include <osg/Version> // OK

// avoid default argument scope error in pyplusplus
static int SHALLOW_COPY = osg::CopyOp::SHALLOW_COPY;

// Disambiguate aliases for file names
// template class std::vector<osg::Group*>;
// template class std::vector<osg::Node*>;
// template class std::vector<osg::StateSet*>;
// template class std::map<std::pair<osg::StateAttribute::Type, unsigned int>, std::pair<osg::ref_ptr<osg::StateAttribute>, unsigned int>, std::less<std::pair<osg::StateAttribute::Type, unsigned int> >, std::allocator<std::pair<std::pair<osg::StateAttribute::Type, unsigned int> const, std::pair<osg::ref_ptr<osg::StateAttribute>, unsigned int> > > >;
namespace pyplusplus { namespace aliases {
    // typedef std::vector<osg::Group*> std_vector_osgGroupPtr;
    // typedef std::vector<osg::Node*> std_vector_osgNodePtr;
    // typedef std::vector<osg::StateSet*> std_vector_osgStateSetPtr;
    // typedef std::map<std::pair<osg::StateAttribute::Type, unsigned int>, std::pair<osg::ref_ptr<osg::StateAttribute>, unsigned int>, std::less<std::pair<osg::StateAttribute::Type, unsigned int> >, std::allocator<std::pair<std::pair<osg::StateAttribute::Type, unsigned int> const, std::pair<osg::ref_ptr<osg::StateAttribute>, unsigned int> > > > longClassName1;
}}

// #include <osg/Matrixf>

