// This file has been generated by Py++.

#include "boost/python.hpp"
#include "wrap_osg.h"
#include "box.pypp.hpp"

namespace bp = boost::python;

struct Box_wrapper : osg::Box, bp::wrapper< osg::Box > {

    Box_wrapper( )
    : osg::Box( )
      , bp::wrapper< osg::Box >(){
        // null constructor
    
    }

    Box_wrapper(::osg::Vec3 const & center, float width )
    : osg::Box( boost::ref(center), width )
      , bp::wrapper< osg::Box >(){
        // constructor
    
    }

    Box_wrapper(::osg::Vec3 const & center, float lengthX, float lengthY, float lengthZ )
    : osg::Box( boost::ref(center), lengthX, lengthY, lengthZ )
      , bp::wrapper< osg::Box >(){
        // constructor
    
    }

    Box_wrapper(::osg::Box const & box, ::osg::CopyOp const & copyop=SHALLOW_COPY )
    : osg::Box( boost::ref(box), boost::ref(copyop) )
      , bp::wrapper< osg::Box >(){
        // constructor
    
    }

    virtual void accept( ::osg::ShapeVisitor & sv ) {
        if( bp::override func_accept = this->get_override( "accept" ) )
            func_accept( boost::ref(sv) );
        else{
            this->osg::Box::accept( boost::ref(sv) );
        }
    }
    
    void default_accept( ::osg::ShapeVisitor & sv ) {
        osg::Box::accept( boost::ref(sv) );
    }

    virtual void accept( ::osg::ConstShapeVisitor & csv ) const  {
        if( bp::override func_accept = this->get_override( "accept" ) )
            func_accept( boost::ref(csv) );
        else{
            this->osg::Box::accept( boost::ref(csv) );
        }
    }
    
    void default_accept( ::osg::ConstShapeVisitor & csv ) const  {
        osg::Box::accept( boost::ref(csv) );
    }

    virtual char const * className(  ) const  {
        if( bp::override func_className = this->get_override( "className" ) )
            return func_className(  );
        else{
            return this->osg::Box::className(  );
        }
    }
    
    char const * default_className(  ) const  {
        return osg::Box::className( );
    }

    virtual ::osg::Object * clone( ::osg::CopyOp const & copyop ) const  {
        if( bp::override func_clone = this->get_override( "clone" ) )
            return func_clone( boost::ref(copyop) );
        else{
            return this->osg::Box::clone( boost::ref(copyop) );
        }
    }
    
    ::osg::Object * default_clone( ::osg::CopyOp const & copyop ) const  {
        return osg::Box::clone( boost::ref(copyop) );
    }

    virtual ::osg::Object * cloneType(  ) const  {
        if( bp::override func_cloneType = this->get_override( "cloneType" ) )
            return func_cloneType(  );
        else{
            return this->osg::Box::cloneType(  );
        }
    }
    
    ::osg::Object * default_cloneType(  ) const  {
        return osg::Box::cloneType( );
    }

    virtual bool isSameKindAs( ::osg::Object const * obj ) const  {
        if( bp::override func_isSameKindAs = this->get_override( "isSameKindAs" ) )
            return func_isSameKindAs( boost::python::ptr(obj) );
        else{
            return this->osg::Box::isSameKindAs( boost::python::ptr(obj) );
        }
    }
    
    bool default_isSameKindAs( ::osg::Object const * obj ) const  {
        return osg::Box::isSameKindAs( boost::python::ptr(obj) );
    }

    virtual char const * libraryName(  ) const  {
        if( bp::override func_libraryName = this->get_override( "libraryName" ) )
            return func_libraryName(  );
        else{
            return this->osg::Box::libraryName(  );
        }
    }
    
