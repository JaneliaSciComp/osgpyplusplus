// This file has been generated by Py++.

#include "boost/python.hpp"
#include "wrap_osg.h"
#include "wrap_referenced.h"
#include "indexing_helpers.h"
#include "drawelementsushort.pypp.hpp"

namespace bp = boost::python;

struct DrawElementsUShort_wrapper : osg::DrawElementsUShort, bp::wrapper< osg::DrawElementsUShort > {

    DrawElementsUShort_wrapper(::GLenum mode=0 )
    : osg::DrawElementsUShort( mode )
      , bp::wrapper< osg::DrawElementsUShort >(){
        // constructor
    
    }

    DrawElementsUShort_wrapper(::GLenum mode, unsigned int no, ::GLushort const * ptr, int numInstances=0 )
    : osg::DrawElementsUShort( mode, no, ptr, numInstances )
      , bp::wrapper< osg::DrawElementsUShort >(){
        // constructor
    
    }

    DrawElementsUShort_wrapper(::GLenum mode, unsigned int no )
    : osg::DrawElementsUShort( mode, no )
      , bp::wrapper< osg::DrawElementsUShort >(){
        // constructor
    
    }

    virtual void accept( ::osg::PrimitiveFunctor & functor ) const  {
        if( bp::override func_accept = this->get_override( "accept" ) )
            func_accept( boost::ref(functor) );
        else{
            this->osg::DrawElementsUShort::accept( boost::ref(functor) );
        }
    }
    
    void default_accept( ::osg::PrimitiveFunctor & functor ) const  {
        osg::DrawElementsUShort::accept( boost::ref(functor) );
    }

    virtual void accept( ::osg::PrimitiveIndexFunctor & functor ) const  {
        if( bp::override func_accept = this->get_override( "accept" ) )
            func_accept( boost::ref(functor) );
        else{
            this->osg::DrawElementsUShort::accept( boost::ref(functor) );
        }
    }
    
    void default_accept( ::osg::PrimitiveIndexFunctor & functor ) const  {
        osg::DrawElementsUShort::accept( boost::ref(functor) );
    }

    virtual void addElement( unsigned int v ) {
        if( bp::override func_addElement = this->get_override( "addElement" ) )
            func_addElement( v );
        else{
            this->osg::DrawElementsUShort::addElement( v );
        }
    }
    
    void default_addElement( unsigned int v ) {
        osg::DrawElementsUShort::addElement( v );
    }

    virtual char const * className(  ) const  {
        if( bp::override func_className = this->get_override( "className" ) )
            return func_className(  );
        else{
            return this->osg::DrawElementsUShort::className(  );
        }
    }
    
    char const * default_className(  ) const  {
        return osg::DrawElementsUShort::className( );
    }

    virtual ::osg::Object * clone( ::osg::CopyOp const & copyop ) const  {
        if( bp::override func_clone = this->get_override( "clone" ) )
            return func_clone( boost::ref(copyop) );
        else{
            return this->osg::DrawElementsUShort::clone( boost::ref(copyop) );
        }
    }
    
    ::osg::Object * default_clone( ::osg::CopyOp const & copyop ) const  {
        return osg::DrawElementsUShort::clone( boost::ref(copyop) );
    }

    virtual ::osg::Object * cloneType(  ) const  {
        if( bp::override func_cloneType = this->get_override( "cloneType" ) )
            return func_cloneType(  );
        else{
            return this->osg::DrawElementsUShort::cloneType(  );
        }
    }
    
    ::osg::Object * default_cloneType(  ) const  {
        return osg::DrawElementsUShort::cloneType( );
    }

    virtual void draw( ::osg::State & state, bool useVertexBufferObjects ) const  {
        if( bp::override func_draw = this->get_override( "draw" ) )
            func_draw( boost::ref(state), useVertexBufferObjects );
        else{
            this->osg::DrawElementsUShort::draw( boost::ref(state), useVertexBufferObjects );
        }
    }
    
    void default_draw( ::osg::State & state, bool useVertexBufferObjects ) const  {
        osg::DrawElementsUShort::draw( boost::ref(state), useVertexBufferObjects );
    }

