// This file has been generated by Py++.

#include "boost/python.hpp"
#include "wrap_osg.h"
#include "wrap_referenced.h"
#include "querygeometry.pypp.hpp"

namespace bp = boost::python;

struct QueryGeometry_wrapper : osg::QueryGeometry, bp::wrapper< osg::QueryGeometry > {

    QueryGeometry_wrapper(::std::string const & oqnName=std::basic_string<char, std::char_traits<char>, std::allocator<char> >(((const char*)"")) )
    : osg::QueryGeometry( oqnName )
      , bp::wrapper< osg::QueryGeometry >(){
        // constructor
    
    }

    virtual void drawImplementation( ::osg::RenderInfo & renderInfo ) const  {
        if( bp::override func_drawImplementation = this->get_override( "drawImplementation" ) )
            func_drawImplementation( boost::ref(renderInfo) );
        else{
            this->osg::QueryGeometry::drawImplementation( boost::ref(renderInfo) );
        }
    }
    
    void default_drawImplementation( ::osg::RenderInfo & renderInfo ) const  {
        osg::QueryGeometry::drawImplementation( boost::ref(renderInfo) );
    }

    virtual void accept( ::osg::Drawable::AttributeFunctor & af ) {
        if( bp::override func_accept = this->get_override( "accept" ) )
            func_accept( boost::ref(af) );
        else{
            this->osg::Geometry::accept( boost::ref(af) );
        }
    }
    
    void default_accept( ::osg::Drawable::AttributeFunctor & af ) {
        osg::Geometry::accept( boost::ref(af) );
    }

    virtual void accept( ::osg::Drawable::ConstAttributeFunctor & af ) const  {
        if( bp::override func_accept = this->get_override( "accept" ) )
            func_accept( boost::ref(af) );
        else{
            this->osg::Geometry::accept( boost::ref(af) );
        }
    }
    
    void default_accept( ::osg::Drawable::ConstAttributeFunctor & af ) const  {
        osg::Geometry::accept( boost::ref(af) );
    }

    virtual void accept( ::osg::PrimitiveFunctor & pf ) const  {
        if( bp::override func_accept = this->get_override( "accept" ) )
            func_accept( boost::ref(pf) );
        else{
            this->osg::Geometry::accept( boost::ref(pf) );
        }
    }
    
    void default_accept( ::osg::PrimitiveFunctor & pf ) const  {
        osg::Geometry::accept( boost::ref(pf) );
    }

    virtual void accept( ::osg::PrimitiveIndexFunctor & pf ) const  {
        if( bp::override func_accept = this->get_override( "accept" ) )
            func_accept( boost::ref(pf) );
        else{
            this->osg::Geometry::accept( boost::ref(pf) );
        }
    }
    
    void default_accept( ::osg::PrimitiveIndexFunctor & pf ) const  {
        osg::Geometry::accept( boost::ref(pf) );
    }

    virtual ::osg::Geometry * asGeometry(  ) {
        if( bp::override func_asGeometry = this->get_override( "asGeometry" ) )
            return func_asGeometry(  );
        else{
            return this->osg::Geometry::asGeometry(  );
        }
    }
    
    ::osg::Geometry * default_asGeometry(  ) {
        return osg::Geometry::asGeometry( );
    }

    virtual ::osg::Geometry const * asGeometry(  ) const  {
        if( bp::override func_asGeometry = this->get_override( "asGeometry" ) )
            return func_asGeometry(  );
        else{
            return this->osg::Geometry::asGeometry(  );
        }
    }
    
    ::osg::Geometry const * default_asGeometry(  ) const  {
        return osg::Geometry::asGeometry( );
    }

    virtual char const * className(  ) const  {
        if( bp::override func_className = this->get_override( "className" ) )
            return func_className(  );
        else{
            return this->osg::Geometry::className(  );
        }
    }
    
    char const * default_className(  ) const  {
        return osg::Geometry::className( );
    }

    virtual ::osg::Object * clone( ::osg::CopyOp const & copyop ) const  {
        if( bp::override func_clone = this->get_override( "clone" ) )
            return func_clone( boost::ref(copyop) );
        else{
            return this->osg::Geometry::clone( boost::ref(copyop) );
        }
    }
    
    ::osg::Object * default_clone( ::osg::CopyOp const & copyop ) const  {
        return osg::Geometry::clone( boost::ref(copyop) );
    }

