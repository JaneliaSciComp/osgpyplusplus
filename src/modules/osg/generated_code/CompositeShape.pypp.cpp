// This file has been generated by Py++.

#include "boost/python.hpp"
#include "wrap_osg.h"
#include "compositeshape.pypp.hpp"

namespace bp = boost::python;

struct CompositeShape_wrapper : osg::CompositeShape, bp::wrapper< osg::CompositeShape > {

    CompositeShape_wrapper( )
    : osg::CompositeShape( )
      , bp::wrapper< osg::CompositeShape >(){
        // null constructor
    
    }

    CompositeShape_wrapper(::osg::CompositeShape const & cs, ::osg::CopyOp const & copyop=SHALLOW_COPY )
    : osg::CompositeShape( boost::ref(cs), boost::ref(copyop) )
      , bp::wrapper< osg::CompositeShape >(){
        // constructor
    
    }

    virtual void accept( ::osg::ShapeVisitor & sv ) {
        if( bp::override func_accept = this->get_override( "accept" ) )
            func_accept( boost::ref(sv) );
        else{
            this->osg::CompositeShape::accept( boost::ref(sv) );
        }
    }
    
    void default_accept( ::osg::ShapeVisitor & sv ) {
        osg::CompositeShape::accept( boost::ref(sv) );
    }

    virtual void accept( ::osg::ConstShapeVisitor & csv ) const  {
        if( bp::override func_accept = this->get_override( "accept" ) )
            func_accept( boost::ref(csv) );
        else{
            this->osg::CompositeShape::accept( boost::ref(csv) );
        }
    }
    
    void default_accept( ::osg::ConstShapeVisitor & csv ) const  {
        osg::CompositeShape::accept( boost::ref(csv) );
    }

    virtual char const * className(  ) const  {
        if( bp::override func_className = this->get_override( "className" ) )
            return func_className(  );
        else{
            return this->osg::CompositeShape::className(  );
        }
    }
    
    char const * default_className(  ) const  {
        return osg::CompositeShape::className( );
    }

    virtual ::osg::Object * clone( ::osg::CopyOp const & copyop ) const  {
        if( bp::override func_clone = this->get_override( "clone" ) )
            return func_clone( boost::ref(copyop) );
        else{
            return this->osg::CompositeShape::clone( boost::ref(copyop) );
        }
    }
    
    ::osg::Object * default_clone( ::osg::CopyOp const & copyop ) const  {
        return osg::CompositeShape::clone( boost::ref(copyop) );
    }

    virtual ::osg::Object * cloneType(  ) const  {
        if( bp::override func_cloneType = this->get_override( "cloneType" ) )
            return func_cloneType(  );
        else{
            return this->osg::CompositeShape::cloneType(  );
        }
    }
    
    ::osg::Object * default_cloneType(  ) const  {
        return osg::CompositeShape::cloneType( );
    }

    virtual bool isSameKindAs( ::osg::Object const * obj ) const  {
        if( bp::override func_isSameKindAs = this->get_override( "isSameKindAs" ) )
            return func_isSameKindAs( boost::python::ptr(obj) );
        else{
            return this->osg::CompositeShape::isSameKindAs( boost::python::ptr(obj) );
        }
    }
    
    bool default_isSameKindAs( ::osg::Object const * obj ) const  {
        return osg::CompositeShape::isSameKindAs( boost::python::ptr(obj) );
    }

    virtual char const * libraryName(  ) const  {
        if( bp::override func_libraryName = this->get_override( "libraryName" ) )
            return func_libraryName(  );
        else{
            return this->osg::CompositeShape::libraryName(  );
        }
    }
    
