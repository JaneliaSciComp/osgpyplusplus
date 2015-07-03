// This file has been generated by Py++.

#include "boost/python.hpp"
#include "wrap_osg.h"
#include "wrap_referenced.h"
#include "cullingset.pypp.hpp"

namespace bp = boost::python;

struct CullingSet_wrapper : osg::CullingSet, bp::wrapper< osg::CullingSet > {

    CullingSet_wrapper( )
    : osg::CullingSet( )
      , bp::wrapper< osg::CullingSet >(){
        // null constructor
    
    }

    CullingSet_wrapper(::osg::CullingSet const & cs )
    : osg::CullingSet( boost::ref(cs) )
      , bp::wrapper< osg::CullingSet >(){
        // copy constructor
    
    }

    CullingSet_wrapper(::osg::CullingSet const & cs, ::osg::Matrix const & matrix, ::osg::Vec4 const & pixelSizeVector )
    : osg::CullingSet( boost::ref(cs), boost::ref(matrix), boost::ref(pixelSizeVector) )
      , bp::wrapper< osg::CullingSet >(){
        // constructor
    
    }

    virtual void setThreadSafeRefUnref( bool threadSafe ) {
        if( bp::override func_setThreadSafeRefUnref = this->get_override( "setThreadSafeRefUnref" ) )
            func_setThreadSafeRefUnref( threadSafe );
        else{
            this->osg::Referenced::setThreadSafeRefUnref( threadSafe );
        }
    }
    
    void default_setThreadSafeRefUnref( bool threadSafe ) {
        osg::Referenced::setThreadSafeRefUnref( threadSafe );
    }

};

