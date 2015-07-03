// This file has been generated by Py++.

#include "boost/python.hpp"
#include "wrap_osg.h"
#include "wrap_referenced.h"
#include "uniformbufferobject.pypp.hpp"

namespace bp = boost::python;

struct UniformBufferObject_wrapper : osg::UniformBufferObject, bp::wrapper< osg::UniformBufferObject > {

    UniformBufferObject_wrapper( )
    : osg::UniformBufferObject( )
      , bp::wrapper< osg::UniformBufferObject >(){
        // null constructor
    
    }

    virtual char const * className(  ) const  {
        if( bp::override func_className = this->get_override( "className" ) )
            return func_className(  );
        else{
            return this->osg::UniformBufferObject::className(  );
        }
    }
    
    char const * default_className(  ) const  {
        return osg::UniformBufferObject::className( );
    }

    virtual ::osg::Object * clone( ::osg::CopyOp const & copyop ) const  {
        if( bp::override func_clone = this->get_override( "clone" ) )
            return func_clone( boost::ref(copyop) );
        else{
            return this->osg::UniformBufferObject::clone( boost::ref(copyop) );
        }
    }
    
    ::osg::Object * default_clone( ::osg::CopyOp const & copyop ) const  {
        return osg::UniformBufferObject::clone( boost::ref(copyop) );
    }

    virtual ::osg::Object * cloneType(  ) const  {
        if( bp::override func_cloneType = this->get_override( "cloneType" ) )
            return func_cloneType(  );
        else{
            return this->osg::UniformBufferObject::cloneType(  );
        }
    }
    
    ::osg::Object * default_cloneType(  ) const  {
        return osg::UniformBufferObject::cloneType( );
    }

    virtual bool isSameKindAs( ::osg::Object const * obj ) const  {
        if( bp::override func_isSameKindAs = this->get_override( "isSameKindAs" ) )
            return func_isSameKindAs( boost::python::ptr(obj) );
        else{
            return this->osg::UniformBufferObject::isSameKindAs( boost::python::ptr(obj) );
        }
    }
    
    bool default_isSameKindAs( ::osg::Object const * obj ) const  {
        return osg::UniformBufferObject::isSameKindAs( boost::python::ptr(obj) );
    }

    virtual char const * libraryName(  ) const  {
        if( bp::override func_libraryName = this->get_override( "libraryName" ) )
            return func_libraryName(  );
        else{
            return this->osg::UniformBufferObject::libraryName(  );
        }
    }
    
