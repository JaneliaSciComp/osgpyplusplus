// This file has been generated by Py++.

#include "boost/python.hpp"
#include "wrap_osganimation.h"
#include "wrap_referenced.h"
#include "stackedquaternionelement.pypp.hpp"

namespace bp = boost::python;

struct StackedQuaternionElement_wrapper : osgAnimation::StackedQuaternionElement, bp::wrapper< osgAnimation::StackedQuaternionElement > {

    StackedQuaternionElement_wrapper( )
    : osgAnimation::StackedQuaternionElement( )
      , bp::wrapper< osgAnimation::StackedQuaternionElement >(){
        // null constructor
    
    }

    StackedQuaternionElement_wrapper(::std::string const & arg0, ::osg::Quat const & q=osg::Quat(0.0, 0.0, 0.0, 1.0e+0) )
    : osgAnimation::StackedQuaternionElement( arg0, boost::ref(q) )
      , bp::wrapper< osgAnimation::StackedQuaternionElement >(){
        // constructor
    
    }

    StackedQuaternionElement_wrapper(::osg::Quat const & arg0 )
    : osgAnimation::StackedQuaternionElement( boost::ref(arg0) )
      , bp::wrapper< osgAnimation::StackedQuaternionElement >(){
        // constructor
    
    }

    virtual void applyToMatrix( ::osg::Matrix & matrix ) const  {
        if( bp::override func_applyToMatrix = this->get_override( "applyToMatrix" ) )
            func_applyToMatrix( boost::ref(matrix) );
        else{
            this->osgAnimation::StackedQuaternionElement::applyToMatrix( boost::ref(matrix) );
        }
    }
    
    void default_applyToMatrix( ::osg::Matrix & matrix ) const  {
        osgAnimation::StackedQuaternionElement::applyToMatrix( boost::ref(matrix) );
    }

    virtual char const * className(  ) const  {
        if( bp::override func_className = this->get_override( "className" ) )
            return func_className(  );
        else{
            return this->osgAnimation::StackedQuaternionElement::className(  );
        }
    }
    
    char const * default_className(  ) const  {
        return osgAnimation::StackedQuaternionElement::className( );
    }

    virtual ::osg::Object * clone( ::osg::CopyOp const & copyop ) const  {
        if( bp::override func_clone = this->get_override( "clone" ) )
            return func_clone( boost::ref(copyop) );
        else{
            return this->osgAnimation::StackedQuaternionElement::clone( boost::ref(copyop) );
        }
    }
    
    ::osg::Object * default_clone( ::osg::CopyOp const & copyop ) const  {
        return osgAnimation::StackedQuaternionElement::clone( boost::ref(copyop) );
    }

    virtual ::osg::Object * cloneType(  ) const  {
        if( bp::override func_cloneType = this->get_override( "cloneType" ) )
            return func_cloneType(  );
        else{
            return this->osgAnimation::StackedQuaternionElement::cloneType(  );
        }
    }
    
    ::osg::Object * default_cloneType(  ) const  {
        return osgAnimation::StackedQuaternionElement::cloneType( );
    }

    virtual ::osg::Matrix getAsMatrix(  ) const  {
        if( bp::override func_getAsMatrix = this->get_override( "getAsMatrix" ) )
            return func_getAsMatrix(  );
        else{
            return this->osgAnimation::StackedQuaternionElement::getAsMatrix(  );
        }
    }
    
    ::osg::Matrix default_getAsMatrix(  ) const  {
        return osgAnimation::StackedQuaternionElement::getAsMatrix( );
    }

    virtual ::osgAnimation::Target * getOrCreateTarget(  ) {
        if( bp::override func_getOrCreateTarget = this->get_override( "getOrCreateTarget" ) )
            return func_getOrCreateTarget(  );
        else{
            return this->osgAnimation::StackedQuaternionElement::getOrCreateTarget(  );
        }
    }
    
    ::osgAnimation::Target * default_getOrCreateTarget(  ) {
        return osgAnimation::StackedQuaternionElement::getOrCreateTarget( );
    }

