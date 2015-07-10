// This file has been generated by Py++.

#include "boost/python.hpp"
#include "__call_policies.pypp.hpp"
#include "__convenience.pypp.hpp"
#include "wrap_osgmanipulator.h"
#include "wrap_referenced.h"
#include "draggertransformcallback.pypp.hpp"

namespace bp = boost::python;

struct DraggerTransformCallback_wrapper : osgManipulator::DraggerTransformCallback, bp::wrapper< osgManipulator::DraggerTransformCallback > {

    DraggerTransformCallback_wrapper(::osg::MatrixTransform * transform, int handleCommandMask=int(::osgManipulator::DraggerTransformCallback::HANDLE_ALL) )
    : osgManipulator::DraggerTransformCallback( boost::python::ptr(transform), handleCommandMask )
      , bp::wrapper< osgManipulator::DraggerTransformCallback >(){
        // constructor
    
    }

    virtual bool receive( ::osgManipulator::MotionCommand const & arg0 ) {
        namespace bpl = boost::python;
        if( bpl::override func_receive = this->get_override( "receive" ) ){
            bpl::object py_result = bpl::call<bpl::object>( func_receive.ptr(), arg0 );
            return bpl::extract< bool >( pyplus_conv::get_out_argument( py_result, 0 ) );
        }
        else{
            return osgManipulator::DraggerTransformCallback::receive( boost::ref(arg0) );
        }
    }
    
    static boost::python::object default_receive_178ffe8a2d148c2b28f6ab6191a997cd( ::osgManipulator::DraggerTransformCallback & inst, ::osgManipulator::MotionCommand & arg0 ){
        bool result;
        if( dynamic_cast< DraggerTransformCallback_wrapper * >( boost::addressof( inst ) ) ){
            result = inst.::osgManipulator::DraggerTransformCallback::receive(arg0);
        }
        else{
            result = inst.receive(arg0);
        }
        return bp::object( result );
    }

    virtual bool receive( ::osgManipulator::TranslateInLineCommand const & command ) {
        namespace bpl = boost::python;
        if( bpl::override func_receive = this->get_override( "receive" ) ){
            bpl::object py_result = bpl::call<bpl::object>( func_receive.ptr(), command );
            return bpl::extract< bool >( pyplus_conv::get_out_argument( py_result, 0 ) );
        }
        else{
            return osgManipulator::DraggerTransformCallback::receive( boost::ref(command) );
        }
    }
    
    static boost::python::object default_receive_6b66af821f8cfe734aa2f85c237ec6a4( ::osgManipulator::DraggerTransformCallback & inst, ::osgManipulator::TranslateInLineCommand & command ){
        bool result;
        if( dynamic_cast< DraggerTransformCallback_wrapper * >( boost::addressof( inst ) ) ){
            result = inst.::osgManipulator::DraggerTransformCallback::receive(command);
        }
        else{
            result = inst.receive(command);
        }
        return bp::object( result );
    }

    virtual bool receive( ::osgManipulator::TranslateInPlaneCommand const & command ) {
        namespace bpl = boost::python;
        if( bpl::override func_receive = this->get_override( "receive" ) ){
            bpl::object py_result = bpl::call<bpl::object>( func_receive.ptr(), command );
            return bpl::extract< bool >( pyplus_conv::get_out_argument( py_result, 0 ) );
        }
        else{
            return osgManipulator::DraggerTransformCallback::receive( boost::ref(command) );
        }
    }
    
    static boost::python::object default_receive_df11c23a37afb7970b0a06fcb58d5ac2( ::osgManipulator::DraggerTransformCallback & inst, ::osgManipulator::TranslateInPlaneCommand & command ){
        bool result;
        if( dynamic_cast< DraggerTransformCallback_wrapper * >( boost::addressof( inst ) ) ){
            result = inst.::osgManipulator::DraggerTransformCallback::receive(command);
        }
        else{
            result = inst.receive(command);
        }
        return bp::object( result );
    }

    virtual bool receive( ::osgManipulator::Scale1DCommand const & command ) {
        namespace bpl = boost::python;
        if( bpl::override func_receive = this->get_override( "receive" ) ){
            bpl::object py_result = bpl::call<bpl::object>( func_receive.ptr(), command );
            return bpl::extract< bool >( pyplus_conv::get_out_argument( py_result, 0 ) );
        }
        else{
            return osgManipulator::DraggerTransformCallback::receive( boost::ref(command) );
        }
    }
    
