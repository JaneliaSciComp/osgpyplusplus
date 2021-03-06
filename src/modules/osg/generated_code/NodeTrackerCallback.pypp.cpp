// This file has been generated by Py++.

#include "boost/python.hpp"
#include "wrap_osg.h"
#include "wrap_referenced.h"
#include "nodetrackercallback.pypp.hpp"

namespace bp = boost::python;

struct NodeTrackerCallback_wrapper : osg::NodeTrackerCallback, bp::wrapper< osg::NodeTrackerCallback > {

    NodeTrackerCallback_wrapper()
    : osg::NodeTrackerCallback()
      , bp::wrapper< osg::NodeTrackerCallback >(){
        // null constructor
        
    }

    virtual void operator()( ::osg::Node * node, ::osg::NodeVisitor * nv ) {
        if( bp::override func___call__ = this->get_override( "__call__" ) )
            func___call__( boost::python::ptr(node), boost::python::ptr(nv) );
        else{
            this->osg::NodeTrackerCallback::operator()( boost::python::ptr(node), boost::python::ptr(nv) );
        }
    }
    
    void default___call__( ::osg::Node * node, ::osg::NodeVisitor * nv ) {
        osg::NodeTrackerCallback::operator()( boost::python::ptr(node), boost::python::ptr(nv) );
    }

    virtual char const * className(  ) const  {
        if( bp::override func_className = this->get_override( "className" ) )
            return func_className(  );
        else{
            return this->osg::NodeCallback::className(  );
        }
    }
    
    char const * default_className(  ) const  {
        return osg::NodeCallback::className( );
    }

    virtual ::osg::Object * clone( ::osg::CopyOp const & copyop ) const  {
        if( bp::override func_clone = this->get_override( "clone" ) )
            return func_clone( boost::ref(copyop) );
        else{
            return this->osg::NodeCallback::clone( boost::ref(copyop) );
        }
    }
    
    ::osg::Object * default_clone( ::osg::CopyOp const & copyop ) const  {
        return osg::NodeCallback::clone( boost::ref(copyop) );
    }

    virtual ::osg::Object * cloneType(  ) const  {
        if( bp::override func_cloneType = this->get_override( "cloneType" ) )
            return func_cloneType(  );
        else{
            return this->osg::NodeCallback::cloneType(  );
        }
    }
    