    virtual ::osgAnimation::Target * getTarget(  ) {
        if( bp::override func_getTarget = this->get_override( "getTarget" ) )
            return func_getTarget(  );
        else{
            return this->osgAnimation::StackedQuaternionElement::getTarget(  );
        }
    }
    
    ::osgAnimation::Target * default_getTarget(  ) {
        return osgAnimation::StackedQuaternionElement::getTarget( );
    }

    virtual ::osgAnimation::Target const * getTarget(  ) const  {
        if( bp::override func_getTarget = this->get_override( "getTarget" ) )
            return func_getTarget(  );
        else{
            return this->osgAnimation::StackedQuaternionElement::getTarget(  );
        }
    }
    
    ::osgAnimation::Target const * default_getTarget(  ) const  {
        return osgAnimation::StackedQuaternionElement::getTarget( );
    }

    virtual bool isIdentity(  ) const  {
        if( bp::override func_isIdentity = this->get_override( "isIdentity" ) )
            return func_isIdentity(  );
        else{
            return this->osgAnimation::StackedQuaternionElement::isIdentity(  );
        }
    }
    
    bool default_isIdentity(  ) const  {
        return osgAnimation::StackedQuaternionElement::isIdentity( );
    }

    virtual bool isSameKindAs( ::osg::Object const * obj ) const  {
        if( bp::override func_isSameKindAs = this->get_override( "isSameKindAs" ) )
            return func_isSameKindAs( boost::python::ptr(obj) );
        else{
            return this->osgAnimation::StackedQuaternionElement::isSameKindAs( boost::python::ptr(obj) );
        }
    }
    
    bool default_isSameKindAs( ::osg::Object const * obj ) const  {
        return osgAnimation::StackedQuaternionElement::isSameKindAs( boost::python::ptr(obj) );
    }

    virtual char const * libraryName(  ) const  {
        if( bp::override func_libraryName = this->get_override( "libraryName" ) )
            return func_libraryName(  );
        else{
            return this->osgAnimation::StackedQuaternionElement::libraryName(  );
        }
    }
    
    char const * default_libraryName(  ) const  {
        return osgAnimation::StackedQuaternionElement::libraryName( );
    }

    virtual void update( float t=0.0 ) {
        if( bp::override func_update = this->get_override( "update" ) )
            func_update( t );
        else{
            this->osgAnimation::StackedQuaternionElement::update( t );
        }
    }
    
