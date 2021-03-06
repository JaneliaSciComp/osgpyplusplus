// This file has been generated by Py++.

#include "boost/python.hpp"
#include "wrap_osgparticle.h"
#include "wrap_referenced.h"
#include "fireeffect.pypp.hpp"

namespace bp = boost::python;

struct FireEffect_wrapper : osgParticle::FireEffect, bp::wrapper< osgParticle::FireEffect > {

    FireEffect_wrapper(bool automaticSetup=true )
    : osgParticle::FireEffect( automaticSetup )
      , bp::wrapper< osgParticle::FireEffect >(){
        // constructor
    
    }

    FireEffect_wrapper(::osg::Vec3 const & position, float scale=1.0e+0f, float intensity=1.0e+0f )
    : osgParticle::FireEffect( boost::ref(position), scale, intensity )
      , bp::wrapper< osgParticle::FireEffect >(){
        // constructor
    
    }

    virtual void accept( ::osg::NodeVisitor & nv ) {
        if( bp::override func_accept = this->get_override( "accept" ) )
            func_accept( boost::ref(nv) );
        else{
            this->osgParticle::FireEffect::accept( boost::ref(nv) );
        }
    }
    
    void default_accept( ::osg::NodeVisitor & nv ) {
        osgParticle::FireEffect::accept( boost::ref(nv) );
    }

    virtual char const * className(  ) const  {
        if( bp::override func_className = this->get_override( "className" ) )
            return func_className(  );
        else{
            return this->osgParticle::FireEffect::className(  );
        }
    }
    
    char const * default_className(  ) const  {
        return osgParticle::FireEffect::className( );
    }

    virtual ::osg::Object * clone( ::osg::CopyOp const & copyop ) const  {
        if( bp::override func_clone = this->get_override( "clone" ) )
            return func_clone( boost::ref(copyop) );
        else{
            return this->osgParticle::FireEffect::clone( boost::ref(copyop) );
        }
    }
    
    ::osg::Object * default_clone( ::osg::CopyOp const & copyop ) const  {
        return osgParticle::FireEffect::clone( boost::ref(copyop) );
    }

    virtual ::osg::Object * cloneType(  ) const  {
        if( bp::override func_cloneType = this->get_override( "cloneType" ) )
            return func_cloneType(  );
        else{
            return this->osgParticle::FireEffect::cloneType(  );
        }
    }
    
    ::osg::Object * default_cloneType(  ) const  {
        return osgParticle::FireEffect::cloneType( );
    }

    virtual ::osgParticle::Emitter * getEmitter(  ) {
        if( bp::override func_getEmitter = this->get_override( "getEmitter" ) )
            return func_getEmitter(  );
        else{
            return this->osgParticle::FireEffect::getEmitter(  );
        }
    }
    
    ::osgParticle::Emitter * default_getEmitter(  ) {
        return osgParticle::FireEffect::getEmitter( );
    }

    virtual ::osgParticle::Emitter const * getEmitter(  ) const  {
        if( bp::override func_getEmitter = this->get_override( "getEmitter" ) )
            return func_getEmitter(  );
        else{
            return this->osgParticle::FireEffect::getEmitter(  );
        }
    }
    
    ::osgParticle::Emitter const * default_getEmitter(  ) const  {
        return osgParticle::FireEffect::getEmitter( );
    }

    virtual ::osgParticle::Program * getProgram(  ) {
        if( bp::override func_getProgram = this->get_override( "getProgram" ) )
            return func_getProgram(  );
        else{
            return this->osgParticle::FireEffect::getProgram(  );
        }
    }
    
    ::osgParticle::Program * default_getProgram(  ) {
        return osgParticle::FireEffect::getProgram( );
    }

    virtual ::osgParticle::Program const * getProgram(  ) const  {
        if( bp::override func_getProgram = this->get_override( "getProgram" ) )
            return func_getProgram(  );
        else{
            return this->osgParticle::FireEffect::getProgram(  );
        }
    }
    
    ::osgParticle::Program const * default_getProgram(  ) const  {
        return osgParticle::FireEffect::getProgram( );
    }

    virtual bool isSameKindAs( ::osg::Object const * obj ) const  {
        if( bp::override func_isSameKindAs = this->get_override( "isSameKindAs" ) )
            return func_isSameKindAs( boost::python::ptr(obj) );
        else{
            return this->osgParticle::FireEffect::isSameKindAs( boost::python::ptr(obj) );
        }
    }
    