    virtual ::osg::Object * cloneType(  ) const  {
        if( bp::override func_cloneType = this->get_override( "cloneType" ) )
            return func_cloneType(  );
        else{
            return this->osg::Geometry::cloneType(  );
        }
    }
    
    ::osg::Object * default_cloneType(  ) const  {
        return osg::Geometry::cloneType( );
    }

    virtual void compileGLObjects( ::osg::RenderInfo & renderInfo ) const  {
        if( bp::override func_compileGLObjects = this->get_override( "compileGLObjects" ) )
            func_compileGLObjects( boost::ref(renderInfo) );
        else{
            this->osg::Geometry::compileGLObjects( boost::ref(renderInfo) );
        }
    }
    
    void default_compileGLObjects( ::osg::RenderInfo & renderInfo ) const  {
        osg::Geometry::compileGLObjects( boost::ref(renderInfo) );
    }

    virtual ::osg::BoundingBox computeBound(  ) const  {
        if( bp::override func_computeBound = this->get_override( "computeBound" ) )
            return func_computeBound(  );
        else{
            return this->osg::Drawable::computeBound(  );
        }
    }
    
    ::osg::BoundingBox default_computeBound(  ) const  {
        return osg::Drawable::computeBound( );
    }

    virtual void computeDataVariance(  ) {
        if( bp::override func_computeDataVariance = this->get_override( "computeDataVariance" ) )
            func_computeDataVariance(  );
        else{
            this->osg::Drawable::computeDataVariance(  );
        }
    }
    
    void default_computeDataVariance(  ) {
        osg::Drawable::computeDataVariance( );
    }

    virtual void dirtyDisplayList(  ) {
        if( bp::override func_dirtyDisplayList = this->get_override( "dirtyDisplayList" ) )
            func_dirtyDisplayList(  );
        else{
            this->osg::Geometry::dirtyDisplayList(  );
        }
    }
    
    void default_dirtyDisplayList(  ) {
        osg::Geometry::dirtyDisplayList( );
    }

    virtual unsigned int getGLObjectSizeHint(  ) const  {
        if( bp::override func_getGLObjectSizeHint = this->get_override( "getGLObjectSizeHint" ) )
            return func_getGLObjectSizeHint(  );
        else{
            return this->osg::Geometry::getGLObjectSizeHint(  );
        }
    }
    