    virtual ::GLvoid const * getDataPointer(  ) const  {
        if( bp::override func_getDataPointer = this->get_override( "getDataPointer" ) )
            return func_getDataPointer(  );
        else{
            return this->osg::DrawElementsUShort::getDataPointer(  );
        }
    }
    
    ::GLvoid const * default_getDataPointer(  ) const  {
        return osg::DrawElementsUShort::getDataPointer( );
    }

    virtual unsigned int getElement( unsigned int i ) {
        if( bp::override func_getElement = this->get_override( "getElement" ) )
            return func_getElement( i );
        else{
            return this->osg::DrawElementsUShort::getElement( i );
        }
    }
    
    unsigned int default_getElement( unsigned int i ) {
        return osg::DrawElementsUShort::getElement( i );
    }

    virtual unsigned int getNumIndices(  ) const  {
        if( bp::override func_getNumIndices = this->get_override( "getNumIndices" ) )
            return func_getNumIndices(  );
        else{
            return this->osg::DrawElementsUShort::getNumIndices(  );
        }
    }
    
    unsigned int default_getNumIndices(  ) const  {
        return osg::DrawElementsUShort::getNumIndices( );
    }

    virtual unsigned int getTotalDataSize(  ) const  {
        if( bp::override func_getTotalDataSize = this->get_override( "getTotalDataSize" ) )
            return func_getTotalDataSize(  );
        else{
            return this->osg::DrawElementsUShort::getTotalDataSize(  );
        }
    }
    
    unsigned int default_getTotalDataSize(  ) const  {
        return osg::DrawElementsUShort::getTotalDataSize( );
    }

    virtual unsigned int index( unsigned int pos ) const  {
        if( bp::override func_index = this->get_override( "index" ) )
            return func_index( pos );
        else{
            return this->osg::DrawElementsUShort::index( pos );
        }
    }
    
    unsigned int default_index( unsigned int pos ) const  {
        return osg::DrawElementsUShort::index( pos );
    }

    virtual bool isSameKindAs( ::osg::Object const * obj ) const  {
        if( bp::override func_isSameKindAs = this->get_override( "isSameKindAs" ) )
            return func_isSameKindAs( boost::python::ptr(obj) );
        else{
            return this->osg::DrawElementsUShort::isSameKindAs( boost::python::ptr(obj) );
        }
    }
    
    bool default_isSameKindAs( ::osg::Object const * obj ) const  {
        return osg::DrawElementsUShort::isSameKindAs( boost::python::ptr(obj) );
    }

    virtual char const * libraryName(  ) const  {
        if( bp::override func_libraryName = this->get_override( "libraryName" ) )
            return func_libraryName(  );
        else{
            return this->osg::DrawElementsUShort::libraryName(  );
        }
    }
    
    char const * default_libraryName(  ) const  {
        return osg::DrawElementsUShort::libraryName( );
    }

    virtual void offsetIndices( int offset ) {
        if( bp::override func_offsetIndices = this->get_override( "offsetIndices" ) )
            func_offsetIndices( offset );
        else{
            this->osg::DrawElementsUShort::offsetIndices( offset );
        }
    }
    
    void default_offsetIndices( int offset ) {
        osg::DrawElementsUShort::offsetIndices( offset );
    }

    virtual void reserveElements( unsigned int numIndices ) {
        if( bp::override func_reserveElements = this->get_override( "reserveElements" ) )
            func_reserveElements( numIndices );
        else{
            this->osg::DrawElementsUShort::reserveElements( numIndices );
        }
    }
    
    void default_reserveElements( unsigned int numIndices ) {
        osg::DrawElementsUShort::reserveElements( numIndices );
    }

    virtual void setElement( unsigned int i, unsigned int v ) {
        if( bp::override func_setElement = this->get_override( "setElement" ) )
            func_setElement( i, v );
        else{
            this->osg::DrawElementsUShort::setElement( i, v );
        }
    }
    
    void default_setElement( unsigned int i, unsigned int v ) {
        osg::DrawElementsUShort::setElement( i, v );
    }

    virtual bool supportsBufferObject(  ) const  {
        if( bp::override func_supportsBufferObject = this->get_override( "supportsBufferObject" ) )
            return func_supportsBufferObject(  );
        else{
            return this->osg::DrawElementsUShort::supportsBufferObject(  );
        }
    }
    
    bool default_supportsBufferObject(  ) const  {
        return osg::DrawElementsUShort::supportsBufferObject( );
    }