    char const * default_libraryName(  ) const  {
        return osg::UniformBufferObject::libraryName( );
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

    virtual void resizeGLObjectBuffers( unsigned int maxSize ) {
        if( bp::override func_resizeGLObjectBuffers = this->get_override( "resizeGLObjectBuffers" ) )
            func_resizeGLObjectBuffers( maxSize );
        else{
            this->osg::BufferObject::resizeGLObjectBuffers( maxSize );
        }
    }
    
    void default_resizeGLObjectBuffers( unsigned int maxSize ) {
        osg::BufferObject::resizeGLObjectBuffers( maxSize );
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

void register_UniformBufferObject_class(){

    bp::class_< UniformBufferObject_wrapper, bp::bases< osg::BufferObject >, osg::ref_ptr< ::osg::UniformBufferObject >, boost::noncopyable >( "UniformBufferObject", bp::no_init )    
        .def( bp::init< >() )    
        .def( 
            "className"
            , (char const * ( ::osg::UniformBufferObject::* )(  ) const)(&::osg::UniformBufferObject::className)
            , (char const * ( UniformBufferObject_wrapper::* )(  ) const)(&UniformBufferObject_wrapper::default_className) )    
        .def( 
            "clone"
            , (::osg::Object * ( ::osg::UniformBufferObject::* )( ::osg::CopyOp const & ) const)(&::osg::UniformBufferObject::clone)
            , (::osg::Object * ( UniformBufferObject_wrapper::* )( ::osg::CopyOp const & ) const)(&UniformBufferObject_wrapper::default_clone)
            , ( bp::arg("copyop") )
            , bp::return_value_policy< bp::reference_existing_object >() )    
        .def( 
            "cloneType"
            , (::osg::Object * ( ::osg::UniformBufferObject::* )(  ) const)(&::osg::UniformBufferObject::cloneType)
            , (::osg::Object * ( UniformBufferObject_wrapper::* )(  ) const)(&UniformBufferObject_wrapper::default_cloneType)
            , bp::return_value_policy< bp::reference_existing_object >() )    
        .def( 
            "isSameKindAs"
            , (bool ( ::osg::UniformBufferObject::* )( ::osg::Object const * ) const)(&::osg::UniformBufferObject::isSameKindAs)
            , (bool ( UniformBufferObject_wrapper::* )( ::osg::Object const * ) const)(&UniformBufferObject_wrapper::default_isSameKindAs)
            , ( bp::arg("obj") ) )    
        .def( 
            "libraryName"
            , (char const * ( ::osg::UniformBufferObject::* )(  ) const)(&::osg::UniformBufferObject::libraryName)
            , (char const * ( UniformBufferObject_wrapper::* )(  ) const)(&UniformBufferObject_wrapper::default_libraryName) )    
        .def( 
            "computeDataVariance"
            , (void ( ::osg::Object::* )(  ) )(&::osg::Object::computeDataVariance)
            , (void ( UniformBufferObject_wrapper::* )(  ) )(&UniformBufferObject_wrapper::default_computeDataVariance) )    
        .def( 
            "getUserData"
            , (::osg::Referenced * ( ::osg::Object::* )(  ) )(&::osg::Object::getUserData)
            , (::osg::Referenced * ( UniformBufferObject_wrapper::* )(  ) )(&UniformBufferObject_wrapper::default_getUserData)
            , bp::return_internal_reference< >() )    
        .def( 
            "getUserData"
            , (::osg::Referenced const * ( ::osg::Object::* )(  ) const)(&::osg::Object::getUserData)
            , (::osg::Referenced const * ( UniformBufferObject_wrapper::* )(  ) const)(&UniformBufferObject_wrapper::default_getUserData)
            , bp::return_internal_reference< >() )    
        .def( 
            "resizeGLObjectBuffers"
            , (void ( ::osg::BufferObject::* )( unsigned int ) )(&::osg::BufferObject::resizeGLObjectBuffers)
            , (void ( UniformBufferObject_wrapper::* )( unsigned int ) )(&UniformBufferObject_wrapper::default_resizeGLObjectBuffers)
            , ( bp::arg("maxSize") ) )    
        .def( 
            "setName"
            , (void ( ::osg::Object::* )( ::std::string const & ) )(&::osg::Object::setName)
            , (void ( UniformBufferObject_wrapper::* )( ::std::string const & ) )(&UniformBufferObject_wrapper::default_setName)
            , ( bp::arg("name") ) )    
        .def( 
            "setName"
            , (void ( ::osg::Object::* )( char const * ) )( &::osg::Object::setName )
            , ( bp::arg("name") )
            , " Set the name of object using a C style string." )    
        .def( 
            "setThreadSafeRefUnref"
            , (void ( ::osg::Object::* )( bool ) )(&::osg::Object::setThreadSafeRefUnref)
            , (void ( UniformBufferObject_wrapper::* )( bool ) )(&UniformBufferObject_wrapper::default_setThreadSafeRefUnref)
            , ( bp::arg("threadSafe") ) )    
        .def( 
            "setUserData"
            , (void ( ::osg::Object::* )( ::osg::Referenced * ) )(&::osg::Object::setUserData)
            , (void ( UniformBufferObject_wrapper::* )( ::osg::Referenced * ) )(&UniformBufferObject_wrapper::default_setUserData)
            , ( bp::arg("obj") ) );

}