    bool default_isSameKindAs( ::osg::Object const * obj ) const  {
        return osgParticle::FireEffect::isSameKindAs( boost::python::ptr(obj) );
    }

    virtual char const * libraryName(  ) const  {
        if( bp::override func_libraryName = this->get_override( "libraryName" ) )
            return func_libraryName(  );
        else{
            return this->osgParticle::FireEffect::libraryName(  );
        }
    }
    
    char const * default_libraryName(  ) const  {
        return osgParticle::FireEffect::libraryName( );
    }

    virtual void setDefaults(  ) {
        if( bp::override func_setDefaults = this->get_override( "setDefaults" ) )
            func_setDefaults(  );
        else{
            this->osgParticle::FireEffect::setDefaults(  );
        }
    }
    
    void default_setDefaults(  ) {
        osgParticle::FireEffect::setDefaults( );
    }

    virtual void setUpEmitterAndProgram(  ) {
        if( bp::override func_setUpEmitterAndProgram = this->get_override( "setUpEmitterAndProgram" ) )
            func_setUpEmitterAndProgram(  );
        else{
            this->osgParticle::FireEffect::setUpEmitterAndProgram(  );
        }
    }
    
    void default_setUpEmitterAndProgram(  ) {
        osgParticle::FireEffect::setUpEmitterAndProgram( );
    }

    virtual bool addChild( ::osg::Node * child ) {
        if( bp::override func_addChild = this->get_override( "addChild" ) )
            return func_addChild( boost::python::ptr(child) );
        else{
            return this->osg::Group::addChild( boost::python::ptr(child) );
        }
    }
    
    bool default_addChild( ::osg::Node * child ) {
        return osg::Group::addChild( boost::python::ptr(child) );
    }

    virtual ::osg::Camera * asCamera(  ) {
        if( bp::override func_asCamera = this->get_override( "asCamera" ) )
            return func_asCamera(  );
        else{
            return this->osg::Node::asCamera(  );
        }
    }
    
    ::osg::Camera * default_asCamera(  ) {
        return osg::Node::asCamera( );
    }

    virtual ::osg::Camera const * asCamera(  ) const  {
        if( bp::override func_asCamera = this->get_override( "asCamera" ) )
            return func_asCamera(  );
        else{
            return this->osg::Node::asCamera(  );
        }
    }
    
    ::osg::Camera const * default_asCamera(  ) const  {
        return osg::Node::asCamera( );
    }

    virtual ::osg::Geode * asGeode(  ) {
        if( bp::override func_asGeode = this->get_override( "asGeode" ) )
            return func_asGeode(  );
        else{
            return this->osg::Node::asGeode(  );
        }
    }
    
    ::osg::Geode * default_asGeode(  ) {
        return osg::Node::asGeode( );
    }

    virtual ::osg::Geode const * asGeode(  ) const  {
        if( bp::override func_asGeode = this->get_override( "asGeode" ) )
            return func_asGeode(  );
        else{
            return this->osg::Node::asGeode(  );
        }
    }
    
    ::osg::Geode const * default_asGeode(  ) const  {
        return osg::Node::asGeode( );
    }

    virtual ::osg::Group * asGroup(  ) {
        if( bp::override func_asGroup = this->get_override( "asGroup" ) )
            return func_asGroup(  );
        else{
            return this->osg::Group::asGroup(  );
        }
    }
    
    ::osg::Group * default_asGroup(  ) {
        return osg::Group::asGroup( );
    }

    virtual ::osg::Group const * asGroup(  ) const  {
        if( bp::override func_asGroup = this->get_override( "asGroup" ) )
            return func_asGroup(  );
        else{
            return this->osg::Group::asGroup(  );
        }
    }
    
    ::osg::Group const * default_asGroup(  ) const  {
        return osg::Group::asGroup( );
    }

    virtual ::osg::Switch * asSwitch(  ) {
        if( bp::override func_asSwitch = this->get_override( "asSwitch" ) )
            return func_asSwitch(  );
        else{
            return this->osg::Node::asSwitch(  );
        }
    }
    
    ::osg::Switch * default_asSwitch(  ) {
        return osg::Node::asSwitch( );
    }

    virtual ::osg::Switch const * asSwitch(  ) const  {
        if( bp::override func_asSwitch = this->get_override( "asSwitch" ) )
            return func_asSwitch(  );
        else{
            return this->osg::Node::asSwitch(  );
        }
    }
    
    ::osg::Switch const * default_asSwitch(  ) const  {
        return osg::Node::asSwitch( );
    }