    static boost::python::object default_receive_d2c13d425eec3d71ad256c3c5ca9b899( ::osgManipulator::DraggerTransformCallback & inst, ::osgManipulator::Scale1DCommand & command ){
        bool result;
        if( dynamic_cast< DraggerTransformCallback_wrapper * >( boost::addressof( inst ) ) ){
            result = inst.::osgManipulator::DraggerTransformCallback::receive(command);
        }
        else{
            result = inst.receive(command);
        }
        return bp::object( result );
    }

    virtual bool receive( ::osgManipulator::Scale2DCommand const & command ) {
        namespace bpl = boost::python;
        if( bpl::override func_receive = this->get_override( "receive" ) ){
            bpl::object py_result = bpl::call<bpl::object>( func_receive.ptr(), command );
            return bpl::extract< bool >( pyplus_conv::get_out_argument( py_result, 0 ) );
        }
        else{
            return osgManipulator::DraggerTransformCallback::receive( boost::ref(command) );
        }
    }
    
    static boost::python::object default_receive_444bf1c311cac98c8b783d112688bcdd( ::osgManipulator::DraggerTransformCallback & inst, ::osgManipulator::Scale2DCommand & command ){
        bool result;
        if( dynamic_cast< DraggerTransformCallback_wrapper * >( boost::addressof( inst ) ) ){
            result = inst.::osgManipulator::DraggerTransformCallback::receive(command);
        }
        else{
            result = inst.receive(command);
        }
        return bp::object( result );
    }

    virtual bool receive( ::osgManipulator::ScaleUniformCommand const & command ) {
        namespace bpl = boost::python;
        if( bpl::override func_receive = this->get_override( "receive" ) ){
            bpl::object py_result = bpl::call<bpl::object>( func_receive.ptr(), command );
            return bpl::extract< bool >( pyplus_conv::get_out_argument( py_result, 0 ) );
        }
        else{
            return osgManipulator::DraggerTransformCallback::receive( boost::ref(command) );
        }
    }
    
    static boost::python::object default_receive_a0251fe8dfdc649b31e6e0e92295ad30( ::osgManipulator::DraggerTransformCallback & inst, ::osgManipulator::ScaleUniformCommand & command ){
        bool result;
        if( dynamic_cast< DraggerTransformCallback_wrapper * >( boost::addressof( inst ) ) ){
            result = inst.::osgManipulator::DraggerTransformCallback::receive(command);
        }
        else{
            result = inst.receive(command);
        }
        return bp::object( result );
    }

    virtual bool receive( ::osgManipulator::Rotate3DCommand const & command ) {
        namespace bpl = boost::python;
        if( bpl::override func_receive = this->get_override( "receive" ) ){
            bpl::object py_result = bpl::call<bpl::object>( func_receive.ptr(), command );
            return bpl::extract< bool >( pyplus_conv::get_out_argument( py_result, 0 ) );
        }
        else{
            return osgManipulator::DraggerTransformCallback::receive( boost::ref(command) );
        }
    }
    
    static boost::python::object default_receive_4ffd06b2c9e883e445e7bd36bbbf0a22( ::osgManipulator::DraggerTransformCallback & inst, ::osgManipulator::Rotate3DCommand & command ){
        bool result;
        if( dynamic_cast< DraggerTransformCallback_wrapper * >( boost::addressof( inst ) ) ){
            result = inst.::osgManipulator::DraggerTransformCallback::receive(command);
        }
        else{
            result = inst.receive(command);
        }
        return bp::object( result );
    }

    virtual char const * className(  ) const  {
        if( bp::override func_className = this->get_override( "className" ) )
            return func_className(  );
        else{
            return this->osgManipulator::DraggerCallback::className(  );
        }
    }
    
    char const * default_className(  ) const  {
        return osgManipulator::DraggerCallback::className( );
    }