    virtual ::osg::Array * asArray(  ) {
        if( bp::override func_asArray = this->get_override( "asArray" ) )
            return func_asArray(  );
        else{
            return this->osg::BufferData::asArray(  );
        }
    }
    
    ::osg::Array * default_asArray(  ) {
        return osg::BufferData::asArray( );
    }

    virtual ::osg::Array const * asArray(  ) const  {
        if( bp::override func_asArray = this->get_override( "asArray" ) )
            return func_asArray(  );
        else{
            return this->osg::BufferData::asArray(  );
        }
    }
    
    ::osg::Array const * default_asArray(  ) const  {
        return osg::BufferData::asArray( );
    }

    virtual ::osg::PrimitiveSet * asPrimitiveSet(  ) {
        if( bp::override func_asPrimitiveSet = this->get_override( "asPrimitiveSet" ) )
            return func_asPrimitiveSet(  );
        else{
            return this->osg::PrimitiveSet::asPrimitiveSet(  );
        }
    }
    
    ::osg::PrimitiveSet * default_asPrimitiveSet(  ) {
        return osg::PrimitiveSet::asPrimitiveSet( );
    }

    virtual ::osg::PrimitiveSet const * asPrimitiveSet(  ) const  {
        if( bp::override func_asPrimitiveSet = this->get_override( "asPrimitiveSet" ) )
            return func_asPrimitiveSet(  );
        else{
            return this->osg::PrimitiveSet::asPrimitiveSet(  );
        }
    }
    