    virtual ::osg::Transform * asTransform(  ) {
        if( bp::override func_asTransform = this->get_override( "asTransform" ) )
            return func_asTransform(  );
        else{
            return this->osg::Node::asTransform(  );
        }
    }
    
    ::osg::Transform * default_asTransform(  ) {
        return osg::Node::asTransform( );
    }

    virtual ::osg::Transform const * asTransform(  ) const  {
        if( bp::override func_asTransform = this->get_override( "asTransform" ) )
            return func_asTransform(  );
        else{
            return this->osg::Node::asTransform(  );
        }
    }
    
    ::osg::Transform const * default_asTransform(  ) const  {
        return osg::Node::asTransform( );
    }

    virtual void ascend( ::osg::NodeVisitor & nv ) {
        if( bp::override func_ascend = this->get_override( "ascend" ) )
            func_ascend( boost::ref(nv) );
        else{
            this->osg::Node::ascend( boost::ref(nv) );
        }
    }
    
    void default_ascend( ::osg::NodeVisitor & nv ) {
        osg::Node::ascend( boost::ref(nv) );
    }

    virtual void buildEffect(  ) {
        if( bp::override func_buildEffect = this->get_override( "buildEffect" ) )
            func_buildEffect(  );
        else{
            this->osgParticle::ParticleEffect::buildEffect(  );
        }
    }
    
    void default_buildEffect(  ) {
        osgParticle::ParticleEffect::buildEffect( );
    }

    virtual ::osg::BoundingSphere computeBound(  ) const  {
        if( bp::override func_computeBound = this->get_override( "computeBound" ) )
            return func_computeBound(  );
        else{
            return this->osg::Group::computeBound(  );
        }
    }
    
    ::osg::BoundingSphere default_computeBound(  ) const  {
        return osg::Group::computeBound( );
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

    virtual bool insertChild( unsigned int index, ::osg::Node * child ) {
        if( bp::override func_insertChild = this->get_override( "insertChild" ) )
            return func_insertChild( index, boost::python::ptr(child) );
        else{
            return this->osg::Group::insertChild( index, boost::python::ptr(child) );
        }
    }
    
    bool default_insertChild( unsigned int index, ::osg::Node * child ) {
        return osg::Group::insertChild( index, boost::python::ptr(child) );
    }

    virtual bool removeChildren( unsigned int pos, unsigned int numChildrenToRemove ) {
        if( bp::override func_removeChildren = this->get_override( "removeChildren" ) )
            return func_removeChildren( pos, numChildrenToRemove );
        else{
            return this->osg::Group::removeChildren( pos, numChildrenToRemove );
        }
    }
    
    bool default_removeChildren( unsigned int pos, unsigned int numChildrenToRemove ) {
        return osg::Group::removeChildren( pos, numChildrenToRemove );
    }

    virtual bool replaceChild( ::osg::Node * origChild, ::osg::Node * newChild ) {
        if( bp::override func_replaceChild = this->get_override( "replaceChild" ) )
            return func_replaceChild( boost::python::ptr(origChild), boost::python::ptr(newChild) );
        else{
            return this->osg::Group::replaceChild( boost::python::ptr(origChild), boost::python::ptr(newChild) );
        }
    }
    
    bool default_replaceChild( ::osg::Node * origChild, ::osg::Node * newChild ) {
        return osg::Group::replaceChild( boost::python::ptr(origChild), boost::python::ptr(newChild) );
    }

    virtual void resizeGLObjectBuffers( unsigned int maxSize ) {
        if( bp::override func_resizeGLObjectBuffers = this->get_override( "resizeGLObjectBuffers" ) )
            func_resizeGLObjectBuffers( maxSize );
        else{
            this->osg::Group::resizeGLObjectBuffers( maxSize );
        }
    }
    
    void default_resizeGLObjectBuffers( unsigned int maxSize ) {
        osg::Group::resizeGLObjectBuffers( maxSize );
    }

    virtual bool setChild( unsigned int i, ::osg::Node * node ) {
        if( bp::override func_setChild = this->get_override( "setChild" ) )
            return func_setChild( i, boost::python::ptr(node) );
        else{
            return this->osg::Group::setChild( i, boost::python::ptr(node) );
        }
    }
    
    bool default_setChild( unsigned int i, ::osg::Node * node ) {
        return osg::Group::setChild( i, boost::python::ptr(node) );
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
            this->osg::Group::setThreadSafeRefUnref( threadSafe );
        }
    }
    