    unsigned int default_getGLObjectSizeHint(  ) const  {
        return osg::Geometry::getGLObjectSizeHint( );
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
            return this->osg::Geometry::isSameKindAs( boost::python::ptr(obj) );
        }
    }
    
    bool default_isSameKindAs( ::osg::Object const * obj ) const  {
        return osg::Geometry::isSameKindAs( boost::python::ptr(obj) );
    }

    virtual char const * libraryName(  ) const  {
        if( bp::override func_libraryName = this->get_override( "libraryName" ) )
            return func_libraryName(  );
        else{
            return this->osg::Geometry::libraryName(  );
        }
    }
    
    char const * default_libraryName(  ) const  {
        return osg::Geometry::libraryName( );
    }

    virtual void resizeGLObjectBuffers( unsigned int maxSize ) {
        if( bp::override func_resizeGLObjectBuffers = this->get_override( "resizeGLObjectBuffers" ) )
            func_resizeGLObjectBuffers( maxSize );
        else{
            this->osg::Geometry::resizeGLObjectBuffers( maxSize );
        }
    }
    
    void default_resizeGLObjectBuffers( unsigned int maxSize ) {
        osg::Geometry::resizeGLObjectBuffers( maxSize );
    }

    virtual void setCullCallback( ::osg::Drawable::CullCallback * cc ) {
        if( bp::override func_setCullCallback = this->get_override( "setCullCallback" ) )
            func_setCullCallback( boost::python::ptr(cc) );
        else{
            this->osg::Drawable::setCullCallback( boost::python::ptr(cc) );
        }
    }
    
    void default_setCullCallback( ::osg::Drawable::CullCallback * cc ) {
        osg::Drawable::setCullCallback( boost::python::ptr(cc) );
    }

    virtual void setDrawCallback( ::osg::Drawable::DrawCallback * dc ) {
        if( bp::override func_setDrawCallback = this->get_override( "setDrawCallback" ) )
            func_setDrawCallback( boost::python::ptr(dc) );
        else{
            this->osg::Drawable::setDrawCallback( boost::python::ptr(dc) );
        }
    }
    
    void default_setDrawCallback( ::osg::Drawable::DrawCallback * dc ) {
        osg::Drawable::setDrawCallback( boost::python::ptr(dc) );
    }

    virtual void setEventCallback( ::osg::Drawable::EventCallback * ac ) {
        if( bp::override func_setEventCallback = this->get_override( "setEventCallback" ) )
            func_setEventCallback( boost::python::ptr(ac) );
        else{
            this->osg::Drawable::setEventCallback( boost::python::ptr(ac) );
        }
    }
    
    void default_setEventCallback( ::osg::Drawable::EventCallback * ac ) {
        osg::Drawable::setEventCallback( boost::python::ptr(ac) );
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
            this->osg::Drawable::setThreadSafeRefUnref( threadSafe );
        }
    }
    
    void default_setThreadSafeRefUnref( bool threadSafe ) {
        osg::Drawable::setThreadSafeRefUnref( threadSafe );
    }

    virtual void setUpdateCallback( ::osg::Drawable::UpdateCallback * ac ) {
        if( bp::override func_setUpdateCallback = this->get_override( "setUpdateCallback" ) )
            func_setUpdateCallback( boost::python::ptr(ac) );
        else{
            this->osg::Drawable::setUpdateCallback( boost::python::ptr(ac) );
        }
    }
    
    void default_setUpdateCallback( ::osg::Drawable::UpdateCallback * ac ) {
        osg::Drawable::setUpdateCallback( boost::python::ptr(ac) );
    }

    virtual void setUseVertexBufferObjects( bool flag ) {
        if( bp::override func_setUseVertexBufferObjects = this->get_override( "setUseVertexBufferObjects" ) )
            func_setUseVertexBufferObjects( flag );
        else{
            this->osg::Geometry::setUseVertexBufferObjects( flag );
        }
    }
    
    void default_setUseVertexBufferObjects( bool flag ) {
        osg::Geometry::setUseVertexBufferObjects( flag );
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

    virtual bool supports( ::osg::Drawable::AttributeFunctor const & arg0 ) const  {
        if( bp::override func_supports = this->get_override( "supports" ) )
            return func_supports( boost::ref(arg0) );
        else{
            return this->osg::Geometry::supports( boost::ref(arg0) );
        }
    }
    
    bool default_supports( ::osg::Drawable::AttributeFunctor const & arg0 ) const  {
        return osg::Geometry::supports( boost::ref(arg0) );
    }

    virtual bool supports( ::osg::Drawable::ConstAttributeFunctor const & arg0 ) const  {
        if( bp::override func_supports = this->get_override( "supports" ) )
            return func_supports( boost::ref(arg0) );
        else{
            return this->osg::Geometry::supports( boost::ref(arg0) );
        }
    }
    
    bool default_supports( ::osg::Drawable::ConstAttributeFunctor const & arg0 ) const  {
        return osg::Geometry::supports( boost::ref(arg0) );
    }

    virtual bool supports( ::osg::PrimitiveFunctor const & arg0 ) const  {
        if( bp::override func_supports = this->get_override( "supports" ) )
            return func_supports( boost::ref(arg0) );
        else{
            return this->osg::Geometry::supports( boost::ref(arg0) );
        }
    }
    
    bool default_supports( ::osg::PrimitiveFunctor const & arg0 ) const  {
        return osg::Geometry::supports( boost::ref(arg0) );
    }

    virtual bool supports( ::osg::PrimitiveIndexFunctor const & arg0 ) const  {
        if( bp::override func_supports = this->get_override( "supports" ) )
            return func_supports( boost::ref(arg0) );
        else{
            return this->osg::Geometry::supports( boost::ref(arg0) );
        }
    }
    
    bool default_supports( ::osg::PrimitiveIndexFunctor const & arg0 ) const  {
        return osg::Geometry::supports( boost::ref(arg0) );
    }

};