    virtual ::osg::Object * clone( ::osg::CopyOp const & copyop ) const  {
        if( bp::override func_clone = this->get_override( "clone" ) )
            return func_clone( boost::ref(copyop) );
        else{
            return this->osgManipulator::DraggerCallback::clone( boost::ref(copyop) );
        }
    }
    
    ::osg::Object * default_clone( ::osg::CopyOp const & copyop ) const  {
        return osgManipulator::DraggerCallback::clone( boost::ref(copyop) );
    }

    virtual ::osg::Object * cloneType(  ) const  {
        if( bp::override func_cloneType = this->get_override( "cloneType" ) )
            return func_cloneType(  );
        else{
            return this->osgManipulator::DraggerCallback::cloneType(  );
        }
    }
    
    ::osg::Object * default_cloneType(  ) const  {
        return osgManipulator::DraggerCallback::cloneType( );
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

    virtual bool isSameKindAs( ::osg::Object const * obj ) const  {
        if( bp::override func_isSameKindAs = this->get_override( "isSameKindAs" ) )
            return func_isSameKindAs( boost::python::ptr(obj) );
        else{
            return this->osgManipulator::DraggerCallback::isSameKindAs( boost::python::ptr(obj) );
        }
    }
    
    bool default_isSameKindAs( ::osg::Object const * obj ) const  {
        return osgManipulator::DraggerCallback::isSameKindAs( boost::python::ptr(obj) );
    }

    virtual char const * libraryName(  ) const  {
        if( bp::override func_libraryName = this->get_override( "libraryName" ) )
            return func_libraryName(  );
        else{
            return this->osgManipulator::DraggerCallback::libraryName(  );
        }
    }
    
    char const * default_libraryName(  ) const  {
        return osgManipulator::DraggerCallback::libraryName( );
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

void register_DraggerTransformCallback_class(){

    { //::osgManipulator::DraggerTransformCallback
        typedef bp::class_< DraggerTransformCallback_wrapper, bp::bases< osgManipulator::DraggerCallback >, osg::ref_ptr< ::osgManipulator::DraggerTransformCallback >, boost::noncopyable > DraggerTransformCallback_exposer_t;
        DraggerTransformCallback_exposer_t DraggerTransformCallback_exposer = DraggerTransformCallback_exposer_t( "DraggerTransformCallback", bp::init< osg::MatrixTransform *, bp::optional< int > >(( bp::arg("transform"), bp::arg("handleCommandMask")=int(::osgManipulator::DraggerTransformCallback::HANDLE_ALL) )) );
        bp::scope DraggerTransformCallback_scope( DraggerTransformCallback_exposer );
        bp::enum_< osgManipulator::DraggerTransformCallback::HandleCommandMask>("HandleCommandMask")
            .value("HANDLE_TRANSLATE_IN_LINE", osgManipulator::DraggerTransformCallback::HANDLE_TRANSLATE_IN_LINE)
            .value("HANDLE_TRANSLATE_IN_PLANE", osgManipulator::DraggerTransformCallback::HANDLE_TRANSLATE_IN_PLANE)
            .value("HANDLE_SCALED_1D", osgManipulator::DraggerTransformCallback::HANDLE_SCALED_1D)
            .value("HANDLE_SCALED_2D", osgManipulator::DraggerTransformCallback::HANDLE_SCALED_2D)
            .value("HANDLE_SCALED_UNIFORM", osgManipulator::DraggerTransformCallback::HANDLE_SCALED_UNIFORM)
            .value("HANDLE_ROTATE_3D", osgManipulator::DraggerTransformCallback::HANDLE_ROTATE_3D)
            .value("HANDLE_ALL", osgManipulator::DraggerTransformCallback::HANDLE_ALL)
            .export_values()
            ;
        bp::implicitly_convertible< osg::MatrixTransform *, osgManipulator::DraggerTransformCallback >();
        { //::osgManipulator::DraggerTransformCallback::getTransform
        
            typedef ::osg::MatrixTransform * ( ::osgManipulator::DraggerTransformCallback::*getTransform_function_type)(  ) ;
            
            DraggerTransformCallback_exposer.def( 
                "getTransform"
                , getTransform_function_type( &::osgManipulator::DraggerTransformCallback::getTransform )
                , bp::return_internal_reference< >() );
        
        }
        { //::osgManipulator::DraggerTransformCallback::getTransform
        
            typedef ::osg::MatrixTransform const * ( ::osgManipulator::DraggerTransformCallback::*getTransform_function_type)(  ) const;
            
            DraggerTransformCallback_exposer.def( 
                "getTransform"
                , getTransform_function_type( &::osgManipulator::DraggerTransformCallback::getTransform )
                , bp::return_internal_reference< >() );
        
        }
        { //::osgManipulator::DraggerTransformCallback::receive
        
            typedef boost::python::object ( *default_receive_178ffe8a2d148c2b28f6ab6191a997cd_function_type )( ::osgManipulator::DraggerTransformCallback &,::osgManipulator::MotionCommand & );
            
            DraggerTransformCallback_exposer.def( 
                "receive_178ffe8a2d148c2b28f6ab6191a997cd"
                , default_receive_178ffe8a2d148c2b28f6ab6191a997cd_function_type( &DraggerTransformCallback_wrapper::default_receive_178ffe8a2d148c2b28f6ab6191a997cd )
                , ( bp::arg("inst"), bp::arg("arg0") ) );
        
        }
        { //::osgManipulator::DraggerTransformCallback::receive
        
            typedef boost::python::object ( *default_receive_6b66af821f8cfe734aa2f85c237ec6a4_function_type )( ::osgManipulator::DraggerTransformCallback &,::osgManipulator::TranslateInLineCommand & );
            
            DraggerTransformCallback_exposer.def( 
                "receive_6b66af821f8cfe734aa2f85c237ec6a4"
                , default_receive_6b66af821f8cfe734aa2f85c237ec6a4_function_type( &DraggerTransformCallback_wrapper::default_receive_6b66af821f8cfe734aa2f85c237ec6a4 )
                , ( bp::arg("inst"), bp::arg("command") ) );
        
        }
        { //::osgManipulator::DraggerTransformCallback::receive
        
            typedef boost::python::object ( *default_receive_df11c23a37afb7970b0a06fcb58d5ac2_function_type )( ::osgManipulator::DraggerTransformCallback &,::osgManipulator::TranslateInPlaneCommand & );
            
            DraggerTransformCallback_exposer.def( 
                "receive_df11c23a37afb7970b0a06fcb58d5ac2"
                , default_receive_df11c23a37afb7970b0a06fcb58d5ac2_function_type( &DraggerTransformCallback_wrapper::default_receive_df11c23a37afb7970b0a06fcb58d5ac2 )
                , ( bp::arg("inst"), bp::arg("command") ) );
        
        }
        { //::osgManipulator::DraggerTransformCallback::receive
        
            typedef boost::python::object ( *default_receive_d2c13d425eec3d71ad256c3c5ca9b899_function_type )( ::osgManipulator::DraggerTransformCallback &,::osgManipulator::Scale1DCommand & );
            
            DraggerTransformCallback_exposer.def( 
                "receive_d2c13d425eec3d71ad256c3c5ca9b899"
                , default_receive_d2c13d425eec3d71ad256c3c5ca9b899_function_type( &DraggerTransformCallback_wrapper::default_receive_d2c13d425eec3d71ad256c3c5ca9b899 )
                , ( bp::arg("inst"), bp::arg("command") ) );
        
        }
        { //::osgManipulator::DraggerTransformCallback::receive
        
            typedef boost::python::object ( *default_receive_444bf1c311cac98c8b783d112688bcdd_function_type )( ::osgManipulator::DraggerTransformCallback &,::osgManipulator::Scale2DCommand & );
            
            DraggerTransformCallback_exposer.def( 
                "receive_444bf1c311cac98c8b783d112688bcdd"
                , default_receive_444bf1c311cac98c8b783d112688bcdd_function_type( &DraggerTransformCallback_wrapper::default_receive_444bf1c311cac98c8b783d112688bcdd )
                , ( bp::arg("inst"), bp::arg("command") ) );
        
        }
        { //::osgManipulator::DraggerTransformCallback::receive
        
            typedef boost::python::object ( *default_receive_a0251fe8dfdc649b31e6e0e92295ad30_function_type )( ::osgManipulator::DraggerTransformCallback &,::osgManipulator::ScaleUniformCommand & );
            
            DraggerTransformCallback_exposer.def( 
                "receive_a0251fe8dfdc649b31e6e0e92295ad30"
                , default_receive_a0251fe8dfdc649b31e6e0e92295ad30_function_type( &DraggerTransformCallback_wrapper::default_receive_a0251fe8dfdc649b31e6e0e92295ad30 )
                , ( bp::arg("inst"), bp::arg("command") ) );
        
        }
        { //::osgManipulator::DraggerTransformCallback::receive
        
            typedef boost::python::object ( *default_receive_4ffd06b2c9e883e445e7bd36bbbf0a22_function_type )( ::osgManipulator::DraggerTransformCallback &,::osgManipulator::Rotate3DCommand & );
            
            DraggerTransformCallback_exposer.def( 
                "receive_4ffd06b2c9e883e445e7bd36bbbf0a22"
                , default_receive_4ffd06b2c9e883e445e7bd36bbbf0a22_function_type( &DraggerTransformCallback_wrapper::default_receive_4ffd06b2c9e883e445e7bd36bbbf0a22 )
                , ( bp::arg("inst"), bp::arg("command") ) );
        
        }
        { //::osgManipulator::DraggerCallback::className
        
            typedef char const * ( ::osgManipulator::DraggerCallback::*className_function_type)(  ) const;
            typedef char const * ( DraggerTransformCallback_wrapper::*default_className_function_type)(  ) const;
            
            DraggerTransformCallback_exposer.def( 
                "className"
                , className_function_type(&::osgManipulator::DraggerCallback::className)
                , default_className_function_type(&DraggerTransformCallback_wrapper::default_className) );
        
        }
        { //::osgManipulator::DraggerCallback::clone
        
            typedef ::osg::Object * ( ::osgManipulator::DraggerCallback::*clone_function_type)( ::osg::CopyOp const & ) const;
            typedef ::osg::Object * ( DraggerTransformCallback_wrapper::*default_clone_function_type)( ::osg::CopyOp const & ) const;
            
            DraggerTransformCallback_exposer.def( 
                "clone"
                , clone_function_type(&::osgManipulator::DraggerCallback::clone)
                , default_clone_function_type(&DraggerTransformCallback_wrapper::default_clone)
                , ( bp::arg("copyop") )
                , bp::return_value_policy< bp::reference_existing_object >() );
        
        }
        { //::osgManipulator::DraggerCallback::cloneType
        
            typedef ::osg::Object * ( ::osgManipulator::DraggerCallback::*cloneType_function_type)(  ) const;
            typedef ::osg::Object * ( DraggerTransformCallback_wrapper::*default_cloneType_function_type)(  ) const;
            
            DraggerTransformCallback_exposer.def( 
                "cloneType"
                , cloneType_function_type(&::osgManipulator::DraggerCallback::cloneType)
                , default_cloneType_function_type(&DraggerTransformCallback_wrapper::default_cloneType)
                , bp::return_value_policy< bp::reference_existing_object >() );
        
        }
        { //::osgManipulator::DraggerCallback::isSameKindAs
        
            typedef bool ( ::osgManipulator::DraggerCallback::*isSameKindAs_function_type)( ::osg::Object const * ) const;
            typedef bool ( DraggerTransformCallback_wrapper::*default_isSameKindAs_function_type)( ::osg::Object const * ) const;
            
            DraggerTransformCallback_exposer.def( 
                "isSameKindAs"
                , isSameKindAs_function_type(&::osgManipulator::DraggerCallback::isSameKindAs)
                , default_isSameKindAs_function_type(&DraggerTransformCallback_wrapper::default_isSameKindAs)
                , ( bp::arg("obj") ) );
        
        }
        { //::osgManipulator::DraggerCallback::libraryName
        
            typedef char const * ( ::osgManipulator::DraggerCallback::*libraryName_function_type)(  ) const;
            typedef char const * ( DraggerTransformCallback_wrapper::*default_libraryName_function_type)(  ) const;
            
            DraggerTransformCallback_exposer.def( 
                "libraryName"
                , libraryName_function_type(&::osgManipulator::DraggerCallback::libraryName)
                , default_libraryName_function_type(&DraggerTransformCallback_wrapper::default_libraryName) );
        
        }
    }

}
