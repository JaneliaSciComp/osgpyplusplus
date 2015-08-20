// This file has been generated by Py++.

#include "boost/python.hpp"
#include "wrap_osgsim.h"
#include "wrap_referenced.h"
#include "overlaynode.pypp.hpp"

namespace bp = boost::python;

struct OverlayNode_wrapper : osgSim::OverlayNode, bp::wrapper< osgSim::OverlayNode > {

    OverlayNode_wrapper(::osgSim::OverlayNode::OverlayTechnique technique=::osgSim::OverlayNode::OBJECT_DEPENDENT_WITH_ORTHOGRAPHIC_OVERLAY )
    : osgSim::OverlayNode( technique )
      , bp::wrapper< osgSim::OverlayNode >(){
        // constructor
    
    }

    virtual void accept( ::osg::NodeVisitor & nv ) {
        if( bp::override func_accept = this->get_override( "accept" ) )
            func_accept( boost::ref(nv) );
        else{
            this->osgSim::OverlayNode::accept( boost::ref(nv) );
        }
    }
    
    void default_accept( ::osg::NodeVisitor & nv ) {
        osgSim::OverlayNode::accept( boost::ref(nv) );
    }

    virtual char const * className(  ) const  {
        if( bp::override func_className = this->get_override( "className" ) )
            return func_className(  );
        else{
            return this->osgSim::OverlayNode::className(  );
        }
    }
    
    char const * default_className(  ) const  {
        return osgSim::OverlayNode::className( );
    }

    virtual ::osg::Object * clone( ::osg::CopyOp const & copyop ) const  {
        if( bp::override func_clone = this->get_override( "clone" ) )
            return func_clone( boost::ref(copyop) );
        else{
            return this->osgSim::OverlayNode::clone( boost::ref(copyop) );
        }
    }
    
    ::osg::Object * default_clone( ::osg::CopyOp const & copyop ) const  {
        return osgSim::OverlayNode::clone( boost::ref(copyop) );
    }

    virtual ::osg::Object * cloneType(  ) const  {
        if( bp::override func_cloneType = this->get_override( "cloneType" ) )
            return func_cloneType(  );
        else{
            return this->osgSim::OverlayNode::cloneType(  );
        }
    }
    
    ::osg::Object * default_cloneType(  ) const  {
        return osgSim::OverlayNode::cloneType( );
    }

    virtual bool isSameKindAs( ::osg::Object const * obj ) const  {
        if( bp::override func_isSameKindAs = this->get_override( "isSameKindAs" ) )
            return func_isSameKindAs( boost::python::ptr(obj) );
        else{
            return this->osgSim::OverlayNode::isSameKindAs( boost::python::ptr(obj) );
        }
    }
    
    bool default_isSameKindAs( ::osg::Object const * obj ) const  {
        return osgSim::OverlayNode::isSameKindAs( boost::python::ptr(obj) );
    }

    virtual char const * libraryName(  ) const  {
        if( bp::override func_libraryName = this->get_override( "libraryName" ) )
            return func_libraryName(  );
        else{
            return this->osgSim::OverlayNode::libraryName(  );
        }
    }
    
    char const * default_libraryName(  ) const  {
        return osgSim::OverlayNode::libraryName( );
    }

    virtual void releaseGLObjects( ::osg::State * arg0=0 ) const  {
        if( bp::override func_releaseGLObjects = this->get_override( "releaseGLObjects" ) )
            func_releaseGLObjects( boost::python::ptr(arg0) );
        else{
            this->osgSim::OverlayNode::releaseGLObjects( boost::python::ptr(arg0) );
        }
    }
    
    void default_releaseGLObjects( ::osg::State * arg0=0 ) const  {
        osgSim::OverlayNode::releaseGLObjects( boost::python::ptr(arg0) );
    }

    virtual void resizeGLObjectBuffers( unsigned int arg0 ) {
        if( bp::override func_resizeGLObjectBuffers = this->get_override( "resizeGLObjectBuffers" ) )
            func_resizeGLObjectBuffers( arg0 );
        else{
            this->osgSim::OverlayNode::resizeGLObjectBuffers( arg0 );
        }
    }
    
    void default_resizeGLObjectBuffers( unsigned int arg0 ) {
        osgSim::OverlayNode::resizeGLObjectBuffers( arg0 );
    }

    virtual void setThreadSafeRefUnref( bool threadSafe ) {
        if( bp::override func_setThreadSafeRefUnref = this->get_override( "setThreadSafeRefUnref" ) )
            func_setThreadSafeRefUnref( threadSafe );
        else{
            this->osgSim::OverlayNode::setThreadSafeRefUnref( threadSafe );
        }
    }
    
