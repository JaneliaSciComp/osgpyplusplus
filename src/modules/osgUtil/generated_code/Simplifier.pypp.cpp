// This file has been generated by Py++.

#include "boost/python.hpp"
#include "wrap_osgutil.h"
#include "wrap_referenced.h"
#include "simplifier.pypp.hpp"

namespace bp = boost::python;

struct Simplifier_wrapper : osgUtil::Simplifier, bp::wrapper< osgUtil::Simplifier > {

    struct ContinueSimplificationCallback_wrapper : osgUtil::Simplifier::ContinueSimplificationCallback, bp::wrapper< osgUtil::Simplifier::ContinueSimplificationCallback > {
    
        ContinueSimplificationCallback_wrapper()
        : osgUtil::Simplifier::ContinueSimplificationCallback()
          , bp::wrapper< osgUtil::Simplifier::ContinueSimplificationCallback >(){
            // null constructor
            
        }
    
        virtual bool continueSimplification( ::osgUtil::Simplifier const & simplifier, float nextError, unsigned int numOriginalPrimitives, unsigned int numRemainingPrimitives ) const  {
            if( bp::override func_continueSimplification = this->get_override( "continueSimplification" ) )
                return func_continueSimplification( boost::ref(simplifier), nextError, numOriginalPrimitives, numRemainingPrimitives );
            else{
                return this->osgUtil::Simplifier::ContinueSimplificationCallback::continueSimplification( boost::ref(simplifier), nextError, numOriginalPrimitives, numRemainingPrimitives );
            }
        }
        