    char const * default_libraryName(  ) const  {
        return osg::CompositeShape::libraryName( );
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

void register_CompositeShape_class(){

    { //::osg::CompositeShape
        typedef bp::class_< CompositeShape_wrapper, bp::bases< osg::Shape >, boost::noncopyable > CompositeShape_exposer_t;
        CompositeShape_exposer_t CompositeShape_exposer = CompositeShape_exposer_t( "CompositeShape", bp::no_init );
        bp::scope CompositeShape_scope( CompositeShape_exposer );
        CompositeShape_exposer.def( bp::init< >() );
        CompositeShape_exposer.def( bp::init< osg::CompositeShape const &, bp::optional< osg::CopyOp const & > >(( bp::arg("cs"), bp::arg("copyop")=SHALLOW_COPY )) );
        bp::implicitly_convertible< osg::CompositeShape const &, osg::CompositeShape >();
        { //::osg::CompositeShape::accept
        
            typedef void ( ::osg::CompositeShape::*accept_function_type)( ::osg::ShapeVisitor & ) ;
            typedef void ( CompositeShape_wrapper::*default_accept_function_type)( ::osg::ShapeVisitor & ) ;
            
            CompositeShape_exposer.def( 
                "accept"
                , accept_function_type(&::osg::CompositeShape::accept)
                , default_accept_function_type(&CompositeShape_wrapper::default_accept)
                , ( bp::arg("sv") ) );
        
        }
        { //::osg::CompositeShape::accept
        
            typedef void ( ::osg::CompositeShape::*accept_function_type)( ::osg::ConstShapeVisitor & ) const;
            typedef void ( CompositeShape_wrapper::*default_accept_function_type)( ::osg::ConstShapeVisitor & ) const;
            
            CompositeShape_exposer.def( 
                "accept"
                , accept_function_type(&::osg::CompositeShape::accept)
                , default_accept_function_type(&CompositeShape_wrapper::default_accept)
                , ( bp::arg("csv") ) );
        
        }
        { //::osg::CompositeShape::addChild
        
            typedef void ( ::osg::CompositeShape::*addChild_function_type)( ::osg::Shape * ) ;
            
            CompositeShape_exposer.def( 
                "addChild"
                , addChild_function_type( &::osg::CompositeShape::addChild )
                , ( bp::arg("shape") ) );
        
        }
        { //::osg::CompositeShape::className
        
            typedef char const * ( ::osg::CompositeShape::*className_function_type)(  ) const;
            typedef char const * ( CompositeShape_wrapper::*default_className_function_type)(  ) const;
            
            CompositeShape_exposer.def( 
                "className"
                , className_function_type(&::osg::CompositeShape::className)
                , default_className_function_type(&CompositeShape_wrapper::default_className) );
        
        }
        { //::osg::CompositeShape::clone
        
            typedef ::osg::Object * ( ::osg::CompositeShape::*clone_function_type)( ::osg::CopyOp const & ) const;
            typedef ::osg::Object * ( CompositeShape_wrapper::*default_clone_function_type)( ::osg::CopyOp const & ) const;
            
            CompositeShape_exposer.def( 
                "clone"
                , clone_function_type(&::osg::CompositeShape::clone)
                , default_clone_function_type(&CompositeShape_wrapper::default_clone)
                , ( bp::arg("copyop") )
                , bp::return_value_policy< bp::reference_existing_object >() );
        
        }
        { //::osg::CompositeShape::cloneType
        
            typedef ::osg::Object * ( ::osg::CompositeShape::*cloneType_function_type)(  ) const;
            typedef ::osg::Object * ( CompositeShape_wrapper::*default_cloneType_function_type)(  ) const;
            
            CompositeShape_exposer.def( 
                "cloneType"
                , cloneType_function_type(&::osg::CompositeShape::cloneType)
                , default_cloneType_function_type(&CompositeShape_wrapper::default_cloneType)
                , bp::return_value_policy< bp::reference_existing_object >() );
        
        }
        { //::osg::CompositeShape::findChildNo
        
            typedef unsigned int ( ::osg::CompositeShape::*findChildNo_function_type)( ::osg::Shape * ) const;
            
            CompositeShape_exposer.def( 
                "findChildNo"
                , findChildNo_function_type( &::osg::CompositeShape::findChildNo )
                , ( bp::arg("shape") ) );
        
        }
        { //::osg::CompositeShape::getChild
        
            typedef ::osg::Shape * ( ::osg::CompositeShape::*getChild_function_type)( unsigned int ) ;
            
            CompositeShape_exposer.def( 
                "getChild"
                , getChild_function_type( &::osg::CompositeShape::getChild )
                , ( bp::arg("i") )
                    /* undefined call policies */ );
        
        }
        { //::osg::CompositeShape::getChild
        
            typedef ::osg::Shape const * ( ::osg::CompositeShape::*getChild_function_type)( unsigned int ) const;
            
            CompositeShape_exposer.def( 
                "getChild"
                , getChild_function_type( &::osg::CompositeShape::getChild )
                , ( bp::arg("i") )
                    /* undefined call policies */ );
        
        }
        { //::osg::CompositeShape::getNumChildren
        
            typedef unsigned int ( ::osg::CompositeShape::*getNumChildren_function_type)(  ) const;
            
            CompositeShape_exposer.def( 
                "getNumChildren"
                , getNumChildren_function_type( &::osg::CompositeShape::getNumChildren ) );
        
        }
        { //::osg::CompositeShape::getShape
        
            typedef ::osg::Shape * ( ::osg::CompositeShape::*getShape_function_type)(  ) ;
            
            CompositeShape_exposer.def( 
                "getShape"
                , getShape_function_type( &::osg::CompositeShape::getShape )
                    /* undefined call policies */ );
        
        }
        { //::osg::CompositeShape::getShape
        
            typedef ::osg::Shape const * ( ::osg::CompositeShape::*getShape_function_type)(  ) const;
            
            CompositeShape_exposer.def( 
                "getShape"
                , getShape_function_type( &::osg::CompositeShape::getShape )
                    /* undefined call policies */ );
        
        }
        { //::osg::CompositeShape::isSameKindAs
        
            typedef bool ( ::osg::CompositeShape::*isSameKindAs_function_type)( ::osg::Object const * ) const;
            typedef bool ( CompositeShape_wrapper::*default_isSameKindAs_function_type)( ::osg::Object const * ) const;
            
            CompositeShape_exposer.def( 
                "isSameKindAs"
                , isSameKindAs_function_type(&::osg::CompositeShape::isSameKindAs)
                , default_isSameKindAs_function_type(&CompositeShape_wrapper::default_isSameKindAs)
                , ( bp::arg("obj") ) );
        
        }
        { //::osg::CompositeShape::libraryName
        
            typedef char const * ( ::osg::CompositeShape::*libraryName_function_type)(  ) const;
            typedef char const * ( CompositeShape_wrapper::*default_libraryName_function_type)(  ) const;
            
            CompositeShape_exposer.def( 
                "libraryName"
                , libraryName_function_type(&::osg::CompositeShape::libraryName)
                , default_libraryName_function_type(&CompositeShape_wrapper::default_libraryName) );
        
        }
        { //::osg::CompositeShape::removeChild
        
            typedef void ( ::osg::CompositeShape::*removeChild_function_type)( unsigned int ) ;
            
            CompositeShape_exposer.def( 
                "removeChild"
                , removeChild_function_type( &::osg::CompositeShape::removeChild )
                , ( bp::arg("i") ) );
        
        }
        { //::osg::CompositeShape::setShape
        
            typedef void ( ::osg::CompositeShape::*setShape_function_type)( ::osg::Shape * ) ;
            
            CompositeShape_exposer.def( 
                "setShape"
                , setShape_function_type( &::osg::CompositeShape::setShape )
                , ( bp::arg("shape") ) );
        
        }
        { //::osg::Object::computeDataVariance
        
            typedef void ( ::osg::Object::*computeDataVariance_function_type)(  ) ;
            typedef void ( CompositeShape_wrapper::*default_computeDataVariance_function_type)(  ) ;
            
            CompositeShape_exposer.def( 
                "computeDataVariance"
                , computeDataVariance_function_type(&::osg::Object::computeDataVariance)
                , default_computeDataVariance_function_type(&CompositeShape_wrapper::default_computeDataVariance) );
        
        }
        { //::osg::Object::getUserData
        
            typedef ::osg::Referenced * ( ::osg::Object::*getUserData_function_type)(  ) ;
            typedef ::osg::Referenced * ( CompositeShape_wrapper::*default_getUserData_function_type)(  ) ;
            
            CompositeShape_exposer.def( 
                "getUserData"
                , getUserData_function_type(&::osg::Object::getUserData)
                , default_getUserData_function_type(&CompositeShape_wrapper::default_getUserData)
                , bp::return_internal_reference< >() );
        
        }
        { //::osg::Object::getUserData
        
            typedef ::osg::Referenced const * ( ::osg::Object::*getUserData_function_type)(  ) const;
            typedef ::osg::Referenced const * ( CompositeShape_wrapper::*default_getUserData_function_type)(  ) const;
            
            CompositeShape_exposer.def( 
                "getUserData"
                , getUserData_function_type(&::osg::Object::getUserData)
                , default_getUserData_function_type(&CompositeShape_wrapper::default_getUserData)
                , bp::return_internal_reference< >() );
        
        }
        { //::osg::Object::resizeGLObjectBuffers
        
            typedef void ( ::osg::Object::*resizeGLObjectBuffers_function_type)( unsigned int ) ;
            typedef void ( CompositeShape_wrapper::*default_resizeGLObjectBuffers_function_type)( unsigned int ) ;
            
            CompositeShape_exposer.def( 
                "resizeGLObjectBuffers"
                , resizeGLObjectBuffers_function_type(&::osg::Object::resizeGLObjectBuffers)
                , default_resizeGLObjectBuffers_function_type(&CompositeShape_wrapper::default_resizeGLObjectBuffers)
                , ( bp::arg("arg0") ) );
        
        }
        { //::osg::Object::setName
        
            typedef void ( ::osg::Object::*setName_function_type)( ::std::string const & ) ;
            typedef void ( CompositeShape_wrapper::*default_setName_function_type)( ::std::string const & ) ;
            
            CompositeShape_exposer.def( 
                "setName"
                , setName_function_type(&::osg::Object::setName)
                , default_setName_function_type(&CompositeShape_wrapper::default_setName)
                , ( bp::arg("name") ) );
        
        }
        { //::osg::Object::setName
        
            typedef void ( ::osg::Object::*setName_function_type)( char const * ) ;
            
            CompositeShape_exposer.def( 
                "setName"
                , setName_function_type( &::osg::Object::setName )
                , ( bp::arg("name") ) );
        
        }
        { //::osg::Object::setThreadSafeRefUnref
        
            typedef void ( ::osg::Object::*setThreadSafeRefUnref_function_type)( bool ) ;
            typedef void ( CompositeShape_wrapper::*default_setThreadSafeRefUnref_function_type)( bool ) ;
            
            CompositeShape_exposer.def( 
                "setThreadSafeRefUnref"
                , setThreadSafeRefUnref_function_type(&::osg::Object::setThreadSafeRefUnref)
                , default_setThreadSafeRefUnref_function_type(&CompositeShape_wrapper::default_setThreadSafeRefUnref)
                , ( bp::arg("threadSafe") ) );
        
        }
        { //::osg::Object::setUserData
        
            typedef void ( ::osg::Object::*setUserData_function_type)( ::osg::Referenced * ) ;
            typedef void ( CompositeShape_wrapper::*default_setUserData_function_type)( ::osg::Referenced * ) ;
            
            CompositeShape_exposer.def( 
                "setUserData"
                , setUserData_function_type(&::osg::Object::setUserData)
                , default_setUserData_function_type(&CompositeShape_wrapper::default_setUserData)
                , ( bp::arg("obj") ) );
        
        }
    }

}