    ::osg::PrimitiveSet const * default_asPrimitiveSet(  ) const  {
        return osg::PrimitiveSet::asPrimitiveSet( );
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

    virtual void computeRange(  ) const  {
        if( bp::override func_computeRange = this->get_override( "computeRange" ) )
            func_computeRange(  );
        else{
            this->osg::PrimitiveSet::computeRange(  );
        }
    }
    
    void default_computeRange(  ) const  {
        osg::PrimitiveSet::computeRange( );
    }

    virtual ::osg::DrawElements * getDrawElements(  ) {
        if( bp::override func_getDrawElements = this->get_override( "getDrawElements" ) )
            return func_getDrawElements(  );
        else{
            return this->osg::DrawElements::getDrawElements(  );
        }
    }
    
    ::osg::DrawElements * default_getDrawElements(  ) {
        return osg::DrawElements::getDrawElements( );
    }

    virtual ::osg::DrawElements const * getDrawElements(  ) const  {
        if( bp::override func_getDrawElements = this->get_override( "getDrawElements" ) )
            return func_getDrawElements(  );
        else{
            return this->osg::DrawElements::getDrawElements(  );
        }
    }
    
    ::osg::DrawElements const * default_getDrawElements(  ) const  {
        return osg::DrawElements::getDrawElements( );
    }

    virtual unsigned int getNumPrimitives(  ) const  {
        if( bp::override func_getNumPrimitives = this->get_override( "getNumPrimitives" ) )
            return func_getNumPrimitives(  );
        else{
            return this->osg::PrimitiveSet::getNumPrimitives(  );
        }
    }
    
    unsigned int default_getNumPrimitives(  ) const  {
        return osg::PrimitiveSet::getNumPrimitives( );
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

    virtual void resizeGLObjectBuffers( unsigned int maxSize ) {
        if( bp::override func_resizeGLObjectBuffers = this->get_override( "resizeGLObjectBuffers" ) )
            func_resizeGLObjectBuffers( maxSize );
        else{
            this->osg::BufferData::resizeGLObjectBuffers( maxSize );
        }
    }
    
    void default_resizeGLObjectBuffers( unsigned int maxSize ) {
        osg::BufferData::resizeGLObjectBuffers( maxSize );
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

void register_DrawElementsUShort_class(){

    { //::osg::DrawElementsUShort
        typedef bp::class_< DrawElementsUShort_wrapper, bp::bases< osg::DrawElements >, osg::ref_ptr< ::osg::DrawElementsUShort >, boost::noncopyable > DrawElementsUShort_exposer_t;
        DrawElementsUShort_exposer_t DrawElementsUShort_exposer = DrawElementsUShort_exposer_t( "DrawElementsUShort", bp::no_init );
        bp::scope DrawElementsUShort_scope( DrawElementsUShort_exposer );
        DrawElementsUShort_exposer.def( bp::init< bp::optional< GLenum > >(( bp::arg("mode")=(::GLenum)(0) )) );
        bp::implicitly_convertible< GLenum, osg::DrawElementsUShort >();
        DrawElementsUShort_exposer.def( bp::init< GLenum, unsigned int, GLushort const *, bp::optional< int > >(( bp::arg("mode"), bp::arg("no"), bp::arg("ptr"), bp::arg("numInstances")=(int)(0) ), "\n @param no: Number of intended elements. This will be the size of the underlying vector.\n") );
        DrawElementsUShort_exposer.def( bp::init< GLenum, unsigned int >(( bp::arg("mode"), bp::arg("no") ), "\n @param no: Number of intended elements. This will be the size of the underlying vector.\n") );
        { //::osg::DrawElementsUShort::accept
        
            typedef void ( ::osg::DrawElementsUShort::*accept_function_type)( ::osg::PrimitiveFunctor & ) const;
            typedef void ( DrawElementsUShort_wrapper::*default_accept_function_type)( ::osg::PrimitiveFunctor & ) const;
            
            DrawElementsUShort_exposer.def( 
                "accept"
                , accept_function_type(&::osg::DrawElementsUShort::accept)
                , default_accept_function_type(&DrawElementsUShort_wrapper::default_accept)
                , ( bp::arg("functor") ) );
        
        }
        { //::osg::DrawElementsUShort::accept
        
            typedef void ( ::osg::DrawElementsUShort::*accept_function_type)( ::osg::PrimitiveIndexFunctor & ) const;
            typedef void ( DrawElementsUShort_wrapper::*default_accept_function_type)( ::osg::PrimitiveIndexFunctor & ) const;
            
            DrawElementsUShort_exposer.def( 
                "accept"
                , accept_function_type(&::osg::DrawElementsUShort::accept)
                , default_accept_function_type(&DrawElementsUShort_wrapper::default_accept)
                , ( bp::arg("functor") ) );
        
        }
        { //::osg::DrawElementsUShort::addElement
        
            typedef void ( ::osg::DrawElementsUShort::*addElement_function_type)( unsigned int ) ;
            typedef void ( DrawElementsUShort_wrapper::*default_addElement_function_type)( unsigned int ) ;
            
            DrawElementsUShort_exposer.def( 
                "addElement"
                , addElement_function_type(&::osg::DrawElementsUShort::addElement)
                , default_addElement_function_type(&DrawElementsUShort_wrapper::default_addElement)
                , ( bp::arg("v") ) );
        
        }
        { //::osg::DrawElementsUShort::className
        
            typedef char const * ( ::osg::DrawElementsUShort::*className_function_type)(  ) const;
            typedef char const * ( DrawElementsUShort_wrapper::*default_className_function_type)(  ) const;
            
            DrawElementsUShort_exposer.def( 
                "className"
                , className_function_type(&::osg::DrawElementsUShort::className)
                , default_className_function_type(&DrawElementsUShort_wrapper::default_className) );
        
        }
        { //::osg::DrawElementsUShort::clone
        
            typedef ::osg::Object * ( ::osg::DrawElementsUShort::*clone_function_type)( ::osg::CopyOp const & ) const;
            typedef ::osg::Object * ( DrawElementsUShort_wrapper::*default_clone_function_type)( ::osg::CopyOp const & ) const;
            
            DrawElementsUShort_exposer.def( 
                "clone"
                , clone_function_type(&::osg::DrawElementsUShort::clone)
                , default_clone_function_type(&DrawElementsUShort_wrapper::default_clone)
                , ( bp::arg("copyop") )
                , bp::return_value_policy< bp::reference_existing_object >() );
        
        }
        { //::osg::DrawElementsUShort::cloneType
        
            typedef ::osg::Object * ( ::osg::DrawElementsUShort::*cloneType_function_type)(  ) const;
            typedef ::osg::Object * ( DrawElementsUShort_wrapper::*default_cloneType_function_type)(  ) const;
            
            DrawElementsUShort_exposer.def( 
                "cloneType"
                , cloneType_function_type(&::osg::DrawElementsUShort::cloneType)
                , default_cloneType_function_type(&DrawElementsUShort_wrapper::default_cloneType)
                , bp::return_value_policy< bp::reference_existing_object >() );
        
        }
        { //::osg::DrawElementsUShort::draw
        
            typedef void ( ::osg::DrawElementsUShort::*draw_function_type)( ::osg::State &,bool ) const;
            typedef void ( DrawElementsUShort_wrapper::*default_draw_function_type)( ::osg::State &,bool ) const;
            
            DrawElementsUShort_exposer.def( 
                "draw"
                , draw_function_type(&::osg::DrawElementsUShort::draw)
                , default_draw_function_type(&DrawElementsUShort_wrapper::default_draw)
                , ( bp::arg("state"), bp::arg("useVertexBufferObjects") ) );
        
        }
        { //::osg::DrawElementsUShort::getDataPointer
        
            typedef ::GLvoid const * ( ::osg::DrawElementsUShort::*getDataPointer_function_type)(  ) const;
            typedef ::GLvoid const * ( DrawElementsUShort_wrapper::*default_getDataPointer_function_type)(  ) const;
            
            DrawElementsUShort_exposer.def( 
                "getDataPointer"
                , getDataPointer_function_type(&::osg::DrawElementsUShort::getDataPointer)
                , default_getDataPointer_function_type(&DrawElementsUShort_wrapper::default_getDataPointer)
                , bp::return_value_policy< bp::return_opaque_pointer >() );
        
        }
        { //::osg::DrawElementsUShort::getElement
        
            typedef unsigned int ( ::osg::DrawElementsUShort::*getElement_function_type)( unsigned int ) ;
            typedef unsigned int ( DrawElementsUShort_wrapper::*default_getElement_function_type)( unsigned int ) ;
            
            DrawElementsUShort_exposer.def( 
                "getElement"
                , getElement_function_type(&::osg::DrawElementsUShort::getElement)
                , default_getElement_function_type(&DrawElementsUShort_wrapper::default_getElement)
                , ( bp::arg("i") ) );
        
        }
        { //::osg::DrawElementsUShort::getNumIndices
        
            typedef unsigned int ( ::osg::DrawElementsUShort::*getNumIndices_function_type)(  ) const;
            typedef unsigned int ( DrawElementsUShort_wrapper::*default_getNumIndices_function_type)(  ) const;
            
            DrawElementsUShort_exposer.def( 
                "getNumIndices"
                , getNumIndices_function_type(&::osg::DrawElementsUShort::getNumIndices)
                , default_getNumIndices_function_type(&DrawElementsUShort_wrapper::default_getNumIndices) );
        
        }
        { //::osg::DrawElementsUShort::getTotalDataSize
        
            typedef unsigned int ( ::osg::DrawElementsUShort::*getTotalDataSize_function_type)(  ) const;
            typedef unsigned int ( DrawElementsUShort_wrapper::*default_getTotalDataSize_function_type)(  ) const;
            
            DrawElementsUShort_exposer.def( 
                "getTotalDataSize"
                , getTotalDataSize_function_type(&::osg::DrawElementsUShort::getTotalDataSize)
                , default_getTotalDataSize_function_type(&DrawElementsUShort_wrapper::default_getTotalDataSize) );
        
        }
        { //::osg::DrawElementsUShort::index
        
            typedef unsigned int ( ::osg::DrawElementsUShort::*index_function_type)( unsigned int ) const;
            typedef unsigned int ( DrawElementsUShort_wrapper::*default_index_function_type)( unsigned int ) const;
            
            DrawElementsUShort_exposer.def( 
                "index"
                , index_function_type(&::osg::DrawElementsUShort::index)
                , default_index_function_type(&DrawElementsUShort_wrapper::default_index)
                , ( bp::arg("pos") ) );
        
        }
        { //::osg::DrawElementsUShort::isSameKindAs
        
            typedef bool ( ::osg::DrawElementsUShort::*isSameKindAs_function_type)( ::osg::Object const * ) const;
            typedef bool ( DrawElementsUShort_wrapper::*default_isSameKindAs_function_type)( ::osg::Object const * ) const;
            
            DrawElementsUShort_exposer.def( 
                "isSameKindAs"
                , isSameKindAs_function_type(&::osg::DrawElementsUShort::isSameKindAs)
                , default_isSameKindAs_function_type(&DrawElementsUShort_wrapper::default_isSameKindAs)
                , ( bp::arg("obj") ) );
        
        }
        { //::osg::DrawElementsUShort::libraryName
        
            typedef char const * ( ::osg::DrawElementsUShort::*libraryName_function_type)(  ) const;
            typedef char const * ( DrawElementsUShort_wrapper::*default_libraryName_function_type)(  ) const;
            
            DrawElementsUShort_exposer.def( 
                "libraryName"
                , libraryName_function_type(&::osg::DrawElementsUShort::libraryName)
                , default_libraryName_function_type(&DrawElementsUShort_wrapper::default_libraryName) );
        
        }
        { //::osg::DrawElementsUShort::offsetIndices
        
            typedef void ( ::osg::DrawElementsUShort::*offsetIndices_function_type)( int ) ;
            typedef void ( DrawElementsUShort_wrapper::*default_offsetIndices_function_type)( int ) ;
            
            DrawElementsUShort_exposer.def( 
                "offsetIndices"
                , offsetIndices_function_type(&::osg::DrawElementsUShort::offsetIndices)
                , default_offsetIndices_function_type(&DrawElementsUShort_wrapper::default_offsetIndices)
                , ( bp::arg("offset") ) );
        
        }
        { //::osg::DrawElementsUShort::reserveElements
        
            typedef void ( ::osg::DrawElementsUShort::*reserveElements_function_type)( unsigned int ) ;
            typedef void ( DrawElementsUShort_wrapper::*default_reserveElements_function_type)( unsigned int ) ;
            
            DrawElementsUShort_exposer.def( 
                "reserveElements"
                , reserveElements_function_type(&::osg::DrawElementsUShort::reserveElements)
                , default_reserveElements_function_type(&DrawElementsUShort_wrapper::default_reserveElements)
                , ( bp::arg("numIndices") ) );
        
        }
        { //::osg::DrawElementsUShort::setElement
        
            typedef void ( ::osg::DrawElementsUShort::*setElement_function_type)( unsigned int,unsigned int ) ;
            typedef void ( DrawElementsUShort_wrapper::*default_setElement_function_type)( unsigned int,unsigned int ) ;
            
            DrawElementsUShort_exposer.def( 
                "setElement"
                , setElement_function_type(&::osg::DrawElementsUShort::setElement)
                , default_setElement_function_type(&DrawElementsUShort_wrapper::default_setElement)
                , ( bp::arg("i"), bp::arg("v") ) );
        
        }
        { //::osg::DrawElementsUShort::supportsBufferObject
        
            typedef bool ( ::osg::DrawElementsUShort::*supportsBufferObject_function_type)(  ) const;
            typedef bool ( DrawElementsUShort_wrapper::*default_supportsBufferObject_function_type)(  ) const;
            
            DrawElementsUShort_exposer.def( 
                "supportsBufferObject"
                , supportsBufferObject_function_type(&::osg::DrawElementsUShort::supportsBufferObject)
                , default_supportsBufferObject_function_type(&DrawElementsUShort_wrapper::default_supportsBufferObject) );
        
        }
        { //::osg::BufferData::asArray
        
            typedef ::osg::Array * ( ::osg::BufferData::*asArray_function_type)(  ) ;
            typedef ::osg::Array * ( DrawElementsUShort_wrapper::*default_asArray_function_type)(  ) ;
            
            DrawElementsUShort_exposer.def( 
                "asArray"
                , asArray_function_type(&::osg::BufferData::asArray)
                , default_asArray_function_type(&DrawElementsUShort_wrapper::default_asArray)
                , bp::return_internal_reference< >() );
        
        }
        { //::osg::BufferData::asArray
        
            typedef ::osg::Array const * ( ::osg::BufferData::*asArray_function_type)(  ) const;
            typedef ::osg::Array const * ( DrawElementsUShort_wrapper::*default_asArray_function_type)(  ) const;
            
            DrawElementsUShort_exposer.def( 
                "asArray"
                , asArray_function_type(&::osg::BufferData::asArray)
                , default_asArray_function_type(&DrawElementsUShort_wrapper::default_asArray)
                , bp::return_internal_reference< >() );
        
        }
        { //::osg::PrimitiveSet::asPrimitiveSet
        
            typedef ::osg::PrimitiveSet * ( ::osg::PrimitiveSet::*asPrimitiveSet_function_type)(  ) ;
            typedef ::osg::PrimitiveSet * ( DrawElementsUShort_wrapper::*default_asPrimitiveSet_function_type)(  ) ;
            
            DrawElementsUShort_exposer.def( 
                "asPrimitiveSet"
                , asPrimitiveSet_function_type(&::osg::PrimitiveSet::asPrimitiveSet)
                , default_asPrimitiveSet_function_type(&DrawElementsUShort_wrapper::default_asPrimitiveSet)
                , bp::return_internal_reference< >() );
        
        }
        { //::osg::PrimitiveSet::asPrimitiveSet
        
            typedef ::osg::PrimitiveSet const * ( ::osg::PrimitiveSet::*asPrimitiveSet_function_type)(  ) const;
            typedef ::osg::PrimitiveSet const * ( DrawElementsUShort_wrapper::*default_asPrimitiveSet_function_type)(  ) const;
            
            DrawElementsUShort_exposer.def( 
                "asPrimitiveSet"
                , asPrimitiveSet_function_type(&::osg::PrimitiveSet::asPrimitiveSet)
                , default_asPrimitiveSet_function_type(&DrawElementsUShort_wrapper::default_asPrimitiveSet)
                , bp::return_internal_reference< >() );
        
        }
        { //::osg::Object::computeDataVariance
        
            typedef void ( ::osg::Object::*computeDataVariance_function_type)(  ) ;
            typedef void ( DrawElementsUShort_wrapper::*default_computeDataVariance_function_type)(  ) ;
            
            DrawElementsUShort_exposer.def( 
                "computeDataVariance"
                , computeDataVariance_function_type(&::osg::Object::computeDataVariance)
                , default_computeDataVariance_function_type(&DrawElementsUShort_wrapper::default_computeDataVariance) );
        
        }
        { //::osg::PrimitiveSet::computeRange
        
            typedef void ( ::osg::PrimitiveSet::*computeRange_function_type)(  ) const;
            typedef void ( DrawElementsUShort_wrapper::*default_computeRange_function_type)(  ) const;
            
            DrawElementsUShort_exposer.def( 
                "computeRange"
                , computeRange_function_type(&::osg::PrimitiveSet::computeRange)
                , default_computeRange_function_type(&DrawElementsUShort_wrapper::default_computeRange) );
        
        }
        { //::osg::DrawElements::getDrawElements
        
            typedef ::osg::DrawElements * ( ::osg::DrawElements::*getDrawElements_function_type)(  ) ;
            typedef ::osg::DrawElements * ( DrawElementsUShort_wrapper::*default_getDrawElements_function_type)(  ) ;
            
            DrawElementsUShort_exposer.def( 
                "getDrawElements"
                , getDrawElements_function_type(&::osg::DrawElements::getDrawElements)
                , default_getDrawElements_function_type(&DrawElementsUShort_wrapper::default_getDrawElements)
                , bp::return_internal_reference< >() );
        
        }
        { //::osg::DrawElements::getDrawElements
        
            typedef ::osg::DrawElements const * ( ::osg::DrawElements::*getDrawElements_function_type)(  ) const;
            typedef ::osg::DrawElements const * ( DrawElementsUShort_wrapper::*default_getDrawElements_function_type)(  ) const;
            
            DrawElementsUShort_exposer.def( 
                "getDrawElements"
                , getDrawElements_function_type(&::osg::DrawElements::getDrawElements)
                , default_getDrawElements_function_type(&DrawElementsUShort_wrapper::default_getDrawElements)
                , bp::return_internal_reference< >() );
        
        }
        { //::osg::PrimitiveSet::getNumPrimitives
        
            typedef unsigned int ( ::osg::PrimitiveSet::*getNumPrimitives_function_type)(  ) const;
            typedef unsigned int ( DrawElementsUShort_wrapper::*default_getNumPrimitives_function_type)(  ) const;
            
            DrawElementsUShort_exposer.def( 
                "getNumPrimitives"
                , getNumPrimitives_function_type(&::osg::PrimitiveSet::getNumPrimitives)
                , default_getNumPrimitives_function_type(&DrawElementsUShort_wrapper::default_getNumPrimitives) );
        
        }
        { //::osg::Object::getUserData
        
            typedef ::osg::Referenced * ( ::osg::Object::*getUserData_function_type)(  ) ;
            typedef ::osg::Referenced * ( DrawElementsUShort_wrapper::*default_getUserData_function_type)(  ) ;
            
            DrawElementsUShort_exposer.def( 
                "getUserData"
                , getUserData_function_type(&::osg::Object::getUserData)
                , default_getUserData_function_type(&DrawElementsUShort_wrapper::default_getUserData)
                , bp::return_internal_reference< >() );
        
        }
        { //::osg::Object::getUserData
        
            typedef ::osg::Referenced const * ( ::osg::Object::*getUserData_function_type)(  ) const;
            typedef ::osg::Referenced const * ( DrawElementsUShort_wrapper::*default_getUserData_function_type)(  ) const;
            
            DrawElementsUShort_exposer.def( 
                "getUserData"
                , getUserData_function_type(&::osg::Object::getUserData)
                , default_getUserData_function_type(&DrawElementsUShort_wrapper::default_getUserData)
                , bp::return_internal_reference< >() );
        
        }
        { //::osg::BufferData::resizeGLObjectBuffers
        
            typedef void ( ::osg::BufferData::*resizeGLObjectBuffers_function_type)( unsigned int ) ;
            typedef void ( DrawElementsUShort_wrapper::*default_resizeGLObjectBuffers_function_type)( unsigned int ) ;
            
            DrawElementsUShort_exposer.def( 
                "resizeGLObjectBuffers"
                , resizeGLObjectBuffers_function_type(&::osg::BufferData::resizeGLObjectBuffers)
                , default_resizeGLObjectBuffers_function_type(&DrawElementsUShort_wrapper::default_resizeGLObjectBuffers)
                , ( bp::arg("maxSize") ) );
        
        }
        { //::osg::Object::setName
        
            typedef void ( ::osg::Object::*setName_function_type)( ::std::string const & ) ;
            typedef void ( DrawElementsUShort_wrapper::*default_setName_function_type)( ::std::string const & ) ;
            
            DrawElementsUShort_exposer.def( 
                "setName"
                , setName_function_type(&::osg::Object::setName)
                , default_setName_function_type(&DrawElementsUShort_wrapper::default_setName)
                , ( bp::arg("name") ) );
        
        }
        { //::osg::Object::setName
        
            typedef void ( ::osg::Object::*setName_function_type)( char const * ) ;
            
            DrawElementsUShort_exposer.def( 
                "setName"
                , setName_function_type( &::osg::Object::setName )
                , ( bp::arg("name") )
                , " Set the name of object using a C style string." );
        
        }
        { //::osg::Object::setThreadSafeRefUnref
        
            typedef void ( ::osg::Object::*setThreadSafeRefUnref_function_type)( bool ) ;
            typedef void ( DrawElementsUShort_wrapper::*default_setThreadSafeRefUnref_function_type)( bool ) ;
            
            DrawElementsUShort_exposer.def( 
                "setThreadSafeRefUnref"
                , setThreadSafeRefUnref_function_type(&::osg::Object::setThreadSafeRefUnref)
                , default_setThreadSafeRefUnref_function_type(&DrawElementsUShort_wrapper::default_setThreadSafeRefUnref)
                , ( bp::arg("threadSafe") ) );
        
        }
        { //::osg::Object::setUserData
        
            typedef void ( ::osg::Object::*setUserData_function_type)( ::osg::Referenced * ) ;
            typedef void ( DrawElementsUShort_wrapper::*default_setUserData_function_type)( ::osg::Referenced * ) ;
            
            DrawElementsUShort_exposer.def( 
                "setUserData"
                , setUserData_function_type(&::osg::Object::setUserData)
                , default_setUserData_function_type(&DrawElementsUShort_wrapper::default_setUserData)
                , ( bp::arg("obj") ) );
        
        }
        DrawElementsUShort_exposer.def(bp::indexing::container_suite<
                        osg::DrawElementsUShort, 
                        bp::indexing::all_methods, 
                        list_algorithms<OsgArray_container_traits<osg::DrawElementsUShort, osg::DrawElementsUShort::vector_type::value_type> > >());
    }

}