void register_QueryGeometry_class(){

    { //::osg::QueryGeometry
        typedef bp::class_< QueryGeometry_wrapper, bp::bases< osg::Geometry >, osg::ref_ptr< ::osg::QueryGeometry >, boost::noncopyable > QueryGeometry_exposer_t;
        QueryGeometry_exposer_t QueryGeometry_exposer = QueryGeometry_exposer_t( "QueryGeometry", bp::init< bp::optional< std::string const & > >(( bp::arg("oqnName")=std::basic_string<char, std::char_traits<char>, std::allocator<char> >(((const char*)"")) )) );
        bp::scope QueryGeometry_scope( QueryGeometry_exposer );
        bp::implicitly_convertible< std::string const &, osg::QueryGeometry >();
        { //::osg::QueryGeometry::deleteQueryObject
        
            typedef void ( *deleteQueryObject_function_type )( unsigned int,::GLuint );
            
            QueryGeometry_exposer.def( 
                "deleteQueryObject"
                , deleteQueryObject_function_type( &::osg::QueryGeometry::deleteQueryObject )
                , ( bp::arg("contextID"), bp::arg("handle") ) );
        
        }
        { //::osg::QueryGeometry::discardDeletedQueryObjects
        
            typedef void ( *discardDeletedQueryObjects_function_type )( unsigned int );
            
            QueryGeometry_exposer.def( 
                "discardDeletedQueryObjects"
                , discardDeletedQueryObjects_function_type( &::osg::QueryGeometry::discardDeletedQueryObjects )
                , ( bp::arg("contextID") ) );
        
        }
        { //::osg::QueryGeometry::drawImplementation
        
            typedef void ( ::osg::QueryGeometry::*drawImplementation_function_type)( ::osg::RenderInfo & ) const;
            typedef void ( QueryGeometry_wrapper::*default_drawImplementation_function_type)( ::osg::RenderInfo & ) const;
            
            QueryGeometry_exposer.def( 
                "drawImplementation"
                , drawImplementation_function_type(&::osg::QueryGeometry::drawImplementation)
                , default_drawImplementation_function_type(&QueryGeometry_wrapper::default_drawImplementation)
                , ( bp::arg("renderInfo") ) );
        
        }
        { //::osg::QueryGeometry::flushDeletedQueryObjects
        
            typedef void ( *flushDeletedQueryObjects_function_type )( unsigned int,double,double & );
            
            QueryGeometry_exposer.def( 
                "flushDeletedQueryObjects"
                , flushDeletedQueryObjects_function_type( &::osg::QueryGeometry::flushDeletedQueryObjects )
                , ( bp::arg("contextID"), bp::arg("currentTime"), bp::arg("availableTime") ) );
        
        }
        { //::osg::QueryGeometry::getNumPixels
        
            typedef unsigned int ( ::osg::QueryGeometry::*getNumPixels_function_type)( ::osg::Camera const * ) ;
            
            QueryGeometry_exposer.def( 
                "getNumPixels"
                , getNumPixels_function_type( &::osg::QueryGeometry::getNumPixels )
                , ( bp::arg("cam") ) );
        
        }
        { //::osg::QueryGeometry::reset
        
            typedef void ( ::osg::QueryGeometry::*reset_function_type)(  ) ;
            
            QueryGeometry_exposer.def( 
                "reset"
                , reset_function_type( &::osg::QueryGeometry::reset ) );
        
        }
        { //::osg::Geometry::accept
        
            typedef void ( ::osg::Geometry::*accept_function_type)( ::osg::Drawable::AttributeFunctor & ) ;
            typedef void ( QueryGeometry_wrapper::*default_accept_function_type)( ::osg::Drawable::AttributeFunctor & ) ;
            
            QueryGeometry_exposer.def( 
                "accept"
                , accept_function_type(&::osg::Geometry::accept)
                , default_accept_function_type(&QueryGeometry_wrapper::default_accept)
                , ( bp::arg("af") ) );
        
        }
        { //::osg::Geometry::accept
        
            typedef void ( ::osg::Geometry::*accept_function_type)( ::osg::Drawable::ConstAttributeFunctor & ) const;
            typedef void ( QueryGeometry_wrapper::*default_accept_function_type)( ::osg::Drawable::ConstAttributeFunctor & ) const;
            
            QueryGeometry_exposer.def( 
                "accept"
                , accept_function_type(&::osg::Geometry::accept)
                , default_accept_function_type(&QueryGeometry_wrapper::default_accept)
                , ( bp::arg("af") ) );
        
        }
        { //::osg::Geometry::accept
        
            typedef void ( ::osg::Geometry::*accept_function_type)( ::osg::PrimitiveFunctor & ) const;
            typedef void ( QueryGeometry_wrapper::*default_accept_function_type)( ::osg::PrimitiveFunctor & ) const;
            
            QueryGeometry_exposer.def( 
                "accept"
                , accept_function_type(&::osg::Geometry::accept)
                , default_accept_function_type(&QueryGeometry_wrapper::default_accept)
                , ( bp::arg("pf") ) );
        
        }
        { //::osg::Geometry::accept
        
            typedef void ( ::osg::Geometry::*accept_function_type)( ::osg::PrimitiveIndexFunctor & ) const;
            typedef void ( QueryGeometry_wrapper::*default_accept_function_type)( ::osg::PrimitiveIndexFunctor & ) const;
            
            QueryGeometry_exposer.def( 
                "accept"
                , accept_function_type(&::osg::Geometry::accept)
                , default_accept_function_type(&QueryGeometry_wrapper::default_accept)
                , ( bp::arg("pf") ) );
        
        }
        { //::osg::Geometry::asGeometry
        
            typedef ::osg::Geometry * ( ::osg::Geometry::*asGeometry_function_type)(  ) ;
            typedef ::osg::Geometry * ( QueryGeometry_wrapper::*default_asGeometry_function_type)(  ) ;
            
            QueryGeometry_exposer.def( 
                "asGeometry"
                , asGeometry_function_type(&::osg::Geometry::asGeometry)
                , default_asGeometry_function_type(&QueryGeometry_wrapper::default_asGeometry)
                , bp::return_internal_reference< >() );
        
        }
        { //::osg::Geometry::asGeometry
        
            typedef ::osg::Geometry const * ( ::osg::Geometry::*asGeometry_function_type)(  ) const;
            typedef ::osg::Geometry const * ( QueryGeometry_wrapper::*default_asGeometry_function_type)(  ) const;
            
            QueryGeometry_exposer.def( 
                "asGeometry"
                , asGeometry_function_type(&::osg::Geometry::asGeometry)
                , default_asGeometry_function_type(&QueryGeometry_wrapper::default_asGeometry)
                , bp::return_internal_reference< >() );
        
        }
        { //::osg::Geometry::className
        
            typedef char const * ( ::osg::Geometry::*className_function_type)(  ) const;
            typedef char const * ( QueryGeometry_wrapper::*default_className_function_type)(  ) const;
            
            QueryGeometry_exposer.def( 
                "className"
                , className_function_type(&::osg::Geometry::className)
                , default_className_function_type(&QueryGeometry_wrapper::default_className) );
        
        }
        { //::osg::Geometry::clone
        
            typedef ::osg::Object * ( ::osg::Geometry::*clone_function_type)( ::osg::CopyOp const & ) const;
            typedef ::osg::Object * ( QueryGeometry_wrapper::*default_clone_function_type)( ::osg::CopyOp const & ) const;
            
            QueryGeometry_exposer.def( 
                "clone"
                , clone_function_type(&::osg::Geometry::clone)
                , default_clone_function_type(&QueryGeometry_wrapper::default_clone)
                , ( bp::arg("copyop") )
                , bp::return_value_policy< bp::reference_existing_object >() );
        
        }
        { //::osg::Geometry::cloneType
        
            typedef ::osg::Object * ( ::osg::Geometry::*cloneType_function_type)(  ) const;
            typedef ::osg::Object * ( QueryGeometry_wrapper::*default_cloneType_function_type)(  ) const;
            
            QueryGeometry_exposer.def( 
                "cloneType"
                , cloneType_function_type(&::osg::Geometry::cloneType)
                , default_cloneType_function_type(&QueryGeometry_wrapper::default_cloneType)
                , bp::return_value_policy< bp::reference_existing_object >() );
        
        }
        { //::osg::Geometry::compileGLObjects
        
            typedef void ( ::osg::Geometry::*compileGLObjects_function_type)( ::osg::RenderInfo & ) const;
            typedef void ( QueryGeometry_wrapper::*default_compileGLObjects_function_type)( ::osg::RenderInfo & ) const;
            
            QueryGeometry_exposer.def( 
                "compileGLObjects"
                , compileGLObjects_function_type(&::osg::Geometry::compileGLObjects)
                , default_compileGLObjects_function_type(&QueryGeometry_wrapper::default_compileGLObjects)
                , ( bp::arg("renderInfo") ) );
        
        }
        { //::osg::Drawable::computeBound
        
            typedef ::osg::BoundingBox ( ::osg::Drawable::*computeBound_function_type)(  ) const;
            typedef ::osg::BoundingBox ( QueryGeometry_wrapper::*default_computeBound_function_type)(  ) const;
            
            QueryGeometry_exposer.def( 
                "computeBound"
                , computeBound_function_type(&::osg::Drawable::computeBound)
                , default_computeBound_function_type(&QueryGeometry_wrapper::default_computeBound) );
        
        }
        { //::osg::Drawable::computeDataVariance
        
            typedef void ( ::osg::Drawable::*computeDataVariance_function_type)(  ) ;
            typedef void ( QueryGeometry_wrapper::*default_computeDataVariance_function_type)(  ) ;
            
            QueryGeometry_exposer.def( 
                "computeDataVariance"
                , computeDataVariance_function_type(&::osg::Drawable::computeDataVariance)
                , default_computeDataVariance_function_type(&QueryGeometry_wrapper::default_computeDataVariance) );
        
        }
        { //::osg::Geometry::dirtyDisplayList
        
            typedef void ( ::osg::Geometry::*dirtyDisplayList_function_type)(  ) ;
            typedef void ( QueryGeometry_wrapper::*default_dirtyDisplayList_function_type)(  ) ;
            
            QueryGeometry_exposer.def( 
                "dirtyDisplayList"
                , dirtyDisplayList_function_type(&::osg::Geometry::dirtyDisplayList)
                , default_dirtyDisplayList_function_type(&QueryGeometry_wrapper::default_dirtyDisplayList) );
        
        }
        { //::osg::Geometry::getGLObjectSizeHint
        
            typedef unsigned int ( ::osg::Geometry::*getGLObjectSizeHint_function_type)(  ) const;
            typedef unsigned int ( QueryGeometry_wrapper::*default_getGLObjectSizeHint_function_type)(  ) const;
            
            QueryGeometry_exposer.def( 
                "getGLObjectSizeHint"
                , getGLObjectSizeHint_function_type(&::osg::Geometry::getGLObjectSizeHint)
                , default_getGLObjectSizeHint_function_type(&QueryGeometry_wrapper::default_getGLObjectSizeHint) );
        
        }
        { //::osg::Object::getUserData
        
            typedef ::osg::Referenced * ( ::osg::Object::*getUserData_function_type)(  ) ;
            typedef ::osg::Referenced * ( QueryGeometry_wrapper::*default_getUserData_function_type)(  ) ;
            
            QueryGeometry_exposer.def( 
                "getUserData"
                , getUserData_function_type(&::osg::Object::getUserData)
                , default_getUserData_function_type(&QueryGeometry_wrapper::default_getUserData)
                , bp::return_internal_reference< >() );
        
        }
        { //::osg::Object::getUserData
        
            typedef ::osg::Referenced const * ( ::osg::Object::*getUserData_function_type)(  ) const;
            typedef ::osg::Referenced const * ( QueryGeometry_wrapper::*default_getUserData_function_type)(  ) const;
            
            QueryGeometry_exposer.def( 
                "getUserData"
                , getUserData_function_type(&::osg::Object::getUserData)
                , default_getUserData_function_type(&QueryGeometry_wrapper::default_getUserData)
                , bp::return_internal_reference< >() );
        
        }
        { //::osg::Geometry::isSameKindAs
        
            typedef bool ( ::osg::Geometry::*isSameKindAs_function_type)( ::osg::Object const * ) const;
            typedef bool ( QueryGeometry_wrapper::*default_isSameKindAs_function_type)( ::osg::Object const * ) const;
            
            QueryGeometry_exposer.def( 
                "isSameKindAs"
                , isSameKindAs_function_type(&::osg::Geometry::isSameKindAs)
                , default_isSameKindAs_function_type(&QueryGeometry_wrapper::default_isSameKindAs)
                , ( bp::arg("obj") ) );
        
        }
        { //::osg::Geometry::libraryName
        
            typedef char const * ( ::osg::Geometry::*libraryName_function_type)(  ) const;
            typedef char const * ( QueryGeometry_wrapper::*default_libraryName_function_type)(  ) const;
            
            QueryGeometry_exposer.def( 
                "libraryName"
                , libraryName_function_type(&::osg::Geometry::libraryName)
                , default_libraryName_function_type(&QueryGeometry_wrapper::default_libraryName) );
        
        }
        { //::osg::Geometry::resizeGLObjectBuffers
        
            typedef void ( ::osg::Geometry::*resizeGLObjectBuffers_function_type)( unsigned int ) ;
            typedef void ( QueryGeometry_wrapper::*default_resizeGLObjectBuffers_function_type)( unsigned int ) ;
            
            QueryGeometry_exposer.def( 
                "resizeGLObjectBuffers"
                , resizeGLObjectBuffers_function_type(&::osg::Geometry::resizeGLObjectBuffers)
                , default_resizeGLObjectBuffers_function_type(&QueryGeometry_wrapper::default_resizeGLObjectBuffers)
                , ( bp::arg("maxSize") ) );
        
        }
        { //::osg::Drawable::setCullCallback
        
            typedef void ( ::osg::Drawable::*setCullCallback_function_type)( ::osg::Drawable::CullCallback * ) ;
            typedef void ( QueryGeometry_wrapper::*default_setCullCallback_function_type)( ::osg::Drawable::CullCallback * ) ;
            
            QueryGeometry_exposer.def( 
                "setCullCallback"
                , setCullCallback_function_type(&::osg::Drawable::setCullCallback)
                , default_setCullCallback_function_type(&QueryGeometry_wrapper::default_setCullCallback)
                , ( bp::arg("cc") ) );
        
        }
        { //::osg::Drawable::setDrawCallback
        
            typedef void ( ::osg::Drawable::*setDrawCallback_function_type)( ::osg::Drawable::DrawCallback * ) ;
            typedef void ( QueryGeometry_wrapper::*default_setDrawCallback_function_type)( ::osg::Drawable::DrawCallback * ) ;
            
            QueryGeometry_exposer.def( 
                "setDrawCallback"
                , setDrawCallback_function_type(&::osg::Drawable::setDrawCallback)
                , default_setDrawCallback_function_type(&QueryGeometry_wrapper::default_setDrawCallback)
                , ( bp::arg("dc") ) );
        
        }
        { //::osg::Drawable::setEventCallback
        
            typedef void ( ::osg::Drawable::*setEventCallback_function_type)( ::osg::Drawable::EventCallback * ) ;
            typedef void ( QueryGeometry_wrapper::*default_setEventCallback_function_type)( ::osg::Drawable::EventCallback * ) ;
            
            QueryGeometry_exposer.def( 
                "setEventCallback"
                , setEventCallback_function_type(&::osg::Drawable::setEventCallback)
                , default_setEventCallback_function_type(&QueryGeometry_wrapper::default_setEventCallback)
                , ( bp::arg("ac") ) );
        
        }
        { //::osg::Object::setName
        
            typedef void ( ::osg::Object::*setName_function_type)( ::std::string const & ) ;
            typedef void ( QueryGeometry_wrapper::*default_setName_function_type)( ::std::string const & ) ;
            
            QueryGeometry_exposer.def( 
                "setName"
                , setName_function_type(&::osg::Object::setName)
                , default_setName_function_type(&QueryGeometry_wrapper::default_setName)
                , ( bp::arg("name") ) );
        
        }
        { //::osg::Object::setName
        
            typedef void ( ::osg::Object::*setName_function_type)( char const * ) ;
            
            QueryGeometry_exposer.def( 
                "setName"
                , setName_function_type( &::osg::Object::setName )
                , ( bp::arg("name") )
                , " Set the name of object using a C style string." );
        
        }
        { //::osg::Drawable::setThreadSafeRefUnref
        
            typedef void ( ::osg::Drawable::*setThreadSafeRefUnref_function_type)( bool ) ;
            typedef void ( QueryGeometry_wrapper::*default_setThreadSafeRefUnref_function_type)( bool ) ;
            
            QueryGeometry_exposer.def( 
                "setThreadSafeRefUnref"
                , setThreadSafeRefUnref_function_type(&::osg::Drawable::setThreadSafeRefUnref)
                , default_setThreadSafeRefUnref_function_type(&QueryGeometry_wrapper::default_setThreadSafeRefUnref)
                , ( bp::arg("threadSafe") ) );
        
        }
        { //::osg::Drawable::setUpdateCallback
        
            typedef void ( ::osg::Drawable::*setUpdateCallback_function_type)( ::osg::Drawable::UpdateCallback * ) ;
            typedef void ( QueryGeometry_wrapper::*default_setUpdateCallback_function_type)( ::osg::Drawable::UpdateCallback * ) ;
            
            QueryGeometry_exposer.def( 
                "setUpdateCallback"
                , setUpdateCallback_function_type(&::osg::Drawable::setUpdateCallback)
                , default_setUpdateCallback_function_type(&QueryGeometry_wrapper::default_setUpdateCallback)
                , ( bp::arg("ac") ) );
        
        }
        { //::osg::Geometry::setUseVertexBufferObjects
        
            typedef void ( ::osg::Geometry::*setUseVertexBufferObjects_function_type)( bool ) ;
            typedef void ( QueryGeometry_wrapper::*default_setUseVertexBufferObjects_function_type)( bool ) ;
            
            QueryGeometry_exposer.def( 
                "setUseVertexBufferObjects"
                , setUseVertexBufferObjects_function_type(&::osg::Geometry::setUseVertexBufferObjects)
                , default_setUseVertexBufferObjects_function_type(&QueryGeometry_wrapper::default_setUseVertexBufferObjects)
                , ( bp::arg("flag") ) );
        
        }
        { //::osg::Object::setUserData
        
            typedef void ( ::osg::Object::*setUserData_function_type)( ::osg::Referenced * ) ;
            typedef void ( QueryGeometry_wrapper::*default_setUserData_function_type)( ::osg::Referenced * ) ;
            
            QueryGeometry_exposer.def( 
                "setUserData"
                , setUserData_function_type(&::osg::Object::setUserData)
                , default_setUserData_function_type(&QueryGeometry_wrapper::default_setUserData)
                , ( bp::arg("obj") ) );
        
        }
        { //::osg::Geometry::supports
        
            typedef bool ( ::osg::Geometry::*supports_function_type)( ::osg::Drawable::AttributeFunctor const & ) const;
            typedef bool ( QueryGeometry_wrapper::*default_supports_function_type)( ::osg::Drawable::AttributeFunctor const & ) const;
            
            QueryGeometry_exposer.def( 
                "supports"
                , supports_function_type(&::osg::Geometry::supports)
                , default_supports_function_type(&QueryGeometry_wrapper::default_supports)
                , ( bp::arg("arg0") ) );
        
        }
        { //::osg::Geometry::supports
        
            typedef bool ( ::osg::Geometry::*supports_function_type)( ::osg::Drawable::ConstAttributeFunctor const & ) const;
            typedef bool ( QueryGeometry_wrapper::*default_supports_function_type)( ::osg::Drawable::ConstAttributeFunctor const & ) const;
            
            QueryGeometry_exposer.def( 
                "supports"
                , supports_function_type(&::osg::Geometry::supports)
                , default_supports_function_type(&QueryGeometry_wrapper::default_supports)
                , ( bp::arg("arg0") ) );
        
        }
        { //::osg::Geometry::supports
        
            typedef bool ( ::osg::Geometry::*supports_function_type)( ::osg::PrimitiveFunctor const & ) const;
            typedef bool ( QueryGeometry_wrapper::*default_supports_function_type)( ::osg::PrimitiveFunctor const & ) const;
            
            QueryGeometry_exposer.def( 
                "supports"
                , supports_function_type(&::osg::Geometry::supports)
                , default_supports_function_type(&QueryGeometry_wrapper::default_supports)
                , ( bp::arg("arg0") ) );
        
        }
        { //::osg::Geometry::supports
        
            typedef bool ( ::osg::Geometry::*supports_function_type)( ::osg::PrimitiveIndexFunctor const & ) const;
            typedef bool ( QueryGeometry_wrapper::*default_supports_function_type)( ::osg::PrimitiveIndexFunctor const & ) const;
            
            QueryGeometry_exposer.def( 
                "supports"
                , supports_function_type(&::osg::Geometry::supports)
                , default_supports_function_type(&QueryGeometry_wrapper::default_supports)
                , ( bp::arg("arg0") ) );
        
        }
        QueryGeometry_exposer.staticmethod( "deleteQueryObject" );
        QueryGeometry_exposer.staticmethod( "discardDeletedQueryObjects" );
        QueryGeometry_exposer.staticmethod( "flushDeletedQueryObjects" );
    }

}