void register_CullingSet_class(){

    { //::osg::CullingSet
        typedef bp::class_< CullingSet_wrapper, bp::bases< osg::Referenced >, osg::ref_ptr< ::osg::CullingSet > > CullingSet_exposer_t;
        CullingSet_exposer_t CullingSet_exposer = CullingSet_exposer_t( "CullingSet", "\n A CullingSet class which contains a frustum and a list of occluders.\n", bp::init< >() );
        bp::scope CullingSet_scope( CullingSet_exposer );
        bp::enum_< osg::CullingSet::MaskValues>("MaskValues")
            .value("NO_CULLING", osg::CullingSet::NO_CULLING)
            .value("VIEW_FRUSTUM_SIDES_CULLING", osg::CullingSet::VIEW_FRUSTUM_SIDES_CULLING)
            .value("NEAR_PLANE_CULLING", osg::CullingSet::NEAR_PLANE_CULLING)
            .value("FAR_PLANE_CULLING", osg::CullingSet::FAR_PLANE_CULLING)
            .value("VIEW_FRUSTUM_CULLING", osg::CullingSet::VIEW_FRUSTUM_CULLING)
            .value("SMALL_FEATURE_CULLING", osg::CullingSet::SMALL_FEATURE_CULLING)
            .value("SHADOW_OCCLUSION_CULLING", osg::CullingSet::SHADOW_OCCLUSION_CULLING)
            .value("DEFAULT_CULLING", osg::CullingSet::DEFAULT_CULLING)
            .value("ENABLE_ALL_CULLING", osg::CullingSet::ENABLE_ALL_CULLING)
            .export_values()
            ;
        CullingSet_exposer.def( bp::init< osg::CullingSet const & >(( bp::arg("cs") )) );
        CullingSet_exposer.def( bp::init< osg::CullingSet const &, osg::Matrix const &, osg::Vec4 const & >(( bp::arg("cs"), bp::arg("matrix"), bp::arg("pixelSizeVector") )) );
        { //::osg::CullingSet::addOccluder
        
            typedef void ( ::osg::CullingSet::*addOccluder_function_type )( ::osg::ShadowVolumeOccluder & ) ;
            
            CullingSet_exposer.def( 
                "addOccluder"
                , addOccluder_function_type( &::osg::CullingSet::addOccluder )
                , ( bp::arg("cv") ) );
        
        }
        { //::osg::CullingSet::addStateFrustum
        
            typedef void ( ::osg::CullingSet::*addStateFrustum_function_type )( ::osg::StateSet *,::osg::Polytope & ) ;
            
            CullingSet_exposer.def( 
                "addStateFrustum"
                , addStateFrustum_function_type( &::osg::CullingSet::addStateFrustum )
                , ( bp::arg("stateset"), bp::arg("polytope") ) );
        
        }
        { //::osg::CullingSet::clampedPixelSize
        
            typedef float ( ::osg::CullingSet::*clampedPixelSize_function_type )( ::osg::Vec3 const &,float ) const;
            
            CullingSet_exposer.def( 
                "clampedPixelSize"
                , clampedPixelSize_function_type( &::osg::CullingSet::clampedPixelSize )
                , ( bp::arg("v"), bp::arg("radius") )
                , " Compute the pixel of an object at position v, with specified radius. fabs()ed to always be positive." );
        
        }
        { //::osg::CullingSet::clampedPixelSize
        
            typedef float ( ::osg::CullingSet::*clampedPixelSize_function_type )( ::osg::BoundingSphere const & ) const;
            
            CullingSet_exposer.def( 
                "clampedPixelSize"
                , clampedPixelSize_function_type( &::osg::CullingSet::clampedPixelSize )
                , ( bp::arg("bs") )
                , " Compute the pixel of a bounding sphere. fabs()ed to always be positive." );
        
        }
        { //::osg::CullingSet::disableAndPushOccludersCurrentMask
        
            typedef void ( ::osg::CullingSet::*disableAndPushOccludersCurrentMask_function_type )( ::osg::NodePath & ) ;
            
            CullingSet_exposer.def( 
                "disableAndPushOccludersCurrentMask"
                , disableAndPushOccludersCurrentMask_function_type( &::osg::CullingSet::disableAndPushOccludersCurrentMask )
                , ( bp::arg("nodePath") ) );
        
        }
        { //::osg::CullingSet::getCullingMask
        
            typedef int ( ::osg::CullingSet::*getCullingMask_function_type )(  ) const;
            
            CullingSet_exposer.def( 
                "getCullingMask"
                , getCullingMask_function_type( &::osg::CullingSet::getCullingMask ) );
        
        }
        { //::osg::CullingSet::getFrustum
        
            typedef ::osg::Polytope & ( ::osg::CullingSet::*getFrustum_function_type )(  ) ;
            
            CullingSet_exposer.def( 
                "getFrustum"
                , getFrustum_function_type( &::osg::CullingSet::getFrustum )
                , bp::return_internal_reference< >() );
        
        }
        { //::osg::CullingSet::getFrustum
        
            typedef ::osg::Polytope const & ( ::osg::CullingSet::*getFrustum_function_type )(  ) const;
            
            CullingSet_exposer.def( 
                "getFrustum"
                , getFrustum_function_type( &::osg::CullingSet::getFrustum )
                , bp::return_internal_reference< >() );
        
        }
        { //::osg::CullingSet::getPixelSizeVector
        
            typedef ::osg::Vec4 & ( ::osg::CullingSet::*getPixelSizeVector_function_type )(  ) ;
            
            CullingSet_exposer.def( 
                "getPixelSizeVector"
                , getPixelSizeVector_function_type( &::osg::CullingSet::getPixelSizeVector )
                , bp::return_internal_reference< >() );
        
        }
        { //::osg::CullingSet::getPixelSizeVector
        
            typedef ::osg::Vec4 const & ( ::osg::CullingSet::*getPixelSizeVector_function_type )(  ) const;
            
            CullingSet_exposer.def( 
                "getPixelSizeVector"
                , getPixelSizeVector_function_type( &::osg::CullingSet::getPixelSizeVector )
                , bp::return_internal_reference< >() );
        
        }
        { //::osg::CullingSet::getSmallFeatureCullingPixelSize
        
            typedef float & ( ::osg::CullingSet::*getSmallFeatureCullingPixelSize_function_type )(  ) ;
            
            CullingSet_exposer.def( 
                "getSmallFeatureCullingPixelSize"
                , getSmallFeatureCullingPixelSize_function_type( &::osg::CullingSet::getSmallFeatureCullingPixelSize )
                , bp::return_value_policy< bp::copy_non_const_reference >() );
        
        }
        { //::osg::CullingSet::getSmallFeatureCullingPixelSize
        
            typedef float ( ::osg::CullingSet::*getSmallFeatureCullingPixelSize_function_type )(  ) const;
            
            CullingSet_exposer.def( 
                "getSmallFeatureCullingPixelSize"
                , getSmallFeatureCullingPixelSize_function_type( &::osg::CullingSet::getSmallFeatureCullingPixelSize ) );
        
        }
        { //::osg::CullingSet::getStateFrustumList
        
            typedef void ( ::osg::CullingSet::*getStateFrustumList_function_type )( ::std::vector< std::pair<osg::ref_ptr<osg::StateSet>, osg::Polytope> > & ) ;
            
            CullingSet_exposer.def( 
                "getStateFrustumList"
                , getStateFrustumList_function_type( &::osg::CullingSet::getStateFrustumList )
                , ( bp::arg("sfl") ) );
        
        }
        { //::osg::CullingSet::getStateFrustumList
        
            typedef ::std::vector< std::pair<osg::ref_ptr<osg::StateSet>, osg::Polytope> > & ( ::osg::CullingSet::*getStateFrustumList_function_type )(  ) ;
            
            CullingSet_exposer.def( 
                "getStateFrustumList"
                , getStateFrustumList_function_type( &::osg::CullingSet::getStateFrustumList )
                , bp::return_internal_reference< >() );
        
        }
        { //::osg::CullingSet::isCulled
        
            typedef bool ( ::osg::CullingSet::*isCulled_function_type )( ::std::vector< osg::Vec3f > const & ) ;
            
            CullingSet_exposer.def( 
                "isCulled"
                , isCulled_function_type( &::osg::CullingSet::isCulled )
                , ( bp::arg("vertices") ) );
        
        }
        { //::osg::CullingSet::isCulled
        
            typedef bool ( ::osg::CullingSet::*isCulled_function_type )( ::osg::BoundingBox const & ) ;
            
            CullingSet_exposer.def( 
                "isCulled"
                , isCulled_function_type( &::osg::CullingSet::isCulled )
                , ( bp::arg("bb") ) );
        
        }
        { //::osg::CullingSet::isCulled
        
            typedef bool ( ::osg::CullingSet::*isCulled_function_type )( ::osg::BoundingSphere const & ) ;
            
            CullingSet_exposer.def( 
                "isCulled"
                , isCulled_function_type( &::osg::CullingSet::isCulled )
                , ( bp::arg("bs") ) );
        
        }
        { //::osg::CullingSet::pixelSize
        
            typedef float ( ::osg::CullingSet::*pixelSize_function_type )( ::osg::Vec3 const &,float ) const;
            
            CullingSet_exposer.def( 
                "pixelSize"
                , pixelSize_function_type( &::osg::CullingSet::pixelSize )
                , ( bp::arg("v"), bp::arg("radius") )
                , " Compute the pixel of an object at position v, with specified radius." );
        
        }
        { //::osg::CullingSet::pixelSize
        
            typedef float ( ::osg::CullingSet::*pixelSize_function_type )( ::osg::BoundingSphere const & ) const;
            
            CullingSet_exposer.def( 
                "pixelSize"
                , pixelSize_function_type( &::osg::CullingSet::pixelSize )
                , ( bp::arg("bs") )
                , " Compute the pixel of a bounding sphere." );
        
        }
        { //::osg::CullingSet::popCurrentMask
        
            typedef void ( ::osg::CullingSet::*popCurrentMask_function_type )(  ) ;
            
            CullingSet_exposer.def( 
                "popCurrentMask"
                , popCurrentMask_function_type( &::osg::CullingSet::popCurrentMask ) );
        
        }
        { //::osg::CullingSet::popOccludersCurrentMask
        
            typedef void ( ::osg::CullingSet::*popOccludersCurrentMask_function_type )( ::osg::NodePath & ) ;
            
            CullingSet_exposer.def( 
                "popOccludersCurrentMask"
                , popOccludersCurrentMask_function_type( &::osg::CullingSet::popOccludersCurrentMask )
                , ( bp::arg("nodePath") ) );
        
        }
        { //::osg::CullingSet::pushCurrentMask
        
            typedef void ( ::osg::CullingSet::*pushCurrentMask_function_type )(  ) ;
            
            CullingSet_exposer.def( 
                "pushCurrentMask"
                , pushCurrentMask_function_type( &::osg::CullingSet::pushCurrentMask ) );
        
        }
        { //::osg::CullingSet::resetCullingMask
        
            typedef void ( ::osg::CullingSet::*resetCullingMask_function_type )(  ) ;
            
            CullingSet_exposer.def( 
                "resetCullingMask"
                , resetCullingMask_function_type( &::osg::CullingSet::resetCullingMask ) );
        
        }
        { //::osg::CullingSet::set
        
            typedef void ( ::osg::CullingSet::*set_function_type )( ::osg::CullingSet const & ) ;
            
            CullingSet_exposer.def( 
                "set"
                , set_function_type( &::osg::CullingSet::set )
                , ( bp::arg("cs") ) );
        
        }
        { //::osg::CullingSet::set
        
            typedef void ( ::osg::CullingSet::*set_function_type )( ::osg::CullingSet const &,::osg::Matrix const &,::osg::Vec4 const & ) ;
            
            CullingSet_exposer.def( 
                "set"
                , set_function_type( &::osg::CullingSet::set )
                , ( bp::arg("cs"), bp::arg("matrix"), bp::arg("pixelSizeVector") ) );
        
        }
        { //::osg::CullingSet::setCullingMask
        
            typedef void ( ::osg::CullingSet::*setCullingMask_function_type )( int ) ;
            
            CullingSet_exposer.def( 
                "setCullingMask"
                , setCullingMask_function_type( &::osg::CullingSet::setCullingMask )
                , ( bp::arg("mask") ) );
        
        }
        { //::osg::CullingSet::setFrustum
        
            typedef void ( ::osg::CullingSet::*setFrustum_function_type )( ::osg::Polytope & ) ;
            
            CullingSet_exposer.def( 
                "setFrustum"
                , setFrustum_function_type( &::osg::CullingSet::setFrustum )
                , ( bp::arg("cv") ) );
        
        }
        { //::osg::CullingSet::setPixelSizeVector
        
            typedef void ( ::osg::CullingSet::*setPixelSizeVector_function_type )( ::osg::Vec4 const & ) ;
            
            CullingSet_exposer.def( 
                "setPixelSizeVector"
                , setPixelSizeVector_function_type( &::osg::CullingSet::setPixelSizeVector )
                , ( bp::arg("v") ) );
        
        }
        { //::osg::CullingSet::setSmallFeatureCullingPixelSize
        
            typedef void ( ::osg::CullingSet::*setSmallFeatureCullingPixelSize_function_type )( float ) ;
            
            CullingSet_exposer.def( 
                "setSmallFeatureCullingPixelSize"
                , setSmallFeatureCullingPixelSize_function_type( &::osg::CullingSet::setSmallFeatureCullingPixelSize )
                , ( bp::arg("value") )
                , " Threshold at which small features are culled.\n        @param value: Boulding volume size in screen space. Default is 2.0." );
        
        }
        { //::osg::Referenced::setThreadSafeRefUnref
        
            typedef void ( ::osg::Referenced::*setThreadSafeRefUnref_function_type )( bool ) ;
            typedef void ( CullingSet_wrapper::*default_setThreadSafeRefUnref_function_type )( bool ) ;
            
            CullingSet_exposer.def( 
                "setThreadSafeRefUnref"
                , setThreadSafeRefUnref_function_type(&::osg::Referenced::setThreadSafeRefUnref)
                , default_setThreadSafeRefUnref_function_type(&CullingSet_wrapper::default_setThreadSafeRefUnref)
                , ( bp::arg("threadSafe") ) );
        
        }
    }

}
