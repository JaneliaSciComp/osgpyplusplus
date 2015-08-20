// This file has been generated by Py++.

#include "boost/python.hpp"
#include "wrap_osgparticle.h"
#include "wrap_referenced.h"
#include "pointplacer.pypp.hpp"

namespace bp = boost::python;

struct PointPlacer_wrapper : osgParticle::PointPlacer, bp::wrapper< osgParticle::PointPlacer > {

    PointPlacer_wrapper( )
    : osgParticle::PointPlacer( )
      , bp::wrapper< osgParticle::PointPlacer >(){
        // null constructor
    
    }

    virtual char const * className(  ) const  {
        if( bp::override func_className = this->get_override( "className" ) )
            return func_className(  );
        else{
            return this->osgParticle::PointPlacer::className(  );
        }
    }
    
    char const * default_className(  ) const  {
        return osgParticle::PointPlacer::className( );
    }

    virtual ::osg::Object * clone( ::osg::CopyOp const & copyop ) const  {
        if( bp::override func_clone = this->get_override( "clone" ) )
            return func_clone( boost::ref(copyop) );
        else{
            return this->osgParticle::PointPlacer::clone( boost::ref(copyop) );
        }
    }
    
    ::osg::Object * default_clone( ::osg::CopyOp const & copyop ) const  {
        return osgParticle::PointPlacer::clone( boost::ref(copyop) );
    }

    virtual ::osg::Object * cloneType(  ) const  {
        if( bp::override func_cloneType = this->get_override( "cloneType" ) )
            return func_cloneType(  );
        else{
            return this->osgParticle::PointPlacer::cloneType(  );
        }
    }
    
    ::osg::Object * default_cloneType(  ) const  {
        return osgParticle::PointPlacer::cloneType( );
    }

    virtual ::osg::Vec3 getControlPosition(  ) const  {
        if( bp::override func_getControlPosition = this->get_override( "getControlPosition" ) )
            return func_getControlPosition(  );
        else{
            return this->osgParticle::PointPlacer::getControlPosition(  );
        }
    }
    
    ::osg::Vec3 default_getControlPosition(  ) const  {
        return osgParticle::PointPlacer::getControlPosition( );
    }

    virtual bool isSameKindAs( ::osg::Object const * obj ) const  {
        if( bp::override func_isSameKindAs = this->get_override( "isSameKindAs" ) )
            return func_isSameKindAs( boost::python::ptr(obj) );
        else{
            return this->osgParticle::PointPlacer::isSameKindAs( boost::python::ptr(obj) );
        }
    }
    
    bool default_isSameKindAs( ::osg::Object const * obj ) const  {
        return osgParticle::PointPlacer::isSameKindAs( boost::python::ptr(obj) );
    }

    virtual char const * libraryName(  ) const  {
        if( bp::override func_libraryName = this->get_override( "libraryName" ) )
            return func_libraryName(  );
        else{
            return this->osgParticle::PointPlacer::libraryName(  );
        }
    }
    
    char const * default_libraryName(  ) const  {
        return osgParticle::PointPlacer::libraryName( );
    }

    virtual void place( ::osgParticle::Particle * P ) const  {
        if( bp::override func_place = this->get_override( "place" ) )
            func_place( boost::python::ptr(P) );
        else{
            this->osgParticle::PointPlacer::place( boost::python::ptr(P) );
        }
    }
    
    void default_place( ::osgParticle::Particle * P ) const  {
        osgParticle::PointPlacer::place( boost::python::ptr(P) );
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

    virtual float volume(  ) const  {
        if( bp::override func_volume = this->get_override( "volume" ) )
            return func_volume(  );
        else{
            return this->osgParticle::Placer::volume(  );
        }
    }
    
    float default_volume(  ) const  {
        return osgParticle::Placer::volume( );
    }

};

void register_PointPlacer_class(){

    bp::class_< PointPlacer_wrapper, bp::bases< osgParticle::CenteredPlacer >, osg::ref_ptr< PointPlacer_wrapper >, boost::noncopyable >( "PointPlacer", "\n    A point-shaped particle placer.\n        This placer class uses the center point defined in its base class <CODE>CenteredPlacer</CODE>\n        to place there all incoming particles.\n", bp::no_init )    
        .def( bp::init< >() )    
        .def( 
            "className"
            , (char const * ( ::osgParticle::PointPlacer::* )(  )const)(&::osgParticle::PointPlacer::className)
            , (char const * ( PointPlacer_wrapper::* )(  )const)(&PointPlacer_wrapper::default_className) )    
        .def( 
            "clone"
            , (::osg::Object * ( ::osgParticle::PointPlacer::* )( ::osg::CopyOp const & )const)(&::osgParticle::PointPlacer::clone)
            , (::osg::Object * ( PointPlacer_wrapper::* )( ::osg::CopyOp const & )const)(&PointPlacer_wrapper::default_clone)
            , ( bp::arg("copyop") )
            , bp::return_value_policy< bp::reference_existing_object >() )    
        .def( 
            "cloneType"
            , (::osg::Object * ( ::osgParticle::PointPlacer::* )(  )const)(&::osgParticle::PointPlacer::cloneType)
            , (::osg::Object * ( PointPlacer_wrapper::* )(  )const)(&PointPlacer_wrapper::default_cloneType)
            , bp::return_value_policy< bp::reference_existing_object >() )    
        .def( 
            "getControlPosition"
            , (::osg::Vec3 ( ::osgParticle::PointPlacer::* )(  )const)(&::osgParticle::PointPlacer::getControlPosition)
            , (::osg::Vec3 ( PointPlacer_wrapper::* )(  )const)(&PointPlacer_wrapper::default_getControlPosition) )    
        .def( 
            "isSameKindAs"
            , (bool ( ::osgParticle::PointPlacer::* )( ::osg::Object const * )const)(&::osgParticle::PointPlacer::isSameKindAs)
            , (bool ( PointPlacer_wrapper::* )( ::osg::Object const * )const)(&PointPlacer_wrapper::default_isSameKindAs)
            , ( bp::arg("obj") ) )    
        .def( 
            "libraryName"
            , (char const * ( ::osgParticle::PointPlacer::* )(  )const)(&::osgParticle::PointPlacer::libraryName)
            , (char const * ( PointPlacer_wrapper::* )(  )const)(&PointPlacer_wrapper::default_libraryName) )    
        .def( 
            "place"
            , (void ( ::osgParticle::PointPlacer::* )( ::osgParticle::Particle * )const)(&::osgParticle::PointPlacer::place)
            , (void ( PointPlacer_wrapper::* )( ::osgParticle::Particle * )const)(&PointPlacer_wrapper::default_place)
            , ( bp::arg("P") ) )    
        .def( 
            "volume"
            , (float ( ::osgParticle::Placer::* )(  )const)(&::osgParticle::Placer::volume)
            , (float ( PointPlacer_wrapper::* )(  )const)(&PointPlacer_wrapper::default_volume) );

}