    void default_setThreadSafeRefUnref( bool threadSafe ) {
        osg::Group::setThreadSafeRefUnref( threadSafe );
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

    virtual void traverse( ::osg::NodeVisitor & nv ) {
        if( bp::override func_traverse = this->get_override( "traverse" ) )
            func_traverse( boost::ref(nv) );
        else{
            this->osg::Group::traverse( boost::ref(nv) );
        }
    }
    
    void default_traverse( ::osg::NodeVisitor & nv ) {
        osg::Group::traverse( boost::ref(nv) );
    }

};

void register_FireEffect_class(){

    { //::osgParticle::FireEffect
        typedef bp::class_< FireEffect_wrapper, bp::bases< osgParticle::ParticleEffect >, osg::ref_ptr< FireEffect_wrapper >, boost::noncopyable > FireEffect_exposer_t;
        FireEffect_exposer_t FireEffect_exposer = FireEffect_exposer_t( "FireEffect", bp::no_init );
        bp::scope FireEffect_scope( FireEffect_exposer );
        FireEffect_exposer.def( bp::init< bp::optional< bool > >(( bp::arg("automaticSetup")=(bool)(true) )) );
        bp::implicitly_convertible< bool, osgParticle::FireEffect >();
        FireEffect_exposer.def( bp::init< osg::Vec3 const &, bp::optional< float, float > >(( bp::arg("position"), bp::arg("scale")=1.0e+0f, bp::arg("intensity")=1.0e+0f )) );
        bp::implicitly_convertible< osg::Vec3 const &, osgParticle::FireEffect >();
        { //::osgParticle::FireEffect::accept
        
            typedef void ( ::osgParticle::FireEffect::*accept_function_type)( ::osg::NodeVisitor & ) ;
            typedef void ( FireEffect_wrapper::*default_accept_function_type)( ::osg::NodeVisitor & ) ;
            
            FireEffect_exposer.def( 
                "accept"
                , accept_function_type(&::osgParticle::FireEffect::accept)
                , default_accept_function_type(&FireEffect_wrapper::default_accept)
                , ( bp::arg("nv") ) );
        
        }
        { //::osgParticle::FireEffect::className
        
            typedef char const * ( ::osgParticle::FireEffect::*className_function_type)(  ) const;
            typedef char const * ( FireEffect_wrapper::*default_className_function_type)(  ) const;
            
            FireEffect_exposer.def( 
                "className"
                , className_function_type(&::osgParticle::FireEffect::className)
                , default_className_function_type(&FireEffect_wrapper::default_className) );
        
        }
        { //::osgParticle::FireEffect::clone
        
            typedef ::osg::Object * ( ::osgParticle::FireEffect::*clone_function_type)( ::osg::CopyOp const & ) const;
            typedef ::osg::Object * ( FireEffect_wrapper::*default_clone_function_type)( ::osg::CopyOp const & ) const;
            
            FireEffect_exposer.def( 
                "clone"
                , clone_function_type(&::osgParticle::FireEffect::clone)
                , default_clone_function_type(&FireEffect_wrapper::default_clone)
                , ( bp::arg("copyop") )
                , bp::return_value_policy< bp::reference_existing_object >() );
        
        }
        { //::osgParticle::FireEffect::cloneType
        
            typedef ::osg::Object * ( ::osgParticle::FireEffect::*cloneType_function_type)(  ) const;
            typedef ::osg::Object * ( FireEffect_wrapper::*default_cloneType_function_type)(  ) const;
            
            FireEffect_exposer.def( 
                "cloneType"
                , cloneType_function_type(&::osgParticle::FireEffect::cloneType)
                , default_cloneType_function_type(&FireEffect_wrapper::default_cloneType)
                , bp::return_value_policy< bp::reference_existing_object >() );
        
        }
        { //::osgParticle::FireEffect::getEmitter
        
            typedef ::osgParticle::Emitter * ( ::osgParticle::FireEffect::*getEmitter_function_type)(  ) ;
            typedef ::osgParticle::Emitter * ( FireEffect_wrapper::*default_getEmitter_function_type)(  ) ;
            
            FireEffect_exposer.def( 
                "getEmitter"
                , getEmitter_function_type(&::osgParticle::FireEffect::getEmitter)
                , default_getEmitter_function_type(&FireEffect_wrapper::default_getEmitter)
                , bp::return_internal_reference< >() );
        
        }
        { //::osgParticle::FireEffect::getEmitter
        
            typedef ::osgParticle::Emitter const * ( ::osgParticle::FireEffect::*getEmitter_function_type)(  ) const;
            typedef ::osgParticle::Emitter const * ( FireEffect_wrapper::*default_getEmitter_function_type)(  ) const;
            
            FireEffect_exposer.def( 
                "getEmitter"
                , getEmitter_function_type(&::osgParticle::FireEffect::getEmitter)
                , default_getEmitter_function_type(&FireEffect_wrapper::default_getEmitter)
                , bp::return_internal_reference< >() );
        
        }
        { //::osgParticle::FireEffect::getProgram
        
            typedef ::osgParticle::Program * ( ::osgParticle::FireEffect::*getProgram_function_type)(  ) ;
            typedef ::osgParticle::Program * ( FireEffect_wrapper::*default_getProgram_function_type)(  ) ;
            
            FireEffect_exposer.def( 
                "getProgram"
                , getProgram_function_type(&::osgParticle::FireEffect::getProgram)
                , default_getProgram_function_type(&FireEffect_wrapper::default_getProgram)
                , bp::return_internal_reference< >() );
        
        }
        { //::osgParticle::FireEffect::getProgram
        
            typedef ::osgParticle::Program const * ( ::osgParticle::FireEffect::*getProgram_function_type)(  ) const;
            typedef ::osgParticle::Program const * ( FireEffect_wrapper::*default_getProgram_function_type)(  ) const;
            
            FireEffect_exposer.def( 
                "getProgram"
                , getProgram_function_type(&::osgParticle::FireEffect::getProgram)
                , default_getProgram_function_type(&FireEffect_wrapper::default_getProgram)
                , bp::return_internal_reference< >() );
        
        }
        { //::osgParticle::FireEffect::isSameKindAs
        
            typedef bool ( ::osgParticle::FireEffect::*isSameKindAs_function_type)( ::osg::Object const * ) const;
            typedef bool ( FireEffect_wrapper::*default_isSameKindAs_function_type)( ::osg::Object const * ) const;
            
            FireEffect_exposer.def( 
                "isSameKindAs"
                , isSameKindAs_function_type(&::osgParticle::FireEffect::isSameKindAs)
                , default_isSameKindAs_function_type(&FireEffect_wrapper::default_isSameKindAs)
                , ( bp::arg("obj") ) );
        
        }
        { //::osgParticle::FireEffect::libraryName
        
            typedef char const * ( ::osgParticle::FireEffect::*libraryName_function_type)(  ) const;
            typedef char const * ( FireEffect_wrapper::*default_libraryName_function_type)(  ) const;
            
            FireEffect_exposer.def( 
                "libraryName"
                , libraryName_function_type(&::osgParticle::FireEffect::libraryName)
                , default_libraryName_function_type(&FireEffect_wrapper::default_libraryName) );
        
        }
        { //::osgParticle::FireEffect::setDefaults
        
            typedef void ( ::osgParticle::FireEffect::*setDefaults_function_type)(  ) ;
            typedef void ( FireEffect_wrapper::*default_setDefaults_function_type)(  ) ;
            
            FireEffect_exposer.def( 
                "setDefaults"
                , setDefaults_function_type(&::osgParticle::FireEffect::setDefaults)
                , default_setDefaults_function_type(&FireEffect_wrapper::default_setDefaults) );
        
        }
        { //::osgParticle::FireEffect::setUpEmitterAndProgram
        
            typedef void ( ::osgParticle::FireEffect::*setUpEmitterAndProgram_function_type)(  ) ;
            typedef void ( FireEffect_wrapper::*default_setUpEmitterAndProgram_function_type)(  ) ;
            
            FireEffect_exposer.def( 
                "setUpEmitterAndProgram"
                , setUpEmitterAndProgram_function_type(&::osgParticle::FireEffect::setUpEmitterAndProgram)
                , default_setUpEmitterAndProgram_function_type(&FireEffect_wrapper::default_setUpEmitterAndProgram) );
        
        }
        { //::osgParticle::ParticleEffect::buildEffect
        
            typedef void ( ::osgParticle::ParticleEffect::*buildEffect_function_type)(  ) ;
            typedef void ( FireEffect_wrapper::*default_buildEffect_function_type)(  ) ;
            
            FireEffect_exposer.def( 
                "buildEffect"
                , buildEffect_function_type(&::osgParticle::ParticleEffect::buildEffect)
                , default_buildEffect_function_type(&FireEffect_wrapper::default_buildEffect) );
        
        }
    }

}
