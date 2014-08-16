// This file has been generated by Py++.

#include "boost/python.hpp"
#include "wrap_osg.h"
#include "glbufferobjectset.pypp.hpp"

namespace bp = boost::python;

struct GLBufferObjectSet_wrapper : osg::GLBufferObjectSet, bp::wrapper< osg::GLBufferObjectSet > {

    GLBufferObjectSet_wrapper(::osg::GLBufferObjectManager * parent, ::osg::BufferObjectProfile const & profile )
    : osg::GLBufferObjectSet( boost::python::ptr(parent), boost::ref(profile) )
      , bp::wrapper< osg::GLBufferObjectSet >(){
        // constructor
    
    }

    virtual void setThreadSafeRefUnref( bool threadSafe ) {
        if( bp::override func_setThreadSafeRefUnref = this->get_override( "setThreadSafeRefUnref" ) )
            func_setThreadSafeRefUnref( threadSafe );
        else{
            this->osg::Referenced::setThreadSafeRefUnref( threadSafe );
        }
    }
    
    void default_setThreadSafeRefUnref( bool threadSafe ) {
        osg::Referenced::setThreadSafeRefUnref( threadSafe );
    }

};

void register_GLBufferObjectSet_class(){

    bp::class_< GLBufferObjectSet_wrapper, bp::bases< osg::Referenced >, boost::noncopyable >( "GLBufferObjectSet", bp::no_init )    
        .def( bp::init< osg::GLBufferObjectManager *, osg::BufferObjectProfile const & >(( bp::arg("parent"), bp::arg("profile") )) )    
        .def( 
            "addToBack"
            , (void ( ::osg::GLBufferObjectSet::* )( ::osg::GLBufferObject * ))( &::osg::GLBufferObjectSet::addToBack )
            , ( bp::arg("to") ) )    
        .def( 
            "checkConsistency"
            , (bool ( ::osg::GLBufferObjectSet::* )(  )const)( &::osg::GLBufferObjectSet::checkConsistency ) )    
        .def( 
            "computeNumGLBufferObjectsInList"
            , (unsigned int ( ::osg::GLBufferObjectSet::* )(  )const)( &::osg::GLBufferObjectSet::computeNumGLBufferObjectsInList ) )    
        .def( 
            "deleteAllGLBufferObjects"
            , (void ( ::osg::GLBufferObjectSet::* )(  ))( &::osg::GLBufferObjectSet::deleteAllGLBufferObjects ) )    
        .def( 
            "discardAllDeletedGLBufferObjects"
            , (void ( ::osg::GLBufferObjectSet::* )(  ))( &::osg::GLBufferObjectSet::discardAllDeletedGLBufferObjects ) )    
        .def( 
            "discardAllGLBufferObjects"
            , (void ( ::osg::GLBufferObjectSet::* )(  ))( &::osg::GLBufferObjectSet::discardAllGLBufferObjects ) )    
        .def( 
            "flushAllDeletedGLBufferObjects"
            , (void ( ::osg::GLBufferObjectSet::* )(  ))( &::osg::GLBufferObjectSet::flushAllDeletedGLBufferObjects ) )    
        .def( 
            "flushDeletedGLBufferObjects"
            , (void ( ::osg::GLBufferObjectSet::* )( double,double & ))( &::osg::GLBufferObjectSet::flushDeletedGLBufferObjects )
            , ( bp::arg("currentTime"), bp::arg("availableTime") ) )    
        .def( 
            "getNumOfGLBufferObjects"
            , (unsigned int ( ::osg::GLBufferObjectSet::* )(  )const)( &::osg::GLBufferObjectSet::getNumOfGLBufferObjects ) )    
        .def( 
            "getNumOrphans"
            , (unsigned int ( ::osg::GLBufferObjectSet::* )(  )const)( &::osg::GLBufferObjectSet::getNumOrphans ) )    
        .def( 
            "getNumPendingOrphans"
            , (unsigned int ( ::osg::GLBufferObjectSet::* )(  )const)( &::osg::GLBufferObjectSet::getNumPendingOrphans ) )    
        .def( 
            "getParent"
            , (::osg::GLBufferObjectManager * ( ::osg::GLBufferObjectSet::* )(  ))( &::osg::GLBufferObjectSet::getParent )
                /* undefined call policies */ )    
        .def( 
            "getProfile"
            , (::osg::BufferObjectProfile const & ( ::osg::GLBufferObjectSet::* )(  )const)( &::osg::GLBufferObjectSet::getProfile )
            , bp::return_internal_reference< >() )    
        .def( 
            "handlePendingOrphandedGLBufferObjects"
            , (void ( ::osg::GLBufferObjectSet::* )(  ))( &::osg::GLBufferObjectSet::handlePendingOrphandedGLBufferObjects ) )    
        .def( 
            "makeSpace"
            , (bool ( ::osg::GLBufferObjectSet::* )( unsigned int & ))( &::osg::GLBufferObjectSet::makeSpace )
            , ( bp::arg("size") ) )    
        .def( 
            "moveToBack"
            , (void ( ::osg::GLBufferObjectSet::* )( ::osg::GLBufferObject * ))( &::osg::GLBufferObjectSet::moveToBack )
            , ( bp::arg("to") ) )    
        .def( 
            "moveToSet"
            , (void ( ::osg::GLBufferObjectSet::* )( ::osg::GLBufferObject *,::osg::GLBufferObjectSet * ))( &::osg::GLBufferObjectSet::moveToSet )
            , ( bp::arg("to"), bp::arg("set") ) )    
        .def( 
            "orphan"
            , (void ( ::osg::GLBufferObjectSet::* )( ::osg::GLBufferObject * ))( &::osg::GLBufferObjectSet::orphan )
            , ( bp::arg("to") ) )    
        .def( 
            "remove"
            , (void ( ::osg::GLBufferObjectSet::* )( ::osg::GLBufferObject * ))( &::osg::GLBufferObjectSet::remove )
            , ( bp::arg("to") ) )    
        .def( 
            "size"
            , (unsigned int ( ::osg::GLBufferObjectSet::* )(  )const)( &::osg::GLBufferObjectSet::size ) )    
        .def( 
            "takeFromOrphans"
            , (::osg::GLBufferObject * ( ::osg::GLBufferObjectSet::* )( ::osg::BufferObject * ))( &::osg::GLBufferObjectSet::takeFromOrphans )
            , ( bp::arg("bufferObject") )
                /* undefined call policies */ )    
        .def( 
            "takeOrGenerate"
            , (::osg::GLBufferObject * ( ::osg::GLBufferObjectSet::* )( ::osg::BufferObject * ))( &::osg::GLBufferObjectSet::takeOrGenerate )
            , ( bp::arg("bufferObject") )
                /* undefined call policies */ )    
        .def( 
            "setThreadSafeRefUnref"
            , (void ( ::osg::Referenced::* )( bool ))(&::osg::Referenced::setThreadSafeRefUnref)
            , (void ( GLBufferObjectSet_wrapper::* )( bool ))(&GLBufferObjectSet_wrapper::default_setThreadSafeRefUnref)
            , ( bp::arg("threadSafe") ) );

}
