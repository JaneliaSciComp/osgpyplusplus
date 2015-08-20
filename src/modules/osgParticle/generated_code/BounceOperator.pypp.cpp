// This file has been generated by Py++.

#include "boost/python.hpp"
#include "wrap_osgparticle.h"
#include "wrap_referenced.h"
#include "bounceoperator.pypp.hpp"

namespace bp = boost::python;

struct BounceOperator_wrapper : osgParticle::BounceOperator, bp::wrapper< osgParticle::BounceOperator > {

    BounceOperator_wrapper( )
    : osgParticle::BounceOperator( )
      , bp::wrapper< osgParticle::BounceOperator >(){
        // null constructor
    
    }

    virtual char const * className(  ) const  {
        if( bp::override func_className = this->get_override( "className" ) )
            return func_className(  );
        else{
            return this->osgParticle::BounceOperator::className(  );
        }
    }
    
    char const * default_className(  ) const  {
        return osgParticle::BounceOperator::className( );
    }

    virtual ::osg::Object * clone( ::osg::CopyOp const & copyop ) const  {
        if( bp::override func_clone = this->get_override( "clone" ) )
            return func_clone( boost::ref(copyop) );
        else{
            return this->osgParticle::BounceOperator::clone( boost::ref(copyop) );
        }
    }
    
    ::osg::Object * default_clone( ::osg::CopyOp const & copyop ) const  {
        return osgParticle::BounceOperator::clone( boost::ref(copyop) );
    }

    virtual ::osg::Object * cloneType(  ) const  {
        if( bp::override func_cloneType = this->get_override( "cloneType" ) )
            return func_cloneType(  );
        else{
            return this->osgParticle::BounceOperator::cloneType(  );
        }
    }
    
    ::osg::Object * default_cloneType(  ) const  {
        return osgParticle::BounceOperator::cloneType( );
    }

    virtual bool isSameKindAs( ::osg::Object const * obj ) const  {
        if( bp::override func_isSameKindAs = this->get_override( "isSameKindAs" ) )
            return func_isSameKindAs( boost::python::ptr(obj) );
        else{
            return this->osgParticle::BounceOperator::isSameKindAs( boost::python::ptr(obj) );
        }
    }
    
    bool default_isSameKindAs( ::osg::Object const * obj ) const  {
        return osgParticle::BounceOperator::isSameKindAs( boost::python::ptr(obj) );
    }

    virtual char const * libraryName(  ) const  {
        if( bp::override func_libraryName = this->get_override( "libraryName" ) )
            return func_libraryName(  );
        else{
            return this->osgParticle::BounceOperator::libraryName(  );
        }
    }
    
    char const * default_libraryName(  ) const  {
        return osgParticle::BounceOperator::libraryName( );
    }

    virtual void beginOperate( ::osgParticle::Program * prg ) {
        if( bp::override func_beginOperate = this->get_override( "beginOperate" ) )
            func_beginOperate( boost::python::ptr(prg) );
        else{
            this->osgParticle::DomainOperator::beginOperate( boost::python::ptr(prg) );
        }
    }
    