    void default_update( float t=0.0 ) {
        osgAnimation::StackedQuaternionElement::update( t );
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

void register_StackedQuaternionElement_class(){

    { //::osgAnimation::StackedQuaternionElement
        typedef bp::class_< StackedQuaternionElement_wrapper, bp::bases< osgAnimation::StackedTransformElement >, osg::ref_ptr< StackedQuaternionElement_wrapper >, boost::noncopyable > StackedQuaternionElement_exposer_t;
        StackedQuaternionElement_exposer_t StackedQuaternionElement_exposer = StackedQuaternionElement_exposer_t( "StackedQuaternionElement", bp::init< >() );
        bp::scope StackedQuaternionElement_scope( StackedQuaternionElement_exposer );
        StackedQuaternionElement_exposer.def( bp::init< std::string const &, bp::optional< osg::Quat const & > >(( bp::arg("arg0"), bp::arg("q")=osg::Quat(0.0, 0.0, 0.0, 1.0e+0) )) );
        bp::implicitly_convertible< std::string const &, osgAnimation::StackedQuaternionElement >();
        StackedQuaternionElement_exposer.def( bp::init< osg::Quat const & >(( bp::arg("arg0") )) );
        bp::implicitly_convertible< osg::Quat const &, osgAnimation::StackedQuaternionElement >();
        { //::osgAnimation::StackedQuaternionElement::applyToMatrix
        
            typedef void ( ::osgAnimation::StackedQuaternionElement::*applyToMatrix_function_type)( ::osg::Matrix & ) const;
            typedef void ( StackedQuaternionElement_wrapper::*default_applyToMatrix_function_type)( ::osg::Matrix & ) const;
            
            StackedQuaternionElement_exposer.def( 
                "applyToMatrix"
                , applyToMatrix_function_type(&::osgAnimation::StackedQuaternionElement::applyToMatrix)
                , default_applyToMatrix_function_type(&StackedQuaternionElement_wrapper::default_applyToMatrix)
                , ( bp::arg("matrix") ) );
        
        }
        { //::osgAnimation::StackedQuaternionElement::className
        
            typedef char const * ( ::osgAnimation::StackedQuaternionElement::*className_function_type)(  ) const;
            typedef char const * ( StackedQuaternionElement_wrapper::*default_className_function_type)(  ) const;
            
            StackedQuaternionElement_exposer.def( 
                "className"
                , className_function_type(&::osgAnimation::StackedQuaternionElement::className)
                , default_className_function_type(&StackedQuaternionElement_wrapper::default_className) );
        
        }
        { //::osgAnimation::StackedQuaternionElement::clone
        
            typedef ::osg::Object * ( ::osgAnimation::StackedQuaternionElement::*clone_function_type)( ::osg::CopyOp const & ) const;
            typedef ::osg::Object * ( StackedQuaternionElement_wrapper::*default_clone_function_type)( ::osg::CopyOp const & ) const;
            
            StackedQuaternionElement_exposer.def( 
                "clone"
                , clone_function_type(&::osgAnimation::StackedQuaternionElement::clone)
                , default_clone_function_type(&StackedQuaternionElement_wrapper::default_clone)
                , ( bp::arg("copyop") )
                , bp::return_value_policy< bp::reference_existing_object >() );
        
        }
        { //::osgAnimation::StackedQuaternionElement::cloneType
        
            typedef ::osg::Object * ( ::osgAnimation::StackedQuaternionElement::*cloneType_function_type)(  ) const;
            typedef ::osg::Object * ( StackedQuaternionElement_wrapper::*default_cloneType_function_type)(  ) const;
            
            StackedQuaternionElement_exposer.def( 
                "cloneType"
                , cloneType_function_type(&::osgAnimation::StackedQuaternionElement::cloneType)
                , default_cloneType_function_type(&StackedQuaternionElement_wrapper::default_cloneType)
                , bp::return_value_policy< bp::reference_existing_object >() );
        
        }
        { //::osgAnimation::StackedQuaternionElement::getAsMatrix
        
            typedef ::osg::Matrix ( ::osgAnimation::StackedQuaternionElement::*getAsMatrix_function_type)(  ) const;
            typedef ::osg::Matrix ( StackedQuaternionElement_wrapper::*default_getAsMatrix_function_type)(  ) const;
            
            StackedQuaternionElement_exposer.def( 
                "getAsMatrix"
                , getAsMatrix_function_type(&::osgAnimation::StackedQuaternionElement::getAsMatrix)
                , default_getAsMatrix_function_type(&StackedQuaternionElement_wrapper::default_getAsMatrix) );
        
        }
        { //::osgAnimation::StackedQuaternionElement::getOrCreateTarget
        
            typedef ::osgAnimation::Target * ( ::osgAnimation::StackedQuaternionElement::*getOrCreateTarget_function_type)(  ) ;
            typedef ::osgAnimation::Target * ( StackedQuaternionElement_wrapper::*default_getOrCreateTarget_function_type)(  ) ;
            
            StackedQuaternionElement_exposer.def( 
                "getOrCreateTarget"
                , getOrCreateTarget_function_type(&::osgAnimation::StackedQuaternionElement::getOrCreateTarget)
                , default_getOrCreateTarget_function_type(&StackedQuaternionElement_wrapper::default_getOrCreateTarget)
                , bp::return_internal_reference< >() );
        
        }
        { //::osgAnimation::StackedQuaternionElement::getQuaternion
        
            typedef ::osg::Quat const & ( ::osgAnimation::StackedQuaternionElement::*getQuaternion_function_type)(  ) const;
            
            StackedQuaternionElement_exposer.def( 
                "getQuaternion"
                , getQuaternion_function_type( &::osgAnimation::StackedQuaternionElement::getQuaternion )
                , bp::return_internal_reference< >() );
        
        }
        { //::osgAnimation::StackedQuaternionElement::getTarget
        
            typedef ::osgAnimation::Target * ( ::osgAnimation::StackedQuaternionElement::*getTarget_function_type)(  ) ;
            typedef ::osgAnimation::Target * ( StackedQuaternionElement_wrapper::*default_getTarget_function_type)(  ) ;
            
            StackedQuaternionElement_exposer.def( 
                "getTarget"
                , getTarget_function_type(&::osgAnimation::StackedQuaternionElement::getTarget)
                , default_getTarget_function_type(&StackedQuaternionElement_wrapper::default_getTarget)
                , bp::return_internal_reference< >() );
        
        }
        { //::osgAnimation::StackedQuaternionElement::getTarget
        
            typedef ::osgAnimation::Target const * ( ::osgAnimation::StackedQuaternionElement::*getTarget_function_type)(  ) const;
            typedef ::osgAnimation::Target const * ( StackedQuaternionElement_wrapper::*default_getTarget_function_type)(  ) const;
            
            StackedQuaternionElement_exposer.def( 
                "getTarget"
                , getTarget_function_type(&::osgAnimation::StackedQuaternionElement::getTarget)
                , default_getTarget_function_type(&StackedQuaternionElement_wrapper::default_getTarget)
                , bp::return_internal_reference< >() );
        
        }
        { //::osgAnimation::StackedQuaternionElement::isIdentity
        
            typedef bool ( ::osgAnimation::StackedQuaternionElement::*isIdentity_function_type)(  ) const;
            typedef bool ( StackedQuaternionElement_wrapper::*default_isIdentity_function_type)(  ) const;
            
            StackedQuaternionElement_exposer.def( 
                "isIdentity"
                , isIdentity_function_type(&::osgAnimation::StackedQuaternionElement::isIdentity)
                , default_isIdentity_function_type(&StackedQuaternionElement_wrapper::default_isIdentity) );
        
        }
        { //::osgAnimation::StackedQuaternionElement::isSameKindAs
        
            typedef bool ( ::osgAnimation::StackedQuaternionElement::*isSameKindAs_function_type)( ::osg::Object const * ) const;
            typedef bool ( StackedQuaternionElement_wrapper::*default_isSameKindAs_function_type)( ::osg::Object const * ) const;
            
            StackedQuaternionElement_exposer.def( 
                "isSameKindAs"
                , isSameKindAs_function_type(&::osgAnimation::StackedQuaternionElement::isSameKindAs)
                , default_isSameKindAs_function_type(&StackedQuaternionElement_wrapper::default_isSameKindAs)
                , ( bp::arg("obj") ) );
        
        }
        { //::osgAnimation::StackedQuaternionElement::libraryName
        
            typedef char const * ( ::osgAnimation::StackedQuaternionElement::*libraryName_function_type)(  ) const;
            typedef char const * ( StackedQuaternionElement_wrapper::*default_libraryName_function_type)(  ) const;
            
            StackedQuaternionElement_exposer.def( 
                "libraryName"
                , libraryName_function_type(&::osgAnimation::StackedQuaternionElement::libraryName)
                , default_libraryName_function_type(&StackedQuaternionElement_wrapper::default_libraryName) );
        
        }
        { //::osgAnimation::StackedQuaternionElement::setQuaternion
        
            typedef void ( ::osgAnimation::StackedQuaternionElement::*setQuaternion_function_type)( ::osg::Quat const & ) ;
            
            StackedQuaternionElement_exposer.def( 
                "setQuaternion"
                , setQuaternion_function_type( &::osgAnimation::StackedQuaternionElement::setQuaternion )
                , ( bp::arg("arg0") ) );
        
        }
        { //::osgAnimation::StackedQuaternionElement::update
        
            typedef void ( ::osgAnimation::StackedQuaternionElement::*update_function_type)( float ) ;
            typedef void ( StackedQuaternionElement_wrapper::*default_update_function_type)( float ) ;
            
            StackedQuaternionElement_exposer.def( 
                "update"
                , update_function_type(&::osgAnimation::StackedQuaternionElement::update)
                , default_update_function_type(&StackedQuaternionElement_wrapper::default_update)
                , ( bp::arg("t")=0.0 ) );
        
        }
    }

}