    ::osg::Object * default_cloneType(  ) const  {
        return osg::NodeCallback::cloneType( );
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

    virtual bool isSameKindAs( ::osg::Object const * obj ) const  {
        if( bp::override func_isSameKindAs = this->get_override( "isSameKindAs" ) )
            return func_isSameKindAs( boost::python::ptr(obj) );
        else{
            return this->osg::NodeCallback::isSameKindAs( boost::python::ptr(obj) );
        }
    }
    
    bool default_isSameKindAs( ::osg::Object const * obj ) const  {
        return osg::NodeCallback::isSameKindAs( boost::python::ptr(obj) );
    }

    virtual char const * libraryName(  ) const  {
        if( bp::override func_libraryName = this->get_override( "libraryName" ) )
            return func_libraryName(  );
        else{
            return this->osg::NodeCallback::libraryName(  );
        }
    }
    
    char const * default_libraryName(  ) const  {
        return osg::NodeCallback::libraryName( );
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

void register_NodeTrackerCallback_class(){

    bp::class_< NodeTrackerCallback_wrapper, bp::bases< osg::NodeCallback >, osg::ref_ptr< NodeTrackerCallback_wrapper >, boost::noncopyable >( "NodeTrackerCallback" )    
        .def( 
            "getTrackNode"
            , (::osg::Node * ( ::osg::NodeTrackerCallback::* )(  ))( &::osg::NodeTrackerCallback::getTrackNode )
            , bp::return_internal_reference< >() )    
        .def( 
            "getTrackNode"
            , (::osg::Node const * ( ::osg::NodeTrackerCallback::* )(  )const)( &::osg::NodeTrackerCallback::getTrackNode )
            , bp::return_internal_reference< >() )    
        .def( 
            "getTrackNodePath"
            , (::osg::ObserverNodePath & ( ::osg::NodeTrackerCallback::* )(  ))( &::osg::NodeTrackerCallback::getTrackNodePath )
            , bp::return_internal_reference< >() )    
        .def( 
            "__call__"
            , (void ( ::osg::NodeTrackerCallback::* )( ::osg::Node *,::osg::NodeVisitor * ))(&::osg::NodeTrackerCallback::operator())
            , (void ( NodeTrackerCallback_wrapper::* )( ::osg::Node *,::osg::NodeVisitor * ))(&NodeTrackerCallback_wrapper::default___call__)
            , ( bp::arg("node"), bp::arg("nv") ) )    
        .def( 
            "setTrackNode"
            , (void ( ::osg::NodeTrackerCallback::* )( ::osg::Node * ))( &::osg::NodeTrackerCallback::setTrackNode )
            , ( bp::arg("node") ) )    
        .def( 
            "setTrackNodePath"
            , (void ( ::osg::NodeTrackerCallback::* )( ::osg::NodePath const & ))( &::osg::NodeTrackerCallback::setTrackNodePath )
            , ( bp::arg("nodePath") ) )    
        .def( 
            "setTrackNodePath"
            , (void ( ::osg::NodeTrackerCallback::* )( ::osg::ObserverNodePath const & ))( &::osg::NodeTrackerCallback::setTrackNodePath )
            , ( bp::arg("nodePath") ) )    
        .def( 
            "update"
            , (void ( ::osg::NodeTrackerCallback::* )( ::osg::Node & ))( &::osg::NodeTrackerCallback::update )
            , ( bp::arg("node") )
            , " Update the node to track the nodepath." )    
        .def( 
            "className"
            , (char const * ( ::osg::NodeCallback::* )(  )const)(&::osg::NodeCallback::className)
            , (char const * ( NodeTrackerCallback_wrapper::* )(  )const)(&NodeTrackerCallback_wrapper::default_className) )    
        .def( 
            "clone"
            , (::osg::Object * ( ::osg::NodeCallback::* )( ::osg::CopyOp const & )const)(&::osg::NodeCallback::clone)
            , (::osg::Object * ( NodeTrackerCallback_wrapper::* )( ::osg::CopyOp const & )const)(&NodeTrackerCallback_wrapper::default_clone)
            , ( bp::arg("copyop") )
            , bp::return_value_policy< bp::reference_existing_object >() )    
        .def( 
            "cloneType"
            , (::osg::Object * ( ::osg::NodeCallback::* )(  )const)(&::osg::NodeCallback::cloneType)
            , (::osg::Object * ( NodeTrackerCallback_wrapper::* )(  )const)(&NodeTrackerCallback_wrapper::default_cloneType)
            , bp::return_value_policy< bp::reference_existing_object >() )    
        .def( 
            "computeDataVariance"
            , (void ( ::osg::Object::* )(  ))(&::osg::Object::computeDataVariance)
            , (void ( NodeTrackerCallback_wrapper::* )(  ))(&NodeTrackerCallback_wrapper::default_computeDataVariance) )    
        .def( 
            "getUserData"
            , (::osg::Referenced * ( ::osg::Object::* )(  ))(&::osg::Object::getUserData)
            , (::osg::Referenced * ( NodeTrackerCallback_wrapper::* )(  ))(&NodeTrackerCallback_wrapper::default_getUserData)
            , bp::return_internal_reference< >() )    
        .def( 
            "getUserData"
            , (::osg::Referenced const * ( ::osg::Object::* )(  )const)(&::osg::Object::getUserData)
            , (::osg::Referenced const * ( NodeTrackerCallback_wrapper::* )(  )const)(&NodeTrackerCallback_wrapper::default_getUserData)
            , bp::return_internal_reference< >() )    
        .def( 
            "isSameKindAs"
            , (bool ( ::osg::NodeCallback::* )( ::osg::Object const * )const)(&::osg::NodeCallback::isSameKindAs)
            , (bool ( NodeTrackerCallback_wrapper::* )( ::osg::Object const * )const)(&NodeTrackerCallback_wrapper::default_isSameKindAs)
            , ( bp::arg("obj") ) )    
        .def( 
            "libraryName"
            , (char const * ( ::osg::NodeCallback::* )(  )const)(&::osg::NodeCallback::libraryName)
            , (char const * ( NodeTrackerCallback_wrapper::* )(  )const)(&NodeTrackerCallback_wrapper::default_libraryName) )    
        .def( 
            "resizeGLObjectBuffers"
            , (void ( ::osg::Object::* )( unsigned int ))(&::osg::Object::resizeGLObjectBuffers)
            , (void ( NodeTrackerCallback_wrapper::* )( unsigned int ))(&NodeTrackerCallback_wrapper::default_resizeGLObjectBuffers)
            , ( bp::arg("arg0") ) )    
        .def( 
            "setName"
            , (void ( ::osg::Object::* )( ::std::string const & ))(&::osg::Object::setName)
            , (void ( NodeTrackerCallback_wrapper::* )( ::std::string const & ))(&NodeTrackerCallback_wrapper::default_setName)
            , ( bp::arg("name") ) )    
        .def( 
            "setName"
            , (void ( ::osg::Object::* )( char const * ))( &::osg::Object::setName )
            , ( bp::arg("name") )
            , " Set the name of object using a C style string." )    
        .def( 
            "setThreadSafeRefUnref"
            , (void ( ::osg::Object::* )( bool ))(&::osg::Object::setThreadSafeRefUnref)
            , (void ( NodeTrackerCallback_wrapper::* )( bool ))(&NodeTrackerCallback_wrapper::default_setThreadSafeRefUnref)
            , ( bp::arg("threadSafe") ) )    
        .def( 
            "setUserData"
            , (void ( ::osg::Object::* )( ::osg::Referenced * ))(&::osg::Object::setUserData)
            , (void ( NodeTrackerCallback_wrapper::* )( ::osg::Referenced * ))(&NodeTrackerCallback_wrapper::default_setUserData)
            , ( bp::arg("obj") ) );

}
