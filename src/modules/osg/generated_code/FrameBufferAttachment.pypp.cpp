// This file has been generated by Py++.

#include "boost/python.hpp"
#include "wrap_osg.h"
#include "framebufferattachment.pypp.hpp"

namespace bp = boost::python;

void register_FrameBufferAttachment_class(){

    { //::osg::FrameBufferAttachment
        typedef bp::class_< osg::FrameBufferAttachment > FrameBufferAttachment_exposer_t;
        FrameBufferAttachment_exposer_t FrameBufferAttachment_exposer = FrameBufferAttachment_exposer_t( "FrameBufferAttachment", bp::init< >() );
        bp::scope FrameBufferAttachment_scope( FrameBufferAttachment_exposer );
        FrameBufferAttachment_exposer.def( bp::init< osg::FrameBufferAttachment const & >(( bp::arg("copy") )) );
        FrameBufferAttachment_exposer.def( bp::init< osg::RenderBuffer * >(( bp::arg("target") )) );
        bp::implicitly_convertible< osg::RenderBuffer *, osg::FrameBufferAttachment >();
        FrameBufferAttachment_exposer.def( bp::init< osg::Texture1D *, bp::optional< unsigned int > >(( bp::arg("target"), bp::arg("level")=(unsigned int)(0) )) );
        bp::implicitly_convertible< osg::Texture1D *, osg::FrameBufferAttachment >();
        FrameBufferAttachment_exposer.def( bp::init< osg::Texture2D *, bp::optional< unsigned int > >(( bp::arg("target"), bp::arg("level")=(unsigned int)(0) )) );
        bp::implicitly_convertible< osg::Texture2D *, osg::FrameBufferAttachment >();
        FrameBufferAttachment_exposer.def( bp::init< osg::Texture2DMultisample *, bp::optional< unsigned int > >(( bp::arg("target"), bp::arg("level")=(unsigned int)(0) )) );
        bp::implicitly_convertible< osg::Texture2DMultisample *, osg::FrameBufferAttachment >();
        FrameBufferAttachment_exposer.def( bp::init< osg::Texture3D *, unsigned int, bp::optional< unsigned int > >(( bp::arg("target"), bp::arg("zoffset"), bp::arg("level")=(unsigned int)(0) )) );
        FrameBufferAttachment_exposer.def( bp::init< osg::Texture2DArray *, unsigned int, bp::optional< unsigned int > >(( bp::arg("target"), bp::arg("layer"), bp::arg("level")=(unsigned int)(0) )) );
        FrameBufferAttachment_exposer.def( bp::init< osg::TextureCubeMap *, unsigned int, bp::optional< unsigned int > >(( bp::arg("target"), bp::arg("face"), bp::arg("level")=(unsigned int)(0) )) );
        FrameBufferAttachment_exposer.def( bp::init< osg::TextureRectangle * >(( bp::arg("target") )) );
        bp::implicitly_convertible< osg::TextureRectangle *, osg::FrameBufferAttachment >();
        FrameBufferAttachment_exposer.def( bp::init< osg::Camera::Attachment & >(( bp::arg("attachment") )) );
        bp::implicitly_convertible< osg::Camera::Attachment &, osg::FrameBufferAttachment >();
        { //::osg::FrameBufferAttachment::attach
        
            typedef void ( ::osg::FrameBufferAttachment::*attach_function_type )( ::osg::State &,::GLenum,::GLenum,::osg::FBOExtensions const * ) const;
            
            FrameBufferAttachment_exposer.def( 
                "attach"
                , attach_function_type( &::osg::FrameBufferAttachment::attach )
                , ( bp::arg("state"), bp::arg("target"), bp::arg("attachment_point"), bp::arg("ext") ) );
        
        }
        { //::osg::FrameBufferAttachment::compare
        
            typedef int ( ::osg::FrameBufferAttachment::*compare_function_type )( ::osg::FrameBufferAttachment const & ) const;
            
            FrameBufferAttachment_exposer.def( 
                "compare"
                , compare_function_type( &::osg::FrameBufferAttachment::compare )
                , ( bp::arg("fa") ) );
        
        }
        { //::osg::FrameBufferAttachment::createRequiredTexturesAndApplyGenerateMipMap
        
            typedef void ( ::osg::FrameBufferAttachment::*createRequiredTexturesAndApplyGenerateMipMap_function_type )( ::osg::State &,::osg::FBOExtensions const * ) const;
            
            FrameBufferAttachment_exposer.def( 
                "createRequiredTexturesAndApplyGenerateMipMap"
                , createRequiredTexturesAndApplyGenerateMipMap_function_type( &::osg::FrameBufferAttachment::createRequiredTexturesAndApplyGenerateMipMap )
                , ( bp::arg("state"), bp::arg("ext") ) );
        
        }
        { //::osg::FrameBufferAttachment::getCubeMapFace
        
            typedef unsigned int ( ::osg::FrameBufferAttachment::*getCubeMapFace_function_type )(  ) const;
            
            FrameBufferAttachment_exposer.def( 
                "getCubeMapFace"
                , getCubeMapFace_function_type( &::osg::FrameBufferAttachment::getCubeMapFace ) );
        
        }
        { //::osg::FrameBufferAttachment::getRenderBuffer
        
            typedef ::osg::RenderBuffer * ( ::osg::FrameBufferAttachment::*getRenderBuffer_function_type )(  ) ;
            
            FrameBufferAttachment_exposer.def( 
                "getRenderBuffer"
                , getRenderBuffer_function_type( &::osg::FrameBufferAttachment::getRenderBuffer )
                , bp::return_internal_reference< >() );
        
        }
        { //::osg::FrameBufferAttachment::getRenderBuffer
        
            typedef ::osg::RenderBuffer const * ( ::osg::FrameBufferAttachment::*getRenderBuffer_function_type )(  ) const;
            
            FrameBufferAttachment_exposer.def( 
                "getRenderBuffer"
                , getRenderBuffer_function_type( &::osg::FrameBufferAttachment::getRenderBuffer )
                , bp::return_internal_reference< >() );
        
        }
        { //::osg::FrameBufferAttachment::getTexture
        
            typedef ::osg::Texture * ( ::osg::FrameBufferAttachment::*getTexture_function_type )(  ) ;
            
            FrameBufferAttachment_exposer.def( 
                "getTexture"
                , getTexture_function_type( &::osg::FrameBufferAttachment::getTexture )
                , bp::return_internal_reference< >() );
        
        }
        { //::osg::FrameBufferAttachment::getTexture
        
            typedef ::osg::Texture const * ( ::osg::FrameBufferAttachment::*getTexture_function_type )(  ) const;
            
            FrameBufferAttachment_exposer.def( 
                "getTexture"
                , getTexture_function_type( &::osg::FrameBufferAttachment::getTexture )
                , bp::return_internal_reference< >() );
        
        }
        { //::osg::FrameBufferAttachment::getTexture3DZOffset
        
            typedef unsigned int ( ::osg::FrameBufferAttachment::*getTexture3DZOffset_function_type )(  ) const;
            
            FrameBufferAttachment_exposer.def( 
                "getTexture3DZOffset"
                , getTexture3DZOffset_function_type( &::osg::FrameBufferAttachment::getTexture3DZOffset ) );
        
        }
        { //::osg::FrameBufferAttachment::getTextureArrayLayer
        
            typedef unsigned int ( ::osg::FrameBufferAttachment::*getTextureArrayLayer_function_type )(  ) const;
            
            FrameBufferAttachment_exposer.def( 
                "getTextureArrayLayer"
                , getTextureArrayLayer_function_type( &::osg::FrameBufferAttachment::getTextureArrayLayer ) );
        
        }
        { //::osg::FrameBufferAttachment::getTextureLevel
        
            typedef unsigned int ( ::osg::FrameBufferAttachment::*getTextureLevel_function_type )(  ) const;
            
            FrameBufferAttachment_exposer.def( 
                "getTextureLevel"
                , getTextureLevel_function_type( &::osg::FrameBufferAttachment::getTextureLevel ) );
        
        }
        { //::osg::FrameBufferAttachment::isMultisample
        
            typedef bool ( ::osg::FrameBufferAttachment::*isMultisample_function_type )(  ) const;
            
            FrameBufferAttachment_exposer.def( 
                "isMultisample"
                , isMultisample_function_type( &::osg::FrameBufferAttachment::isMultisample ) );
        
        }
        { //::osg::FrameBufferAttachment::operator=
        
            typedef ::osg::FrameBufferAttachment & ( ::osg::FrameBufferAttachment::*assign_function_type )( ::osg::FrameBufferAttachment const & ) ;
            
            FrameBufferAttachment_exposer.def( 
                "assign"
                , assign_function_type( &::osg::FrameBufferAttachment::operator= )
                , ( bp::arg("copy") )
                , bp::return_self< >() );
        
        }
    }

}