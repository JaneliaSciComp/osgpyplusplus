// This file has been generated by Py++.

#include "boost/python.hpp"
#include "wrap_osg.h"
#include "wrap_referenced.h"
#include "arraydispatchers.pypp.hpp"

namespace bp = boost::python;

struct ArrayDispatchers_wrapper : osg::ArrayDispatchers, bp::wrapper< osg::ArrayDispatchers > {

    ArrayDispatchers_wrapper( )
    : osg::ArrayDispatchers( )
      , bp::wrapper< osg::ArrayDispatchers >(){
        // null constructor
    
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

void register_ArrayDispatchers_class(){

    bp::class_< ArrayDispatchers_wrapper, bp::bases< osg::Referenced >, osg::ref_ptr< ::osg::ArrayDispatchers >, boost::noncopyable >( "ArrayDispatchers", "\n Helper class for managing the dispatch to OpenGL of various attribute arrays such as stored in osg::Geometry.\n", bp::init< >("\n Helper class for managing the dispatch to OpenGL of various attribute arrays such as stored in osg::Geometry.\n") )    
        .def( 
            "activate"
            , (void ( ::osg::ArrayDispatchers::* )( unsigned int,::osg::AttributeDispatch * ))( &::osg::ArrayDispatchers::activate )
            , ( bp::arg("binding"), bp::arg("at") ) )    
        .def( 
            "activateColorArray"
            , (void ( ::osg::ArrayDispatchers::* )( ::osg::Array * ))( &::osg::ArrayDispatchers::activateColorArray )
            , ( bp::arg("array") ) )    
        .def( 
            "activateFogCoordArray"
            , (void ( ::osg::ArrayDispatchers::* )( ::osg::Array * ))( &::osg::ArrayDispatchers::activateFogCoordArray )
            , ( bp::arg("array") ) )    
        .def( 
            "activateNormalArray"
            , (void ( ::osg::ArrayDispatchers::* )( ::osg::Array * ))( &::osg::ArrayDispatchers::activateNormalArray )
            , ( bp::arg("array") ) )    
        .def( 
            "activateSecondaryColorArray"
            , (void ( ::osg::ArrayDispatchers::* )( ::osg::Array * ))( &::osg::ArrayDispatchers::activateSecondaryColorArray )
            , ( bp::arg("array") ) )    
        .def( 
            "activateTexCoordArray"
            , (void ( ::osg::ArrayDispatchers::* )( unsigned int,::osg::Array * ))( &::osg::ArrayDispatchers::activateTexCoordArray )
            , ( bp::arg("unit"), bp::arg("array") ) )    
        .def( 
            "activateVertexArray"
            , (void ( ::osg::ArrayDispatchers::* )( ::osg::Array * ))( &::osg::ArrayDispatchers::activateVertexArray )
            , ( bp::arg("array") ) )    
        .def( 
            "activateVertexAttribArray"
            , (void ( ::osg::ArrayDispatchers::* )( unsigned int,::osg::Array * ))( &::osg::ArrayDispatchers::activateVertexAttribArray )
            , ( bp::arg("unit"), bp::arg("array") ) )    
        .def( 
            "active"
            , (bool ( ::osg::ArrayDispatchers::* )( unsigned int )const)( &::osg::ArrayDispatchers::active )
            , ( bp::arg("binding") ) )    
        .def( 
            "colorDispatcher"
            , (::osg::AttributeDispatch * ( ::osg::ArrayDispatchers::* )( ::osg::Array * ))( &::osg::ArrayDispatchers::colorDispatcher )
            , ( bp::arg("array") )
            , bp::return_internal_reference< >() )    
        .def( 
            "dispatch"
            , (void ( ::osg::ArrayDispatchers::* )( unsigned int,unsigned int ))( &::osg::ArrayDispatchers::dispatch )
            , ( bp::arg("binding"), bp::arg("index") ) )    
        .def( 
            "fogCoordDispatcher"
            , (::osg::AttributeDispatch * ( ::osg::ArrayDispatchers::* )( ::osg::Array * ))( &::osg::ArrayDispatchers::fogCoordDispatcher )
            , ( bp::arg("array") )
            , bp::return_internal_reference< >() )    
        .def( 
            "getUseVertexAttribAlias"
            , (bool ( ::osg::ArrayDispatchers::* )(  )const)( &::osg::ArrayDispatchers::getUseVertexAttribAlias ) )    
        .def( 
            "normalDispatcher"
            , (::osg::AttributeDispatch * ( ::osg::ArrayDispatchers::* )( ::osg::Array * ))( &::osg::ArrayDispatchers::normalDispatcher )
            , ( bp::arg("array") )
            , bp::return_internal_reference< >() )    
        .def( 
            "reset"
            , (void ( ::osg::ArrayDispatchers::* )(  ))( &::osg::ArrayDispatchers::reset ) )    
        .def( 
            "secondaryColorDispatcher"
            , (::osg::AttributeDispatch * ( ::osg::ArrayDispatchers::* )( ::osg::Array * ))( &::osg::ArrayDispatchers::secondaryColorDispatcher )
            , ( bp::arg("array") )
            , bp::return_internal_reference< >() )    
        .def( 
            "setState"
            , (void ( ::osg::ArrayDispatchers::* )( ::osg::State * ))( &::osg::ArrayDispatchers::setState )
            , ( bp::arg("state") ) )    
        .def( 
            "setUseVertexAttribAlias"
            , (void ( ::osg::ArrayDispatchers::* )( bool ))( &::osg::ArrayDispatchers::setUseVertexAttribAlias )
            , ( bp::arg("flag") ) )    
        .def( 
            "texCoordDispatcher"
            , (::osg::AttributeDispatch * ( ::osg::ArrayDispatchers::* )( unsigned int,::osg::Array * ))( &::osg::ArrayDispatchers::texCoordDispatcher )
            , ( bp::arg("unit"), bp::arg("array") )
            , bp::return_internal_reference< >() )    
        .def( 
            "vertexAttribDispatcher"
            , (::osg::AttributeDispatch * ( ::osg::ArrayDispatchers::* )( unsigned int,::osg::Array * ))( &::osg::ArrayDispatchers::vertexAttribDispatcher )
            , ( bp::arg("unit"), bp::arg("array") )
            , bp::return_internal_reference< >() )    
        .def( 
            "vertexDispatcher"
            , (::osg::AttributeDispatch * ( ::osg::ArrayDispatchers::* )( ::osg::Array * ))( &::osg::ArrayDispatchers::vertexDispatcher )
            , ( bp::arg("array") )
            , bp::return_internal_reference< >() )    
        .def( 
            "setThreadSafeRefUnref"
            , (void ( ::osg::Referenced::* )( bool ))(&::osg::Referenced::setThreadSafeRefUnref)
            , (void ( ArrayDispatchers_wrapper::* )( bool ))(&ArrayDispatchers_wrapper::default_setThreadSafeRefUnref)
            , ( bp::arg("threadSafe") ) );

}
