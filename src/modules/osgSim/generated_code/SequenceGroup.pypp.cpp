// This file has been generated by Py++.

#include "boost/python.hpp"
#include "wrap_osgsim.h"
#include "wrap_referenced.h"
#include "sequencegroup.pypp.hpp"

namespace bp = boost::python;

struct SequenceGroup_wrapper : osgSim::SequenceGroup, bp::wrapper< osgSim::SequenceGroup > {

    SequenceGroup_wrapper( )
    : osgSim::SequenceGroup( )
      , bp::wrapper< osgSim::SequenceGroup >(){
        // null constructor
    
    }

    SequenceGroup_wrapper(double baseTime )
    : osgSim::SequenceGroup( baseTime )
      , bp::wrapper< osgSim::SequenceGroup >(){
        // constructor
    
    }

    virtual char const * className(  ) const  {
        if( bp::override func_className = this->get_override( "className" ) )
            return func_className(  );
        else{
            return this->osgSim::SequenceGroup::className(  );
        }
    }
    
    char const * default_className(  ) const  {
        return osgSim::SequenceGroup::className( );
    }

    virtual ::osg::Object * clone( ::osg::CopyOp const & copyop ) const  {
        if( bp::override func_clone = this->get_override( "clone" ) )
            return func_clone( boost::ref(copyop) );
        else{
            return this->osgSim::SequenceGroup::clone( boost::ref(copyop) );
        }
    }
    
    ::osg::Object * default_clone( ::osg::CopyOp const & copyop ) const  {
        return osgSim::SequenceGroup::clone( boost::ref(copyop) );
    }

    virtual ::osg::Object * cloneType(  ) const  {
        if( bp::override func_cloneType = this->get_override( "cloneType" ) )
            return func_cloneType(  );
        else{
            return this->osgSim::SequenceGroup::cloneType(  );
        }
    }
    
    ::osg::Object * default_cloneType(  ) const  {
        return osgSim::SequenceGroup::cloneType( );
    }

    virtual bool isSameKindAs( ::osg::Object const * obj ) const  {
        if( bp::override func_isSameKindAs = this->get_override( "isSameKindAs" ) )
            return func_isSameKindAs( boost::python::ptr(obj) );
        else{
            return this->osgSim::SequenceGroup::isSameKindAs( boost::python::ptr(obj) );
        }
    }
    
    bool default_isSameKindAs( ::osg::Object const * obj ) const  {
        return osgSim::SequenceGroup::isSameKindAs( boost::python::ptr(obj) );
    }

    virtual char const * libraryName(  ) const  {
        if( bp::override func_libraryName = this->get_override( "libraryName" ) )
            return func_libraryName(  );
        else{
            return this->osgSim::SequenceGroup::libraryName(  );
        }
    }
    
    char const * default_libraryName(  ) const  {
        return osgSim::SequenceGroup::libraryName( );
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

void register_SequenceGroup_class(){

    { //::osgSim::SequenceGroup
        typedef bp::class_< SequenceGroup_wrapper, bp::bases< ::osg::Object >, osg::ref_ptr< SequenceGroup_wrapper >, boost::noncopyable > SequenceGroup_exposer_t;
        SequenceGroup_exposer_t SequenceGroup_exposer = SequenceGroup_exposer_t( "SequenceGroup", "\n sequence group which can be used to synchronize related blink sequences.\n", bp::init< >("\n sequence group which can be used to synchronize related blink sequences.\n") );
        bp::scope SequenceGroup_scope( SequenceGroup_exposer );
        SequenceGroup_exposer.def( bp::init< double >(( bp::arg("baseTime") )) );
        bp::implicitly_convertible< double, osgSim::SequenceGroup >();
        { //::osgSim::SequenceGroup::className
        
            typedef char const * ( ::osgSim::SequenceGroup::*className_function_type)(  ) const;
            typedef char const * ( SequenceGroup_wrapper::*default_className_function_type)(  ) const;
            
            SequenceGroup_exposer.def( 
                "className"
                , className_function_type(&::osgSim::SequenceGroup::className)
                , default_className_function_type(&SequenceGroup_wrapper::default_className) );
        
        }
        { //::osgSim::SequenceGroup::clone
        
            typedef ::osg::Object * ( ::osgSim::SequenceGroup::*clone_function_type)( ::osg::CopyOp const & ) const;
            typedef ::osg::Object * ( SequenceGroup_wrapper::*default_clone_function_type)( ::osg::CopyOp const & ) const;
            
            SequenceGroup_exposer.def( 
                "clone"
                , clone_function_type(&::osgSim::SequenceGroup::clone)
                , default_clone_function_type(&SequenceGroup_wrapper::default_clone)
                , ( bp::arg("copyop") )
                , bp::return_value_policy< bp::reference_existing_object >() );
        
        }
        { //::osgSim::SequenceGroup::cloneType
        
            typedef ::osg::Object * ( ::osgSim::SequenceGroup::*cloneType_function_type)(  ) const;
            typedef ::osg::Object * ( SequenceGroup_wrapper::*default_cloneType_function_type)(  ) const;
            
            SequenceGroup_exposer.def( 
                "cloneType"
                , cloneType_function_type(&::osgSim::SequenceGroup::cloneType)
                , default_cloneType_function_type(&SequenceGroup_wrapper::default_cloneType)
                , bp::return_value_policy< bp::reference_existing_object >() );
        
        }
        { //::osgSim::SequenceGroup::getBaseTime
        
            typedef double ( ::osgSim::SequenceGroup::*getBaseTime_function_type)(  ) const;
            
            SequenceGroup_exposer.def( 
                "getBaseTime"
                , getBaseTime_function_type( &::osgSim::SequenceGroup::getBaseTime ) );
        
        }
        { //::osgSim::SequenceGroup::isSameKindAs
        
            typedef bool ( ::osgSim::SequenceGroup::*isSameKindAs_function_type)( ::osg::Object const * ) const;
            typedef bool ( SequenceGroup_wrapper::*default_isSameKindAs_function_type)( ::osg::Object const * ) const;
            
            SequenceGroup_exposer.def( 
                "isSameKindAs"
                , isSameKindAs_function_type(&::osgSim::SequenceGroup::isSameKindAs)
                , default_isSameKindAs_function_type(&SequenceGroup_wrapper::default_isSameKindAs)
                , ( bp::arg("obj") ) );
        
        }
        { //::osgSim::SequenceGroup::libraryName
        
            typedef char const * ( ::osgSim::SequenceGroup::*libraryName_function_type)(  ) const;
            typedef char const * ( SequenceGroup_wrapper::*default_libraryName_function_type)(  ) const;
            
            SequenceGroup_exposer.def( 
                "libraryName"
                , libraryName_function_type(&::osgSim::SequenceGroup::libraryName)
                , default_libraryName_function_type(&SequenceGroup_wrapper::default_libraryName) );
        
        }
        { //::osgSim::SequenceGroup::setBaseTime
        
            typedef void ( ::osgSim::SequenceGroup::*setBaseTime_function_type)( double ) ;
            
            SequenceGroup_exposer.def( 
                "setBaseTime"
                , setBaseTime_function_type( &::osgSim::SequenceGroup::setBaseTime )
                , ( bp::arg("t") ) );
        
        }
        SequenceGroup_exposer.def_readwrite( "_baseTime", &osgSim::SequenceGroup::_baseTime );
    }

}