    void default_setThreadSafeRefUnref( bool threadSafe ) {
        osgSim::OverlayNode::setThreadSafeRefUnref( threadSafe );
    }

    virtual void traverse( ::osg::NodeVisitor & nv ) {
        if( bp::override func_traverse = this->get_override( "traverse" ) )
            func_traverse( boost::ref(nv) );
        else{
            this->osgSim::OverlayNode::traverse( boost::ref(nv) );
        }
    }
    
    void default_traverse( ::osg::NodeVisitor & nv ) {
        osgSim::OverlayNode::traverse( boost::ref(nv) );
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

void register_OverlayNode_class(){

    { //::osgSim::OverlayNode
        typedef bp::class_< OverlayNode_wrapper, bp::bases< ::osg::Group >, osg::ref_ptr< OverlayNode_wrapper >, boost::noncopyable > OverlayNode_exposer_t;
        OverlayNode_exposer_t OverlayNode_exposer = OverlayNode_exposer_t( "OverlayNode", "\n OverlayNode is for creating texture overlays on scenes, with the overlay texture being generated\n by pre rendering an Overlay Subgraph to a texture, then projecting this resulting texture on the scene.\n", bp::no_init );
        bp::scope OverlayNode_scope( OverlayNode_exposer );
        bp::enum_< osgSim::OverlayNode::OverlayTechnique>("OverlayTechnique")
            .value("OBJECT_DEPENDENT_WITH_ORTHOGRAPHIC_OVERLAY", osgSim::OverlayNode::OBJECT_DEPENDENT_WITH_ORTHOGRAPHIC_OVERLAY)
            .value("VIEW_DEPENDENT_WITH_ORTHOGRAPHIC_OVERLAY", osgSim::OverlayNode::VIEW_DEPENDENT_WITH_ORTHOGRAPHIC_OVERLAY)
            .value("VIEW_DEPENDENT_WITH_PERSPECTIVE_OVERLAY", osgSim::OverlayNode::VIEW_DEPENDENT_WITH_PERSPECTIVE_OVERLAY)
            .export_values()
            ;
        OverlayNode_exposer.def( bp::init< bp::optional< osgSim::OverlayNode::OverlayTechnique > >(( bp::arg("technique")=(long)(::osgSim::OverlayNode::OBJECT_DEPENDENT_WITH_ORTHOGRAPHIC_OVERLAY) )) );
        bp::implicitly_convertible< osgSim::OverlayNode::OverlayTechnique, osgSim::OverlayNode >();
        { //::osgSim::OverlayNode::accept
        
            typedef void ( ::osgSim::OverlayNode::*accept_function_type)( ::osg::NodeVisitor & ) ;
            typedef void ( OverlayNode_wrapper::*default_accept_function_type)( ::osg::NodeVisitor & ) ;
            
            OverlayNode_exposer.def( 
                "accept"
                , accept_function_type(&::osgSim::OverlayNode::accept)
                , default_accept_function_type(&OverlayNode_wrapper::default_accept)
                , ( bp::arg("nv") ) );
        
        }
        { //::osgSim::OverlayNode::className
        
            typedef char const * ( ::osgSim::OverlayNode::*className_function_type)(  ) const;
            typedef char const * ( OverlayNode_wrapper::*default_className_function_type)(  ) const;
            
            OverlayNode_exposer.def( 
                "className"
                , className_function_type(&::osgSim::OverlayNode::className)
                , default_className_function_type(&OverlayNode_wrapper::default_className) );
        
        }
        { //::osgSim::OverlayNode::clone
        
            typedef ::osg::Object * ( ::osgSim::OverlayNode::*clone_function_type)( ::osg::CopyOp const & ) const;
            typedef ::osg::Object * ( OverlayNode_wrapper::*default_clone_function_type)( ::osg::CopyOp const & ) const;
            
            OverlayNode_exposer.def( 
                "clone"
                , clone_function_type(&::osgSim::OverlayNode::clone)
                , default_clone_function_type(&OverlayNode_wrapper::default_clone)
                , ( bp::arg("copyop") )
                , bp::return_value_policy< bp::reference_existing_object >() );
        
        }
        { //::osgSim::OverlayNode::cloneType
        
            typedef ::osg::Object * ( ::osgSim::OverlayNode::*cloneType_function_type)(  ) const;
            typedef ::osg::Object * ( OverlayNode_wrapper::*default_cloneType_function_type)(  ) const;
            
            OverlayNode_exposer.def( 
                "cloneType"
                , cloneType_function_type(&::osgSim::OverlayNode::cloneType)
                , default_cloneType_function_type(&OverlayNode_wrapper::default_cloneType)
                , bp::return_value_policy< bp::reference_existing_object >() );
        
        }
        { //::osgSim::OverlayNode::dirtyOverlayTexture
        
            typedef void ( ::osgSim::OverlayNode::*dirtyOverlayTexture_function_type)(  ) ;
            
            OverlayNode_exposer.def( 
                "dirtyOverlayTexture"
                , dirtyOverlayTexture_function_type( &::osgSim::OverlayNode::dirtyOverlayTexture )
                , " Inform the OverlayNode that the overlay texture needs to be updated." );
        
        }
        { //::osgSim::OverlayNode::getContinuousUpdate
        
            typedef bool ( ::osgSim::OverlayNode::*getContinuousUpdate_function_type)(  ) const;
            
            OverlayNode_exposer.def( 
                "getContinuousUpdate"
                , getContinuousUpdate_function_type( &::osgSim::OverlayNode::getContinuousUpdate )
                , " Get whether the OverlayNode should update the overlay texture on every frame." );
        
        }
        { //::osgSim::OverlayNode::getOverlayBaseHeight
        
            typedef double ( ::osgSim::OverlayNode::*getOverlayBaseHeight_function_type)(  ) const;
            
            OverlayNode_exposer.def( 
                "getOverlayBaseHeight"
                , getOverlayBaseHeight_function_type( &::osgSim::OverlayNode::getOverlayBaseHeight )
                , " Get the base height that the overlay subgraph will be projected down to." );
        
        }
        { //::osgSim::OverlayNode::getOverlayClearColor
        
            typedef ::osg::Vec4 const & ( ::osgSim::OverlayNode::*getOverlayClearColor_function_type)(  ) const;
            
            OverlayNode_exposer.def( 
                "getOverlayClearColor"
                , getOverlayClearColor_function_type( &::osgSim::OverlayNode::getOverlayClearColor )
                , bp::return_internal_reference< >()
                , " Get the clear color to use when rendering the overlay subgraph." );
        
        }
        { //::osgSim::OverlayNode::getOverlaySubgraph
        
            typedef ::osg::Node * ( ::osgSim::OverlayNode::*getOverlaySubgraph_function_type)(  ) ;
            
            OverlayNode_exposer.def( 
                "getOverlaySubgraph"
                , getOverlaySubgraph_function_type( &::osgSim::OverlayNode::getOverlaySubgraph )
                , bp::return_internal_reference< >()
                , " Get the overlay subgraph which will be rendered to texture." );
        
        }
        { //::osgSim::OverlayNode::getOverlaySubgraph
        
            typedef ::osg::Node const * ( ::osgSim::OverlayNode::*getOverlaySubgraph_function_type)(  ) const;
            
            OverlayNode_exposer.def( 
                "getOverlaySubgraph"
                , getOverlaySubgraph_function_type( &::osgSim::OverlayNode::getOverlaySubgraph )
                , bp::return_internal_reference< >()
                , " Get the const overlay subgraph which will be render to texture." );
        
        }
        { //::osgSim::OverlayNode::getOverlayTechnique
        
            typedef ::osgSim::OverlayNode::OverlayTechnique ( ::osgSim::OverlayNode::*getOverlayTechnique_function_type)(  ) const;
            
            OverlayNode_exposer.def( 
                "getOverlayTechnique"
                , getOverlayTechnique_function_type( &::osgSim::OverlayNode::getOverlayTechnique ) );
        
        }
        { //::osgSim::OverlayNode::getOverlayTextureSizeHint
        
            typedef unsigned int ( ::osgSim::OverlayNode::*getOverlayTextureSizeHint_function_type)(  ) const;
            
            OverlayNode_exposer.def( 
                "getOverlayTextureSizeHint"
                , getOverlayTextureSizeHint_function_type( &::osgSim::OverlayNode::getOverlayTextureSizeHint )
                , " Get the texture size hint." );
        
        }
        { //::osgSim::OverlayNode::getOverlayTextureUnit
        
            typedef unsigned int ( ::osgSim::OverlayNode::*getOverlayTextureUnit_function_type)(  ) const;
            
            OverlayNode_exposer.def( 
                "getOverlayTextureUnit"
                , getOverlayTextureUnit_function_type( &::osgSim::OverlayNode::getOverlayTextureUnit )
                , " Get the texture unit that the texture should be assigned to." );
        
        }
        { //::osgSim::OverlayNode::getTexEnvMode
        
            typedef ::GLenum ( ::osgSim::OverlayNode::*getTexEnvMode_function_type)(  ) const;
            
            OverlayNode_exposer.def( 
                "getTexEnvMode"
                , getTexEnvMode_function_type( &::osgSim::OverlayNode::getTexEnvMode )
                , " Get the TexEnv mode used to combine the overlay texture with the base color/texture of the OverlayNodes decorate subgraph." );
        
        }
        { //::osgSim::OverlayNode::isSameKindAs
        
            typedef bool ( ::osgSim::OverlayNode::*isSameKindAs_function_type)( ::osg::Object const * ) const;
            typedef bool ( OverlayNode_wrapper::*default_isSameKindAs_function_type)( ::osg::Object const * ) const;
            
            OverlayNode_exposer.def( 
                "isSameKindAs"
                , isSameKindAs_function_type(&::osgSim::OverlayNode::isSameKindAs)
                , default_isSameKindAs_function_type(&OverlayNode_wrapper::default_isSameKindAs)
                , ( bp::arg("obj") ) );
        
        }
        { //::osgSim::OverlayNode::libraryName
        
            typedef char const * ( ::osgSim::OverlayNode::*libraryName_function_type)(  ) const;
            typedef char const * ( OverlayNode_wrapper::*default_libraryName_function_type)(  ) const;
            
            OverlayNode_exposer.def( 
                "libraryName"
                , libraryName_function_type(&::osgSim::OverlayNode::libraryName)
                , default_libraryName_function_type(&OverlayNode_wrapper::default_libraryName) );
        
        }
        { //::osgSim::OverlayNode::releaseGLObjects
        
            typedef void ( ::osgSim::OverlayNode::*releaseGLObjects_function_type)( ::osg::State * ) const;
            typedef void ( OverlayNode_wrapper::*default_releaseGLObjects_function_type)( ::osg::State * ) const;
            
            OverlayNode_exposer.def( 
                "releaseGLObjects"
                , releaseGLObjects_function_type(&::osgSim::OverlayNode::releaseGLObjects)
                , default_releaseGLObjects_function_type(&OverlayNode_wrapper::default_releaseGLObjects)
                , ( bp::arg("arg0")=bp::object() ) );
        
        }
        { //::osgSim::OverlayNode::resizeGLObjectBuffers
        
            typedef void ( ::osgSim::OverlayNode::*resizeGLObjectBuffers_function_type)( unsigned int ) ;
            typedef void ( OverlayNode_wrapper::*default_resizeGLObjectBuffers_function_type)( unsigned int ) ;
            
            OverlayNode_exposer.def( 
                "resizeGLObjectBuffers"
                , resizeGLObjectBuffers_function_type(&::osgSim::OverlayNode::resizeGLObjectBuffers)
                , default_resizeGLObjectBuffers_function_type(&OverlayNode_wrapper::default_resizeGLObjectBuffers)
                , ( bp::arg("arg0") ) );
        
        }
        { //::osgSim::OverlayNode::setContinuousUpdate
        
            typedef void ( ::osgSim::OverlayNode::*setContinuousUpdate_function_type)( bool ) ;
            
            OverlayNode_exposer.def( 
                "setContinuousUpdate"
                , setContinuousUpdate_function_type( &::osgSim::OverlayNode::setContinuousUpdate )
                , ( bp::arg("update") )
                , " Set whether the OverlayNode should update the overlay texture on every frame." );
        
        }
        { //::osgSim::OverlayNode::setOverlayBaseHeight
        
            typedef void ( ::osgSim::OverlayNode::*setOverlayBaseHeight_function_type)( double ) ;
            
            OverlayNode_exposer.def( 
                "setOverlayBaseHeight"
                , setOverlayBaseHeight_function_type( &::osgSim::OverlayNode::setOverlayBaseHeight )
                , ( bp::arg("baseHeight") )
                , " Set the base height that the overlay subgraph will be projected down to.\n Normally youll set this to just below ground level, if you set it too high\n then the overlay texture can end up being clipped in certain viewing directions,\n while if its too low then there will be a limit to how close you can get to the\n terrain before pixaltion becomes an issue." );
        
        }
        { //::osgSim::OverlayNode::setOverlayClearColor
        
            typedef void ( ::osgSim::OverlayNode::*setOverlayClearColor_function_type)( ::osg::Vec4 const & ) ;
            
            OverlayNode_exposer.def( 
                "setOverlayClearColor"
                , setOverlayClearColor_function_type( &::osgSim::OverlayNode::setOverlayClearColor )
                , ( bp::arg("color") )
                , " Set the clear color to use when rendering the overlay subgraph." );
        
        }
        { //::osgSim::OverlayNode::setOverlaySubgraph
        
            typedef void ( ::osgSim::OverlayNode::*setOverlaySubgraph_function_type)( ::osg::Node * ) ;
            
            OverlayNode_exposer.def( 
                "setOverlaySubgraph"
                , setOverlaySubgraph_function_type( &::osgSim::OverlayNode::setOverlaySubgraph )
                , ( bp::arg("node") )
                , " Set the overlay subgraph which will be rendered to texture." );
        
        }
        { //::osgSim::OverlayNode::setOverlayTechnique
        
            typedef void ( ::osgSim::OverlayNode::*setOverlayTechnique_function_type)( ::osgSim::OverlayNode::OverlayTechnique ) ;
            
            OverlayNode_exposer.def( 
                "setOverlayTechnique"
                , setOverlayTechnique_function_type( &::osgSim::OverlayNode::setOverlayTechnique )
                , ( bp::arg("technique") ) );
        
        }
        { //::osgSim::OverlayNode::setOverlayTextureSizeHint
        
            typedef void ( ::osgSim::OverlayNode::*setOverlayTextureSizeHint_function_type)( unsigned int ) ;
            
            OverlayNode_exposer.def( 
                "setOverlayTextureSizeHint"
                , setOverlayTextureSizeHint_function_type( &::osgSim::OverlayNode::setOverlayTextureSizeHint )
                , ( bp::arg("size") )
                , " Set the texture size hint. The size hint is used to request a texture of specified size." );
        
        }
        { //::osgSim::OverlayNode::setOverlayTextureUnit
        
            typedef void ( ::osgSim::OverlayNode::*setOverlayTextureUnit_function_type)( unsigned int ) ;
            
            OverlayNode_exposer.def( 
                "setOverlayTextureUnit"
                , setOverlayTextureUnit_function_type( &::osgSim::OverlayNode::setOverlayTextureUnit )
                , ( bp::arg("unit") )
                , " Set the texture unit that the texture should be assigned to." );
        
        }
        { //::osgSim::OverlayNode::setRenderTargetImplementation
        
            typedef void ( ::osgSim::OverlayNode::*setRenderTargetImplementation_function_type)( ::osg::Camera::RenderTargetImplementation ) ;
            
            OverlayNode_exposer.def( 
                "setRenderTargetImplementation"
                , setRenderTargetImplementation_function_type( &::osgSim::OverlayNode::setRenderTargetImplementation )
                , ( bp::arg("impl") )
                , " Set the implementation to be used when creating the overlay texture." );
        
        }
        { //::osgSim::OverlayNode::setTexEnvMode
        
            typedef void ( ::osgSim::OverlayNode::*setTexEnvMode_function_type)( ::GLenum ) ;
            
            OverlayNode_exposer.def( 
                "setTexEnvMode"
                , setTexEnvMode_function_type( &::osgSim::OverlayNode::setTexEnvMode )
                , ( bp::arg("mode") )
                , " Set the TexEnv mode used to combine the overlay texture with the base color/texture of the OverlayNodes decorate subgraph." );
        
        }
        { //::osgSim::OverlayNode::setThreadSafeRefUnref
        
            typedef void ( ::osgSim::OverlayNode::*setThreadSafeRefUnref_function_type)( bool ) ;
            typedef void ( OverlayNode_wrapper::*default_setThreadSafeRefUnref_function_type)( bool ) ;
            
            OverlayNode_exposer.def( 
                "setThreadSafeRefUnref"
                , setThreadSafeRefUnref_function_type(&::osgSim::OverlayNode::setThreadSafeRefUnref)
                , default_setThreadSafeRefUnref_function_type(&OverlayNode_wrapper::default_setThreadSafeRefUnref)
                , ( bp::arg("threadSafe") ) );
        
        }
        { //::osgSim::OverlayNode::traverse
        
            typedef void ( ::osgSim::OverlayNode::*traverse_function_type)( ::osg::NodeVisitor & ) ;
            typedef void ( OverlayNode_wrapper::*default_traverse_function_type)( ::osg::NodeVisitor & ) ;
            
            OverlayNode_exposer.def( 
                "traverse"
                , traverse_function_type(&::osgSim::OverlayNode::traverse)
                , default_traverse_function_type(&OverlayNode_wrapper::default_traverse)
                , ( bp::arg("nv") ) );
        
        }
    }

}
