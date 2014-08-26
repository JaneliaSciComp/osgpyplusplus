// This file has been generated by Py++.

#include "boost/python.hpp"
#include "wrap_osg.h"
#include "wrap_referenced.h"
#include "cylinder.pypp.hpp"

namespace bp = boost::python;

struct Cylinder_wrapper : osg::Cylinder, bp::wrapper< osg::Cylinder > {

    Cylinder_wrapper( )
    : osg::Cylinder( )
      , bp::wrapper< osg::Cylinder >(){
        // null constructor
    
    }

    Cylinder_wrapper(::osg::Vec3 const & center, float radius, float height )
    : osg::Cylinder( boost::ref(center), radius, height )
      , bp::wrapper< osg::Cylinder >(){
        // constructor
    
    }

    virtual void accept( ::osg::ShapeVisitor & sv ) {
        if( bp::override func_accept = this->get_override( "accept" ) )
            func_accept( boost::ref(sv) );
        else{
            this->osg::Cylinder::accept( boost::ref(sv) );
        }
    }
    
    void default_accept( ::osg::ShapeVisitor & sv ) {
        osg::Cylinder::accept( boost::ref(sv) );
    }

    virtual void accept( ::osg::ConstShapeVisitor & csv ) const  {
        if( bp::override func_accept = this->get_override( "accept" ) )
            func_accept( boost::ref(csv) );
        else{
            this->osg::Cylinder::accept( boost::ref(csv) );
        }
    }
    
    void default_accept( ::osg::ConstShapeVisitor & csv ) const  {
        osg::Cylinder::accept( boost::ref(csv) );
    }

    virtual char const * className(  ) const  {
        if( bp::override func_className = this->get_override( "className" ) )
            return func_className(  );
        else{
            return this->osg::Cylinder::className(  );
        }
    }
    
    char const * default_className(  ) const  {
        return osg::Cylinder::className( );
    }

    virtual ::osg::Object * clone( ::osg::CopyOp const & copyop ) const  {
        if( bp::override func_clone = this->get_override( "clone" ) )
            return func_clone( boost::ref(copyop) );
        else{
            return this->osg::Cylinder::clone( boost::ref(copyop) );
        }
    }
    
    ::osg::Object * default_clone( ::osg::CopyOp const & copyop ) const  {
        return osg::Cylinder::clone( boost::ref(copyop) );
    }

    virtual ::osg::Object * cloneType(  ) const  {
        if( bp::override func_cloneType = this->get_override( "cloneType" ) )
            return func_cloneType(  );
        else{
            return this->osg::Cylinder::cloneType(  );
        }
    }
    
    ::osg::Object * default_cloneType(  ) const  {
        return osg::Cylinder::cloneType( );
    }

    virtual bool isSameKindAs( ::osg::Object const * obj ) const  {
        if( bp::override func_isSameKindAs = this->get_override( "isSameKindAs" ) )
            return func_isSameKindAs( boost::python::ptr(obj) );
        else{
            return this->osg::Cylinder::isSameKindAs( boost::python::ptr(obj) );
        }
    }
    
    bool default_isSameKindAs( ::osg::Object const * obj ) const  {
        return osg::Cylinder::isSameKindAs( boost::python::ptr(obj) );
    }

    virtual char const * libraryName(  ) const  {
        if( bp::override func_libraryName = this->get_override( "libraryName" ) )
            return func_libraryName(  );
        else{
            return this->osg::Cylinder::libraryName(  );
        }
    }
    