    void default_beginOperate( ::osgParticle::Program * prg ) {
        osgParticle::DomainOperator::beginOperate( boost::python::ptr(prg) );
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

    virtual void endOperate(  ) {
        if( bp::override func_endOperate = this->get_override( "endOperate" ) )
            func_endOperate(  );
        else{
            this->osgParticle::DomainOperator::endOperate(  );
        }
    }
    
    void default_endOperate(  ) {
        osgParticle::DomainOperator::endOperate( );
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

    virtual void operate( ::osgParticle::Particle * P, double dt ) {
        if( bp::override func_operate = this->get_override( "operate" ) )
            func_operate( boost::python::ptr(P), dt );
        else{
            this->osgParticle::DomainOperator::operate( boost::python::ptr(P), dt );
        }
    }
    
    void default_operate( ::osgParticle::Particle * P, double dt ) {
        osgParticle::DomainOperator::operate( boost::python::ptr(P), dt );
    }

    virtual void operateParticles( ::osgParticle::ParticleSystem * ps, double dt ) {
        if( bp::override func_operateParticles = this->get_override( "operateParticles" ) )
            func_operateParticles( boost::python::ptr(ps), dt );
        else{
            this->osgParticle::Operator::operateParticles( boost::python::ptr(ps), dt );
        }
    }
    
    void default_operateParticles( ::osgParticle::ParticleSystem * ps, double dt ) {
        osgParticle::Operator::operateParticles( boost::python::ptr(ps), dt );
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

void register_BounceOperator_class(){

    bp::class_< BounceOperator_wrapper, bp::bases< osgParticle::DomainOperator >, osg::ref_ptr< BounceOperator_wrapper >, boost::noncopyable >( "BounceOperator", "\n A bounce operator can affect the particles velocity to make it rebound.\n    Refer to David McAllisters Particle System API (http://www.particlesystems.org)\n", bp::no_init )    
        .def( bp::init< >("\n A bounce operator can affect the particles velocity to make it rebound.\n    Refer to David McAllisters Particle System API (http://www.particlesystems.org)\n") )    
        .def( 
            "className"
            , (char const * ( ::osgParticle::BounceOperator::* )(  )const)(&::osgParticle::BounceOperator::className)
            , (char const * ( BounceOperator_wrapper::* )(  )const)(&BounceOperator_wrapper::default_className) )    
        .def( 
            "clone"
            , (::osg::Object * ( ::osgParticle::BounceOperator::* )( ::osg::CopyOp const & )const)(&::osgParticle::BounceOperator::clone)
            , (::osg::Object * ( BounceOperator_wrapper::* )( ::osg::CopyOp const & )const)(&BounceOperator_wrapper::default_clone)
            , ( bp::arg("copyop") )
            , bp::return_value_policy< bp::reference_existing_object >() )    
        .def( 
            "cloneType"
            , (::osg::Object * ( ::osgParticle::BounceOperator::* )(  )const)(&::osgParticle::BounceOperator::cloneType)
            , (::osg::Object * ( BounceOperator_wrapper::* )(  )const)(&BounceOperator_wrapper::default_cloneType)
            , bp::return_value_policy< bp::reference_existing_object >() )    
        .def( 
            "getCutoff"
            , (float ( ::osgParticle::BounceOperator::* )(  )const)( &::osgParticle::BounceOperator::getCutoff )
            , " Get the velocity cutoff factor" )    
        .def( 
            "getFriction"
            , (float ( ::osgParticle::BounceOperator::* )(  )const)( &::osgParticle::BounceOperator::getFriction )
            , " Get the friction" )    
        .def( 
            "getResilience"
            , (float ( ::osgParticle::BounceOperator::* )(  )const)( &::osgParticle::BounceOperator::getResilience )
            , " Get the velocity cutoff factor" )    
        .def( 
            "isSameKindAs"
            , (bool ( ::osgParticle::BounceOperator::* )( ::osg::Object const * )const)(&::osgParticle::BounceOperator::isSameKindAs)
            , (bool ( BounceOperator_wrapper::* )( ::osg::Object const * )const)(&BounceOperator_wrapper::default_isSameKindAs)
            , ( bp::arg("obj") ) )    
        .def( 
            "libraryName"
            , (char const * ( ::osgParticle::BounceOperator::* )(  )const)(&::osgParticle::BounceOperator::libraryName)
            , (char const * ( BounceOperator_wrapper::* )(  )const)(&BounceOperator_wrapper::default_libraryName) )    
        .def( 
            "setCutoff"
            , (void ( ::osgParticle::BounceOperator::* )( float ))( &::osgParticle::BounceOperator::setCutoff )
            , ( bp::arg("v") )
            , " Set the velocity cutoff factor" )    
        .def( 
            "setFriction"
            , (void ( ::osgParticle::BounceOperator::* )( float ))( &::osgParticle::BounceOperator::setFriction )
            , ( bp::arg("f") )
            , " Set the friction" )    
        .def( 
            "setResilience"
            , (void ( ::osgParticle::BounceOperator::* )( float ))( &::osgParticle::BounceOperator::setResilience )
            , ( bp::arg("r") )
            , " Set the resilience" )    
        .def( 
            "beginOperate"
            , (void ( ::osgParticle::DomainOperator::* )( ::osgParticle::Program * ))(&::osgParticle::DomainOperator::beginOperate)
            , (void ( BounceOperator_wrapper::* )( ::osgParticle::Program * ))(&BounceOperator_wrapper::default_beginOperate)
            , ( bp::arg("prg") ) )    
        .def( 
            "endOperate"
            , (void ( ::osgParticle::DomainOperator::* )(  ))(&::osgParticle::DomainOperator::endOperate)
            , (void ( BounceOperator_wrapper::* )(  ))(&BounceOperator_wrapper::default_endOperate) )    
        .def( 
            "operate"
            , (void ( ::osgParticle::DomainOperator::* )( ::osgParticle::Particle *,double ))(&::osgParticle::DomainOperator::operate)
            , (void ( BounceOperator_wrapper::* )( ::osgParticle::Particle *,double ))(&BounceOperator_wrapper::default_operate)
            , ( bp::arg("P"), bp::arg("dt") ) )    
        .def( 
            "operateParticles"
            , (void ( ::osgParticle::Operator::* )( ::osgParticle::ParticleSystem *,double ))(&::osgParticle::Operator::operateParticles)
            , (void ( BounceOperator_wrapper::* )( ::osgParticle::ParticleSystem *,double ))(&BounceOperator_wrapper::default_operateParticles)
            , ( bp::arg("ps"), bp::arg("dt") ) );

}
