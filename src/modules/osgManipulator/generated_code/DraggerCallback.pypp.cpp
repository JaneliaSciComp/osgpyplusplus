// This file has been generated by Py++.

#include "boost/python.hpp"
#include "__call_policies.pypp.hpp"
#include "__convenience.pypp.hpp"
#include "wrap_osgmanipulator.h"
#include "wrap_referenced.h"
#include "draggercallback.pypp.hpp"

namespace bp = boost::python;

struct DraggerCallback_wrapper : osgManipulator::DraggerCallback, bp::wrapper< osgManipulator::DraggerCallback > {

    DraggerCallback_wrapper( )
    : osgManipulator::DraggerCallback( )
      , bp::wrapper< osgManipulator::DraggerCallback >(){
        // null constructor
    
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

    virtual bool receive( ::osgManipulator::MotionCommand const & arg0 ) {
        namespace bpl = boost::python;
        if( bpl::override func_receive = this->get_override( "receive" ) ){
            bpl::object py_result = bpl::call<bpl::object>( func_receive.ptr(), arg0 );
            return bpl::extract< bool >( pyplus_conv::get_out_argument( py_result, 0 ) );
        }
        else{
            return osgManipulator::DraggerCallback::receive( boost::ref(arg0) );
        }
    }
    
    static boost::python::object default_receive_a81453cad0b55e6a30e46933e3b5b17c( ::osgManipulator::DraggerCallback & inst, ::osgManipulator::MotionCommand & arg0 ){
        bool result;
        if( dynamic_cast< DraggerCallback_wrapper * >( boost::addressof( inst ) ) ){
            result = inst.::osgManipulator::DraggerCallback::receive(arg0);
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
            return osgManipulator::DraggerCallback::receive( boost::ref(command) );
        }
    }
    
    static boost::python::object default_receive_e7cc153a637f6f3432496652cc9d1858( ::osgManipulator::DraggerCallback & inst, ::osgManipulator::TranslateInLineCommand & command ){
        bool result;
        if( dynamic_cast< DraggerCallback_wrapper * >( boost::addressof( inst ) ) ){
            result = inst.::osgManipulator::DraggerCallback::receive(command);
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
            return osgManipulator::DraggerCallback::receive( boost::ref(command) );
        }
    }
    
    static boost::python::object default_receive_5488ed9d7f0cca5b12d7517033a20f51( ::osgManipulator::DraggerCallback & inst, ::osgManipulator::TranslateInPlaneCommand & command ){
        bool result;
        if( dynamic_cast< DraggerCallback_wrapper * >( boost::addressof( inst ) ) ){
            result = inst.::osgManipulator::DraggerCallback::receive(command);
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
            return osgManipulator::DraggerCallback::receive( boost::ref(command) );
        }
    }
    
    static boost::python::object default_receive_11781cc69a44ac6348a6c71d668d3b81( ::osgManipulator::DraggerCallback & inst, ::osgManipulator::Scale1DCommand & command ){
        bool result;
        if( dynamic_cast< DraggerCallback_wrapper * >( boost::addressof( inst ) ) ){
            result = inst.::osgManipulator::DraggerCallback::receive(command);
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
            return osgManipulator::DraggerCallback::receive( boost::ref(command) );
        }
    }
    
    static boost::python::object default_receive_8b77b025db4546a6ef47457de56e9579( ::osgManipulator::DraggerCallback & inst, ::osgManipulator::Scale2DCommand & command ){
        bool result;
        if( dynamic_cast< DraggerCallback_wrapper * >( boost::addressof( inst ) ) ){
            result = inst.::osgManipulator::DraggerCallback::receive(command);
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
            return osgManipulator::DraggerCallback::receive( boost::ref(command) );
        }
    }
    
    static boost::python::object default_receive_2bb013936d212b1ee8ce88da814e247f( ::osgManipulator::DraggerCallback & inst, ::osgManipulator::ScaleUniformCommand & command ){
        bool result;
        if( dynamic_cast< DraggerCallback_wrapper * >( boost::addressof( inst ) ) ){
            result = inst.::osgManipulator::DraggerCallback::receive(command);
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
            return osgManipulator::DraggerCallback::receive( boost::ref(command) );
        }
    }
    
    static boost::python::object default_receive_236194aaae50ce6fada1a0f669208c0a( ::osgManipulator::DraggerCallback & inst, ::osgManipulator::Rotate3DCommand & command ){
        bool result;
        if( dynamic_cast< DraggerCallback_wrapper * >( boost::addressof( inst ) ) ){
            result = inst.::osgManipulator::DraggerCallback::receive(command);
        }
        else{
            result = inst.receive(command);
        }
        return bp::object( result );
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

void register_DraggerCallback_class(){

    bp::class_< DraggerCallback_wrapper, bp::bases< ::osg::Object >, osg::ref_ptr< ::osgManipulator::DraggerCallback >, boost::noncopyable >( "DraggerCallback", bp::init< >() )    
        .def( 
            "className"
            , (char const * ( ::osgManipulator::DraggerCallback::* )(  )const)(&::osgManipulator::DraggerCallback::className)
            , (char const * ( DraggerCallback_wrapper::* )(  )const)(&DraggerCallback_wrapper::default_className) )    
        .def( 
            "clone"
            , (::osg::Object * ( ::osgManipulator::DraggerCallback::* )( ::osg::CopyOp const & )const)(&::osgManipulator::DraggerCallback::clone)
            , (::osg::Object * ( DraggerCallback_wrapper::* )( ::osg::CopyOp const & )const)(&DraggerCallback_wrapper::default_clone)
            , ( bp::arg("copyop") )
            , bp::return_value_policy< bp::reference_existing_object >() )    
        .def( 
            "cloneType"
            , (::osg::Object * ( ::osgManipulator::DraggerCallback::* )(  )const)(&::osgManipulator::DraggerCallback::cloneType)
            , (::osg::Object * ( DraggerCallback_wrapper::* )(  )const)(&DraggerCallback_wrapper::default_cloneType)
            , bp::return_value_policy< bp::reference_existing_object >() )    
        .def( 
            "isSameKindAs"
            , (bool ( ::osgManipulator::DraggerCallback::* )( ::osg::Object const * )const)(&::osgManipulator::DraggerCallback::isSameKindAs)
            , (bool ( DraggerCallback_wrapper::* )( ::osg::Object const * )const)(&DraggerCallback_wrapper::default_isSameKindAs)
            , ( bp::arg("obj") ) )    
        .def( 
            "libraryName"
            , (char const * ( ::osgManipulator::DraggerCallback::* )(  )const)(&::osgManipulator::DraggerCallback::libraryName)
            , (char const * ( DraggerCallback_wrapper::* )(  )const)(&DraggerCallback_wrapper::default_libraryName) )    
        .def( 
            "receive_a81453cad0b55e6a30e46933e3b5b17c"
            , (boost::python::object (*)( ::osgManipulator::DraggerCallback &,::osgManipulator::MotionCommand & ))( &DraggerCallback_wrapper::default_receive_a81453cad0b55e6a30e46933e3b5b17c )
            , ( bp::arg("inst"), bp::arg("arg0") )
            , "\n Receive motion commands. Returns true on success.\n" )    
        .def( 
            "receive_e7cc153a637f6f3432496652cc9d1858"
            , (boost::python::object (*)( ::osgManipulator::DraggerCallback &,::osgManipulator::TranslateInLineCommand & ))( &DraggerCallback_wrapper::default_receive_e7cc153a637f6f3432496652cc9d1858 )
            , ( bp::arg("inst"), bp::arg("command") ) )    
        .def( 
            "receive_5488ed9d7f0cca5b12d7517033a20f51"
            , (boost::python::object (*)( ::osgManipulator::DraggerCallback &,::osgManipulator::TranslateInPlaneCommand & ))( &DraggerCallback_wrapper::default_receive_5488ed9d7f0cca5b12d7517033a20f51 )
            , ( bp::arg("inst"), bp::arg("command") ) )    
        .def( 
            "receive_11781cc69a44ac6348a6c71d668d3b81"
            , (boost::python::object (*)( ::osgManipulator::DraggerCallback &,::osgManipulator::Scale1DCommand & ))( &DraggerCallback_wrapper::default_receive_11781cc69a44ac6348a6c71d668d3b81 )
            , ( bp::arg("inst"), bp::arg("command") ) )    
        .def( 
            "receive_8b77b025db4546a6ef47457de56e9579"
            , (boost::python::object (*)( ::osgManipulator::DraggerCallback &,::osgManipulator::Scale2DCommand & ))( &DraggerCallback_wrapper::default_receive_8b77b025db4546a6ef47457de56e9579 )
            , ( bp::arg("inst"), bp::arg("command") ) )    
        .def( 
            "receive_2bb013936d212b1ee8ce88da814e247f"
            , (boost::python::object (*)( ::osgManipulator::DraggerCallback &,::osgManipulator::ScaleUniformCommand & ))( &DraggerCallback_wrapper::default_receive_2bb013936d212b1ee8ce88da814e247f )
            , ( bp::arg("inst"), bp::arg("command") ) )    
        .def( 
            "receive_236194aaae50ce6fada1a0f669208c0a"
            , (boost::python::object (*)( ::osgManipulator::DraggerCallback &,::osgManipulator::Rotate3DCommand & ))( &DraggerCallback_wrapper::default_receive_236194aaae50ce6fada1a0f669208c0a )
            , ( bp::arg("inst"), bp::arg("command") ) );

}