    char const * default_libraryName(  ) const  {
        return osg::Cylinder::libraryName( );
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

void register_Cylinder_class(){

    bp::class_< Cylinder_wrapper, bp::bases< osg::Shape >, osg::ref_ptr< ::osg::Cylinder >, boost::noncopyable >( "Cylinder", bp::no_init )    
        .def( bp::init< >() )    
        .def( bp::init< osg::Vec3 const &, float, float >(( bp::arg("center"), bp::arg("radius"), bp::arg("height") )) )    
        .def( 
            "accept"
            , (void ( ::osg::Cylinder::* )( ::osg::ShapeVisitor & ))(&::osg::Cylinder::accept)
            , (void ( Cylinder_wrapper::* )( ::osg::ShapeVisitor & ))(&Cylinder_wrapper::default_accept)
            , ( bp::arg("sv") ) )    
        .def( 
            "accept"
            , (void ( ::osg::Cylinder::* )( ::osg::ConstShapeVisitor & )const)(&::osg::Cylinder::accept)
            , (void ( Cylinder_wrapper::* )( ::osg::ConstShapeVisitor & )const)(&Cylinder_wrapper::default_accept)
            , ( bp::arg("csv") ) )    
        .def( 
            "className"
            , (char const * ( ::osg::Cylinder::* )(  )const)(&::osg::Cylinder::className)
            , (char const * ( Cylinder_wrapper::* )(  )const)(&Cylinder_wrapper::default_className) )    
        .def( 
            "clone"
            , (::osg::Object * ( ::osg::Cylinder::* )( ::osg::CopyOp const & )const)(&::osg::Cylinder::clone)
            , (::osg::Object * ( Cylinder_wrapper::* )( ::osg::CopyOp const & )const)(&Cylinder_wrapper::default_clone)
            , ( bp::arg("copyop") )
            , bp::return_value_policy< bp::reference_existing_object >() )    
        .def( 
            "cloneType"
            , (::osg::Object * ( ::osg::Cylinder::* )(  )const)(&::osg::Cylinder::cloneType)
            , (::osg::Object * ( Cylinder_wrapper::* )(  )const)(&Cylinder_wrapper::default_cloneType)
            , bp::return_value_policy< bp::reference_existing_object >() )    
        .def( 
            "computeRotationMatrix"
            , (::osg::Matrix ( ::osg::Cylinder::* )(  )const)( &::osg::Cylinder::computeRotationMatrix ) )    
        .def( 
            "getCenter"
            , (::osg::Vec3 const & ( ::osg::Cylinder::* )(  )const)( &::osg::Cylinder::getCenter )
            , bp::return_internal_reference< >() )    
        .def( 
            "getHeight"
            , (float ( ::osg::Cylinder::* )(  )const)( &::osg::Cylinder::getHeight ) )    
        .def( 
            "getRadius"
            , (float ( ::osg::Cylinder::* )(  )const)( &::osg::Cylinder::getRadius ) )    
        .def( 
            "getRotation"
            , (::osg::Quat const & ( ::osg::Cylinder::* )(  )const)( &::osg::Cylinder::getRotation )
            , bp::return_internal_reference< >() )    
        .def( 
            "isSameKindAs"
            , (bool ( ::osg::Cylinder::* )( ::osg::Object const * )const)(&::osg::Cylinder::isSameKindAs)
            , (bool ( Cylinder_wrapper::* )( ::osg::Object const * )const)(&Cylinder_wrapper::default_isSameKindAs)
            , ( bp::arg("obj") ) )    
        .def( 
            "libraryName"
            , (char const * ( ::osg::Cylinder::* )(  )const)(&::osg::Cylinder::libraryName)
            , (char const * ( Cylinder_wrapper::* )(  )const)(&Cylinder_wrapper::default_libraryName) )    
        .def( 
            "set"
            , (void ( ::osg::Cylinder::* )( ::osg::Vec3 const &,float,float ))( &::osg::Cylinder::set )
            , ( bp::arg("center"), bp::arg("radius"), bp::arg("height") ) )    
        .def( 
            "setCenter"
            , (void ( ::osg::Cylinder::* )( ::osg::Vec3 const & ))( &::osg::Cylinder::setCenter )
            , ( bp::arg("center") ) )    
        .def( 
            "setHeight"
            , (void ( ::osg::Cylinder::* )( float ))( &::osg::Cylinder::setHeight )
            , ( bp::arg("height") ) )    
        .def( 
            "setRadius"
            , (void ( ::osg::Cylinder::* )( float ))( &::osg::Cylinder::setRadius )
            , ( bp::arg("radius") ) )    
        .def( 
            "setRotation"
            , (void ( ::osg::Cylinder::* )( ::osg::Quat const & ))( &::osg::Cylinder::setRotation )
            , ( bp::arg("quat") ) )    
        .def( 
            "valid"
            , (bool ( ::osg::Cylinder::* )(  )const)( &::osg::Cylinder::valid ) )    
        .def( 
            "zeroRotation"
            , (bool ( ::osg::Cylinder::* )(  )const)( &::osg::Cylinder::zeroRotation ) )    
        .def( 
            "computeDataVariance"
            , (void ( ::osg::Object::* )(  ))(&::osg::Object::computeDataVariance)
            , (void ( Cylinder_wrapper::* )(  ))(&Cylinder_wrapper::default_computeDataVariance) )    
        .def( 
            "getUserData"
            , (::osg::Referenced * ( ::osg::Object::* )(  ))(&::osg::Object::getUserData)
            , (::osg::Referenced * ( Cylinder_wrapper::* )(  ))(&Cylinder_wrapper::default_getUserData)
            , bp::return_internal_reference< >() )    
        .def( 
            "getUserData"
            , (::osg::Referenced const * ( ::osg::Object::* )(  )const)(&::osg::Object::getUserData)
            , (::osg::Referenced const * ( Cylinder_wrapper::* )(  )const)(&Cylinder_wrapper::default_getUserData)
            , bp::return_internal_reference< >() )    
        .def( 
            "resizeGLObjectBuffers"
            , (void ( ::osg::Object::* )( unsigned int ))(&::osg::Object::resizeGLObjectBuffers)
            , (void ( Cylinder_wrapper::* )( unsigned int ))(&Cylinder_wrapper::default_resizeGLObjectBuffers)
            , ( bp::arg("arg0") ) )    
        .def( 
            "setName"
            , (void ( ::osg::Object::* )( ::std::string const & ))(&::osg::Object::setName)
            , (void ( Cylinder_wrapper::* )( ::std::string const & ))(&Cylinder_wrapper::default_setName)
            , ( bp::arg("name") ) )    
        .def( 
            "setName"
            , (void ( ::osg::Object::* )( char const * ))( &::osg::Object::setName )
            , ( bp::arg("name") ) )    
        .def( 
            "setThreadSafeRefUnref"
            , (void ( ::osg::Object::* )( bool ))(&::osg::Object::setThreadSafeRefUnref)
            , (void ( Cylinder_wrapper::* )( bool ))(&Cylinder_wrapper::default_setThreadSafeRefUnref)
            , ( bp::arg("threadSafe") ) )    
        .def( 
            "setUserData"
            , (void ( ::osg::Object::* )( ::osg::Referenced * ))(&::osg::Object::setUserData)
            , (void ( Cylinder_wrapper::* )( ::osg::Referenced * ))(&Cylinder_wrapper::default_setUserData)
            , ( bp::arg("obj") ) );

}