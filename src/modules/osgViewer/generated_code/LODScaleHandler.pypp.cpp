// This file has been generated by Py++.

#include "boost/python.hpp"
#include "wrap_osgviewer.h"
#include "wrap_referenced.h"
#include "lodscalehandler.pypp.hpp"

namespace bp = boost::python;

struct LODScaleHandler_wrapper : osgViewer::LODScaleHandler, bp::wrapper< osgViewer::LODScaleHandler > {

    LODScaleHandler_wrapper( )
    : osgViewer::LODScaleHandler( )
      , bp::wrapper< osgViewer::LODScaleHandler >(){
        // null constructor
    
    }

    virtual void getUsage( ::osg::ApplicationUsage & usage ) const  {
        if( bp::override func_getUsage = this->get_override( "getUsage" ) )
            func_getUsage( boost::ref(usage) );
        else{
            this->osgViewer::LODScaleHandler::getUsage( boost::ref(usage) );
        }
    }
    
    void default_getUsage( ::osg::ApplicationUsage & usage ) const  {
        osgViewer::LODScaleHandler::getUsage( boost::ref(usage) );
    }

    virtual void computeDataVariance(  ) {
        if( bp::override func_computeDataVariance = this->get_override( "computeDataVariance" ) )
            func_computeDataVariance(  );
        else{
            this->osg::Object::computeDataVariance(  );
        }
    }
    
    void default_computeDataVariance(  ) {
        osg::Object::computeDataVariance( );
    }

    virtual ::osg::Referenced * getUserData(  ) {
        if( bp::override func_getUserData = this->get_override( "getUserData" ) )
            return func_getUserData(  );
        else{
            return this->osg::Object::getUserData(  );
        }
    }
    
    ::osg::Referenced * default_getUserData(  ) {
        return osg::Object::getUserData( );
    }

    virtual ::osg::Referenced const * getUserData(  ) const  {
        if( bp::override func_getUserData = this->get_override( "getUserData" ) )
            return func_getUserData(  );
        else{
            return this->osg::Object::getUserData(  );
        }
    }
    
    ::osg::Referenced const * default_getUserData(  ) const  {
        return osg::Object::getUserData( );
    }

    virtual void resizeGLObjectBuffers( unsigned int arg0 ) {
        if( bp::override func_resizeGLObjectBuffers = this->get_override( "resizeGLObjectBuffers" ) )
            func_resizeGLObjectBuffers( arg0 );
        else{
            this->osg::Object::resizeGLObjectBuffers( arg0 );
        }
    }
    
    void default_resizeGLObjectBuffers( unsigned int arg0 ) {
        osg::Object::resizeGLObjectBuffers( arg0 );
    }

    virtual void setName( ::std::string const & name ) {
        if( bp::override func_setName = this->get_override( "setName" ) )
            func_setName( name );
        else{
            this->osg::Object::setName( name );
        }
    }
    
    void default_setName( ::std::string const & name ) {
        osg::Object::setName( name );
    }

    virtual void setThreadSafeRefUnref( bool threadSafe ) {
        if( bp::override func_setThreadSafeRefUnref = this->get_override( "setThreadSafeRefUnref" ) )
            func_setThreadSafeRefUnref( threadSafe );
        else{
            this->osg::Object::setThreadSafeRefUnref( threadSafe );
        }
    }
    
    void default_setThreadSafeRefUnref( bool threadSafe ) {
        osg::Object::setThreadSafeRefUnref( threadSafe );
    }

    virtual void setUserData( ::osg::Referenced * obj ) {
        if( bp::override func_setUserData = this->get_override( "setUserData" ) )
            func_setUserData( boost::python::ptr(obj) );
        else{
            this->osg::Object::setUserData( boost::python::ptr(obj) );
        }
    }
    
    void default_setUserData( ::osg::Referenced * obj ) {
        osg::Object::setUserData( boost::python::ptr(obj) );
    }

};

void register_LODScaleHandler_class(){

    bp::class_< LODScaleHandler_wrapper, osg::ref_ptr< ::osgViewer::LODScaleHandler >, boost::noncopyable >( "LODScaleHandler", bp::init< >() )    
        .def( 
            "getKeyEventDecreaseLODScale"
            , (int ( ::osgViewer::LODScaleHandler::* )(  )const)( &::osgViewer::LODScaleHandler::getKeyEventDecreaseLODScale ) )    
        .def( 
            "getKeyEventIncreaseLODScale"
            , (int ( ::osgViewer::LODScaleHandler::* )(  )const)( &::osgViewer::LODScaleHandler::getKeyEventIncreaseLODScale ) )    
        .def( 
            "getUsage"
            , (void ( ::osgViewer::LODScaleHandler::* )( ::osg::ApplicationUsage & )const)(&::osgViewer::LODScaleHandler::getUsage)
            , (void ( LODScaleHandler_wrapper::* )( ::osg::ApplicationUsage & )const)(&LODScaleHandler_wrapper::default_getUsage)
            , ( bp::arg("usage") ) )    
        .def( 
            "setKeyEventDecreaseLODScale"
            , (void ( ::osgViewer::LODScaleHandler::* )( int ))( &::osgViewer::LODScaleHandler::setKeyEventDecreaseLODScale )
            , ( bp::arg("key") ) )    
        .def( 
            "setKeyEventIncreaseLODScale"
            , (void ( ::osgViewer::LODScaleHandler::* )( int ))( &::osgViewer::LODScaleHandler::setKeyEventIncreaseLODScale )
            , ( bp::arg("key") ) );

}