        bool default_continueSimplification( ::osgUtil::Simplifier const & simplifier, float nextError, unsigned int numOriginalPrimitives, unsigned int numRemainingPrimitives ) const  {
            return osgUtil::Simplifier::ContinueSimplificationCallback::continueSimplification( boost::ref(simplifier), nextError, numOriginalPrimitives, numRemainingPrimitives );
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

    Simplifier_wrapper(double sampleRatio=1.0e+0, double maximumError=3.4028234663852885981170418348451692544e+38f, double maximumLength=0.0 )
    : osgUtil::Simplifier( sampleRatio, maximumError, maximumLength )
      , bp::wrapper< osgUtil::Simplifier >(){
        // constructor
    
    }

    virtual void apply( ::osg::Geode & geode ) {
        if( bp::override func_apply = this->get_override( "apply" ) )
            func_apply( boost::ref(geode) );
        else{
            this->osgUtil::Simplifier::apply( boost::ref(geode) );
        }
    }
    
    void default_apply( ::osg::Geode & geode ) {
        osgUtil::Simplifier::apply( boost::ref(geode) );
    }

    virtual char const * className(  ) const  {
        if( bp::override func_className = this->get_override( "className" ) )
            return func_className(  );
        else{
            return this->osgUtil::Simplifier::className(  );
        }
    }
    
    char const * default_className(  ) const  {
        return osgUtil::Simplifier::className( );
    }

    virtual bool continueSimplificationImplementation( float nextError, unsigned int numOriginalPrimitives, unsigned int numRemainingPrimitives ) const  {
        if( bp::override func_continueSimplificationImplementation = this->get_override( "continueSimplificationImplementation" ) )
            return func_continueSimplificationImplementation( nextError, numOriginalPrimitives, numRemainingPrimitives );
        else{
            return this->osgUtil::Simplifier::continueSimplificationImplementation( nextError, numOriginalPrimitives, numRemainingPrimitives );
        }
    }
    
    bool default_continueSimplificationImplementation( float nextError, unsigned int numOriginalPrimitives, unsigned int numRemainingPrimitives ) const  {
        return osgUtil::Simplifier::continueSimplificationImplementation( nextError, numOriginalPrimitives, numRemainingPrimitives );
    }

    virtual char const * libraryName(  ) const  {
        if( bp::override func_libraryName = this->get_override( "libraryName" ) )
            return func_libraryName(  );
        else{
            return this->osgUtil::Simplifier::libraryName(  );
        }
    }
    
    char const * default_libraryName(  ) const  {
        return osgUtil::Simplifier::libraryName( );
    }

    virtual void apply( ::osg::Node & node ) {
        if( bp::override func_apply = this->get_override( "apply" ) )
            func_apply( boost::ref(node) );
        else{
            this->osg::NodeVisitor::apply( boost::ref(node) );
        }
    }
    
    void default_apply( ::osg::Node & node ) {
        osg::NodeVisitor::apply( boost::ref(node) );
    }

    virtual void apply( ::osg::Billboard & node ) {
        if( bp::override func_apply = this->get_override( "apply" ) )
            func_apply( boost::ref(node) );
        else{
            this->osg::NodeVisitor::apply( boost::ref(node) );
        }
    }
    
    void default_apply( ::osg::Billboard & node ) {
        osg::NodeVisitor::apply( boost::ref(node) );
    }

    virtual void apply( ::osg::Group & node ) {
        if( bp::override func_apply = this->get_override( "apply" ) )
            func_apply( boost::ref(node) );
        else{
            this->osg::NodeVisitor::apply( boost::ref(node) );
        }
    }
    
    void default_apply( ::osg::Group & node ) {
        osg::NodeVisitor::apply( boost::ref(node) );
    }

    virtual void apply( ::osg::ProxyNode & node ) {
        if( bp::override func_apply = this->get_override( "apply" ) )
            func_apply( boost::ref(node) );
        else{
            this->osg::NodeVisitor::apply( boost::ref(node) );
        }
    }
    
    void default_apply( ::osg::ProxyNode & node ) {
        osg::NodeVisitor::apply( boost::ref(node) );
    }

    virtual void apply( ::osg::Projection & node ) {
        if( bp::override func_apply = this->get_override( "apply" ) )
            func_apply( boost::ref(node) );
        else{
            this->osg::NodeVisitor::apply( boost::ref(node) );
        }
    }
    
    void default_apply( ::osg::Projection & node ) {
        osg::NodeVisitor::apply( boost::ref(node) );
    }

    virtual void apply( ::osg::CoordinateSystemNode & node ) {
        if( bp::override func_apply = this->get_override( "apply" ) )
            func_apply( boost::ref(node) );
        else{
            this->osg::NodeVisitor::apply( boost::ref(node) );
        }
    }
    
    void default_apply( ::osg::CoordinateSystemNode & node ) {
        osg::NodeVisitor::apply( boost::ref(node) );
    }

    virtual void apply( ::osg::ClipNode & node ) {
        if( bp::override func_apply = this->get_override( "apply" ) )
            func_apply( boost::ref(node) );
        else{
            this->osg::NodeVisitor::apply( boost::ref(node) );
        }
    }
    
    void default_apply( ::osg::ClipNode & node ) {
        osg::NodeVisitor::apply( boost::ref(node) );
    }

    virtual void apply( ::osg::TexGenNode & node ) {
        if( bp::override func_apply = this->get_override( "apply" ) )
            func_apply( boost::ref(node) );
        else{
            this->osg::NodeVisitor::apply( boost::ref(node) );
        }
    }
    
    void default_apply( ::osg::TexGenNode & node ) {
        osg::NodeVisitor::apply( boost::ref(node) );
    }

    virtual void apply( ::osg::LightSource & node ) {
        if( bp::override func_apply = this->get_override( "apply" ) )
            func_apply( boost::ref(node) );
        else{
            this->osg::NodeVisitor::apply( boost::ref(node) );
        }
    }
    
    void default_apply( ::osg::LightSource & node ) {
        osg::NodeVisitor::apply( boost::ref(node) );
    }

    virtual void apply( ::osg::Transform & node ) {
        if( bp::override func_apply = this->get_override( "apply" ) )
            func_apply( boost::ref(node) );
        else{
            this->osg::NodeVisitor::apply( boost::ref(node) );
        }
    }
    
    void default_apply( ::osg::Transform & node ) {
        osg::NodeVisitor::apply( boost::ref(node) );
    }

    virtual void apply( ::osg::Camera & node ) {
        if( bp::override func_apply = this->get_override( "apply" ) )
            func_apply( boost::ref(node) );
        else{
            this->osg::NodeVisitor::apply( boost::ref(node) );
        }
    }
    
    void default_apply( ::osg::Camera & node ) {
        osg::NodeVisitor::apply( boost::ref(node) );
    }

    virtual void apply( ::osg::CameraView & node ) {
        if( bp::override func_apply = this->get_override( "apply" ) )
            func_apply( boost::ref(node) );
        else{
            this->osg::NodeVisitor::apply( boost::ref(node) );
        }
    }
    
    void default_apply( ::osg::CameraView & node ) {
        osg::NodeVisitor::apply( boost::ref(node) );
    }

    virtual void apply( ::osg::MatrixTransform & node ) {
        if( bp::override func_apply = this->get_override( "apply" ) )
            func_apply( boost::ref(node) );
        else{
            this->osg::NodeVisitor::apply( boost::ref(node) );
        }
    }
    
    void default_apply( ::osg::MatrixTransform & node ) {
        osg::NodeVisitor::apply( boost::ref(node) );
    }

    virtual void apply( ::osg::PositionAttitudeTransform & node ) {
        if( bp::override func_apply = this->get_override( "apply" ) )
            func_apply( boost::ref(node) );
        else{
            this->osg::NodeVisitor::apply( boost::ref(node) );
        }
    }
    
    void default_apply( ::osg::PositionAttitudeTransform & node ) {
        osg::NodeVisitor::apply( boost::ref(node) );
    }

    virtual void apply( ::osg::Switch & node ) {
        if( bp::override func_apply = this->get_override( "apply" ) )
            func_apply( boost::ref(node) );
        else{
            this->osg::NodeVisitor::apply( boost::ref(node) );
        }
    }
    
    void default_apply( ::osg::Switch & node ) {
        osg::NodeVisitor::apply( boost::ref(node) );
    }

    virtual void apply( ::osg::Sequence & node ) {
        if( bp::override func_apply = this->get_override( "apply" ) )
            func_apply( boost::ref(node) );
        else{
            this->osg::NodeVisitor::apply( boost::ref(node) );
        }
    }
    
    void default_apply( ::osg::Sequence & node ) {
        osg::NodeVisitor::apply( boost::ref(node) );
    }

    virtual void apply( ::osg::LOD & node ) {
        if( bp::override func_apply = this->get_override( "apply" ) )
            func_apply( boost::ref(node) );
        else{
            this->osg::NodeVisitor::apply( boost::ref(node) );
        }
    }
    
    void default_apply( ::osg::LOD & node ) {
        osg::NodeVisitor::apply( boost::ref(node) );
    }

    virtual void apply( ::osg::PagedLOD & node ) {
        if( bp::override func_apply = this->get_override( "apply" ) )
            func_apply( boost::ref(node) );
        else{
            this->osg::NodeVisitor::apply( boost::ref(node) );
        }
    }
    
    void default_apply( ::osg::PagedLOD & node ) {
        osg::NodeVisitor::apply( boost::ref(node) );
    }

    virtual void apply( ::osg::ClearNode & node ) {
        if( bp::override func_apply = this->get_override( "apply" ) )
            func_apply( boost::ref(node) );
        else{
            this->osg::NodeVisitor::apply( boost::ref(node) );
        }
    }
    
    void default_apply( ::osg::ClearNode & node ) {
        osg::NodeVisitor::apply( boost::ref(node) );
    }

    virtual void apply( ::osg::OccluderNode & node ) {
        if( bp::override func_apply = this->get_override( "apply" ) )
            func_apply( boost::ref(node) );
        else{
            this->osg::NodeVisitor::apply( boost::ref(node) );
        }
    }
    
    void default_apply( ::osg::OccluderNode & node ) {
        osg::NodeVisitor::apply( boost::ref(node) );
    }

    virtual void apply( ::osg::OcclusionQueryNode & node ) {
        if( bp::override func_apply = this->get_override( "apply" ) )
            func_apply( boost::ref(node) );
        else{
            this->osg::NodeVisitor::apply( boost::ref(node) );
        }
    }
    
    void default_apply( ::osg::OcclusionQueryNode & node ) {
        osg::NodeVisitor::apply( boost::ref(node) );
    }

    virtual float getDistanceFromEyePoint( ::osg::Vec3 const & arg0, bool arg1 ) const  {
        if( bp::override func_getDistanceFromEyePoint = this->get_override( "getDistanceFromEyePoint" ) )
            return func_getDistanceFromEyePoint( boost::ref(arg0), arg1 );
        else{
            return this->osg::NodeVisitor::getDistanceFromEyePoint( boost::ref(arg0), arg1 );
        }
    }
    
    float default_getDistanceFromEyePoint( ::osg::Vec3 const & arg0, bool arg1 ) const  {
        return osg::NodeVisitor::getDistanceFromEyePoint( boost::ref(arg0), arg1 );
    }

    virtual float getDistanceToEyePoint( ::osg::Vec3 const & arg0, bool arg1 ) const  {
        if( bp::override func_getDistanceToEyePoint = this->get_override( "getDistanceToEyePoint" ) )
            return func_getDistanceToEyePoint( boost::ref(arg0), arg1 );
        else{
            return this->osg::NodeVisitor::getDistanceToEyePoint( boost::ref(arg0), arg1 );
        }
    }
    
    float default_getDistanceToEyePoint( ::osg::Vec3 const & arg0, bool arg1 ) const  {
        return osg::NodeVisitor::getDistanceToEyePoint( boost::ref(arg0), arg1 );
    }

    virtual float getDistanceToViewPoint( ::osg::Vec3 const & arg0, bool arg1 ) const  {
        if( bp::override func_getDistanceToViewPoint = this->get_override( "getDistanceToViewPoint" ) )
            return func_getDistanceToViewPoint( boost::ref(arg0), arg1 );
        else{
            return this->osg::NodeVisitor::getDistanceToViewPoint( boost::ref(arg0), arg1 );
        }
    }
    
    float default_getDistanceToViewPoint( ::osg::Vec3 const & arg0, bool arg1 ) const  {
        return osg::NodeVisitor::getDistanceToViewPoint( boost::ref(arg0), arg1 );
    }

    virtual ::osg::Vec3 getEyePoint(  ) const  {
        if( bp::override func_getEyePoint = this->get_override( "getEyePoint" ) )
            return func_getEyePoint(  );
        else{
            return this->osg::NodeVisitor::getEyePoint(  );
        }
    }
    
    ::osg::Vec3 default_getEyePoint(  ) const  {
        return osg::NodeVisitor::getEyePoint( );
    }

    virtual ::osg::Vec3 getViewPoint(  ) const  {
        if( bp::override func_getViewPoint = this->get_override( "getViewPoint" ) )
            return func_getViewPoint(  );
        else{
            return this->osg::NodeVisitor::getViewPoint(  );
        }
    }
    
    ::osg::Vec3 default_getViewPoint(  ) const  {
        return osg::NodeVisitor::getViewPoint( );
    }

    virtual void reset(  ) {
        if( bp::override func_reset = this->get_override( "reset" ) )
            func_reset(  );
        else{
            this->osg::NodeVisitor::reset(  );
        }
    }
    
    void default_reset(  ) {
        osg::NodeVisitor::reset( );
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

void register_Simplifier_class(){

    { //::osgUtil::Simplifier
        typedef bp::class_< Simplifier_wrapper, bp::bases< ::osg::NodeVisitor >, osg::ref_ptr< Simplifier_wrapper >, boost::noncopyable > Simplifier_exposer_t;
        Simplifier_exposer_t Simplifier_exposer = Simplifier_exposer_t( "Simplifier", bp::init< bp::optional< double, double, double > >(( bp::arg("sampleRatio")=1.0e+0, bp::arg("maximumError")=3.4028234663852885981170418348451692544e+38f, bp::arg("maximumLength")=0.0 )) );
        bp::scope Simplifier_scope( Simplifier_exposer );
        bp::class_< Simplifier_wrapper::ContinueSimplificationCallback_wrapper, bp::bases< ::osg::Referenced >, osg::ref_ptr< Simplifier_wrapper::ContinueSimplificationCallback_wrapper >, boost::noncopyable >( "ContinueSimplificationCallback", bp::no_init )    
            .def( 
                "continueSimplification"
                , (bool ( ::osgUtil::Simplifier::ContinueSimplificationCallback::* )( ::osgUtil::Simplifier const &,float,unsigned int,unsigned int )const)(&::osgUtil::Simplifier::ContinueSimplificationCallback::continueSimplification)
                , (bool ( Simplifier_wrapper::ContinueSimplificationCallback_wrapper::* )( ::osgUtil::Simplifier const &,float,unsigned int,unsigned int )const)(&Simplifier_wrapper::ContinueSimplificationCallback_wrapper::default_continueSimplification)
                , ( bp::arg("simplifier"), bp::arg("nextError"), bp::arg("numOriginalPrimitives"), bp::arg("numRemainingPrimitives") ) );
        bp::implicitly_convertible< double, osgUtil::Simplifier >();
        { //::osgUtil::Simplifier::apply
        
            typedef void ( ::osgUtil::Simplifier::*apply_function_type)( ::osg::Geode & ) ;
            typedef void ( Simplifier_wrapper::*default_apply_function_type)( ::osg::Geode & ) ;
            
            Simplifier_exposer.def( 
                "apply"
                , apply_function_type(&::osgUtil::Simplifier::apply)
                , default_apply_function_type(&Simplifier_wrapper::default_apply)
                , ( bp::arg("geode") ) );
        
        }
        { //::osgUtil::Simplifier::className
        
            typedef char const * ( ::osgUtil::Simplifier::*className_function_type)(  ) const;
            typedef char const * ( Simplifier_wrapper::*default_className_function_type)(  ) const;
            
            Simplifier_exposer.def( 
                "className"
                , className_function_type(&::osgUtil::Simplifier::className)
                , default_className_function_type(&Simplifier_wrapper::default_className) );
        
        }
        { //::osgUtil::Simplifier::continueSimplification
        
            typedef bool ( ::osgUtil::Simplifier::*continueSimplification_function_type)( float,unsigned int,unsigned int ) const;
            
            Simplifier_exposer.def( 
                "continueSimplification"
                , continueSimplification_function_type( &::osgUtil::Simplifier::continueSimplification )
                , ( bp::arg("nextError"), bp::arg("numOriginalPrimitives"), bp::arg("numRemainingPrimitives") ) );
        
        }
        { //::osgUtil::Simplifier::continueSimplificationImplementation
        
            typedef bool ( ::osgUtil::Simplifier::*continueSimplificationImplementation_function_type)( float,unsigned int,unsigned int ) const;
            typedef bool ( Simplifier_wrapper::*default_continueSimplificationImplementation_function_type)( float,unsigned int,unsigned int ) const;
            
            Simplifier_exposer.def( 
                "continueSimplificationImplementation"
                , continueSimplificationImplementation_function_type(&::osgUtil::Simplifier::continueSimplificationImplementation)
                , default_continueSimplificationImplementation_function_type(&Simplifier_wrapper::default_continueSimplificationImplementation)
                , ( bp::arg("nextError"), bp::arg("numOriginalPrimitives"), bp::arg("numRemainingPrimitives") ) );
        
        }
        { //::osgUtil::Simplifier::getContinueSimplificationCallback
        
            typedef ::osgUtil::Simplifier::ContinueSimplificationCallback * ( ::osgUtil::Simplifier::*getContinueSimplificationCallback_function_type)(  ) ;
            
            Simplifier_exposer.def( 
                "getContinueSimplificationCallback"
                , getContinueSimplificationCallback_function_type( &::osgUtil::Simplifier::getContinueSimplificationCallback )
                , bp::return_internal_reference< >() );
        
        }
        { //::osgUtil::Simplifier::getContinueSimplificationCallback
        
            typedef ::osgUtil::Simplifier::ContinueSimplificationCallback const * ( ::osgUtil::Simplifier::*getContinueSimplificationCallback_function_type)(  ) const;
            
            Simplifier_exposer.def( 
                "getContinueSimplificationCallback"
                , getContinueSimplificationCallback_function_type( &::osgUtil::Simplifier::getContinueSimplificationCallback )
                , bp::return_internal_reference< >() );
        
        }
        { //::osgUtil::Simplifier::getDoTriStrip
        
            typedef bool ( ::osgUtil::Simplifier::*getDoTriStrip_function_type)(  ) const;
            
            Simplifier_exposer.def( 
                "getDoTriStrip"
                , getDoTriStrip_function_type( &::osgUtil::Simplifier::getDoTriStrip ) );
        
        }
        { //::osgUtil::Simplifier::getMaximumError
        
            typedef float ( ::osgUtil::Simplifier::*getMaximumError_function_type)(  ) const;
            
            Simplifier_exposer.def( 
                "getMaximumError"
                , getMaximumError_function_type( &::osgUtil::Simplifier::getMaximumError ) );
        
        }
        { //::osgUtil::Simplifier::getMaximumLength
        
            typedef float ( ::osgUtil::Simplifier::*getMaximumLength_function_type)(  ) const;
            
            Simplifier_exposer.def( 
                "getMaximumLength"
                , getMaximumLength_function_type( &::osgUtil::Simplifier::getMaximumLength ) );
        
        }
        { //::osgUtil::Simplifier::getSampleRatio
        
            typedef float ( ::osgUtil::Simplifier::*getSampleRatio_function_type)(  ) const;
            
            Simplifier_exposer.def( 
                "getSampleRatio"
                , getSampleRatio_function_type( &::osgUtil::Simplifier::getSampleRatio ) );
        
        }
        { //::osgUtil::Simplifier::getSmoothing
        
            typedef bool ( ::osgUtil::Simplifier::*getSmoothing_function_type)(  ) const;
            
            Simplifier_exposer.def( 
                "getSmoothing"
                , getSmoothing_function_type( &::osgUtil::Simplifier::getSmoothing ) );
        
        }
        { //::osgUtil::Simplifier::libraryName
        
            typedef char const * ( ::osgUtil::Simplifier::*libraryName_function_type)(  ) const;
            typedef char const * ( Simplifier_wrapper::*default_libraryName_function_type)(  ) const;
            
            Simplifier_exposer.def( 
                "libraryName"
                , libraryName_function_type(&::osgUtil::Simplifier::libraryName)
                , default_libraryName_function_type(&Simplifier_wrapper::default_libraryName) );
        
        }
        { //::osgUtil::Simplifier::setContinueSimplificationCallback
        
            typedef void ( ::osgUtil::Simplifier::*setContinueSimplificationCallback_function_type)( ::osgUtil::Simplifier::ContinueSimplificationCallback * ) ;
            
            Simplifier_exposer.def( 
                "setContinueSimplificationCallback"
                , setContinueSimplificationCallback_function_type( &::osgUtil::Simplifier::setContinueSimplificationCallback )
                , ( bp::arg("cb") ) );
        
        }
        { //::osgUtil::Simplifier::setDoTriStrip
        
            typedef void ( ::osgUtil::Simplifier::*setDoTriStrip_function_type)( bool ) ;
            
            Simplifier_exposer.def( 
                "setDoTriStrip"
                , setDoTriStrip_function_type( &::osgUtil::Simplifier::setDoTriStrip )
                , ( bp::arg("on") ) );
        
        }
        { //::osgUtil::Simplifier::setMaximumError
        
            typedef void ( ::osgUtil::Simplifier::*setMaximumError_function_type)( float ) ;
            
            Simplifier_exposer.def( 
                "setMaximumError"
                , setMaximumError_function_type( &::osgUtil::Simplifier::setMaximumError )
                , ( bp::arg("error") ) );
        
        }
        { //::osgUtil::Simplifier::setMaximumLength
        
            typedef void ( ::osgUtil::Simplifier::*setMaximumLength_function_type)( float ) ;
            
            Simplifier_exposer.def( 
                "setMaximumLength"
                , setMaximumLength_function_type( &::osgUtil::Simplifier::setMaximumLength )
                , ( bp::arg("length") ) );
        
        }
        { //::osgUtil::Simplifier::setSampleRatio
        
            typedef void ( ::osgUtil::Simplifier::*setSampleRatio_function_type)( float ) ;
            
            Simplifier_exposer.def( 
                "setSampleRatio"
                , setSampleRatio_function_type( &::osgUtil::Simplifier::setSampleRatio )
                , ( bp::arg("sampleRatio") ) );
        
        }
        { //::osgUtil::Simplifier::setSmoothing
        
            typedef void ( ::osgUtil::Simplifier::*setSmoothing_function_type)( bool ) ;
            
            Simplifier_exposer.def( 
                "setSmoothing"
                , setSmoothing_function_type( &::osgUtil::Simplifier::setSmoothing )
                , ( bp::arg("on") ) );
        
        }
        { //::osgUtil::Simplifier::simplify
        
            typedef void ( ::osgUtil::Simplifier::*simplify_function_type)( ::osg::Geometry & ) ;
            
            Simplifier_exposer.def( 
                "simplify"
                , simplify_function_type( &::osgUtil::Simplifier::simplify )
                , ( bp::arg("geometry") ) );
        
        }
        { //::osgUtil::Simplifier::simplify
        
            typedef void ( ::osgUtil::Simplifier::*simplify_function_type)( ::osg::Geometry &,::std::vector< unsigned int > const & ) ;
            
            Simplifier_exposer.def( 
                "simplify"
                , simplify_function_type( &::osgUtil::Simplifier::simplify )
                , ( bp::arg("geometry"), bp::arg("protectedPoints") ) );
        
        }
    }

}