    char const * default_libraryName(  ) const  {
        return osg::Box::libraryName( );
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

void register_Box_class(){

    { //::osg::Box
        typedef bp::class_< Box_wrapper, bp::bases< osg::Shape >, boost::noncopyable > Box_exposer_t;
        Box_exposer_t Box_exposer = Box_exposer_t( "Box", bp::no_init );
        bp::scope Box_scope( Box_exposer );
        Box_exposer.def( bp::init< >() );
        Box_exposer.def( bp::init< osg::Vec3 const &, float >(( bp::arg("center"), bp::arg("width") )) );
        Box_exposer.def( bp::init< osg::Vec3 const &, float, float, float >(( bp::arg("center"), bp::arg("lengthX"), bp::arg("lengthY"), bp::arg("lengthZ") )) );
        Box_exposer.def( bp::init< osg::Box const &, bp::optional< osg::CopyOp const & > >(( bp::arg("box"), bp::arg("copyop")=SHALLOW_COPY )) );
        bp::implicitly_convertible< osg::Box const &, osg::Box >();
        { //::osg::Box::accept
        
            typedef void ( ::osg::Box::*accept_function_type)( ::osg::ShapeVisitor & ) ;
            typedef void ( Box_wrapper::*default_accept_function_type)( ::osg::ShapeVisitor & ) ;
            
            Box_exposer.def( 
                "accept"
                , accept_function_type(&::osg::Box::accept)
                , default_accept_function_type(&Box_wrapper::default_accept)
                , ( bp::arg("sv") ) );
        
        }
        { //::osg::Box::accept
        
            typedef void ( ::osg::Box::*accept_function_type)( ::osg::ConstShapeVisitor & ) const;
            typedef void ( Box_wrapper::*default_accept_function_type)( ::osg::ConstShapeVisitor & ) const;
            
            Box_exposer.def( 
                "accept"
                , accept_function_type(&::osg::Box::accept)
                , default_accept_function_type(&Box_wrapper::default_accept)
                , ( bp::arg("csv") ) );
        
        }
        { //::osg::Box::className
        
            typedef char const * ( ::osg::Box::*className_function_type)(  ) const;
            typedef char const * ( Box_wrapper::*default_className_function_type)(  ) const;
            
            Box_exposer.def( 
                "className"
                , className_function_type(&::osg::Box::className)
                , default_className_function_type(&Box_wrapper::default_className) );
        
        }
        { //::osg::Box::clone
        
            typedef ::osg::Object * ( ::osg::Box::*clone_function_type)( ::osg::CopyOp const & ) const;
            typedef ::osg::Object * ( Box_wrapper::*default_clone_function_type)( ::osg::CopyOp const & ) const;
            
            Box_exposer.def( 
                "clone"
                , clone_function_type(&::osg::Box::clone)
                , default_clone_function_type(&Box_wrapper::default_clone)
                , ( bp::arg("copyop") )
                , bp::return_value_policy< bp::reference_existing_object >() );
        
        }
        { //::osg::Box::cloneType
        
            typedef ::osg::Object * ( ::osg::Box::*cloneType_function_type)(  ) const;
            typedef ::osg::Object * ( Box_wrapper::*default_cloneType_function_type)(  ) const;
            
            Box_exposer.def( 
                "cloneType"
                , cloneType_function_type(&::osg::Box::cloneType)
                , default_cloneType_function_type(&Box_wrapper::default_cloneType)
                , bp::return_value_policy< bp::reference_existing_object >() );
        
        }
        { //::osg::Box::computeRotationMatrix
        
            typedef ::osg::Matrix ( ::osg::Box::*computeRotationMatrix_function_type)(  ) const;
            
            Box_exposer.def( 
                "computeRotationMatrix"
                , computeRotationMatrix_function_type( &::osg::Box::computeRotationMatrix ) );
        
        }
        { //::osg::Box::getCenter
        
            typedef ::osg::Vec3 const & ( ::osg::Box::*getCenter_function_type)(  ) const;
            
            Box_exposer.def( 
                "getCenter"
                , getCenter_function_type( &::osg::Box::getCenter )
                , bp::return_internal_reference< >() );
        
        }
        { //::osg::Box::getHalfLengths
        
            typedef ::osg::Vec3 const & ( ::osg::Box::*getHalfLengths_function_type)(  ) const;
            
            Box_exposer.def( 
                "getHalfLengths"
                , getHalfLengths_function_type( &::osg::Box::getHalfLengths )
                , bp::return_internal_reference< >() );
        
        }
        { //::osg::Box::getRotation
        
            typedef ::osg::Quat const & ( ::osg::Box::*getRotation_function_type)(  ) const;
            
            Box_exposer.def( 
                "getRotation"
                , getRotation_function_type( &::osg::Box::getRotation )
                , bp::return_internal_reference< >() );
        
        }
        { //::osg::Box::isSameKindAs
        
            typedef bool ( ::osg::Box::*isSameKindAs_function_type)( ::osg::Object const * ) const;
            typedef bool ( Box_wrapper::*default_isSameKindAs_function_type)( ::osg::Object const * ) const;
            
            Box_exposer.def( 
                "isSameKindAs"
                , isSameKindAs_function_type(&::osg::Box::isSameKindAs)
                , default_isSameKindAs_function_type(&Box_wrapper::default_isSameKindAs)
                , ( bp::arg("obj") ) );
        
        }
        { //::osg::Box::libraryName
        
            typedef char const * ( ::osg::Box::*libraryName_function_type)(  ) const;
            typedef char const * ( Box_wrapper::*default_libraryName_function_type)(  ) const;
            
            Box_exposer.def( 
                "libraryName"
                , libraryName_function_type(&::osg::Box::libraryName)
                , default_libraryName_function_type(&Box_wrapper::default_libraryName) );
        
        }
        { //::osg::Box::set
        
            typedef void ( ::osg::Box::*set_function_type)( ::osg::Vec3 const &,::osg::Vec3 const & ) ;
            
            Box_exposer.def( 
                "set"
                , set_function_type( &::osg::Box::set )
                , ( bp::arg("center"), bp::arg("halfLengths") ) );
        
        }
        { //::osg::Box::setCenter
        
            typedef void ( ::osg::Box::*setCenter_function_type)( ::osg::Vec3 const & ) ;
            
            Box_exposer.def( 
                "setCenter"
                , setCenter_function_type( &::osg::Box::setCenter )
                , ( bp::arg("center") ) );
        
        }
        { //::osg::Box::setHalfLengths
        
            typedef void ( ::osg::Box::*setHalfLengths_function_type)( ::osg::Vec3 const & ) ;
            
            Box_exposer.def( 
                "setHalfLengths"
                , setHalfLengths_function_type( &::osg::Box::setHalfLengths )
                , ( bp::arg("halfLengths") ) );
        
        }
        { //::osg::Box::setRotation
        
            typedef void ( ::osg::Box::*setRotation_function_type)( ::osg::Quat const & ) ;
            
            Box_exposer.def( 
                "setRotation"
                , setRotation_function_type( &::osg::Box::setRotation )
                , ( bp::arg("quat") ) );
        
        }
        { //::osg::Box::valid
        
            typedef bool ( ::osg::Box::*valid_function_type)(  ) const;
            
            Box_exposer.def( 
                "valid"
                , valid_function_type( &::osg::Box::valid ) );
        
        }
        { //::osg::Box::zeroRotation
        
            typedef bool ( ::osg::Box::*zeroRotation_function_type)(  ) const;
            
            Box_exposer.def( 
                "zeroRotation"
                , zeroRotation_function_type( &::osg::Box::zeroRotation ) );
        
        }
        { //::osg::Object::computeDataVariance
        
            typedef void ( ::osg::Object::*computeDataVariance_function_type)(  ) ;
            typedef void ( Box_wrapper::*default_computeDataVariance_function_type)(  ) ;
            
            Box_exposer.def( 
                "computeDataVariance"
                , computeDataVariance_function_type(&::osg::Object::computeDataVariance)
                , default_computeDataVariance_function_type(&Box_wrapper::default_computeDataVariance) );
        
        }
        { //::osg::Object::getUserData
        
            typedef ::osg::Referenced * ( ::osg::Object::*getUserData_function_type)(  ) ;
            typedef ::osg::Referenced * ( Box_wrapper::*default_getUserData_function_type)(  ) ;
            
            Box_exposer.def( 
                "getUserData"
                , getUserData_function_type(&::osg::Object::getUserData)
                , default_getUserData_function_type(&Box_wrapper::default_getUserData)
                , bp::return_internal_reference< >() );
        
        }
        { //::osg::Object::getUserData
        
            typedef ::osg::Referenced const * ( ::osg::Object::*getUserData_function_type)(  ) const;
            typedef ::osg::Referenced const * ( Box_wrapper::*default_getUserData_function_type)(  ) const;
            
            Box_exposer.def( 
                "getUserData"
                , getUserData_function_type(&::osg::Object::getUserData)
                , default_getUserData_function_type(&Box_wrapper::default_getUserData)
                , bp::return_internal_reference< >() );
        
        }
        { //::osg::Object::resizeGLObjectBuffers
        
            typedef void ( ::osg::Object::*resizeGLObjectBuffers_function_type)( unsigned int ) ;
            typedef void ( Box_wrapper::*default_resizeGLObjectBuffers_function_type)( unsigned int ) ;
            
            Box_exposer.def( 
                "resizeGLObjectBuffers"
                , resizeGLObjectBuffers_function_type(&::osg::Object::resizeGLObjectBuffers)
                , default_resizeGLObjectBuffers_function_type(&Box_wrapper::default_resizeGLObjectBuffers)
                , ( bp::arg("arg0") ) );
        
        }
        { //::osg::Object::setName
        
            typedef void ( ::osg::Object::*setName_function_type)( ::std::string const & ) ;
            typedef void ( Box_wrapper::*default_setName_function_type)( ::std::string const & ) ;
            
            Box_exposer.def( 
                "setName"
                , setName_function_type(&::osg::Object::setName)
                , default_setName_function_type(&Box_wrapper::default_setName)
                , ( bp::arg("name") ) );
        
        }
        { //::osg::Object::setName
        
            typedef void ( ::osg::Object::*setName_function_type)( char const * ) ;
            
            Box_exposer.def( 
                "setName"
                , setName_function_type( &::osg::Object::setName )
                , ( bp::arg("name") ) );
        
        }
        { //::osg::Object::setThreadSafeRefUnref
        
            typedef void ( ::osg::Object::*setThreadSafeRefUnref_function_type)( bool ) ;
            typedef void ( Box_wrapper::*default_setThreadSafeRefUnref_function_type)( bool ) ;
            
            Box_exposer.def( 
                "setThreadSafeRefUnref"
                , setThreadSafeRefUnref_function_type(&::osg::Object::setThreadSafeRefUnref)
                , default_setThreadSafeRefUnref_function_type(&Box_wrapper::default_setThreadSafeRefUnref)
                , ( bp::arg("threadSafe") ) );
        
        }
        { //::osg::Object::setUserData
        
            typedef void ( ::osg::Object::*setUserData_function_type)( ::osg::Referenced * ) ;
            typedef void ( Box_wrapper::*default_setUserData_function_type)( ::osg::Referenced * ) ;
            
            Box_exposer.def( 
                "setUserData"
                , setUserData_function_type(&::osg::Object::setUserData)
                , default_setUserData_function_type(&Box_wrapper::default_setUserData)
                , ( bp::arg("obj") ) );
        
        }
    }

}
