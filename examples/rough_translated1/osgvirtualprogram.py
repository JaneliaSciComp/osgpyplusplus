#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgvirtualprogram"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osg
from osgpypp import osgDB
from osgpypp import osgText
from osgpypp import osgViewer


# Translated from file 'CreateAdvancedHierachy.cpp'

#include <iostream>
#include <osg/Geode>
#include <osg/TexGen>
#include <osg/Texture2D>
#include <osg/MatrixTransform>
#include <osg/BlendFunc>
#include <osgText/Text>
#include <osgDB/ReadFile>

#include "VirtualProgram.h"

using osgCandidate.VirtualProgram

########################################
# Example shaders assume:
# one texture
# one directional light 
# front face lighting
# color material mode not used (its not supported by GLSL anyway)
# diffuse/ambient/emissive/specular factors defined in material structure
# all coords and normal except gl_Position are in view space
########################################

char MainVertexShaderSource[] =
"vec4 texture( in vec3 position, in vec3 normal )                          \n" #1
"void lighting( in vec3 position, in vec3 normal )                         \n" #2
"                                                                           \n" #3
"void main ()                                                               \n" #4
"                                                                          \n" #5
"    gl_Position = gl_ModelViewProjectionMatrix * gl_Vertex                \n" #6
"    vec4 position4 = gl_ModelViewMatrix * gl_Vertex                       \n" #7
"    vec3 position = position4.xyz / position4.w                           \n" #8
"    vec3 normal = normalize( gl_NormalMatrix * gl_Normal )                \n" #9
"    gl_TexCoord[0] = texture( position, normal )                          \n" #10
"    lighting( position, normal )                                          \n" #11
"                                                                          \n"#12

char TexCoordTextureVertexShaderSource[] =
"vec4 texture( in vec3 position, in vec3 normal )                           \n" #1
"                                                                          \n" #2
"    return gl_TextureMatrix[0] * gl_MultiTexCoord0                        \n" #3
"                                                                          \n"#4

char SphereMapTextureVertexShaderSource[] =
"vec4 texture( in vec3 position, in vec3 normal )                           \n" #1
"                                                                          \n" #2
"    vec3 u = normalize( position )                                        \n" #3
"    vec3 r = reflect(u, normal)                                           \n" #4
"    float m = 2.0 * sqrt(r.x * r.x + r.y * r.y + (r.z+1.0) * (r.z+1.0))   \n" #5
"    return vec4(r.x / m + 0.5, r.y / m + 0.5, 1.0, 1.0 )                  \n" #6
"                                                                          \n"#7

char PerVertexDirectionalLightingVertexShaderSource[] = 
"void lighting( in vec3 position, in vec3 normal )                          \n" #1
"                                                                          \n" #2
"    float NdotL = dot( normal, normalize(gl_LightSource[0].position.xyz) )\n" #3
"    NdotL = max( 0.0, NdotL )                                             \n" #4
"    float NdotHV = dot( normal, gl_LightSource[0].halfVector.xyz )        \n" #5
"    NdotHV = max( 0.0, NdotHV )                                           \n" #6
"                                                                           \n" #7
"    gl_FrontColor = gl_FrontLightModelProduct.sceneColor +                 \n" #8
"                    gl_FrontLightProduct[0].ambient +                      \n" #9
"                    gl_FrontLightProduct[0].diffuse * NdotL               \n" #10
"                                                                           \n" #11
"    gl_FrontSecondaryColor = vec4(0.0)                                    \n" #12
"                                                                           \n" #13
"    if  NdotL * NdotHV > 0.0  :                                            \n" #14
"        gl_FrontSecondaryColor = gl_FrontLightProduct[0].specular *        \n" #15
"                                 pow( NdotHV, gl_FrontMaterial.shininess )\n" #16
"                                                                           \n" #17
"    gl_BackColor = gl_FrontColor                                          \n" #18
"    gl_BackSecondaryColor = gl_FrontSecondaryColor                        \n" #19
"                                                                          \n"#20

char MainFragmentShaderSource[] =
"vec4 texture( void )                                                      \n" #1
"void lighting( inout vec4 color )                                         \n" #2
"                                                                           \n" #3
"void main ()                                                               \n" #4
"                                                                          \n" #5
"    vec4 color = texture()                                                \n" #6
"    lighting( color )                                                     \n" #7
"    gl_FragColor = color                                                  \n" #8
"                                                                          \n"#9

char TextureFragmentShaderSource[] =
"uniform sampler2D baseTexture                                             \n" #1
"vec4 texture( void )                                                       \n" #2
"                                                                          \n" #3
"    return texture2D( baseTexture, gl_TexCoord[0].xy )                    \n" #4
"                                                                          \n"#5

char ProceduralBlueTextureFragmentShaderSource[] =
"vec4 texture( void )                                                       \n" #1
"                                                                          \n" #2
"    return vec4( 0.3, 0.3, 1.0, 1.0 )                                     \n" #3
"                                                                          \n"#4

char PerVertexLightingFragmentShaderSource[] =
"void lighting( inout vec4 color )                                          \n" #1
"                                                                          \n" #2
"    color = color * gl_Color + gl_SecondaryColor                          \n" #3
"                                                                          \n"#4

char PerFragmentLightingVertexShaderSource[] =
"varying vec3 Normal                                                       \n" #1
"varying vec3 Position                                                     \n" #2
"                                                                           \n" #3
"void lighting( in vec3 position, in vec3 normal )                          \n" #4
"                                                                          \n" #5
"    Normal = normal                                                       \n" #6
"    Position = position                                                   \n" #7
"                                                                          \n"#8

char PerFragmentDirectionalLightingFragmentShaderSource[] =
"varying vec3 Normal                                                       \n" #1
"varying vec3 Position # not used for directional lighting                \n" #2
"                                                                           \n" #3
"void lighting( inout vec4 color )                                          \n" #4
"                                                                          \n" #5
"    vec3 n = normalize( Normal )                                          \n" #5
"    float NdotL = dot( n, normalize(gl_LightSource[0].position.xyz) )     \n" #6
"    NdotL = max( 0.0, NdotL )                                             \n" #7
"    float NdotHV = dot( n, gl_LightSource[0].halfVector.xyz )             \n" #8
"    NdotHV = max( 0.0, NdotHV )                                           \n" #9
"                                                                           \n" #10
"    color *= gl_FrontLightModelProduct.sceneColor +                        \n" #11
"             gl_FrontLightProduct[0].ambient +                             \n" #12
"             gl_FrontLightProduct[0].diffuse * NdotL                      \n" #13
"                                                                           \n" #14
"    if  NdotL * NdotHV > 0.0  :                                            \n" #15
"        color += gl_FrontLightProduct[0].specular *                        \n" #16
"                 pow( NdotHV, gl_FrontMaterial.shininess )                \n" #17
"                                                                          \n"#18

########################################
# Convenience method to simplify code a little ...
def SetVirtualProgramShader(virtualProgram, shader_semantics, shader_type, shader_name, shader_source):
    
    shader = osg.Shader( shader_type )
    shader.setName( shader_name )
    shader.setShaderSource( shader_source )
    virtualProgram.setShader( shader_semantics, shader )
#######################################/
void AddLabel( osg.Group * group,  str  label, float offset )
    center = osg.Vec3( 0, 0, offset * 0.5 )
    geode = osg.Geode()

    # Make sure no program breaks text outputs 
    geode.getOrCreateStateSet().setAttribute
      ( osg.Program, osg.StateAttribute.ON | osg.StateAttribute.PROTECTED )()

    # Turn off stage 1 texture set in parent transform (otherwise it darkens text)
    geode.getOrCreateStateSet().setTextureMode( 1, GL_TEXTURE_2D, osg.StateAttribute.OFF )

    group.addChild( geode )

    text = osgText.Text()
    geode.addDrawable( text )
    text.setFont("fonts/times.ttf")
    text.setCharacterSize( offset * 0.1 )
    text.setPosition(center)
    text.setAlignment( osgText.TextBase.CENTER_CENTER )
    text.setAxisAlignment(osgText.Text.SCREEN)

    characterSizeModeColor = osg.Vec4(1.0,0.0,0.5,1.0)
#if 1
    # reproduce outline bounding box compute problem with backdrop on.
    text.setBackdropType(osgText.Text.OUTLINE)
    text.setDrawMode(osgText.Text.TEXT | osgText.Text.BOUNDINGBOX)
#endif

    text.setText( label )
########################################
def CreateAdvancedHierarchy(model):
    
    if  !model  : return NULL
    offset = model.getBound().radius() * 1.3 # diameter

    # Create transforms for translated instances of the model
    transformCenterMiddle = osg.MatrixTransform( )
    transformCenterMiddle.setMatrix( osg.Matrix.translate( 0,0, offset * 0.5 ) )
    transformCenterMiddle.addChild( model )

    transformCenterTop = osg.MatrixTransform( )
    transformCenterMiddle.addChild( transformCenterTop )
    transformCenterTop.setMatrix( osg.Matrix.translate( 0,0,offset ) )
    transformCenterTop.addChild( model )

    transformCenterBottom = osg.MatrixTransform( )
    transformCenterMiddle.addChild( transformCenterBottom )
    transformCenterBottom.setMatrix( osg.Matrix.translate( 0,0,-offset ) )
    transformCenterBottom.addChild( model )

    transformLeftBottom = osg.MatrixTransform( )
    transformCenterBottom.addChild( transformLeftBottom )
    transformLeftBottom.setMatrix( osg.Matrix.translate( -offset * 0.8,0, -offset * 0.8 ) )
    transformLeftBottom.addChild( model )

    transformRightBottom = osg.MatrixTransform( )
    transformCenterBottom.addChild( transformRightBottom )
    transformRightBottom.setMatrix( osg.Matrix.translate( offset * 0.8,0, -offset * 0.8 ) )
    transformRightBottom.addChild( model )

    # Set default VirtualProgram in root StateSet 
    # With main vertex and main fragment shaders calling 
    # lighting and texture functions defined in aditional shaders
    # Lighting is done per vertex using simple directional light
    # Texture uses stage 0 TexCoords and TexMap

    if  1  : 
        # NOTE:
        # duplicating the same semantics name in virtual program 
        # is only possible if its used for shaders of differing types
        # here for VERTEX and FRAGMENT

        vp = VirtualProgram( )
        transformCenterMiddle.getOrCreateStateSet().setAttribute( vp )
        AddLabel( transformCenterMiddle, "Per Vertex Lighting Virtual Program", offset )

        SetVirtualProgramShader( vp, "main", osg.Shader.VERTEX,
            "Vertex Main", MainVertexShaderSource )

        SetVirtualProgramShader( vp, "main", osg.Shader.FRAGMENT,
            "Fragment Main", MainFragmentShaderSource )

        SetVirtualProgramShader( vp, "texture",osg.Shader.VERTEX,
            "Vertex Texture Coord 0", TexCoordTextureVertexShaderSource )

        SetVirtualProgramShader( vp, "texture",osg.Shader.FRAGMENT,
            "Fragment Texture", TextureFragmentShaderSource )

        SetVirtualProgramShader( vp, "lighting",osg.Shader.VERTEX,
            "Vertex Lighting", PerVertexDirectionalLightingVertexShaderSource )

        SetVirtualProgramShader( vp, "lighting",osg.Shader.FRAGMENT,
            "Fragment Lighting", PerVertexLightingFragmentShaderSource )

        transformCenterMiddle.getOrCreateStateSet().
            addUniform( osg.Uniform( "baseTexture", 0 ) )


    # Override default vertex ligting with pixel lighting shaders
    # For three bottom models
    if  1  : 
        AddLabel( transformCenterBottom, "Per Pixel Lighting VP", offset )
        vp = VirtualProgram( )
        transformCenterBottom.getOrCreateStateSet().setAttribute( vp )

        SetVirtualProgramShader( vp, "lighting",osg.Shader.VERTEX,
            "Vertex Shader For Per Pixel Lighting", 
            PerFragmentLightingVertexShaderSource )

        SetVirtualProgramShader( vp, "lighting",osg.Shader.FRAGMENT,
            "Fragment Shader For Per Pixel Lighting", 
            PerFragmentDirectionalLightingFragmentShaderSource )

    # Additionaly set bottom left model texture to procedural blue to 
    # better observe smooth speculars done through per pixel lighting
    if  1  : 
        AddLabel( transformLeftBottom, "Blue Tex VP", offset )
        vp = VirtualProgram( )
        transformLeftBottom.getOrCreateStateSet().setAttribute( vp )

        SetVirtualProgramShader( vp, "texture",osg.Shader.FRAGMENT,
            "Fragment Shader Procedural Blue Tex", 
            ProceduralBlueTextureFragmentShaderSource )

    # Additionaly change texture mapping to SphereMAp in bottom right model 
    if  1  :
        AddLabel( transformRightBottom, "EnvMap Sphere VP", offset )

        ss = transformRightBottom.getOrCreateStateSet()
        vp = VirtualProgram( )
        ss.setAttribute( vp )
        SetVirtualProgramShader( vp, "texture",osg.Shader.VERTEX,
            "Vertex Texture Sphere Map", SphereMapTextureVertexShaderSource )

        texture = osg.Texture2D(
#            osgDB.readImageFile("Images/reflect.rgb") 
            osgDB.readImageFile("Images/skymap.jpg") 
        )

        # Texture is set on stage 1 to not interfere with label text
        # The same could be achieved with texture override 
        # but such approach also turns off label texture
        ss.setTextureAttributeAndModes( 1, texture, osg.StateAttribute.ON )
        ss.addUniform( osg.Uniform( "baseTexture", 1 ) )

#if 0 # Could be useful with Fixed Vertex Pipeline
        texGen = osg.TexGen()
        texGen.setMode( osg.TexGen.SPHERE_MAP )

        # Texture states applied
        ss.setTextureAttributeAndModes( 1, texGen, osg.StateAttribute.ON )
#endif



    # Top center model usues osg.Program overriding VirtualProgram in model
    if  1  : 
        AddLabel( transformCenterTop, "Fixed Vertex + Simple Fragment osg.Program", offset )
        program = osg.Program()
        program.setName( "Trivial Fragment + Fixed Vertex Program" )

        transformCenterTop.getOrCreateStateSet( ).setAttributeAndModes
            ( program, osg.StateAttribute.ON | osg.StateAttribute.OVERRIDE )

        shader = osg.Shader( osg.Shader.FRAGMENT )
        shader.setName( "Trivial Fragment Shader" )
        shader.setShaderSource(
            "uniform sampler2D baseTexture                                          \n"
            "void main(void)                                                         \n"
            "                                                                       \n"
            "    gl_FragColor = gl_Color * texture2D( baseTexture,gl_TexCoord[0].xy)\n"
            "                                                                       \n"
            )

        program.addShader( shader )

    return transformCenterMiddle

########################################
# Shders not used in the example but left for fun if anyone wants to play 
char LightingVertexShaderSource[] = 
"# Forward declarations                                                    \n" #1
"                                                                           \n" #2
"void SpotLight( in int i, in vec3 eye, in vec3 position, in vec3 normal,   \n" #3
"            inout vec4 ambient, inout vec4 diffuse, inout vec4 specular ) \n" #4
"                                                                           \n" #5
"void PointLight( in int i, in vec3 eye, in vec3 position, in vec3 normal,  \n" #6
"            inout vec4 ambient, inout vec4 diffuse, inout vec4 specular ) \n" #7
"                                                                           \n" #8
"void DirectionalLight( in int i, in vec3 normal,                           \n" #9
"            inout vec4 ambient, inout vec4 diffuse, inout vec4 specular ) \n" #10
"                                                                           \n" #11
" int NumEnabledLights = 1                                            \n" #12
"                                                                           \n" #13
"void lighting( in vec3 position, in vec3 normal )                          \n" #14
"                                                                          \n" #15
"    vec3  eye = vec3( 0.0, 0.0, 1.0 )                                     \n" #16
"    #vec3  eye = -normalize(position)                                    \n" #17
"                                                                           \n" #18
"    # Clear the light intensity accumulators                              \n" #19
"    vec4 amb  = vec4(0.0)                                                 \n" #20
"    vec4 diff = vec4(0.0)                                                 \n" #21
"    vec4 spec = vec4(0.0)                                                 \n" #22
"                                                                           \n" #23
"    # Loop through enabled lights, compute contribution from each         \n" #24
"    for (int i = 0 i < NumEnabledLights i++)                             \n" #25
"                                                                          \n" #26
"       if gl_LightSource[i].position.w == 0.0 :                            \n" #27
"           DirectionalLight(i, normal, amb, diff, spec)                   \n" #28
"       elif gl_LightSource[i].spotCutoff == 180.0 :                     \n" #29
"           PointLight(i, eye, position, normal, amb, diff, spec)          \n" #30
"       else :                                                                \n" #31
"           SpotLight(i, eye, position, normal, amb, diff, spec)           \n" #32
"                                                                          \n" #33
"                                                                           \n" #34
"    gl_FrontColor = gl_FrontLightModelProduct.sceneColor +                 \n" #35
"                    amb * gl_FrontMaterial.ambient +                       \n" #36
"                    diff * gl_FrontMaterial.diffuse                       \n" #37
"                                                                           \n" #38
"    gl_FrontSecondaryColor = vec4(spec*gl_FrontMaterial.specular)         \n" #39
"                                                                           \n" #40
"    gl_BackColor = gl_FrontColor                                          \n" #41
"    gl_BackSecondaryColor = gl_FrontSecondaryColor                        \n" #42
"                                                                          \n"#43

char SpotLightShaderSource[] = 
"void SpotLight(in int i,                                                   \n" #1
"               in vec3 eye,                                                \n" #2
"               in vec3 position,                                           \n" #3
"               in vec3 normal,                                             \n" #4
"               inout vec4 ambient,                                         \n" #5
"               inout vec4 diffuse,                                         \n" #6
"               inout vec4 specular)                                        \n" #7
"                                                                          \n" #8
"    float nDotVP          # normal . light direction                     \n" #9
"    float nDotHV          # normal . light half vector                   \n" #10
"    float pf              # power factor                                 \n" #11
"    float spotDot         # cosine of angle between spotlight            \n" #12
"    float spotAttenuation # spotlight attenuation factor                 \n" #13
"    float attenuation     # computed attenuation factor                  \n" #14
"    float d               # distance from surface to light source        \n" #15
"    vec3 VP               # direction from surface to light position     \n" #16
"    vec3 halfVector       # direction of maximum highlights              \n" #17
"                                                                           \n" #18
"    # Compute vector from surface to light position                       \n" #19
"    VP = vec3(gl_LightSource[i].position) - position                      \n" #20
"                                                                           \n" #21
"    # Compute distance between surface and light position                 \n" #22
"    d = length(VP)                                                        \n" #23
"                                                                           \n" #24
"    # Normalize the vector from surface to light position                 \n" #25
"    VP = normalize(VP)                                                    \n" #26
"                                                                           \n" #27
"    # Compute attenuation                                                 \n" #28
"    attenuation = 1.0 / (gl_LightSource[i].constantAttenuation +           \n" #29
"                         gl_LightSource[i].linearAttenuation * d +         \n" #30
"                         gl_LightSource[i].quadraticAttenuation *d*d)     \n" #31
"                                                                           \n" #32
"    # See if point on surface is inside cone of illumination              \n" #33
"    spotDot = dot(-VP, normalize(gl_LightSource[i].spotDirection))        \n" #34
"                                                                           \n" #35
"    if spotDot < gl_LightSource[i].spotCosCutoff :                         \n" #36
"        spotAttenuation = 0.0 # light adds no contribution               \n" #37
"    else :                                                                   \n" #38
"        spotAttenuation = pow(spotDot, gl_LightSource[i].spotExponent)    \n" #39
"                                                                           \n" #40
"    # Combine the spotlight and distance attenuation.                     \n" #41
"    attenuation *= spotAttenuation                                        \n" #42
"                                                                           \n" #43
"    halfVector = normalize(VP + eye)                                      \n" #44
"                                                                           \n" #45
"    nDotVP = max(0.0, dot(normal, VP))                                    \n" #46
"    nDotHV = max(0.0, dot(normal, halfVector))                            \n" #47
"                                                                           \n" #48
"    if nDotVP == 0.0 :                                                     \n" #49
"        pf = 0.0                                                          \n" #50
"    else :                                                                   \n" #51
"        pf = pow(nDotHV, gl_FrontMaterial.shininess)                      \n" #52
"                                                                           \n" #53
"    ambient  += gl_LightSource[i].ambient * attenuation                   \n" #54
"    diffuse  += gl_LightSource[i].diffuse * nDotVP * attenuation          \n" #55
"    specular += gl_LightSource[i].specular * pf * attenuation             \n" #56
"                                                                          \n"#57

char PointLightShaderSource[] = 
"void PointLight(in int i,                                                  \n" #1
"                in vec3 eye,                                               \n" #2
"                in vec3 position,                                          \n" #3
"                in vec3 normal,                                            \n" #4
"                inout vec4 ambient,                                        \n" #5
"                inout vec4 diffuse,                                        \n" #6
"                inout vec4 specular)                                       \n" #7
"                                                                          \n" #8
"    float nDotVP      # normal . light direction                         \n" #9
"    float nDotHV      # normal . light half vector                       \n" #10
"    float pf          # power factor                                     \n" #11
"    float attenuation # computed attenuation factor                      \n" #12
"    float d           # distance from surface to light source            \n" #13
"    vec3  VP          # direction from surface to light position         \n" #14
"    vec3  halfVector  # direction of maximum highlights                  \n" #15
"                                                                           \n" #16
"    # Compute vector from surface to light position                       \n" #17
"    VP = vec3(gl_LightSource[i].position) - position                      \n" #18
"                                                                           \n" #19
"    # Compute distance between surface and light position                 \n" #20
"    d = length(VP)                                                        \n" #21
"                                                                           \n" #22
"    # Normalize the vector from surface to light position                 \n" #23
"    VP = normalize(VP)                                                    \n" #24
"                                                                           \n" #25
"    # Compute attenuation                                                 \n" #26
"    attenuation = 1.0 / (gl_LightSource[i].constantAttenuation +           \n" #27
"                         gl_LightSource[i].linearAttenuation * d +         \n" #28
"                         gl_LightSource[i].quadraticAttenuation * d*d)    \n" #29
"                                                                           \n" #30
"    halfVector = normalize(VP + eye)                                      \n" #31
"                                                                           \n" #32
"    nDotVP = max(0.0, dot(normal, VP))                                    \n" #33
"    nDotHV = max(0.0, dot(normal, halfVector))                            \n" #34
"                                                                           \n" #35
"    if nDotVP == 0.0 :                                                     \n" #36
"        pf = 0.0                                                          \n" #37
"    else :                                                                   \n" #38
"        pf = pow(nDotHV, gl_FrontMaterial.shininess)                      \n" #39
"                                                                           \n" #40
"    ambient += gl_LightSource[i].ambient * attenuation                    \n" #41
"    diffuse += gl_LightSource[i].diffuse * nDotVP * attenuation           \n" #42
"    specular += gl_LightSource[i].specular * pf * attenuation             \n" #43
"                                                                          \n"#44

char DirectionalLightShaderSource[] =
"void DirectionalLight(in int i,                                            \n" #1
"                      in vec3 normal,                                      \n" #2
"                      inout vec4 ambient,                                  \n" #3
"                      inout vec4 diffuse,                                  \n" #4
"                      inout vec4 specular)                                 \n" #5
"                                                                          \n" #6
"     float nDotVP         # normal . light direction                     \n" #7
"     float nDotHV         # normal . light half vector                   \n" #8
"     float pf             # power factor                                 \n" #9
"                                                                           \n" #10
"     nDotVP = max(0.0, dot(normal,                                         \n" #11
"                normalize(vec3(gl_LightSource[i].position))))             \n" #12
"     nDotHV = max(0.0, dot(normal,                                         \n" #13
"                      vec3(gl_LightSource[i].halfVector)))                \n" #14
"                                                                           \n" #15
"     if nDotVP == 0.0 :                                                    \n" #16
"         pf = 0.0                                                         \n" #17
"     else :                                                                  \n" #18
"         pf = pow(nDotHV, gl_FrontMaterial.shininess)                     \n" #19
"                                                                           \n" #20
"     ambient  += gl_LightSource[i].ambient                                \n" #21
"     diffuse  += gl_LightSource[i].diffuse * nDotVP                       \n" #22
"     specular += gl_LightSource[i].specular * pf                          \n" #23
"                                                                          \n"#24


# Translated from file 'CreateSimpleHierachy.cpp'

#include <iostream>
#include <osg/Geode>
#include <osg/TexGen>
#include <osg/Texture2D>
#include <osg/MatrixTransform>
#include <osgDB/ReadFile>
#include <osgViewer/Viewer>

#include "VirtualProgram.h"

using osgCandidate.VirtualProgram

########################################
def CreateSimpleHierarchy(node):
    
    if  !node  : return NULL
    r = node.getBound().radius() # diameter
    root = osg.Group()
    group = osg.Group()

    # Create four matrices for translated instances of the cow
    transform0 = osg.MatrixTransform( )
    transform0.setMatrix( osg.Matrix.translate( 0,0,r ) )

    transform1 = osg.MatrixTransform( )
    transform1.setMatrix( osg.Matrix.translate( 0,0,0 ) )

    transform2 = osg.MatrixTransform( )
    transform2.setMatrix( osg.Matrix.translate( -r,0,-r ) )

    transform3 = osg.MatrixTransform( )
    transform3.setMatrix( osg.Matrix.translate(  r,0,-r ) )

    root.addChild( transform0 )
    root.addChild( group )
    group.addChild( transform1 )
    group.addChild( transform2 )
    group.addChild( transform3 )

    transform0.addChild( node )
    transform1.addChild( node )
    transform2.addChild( node )
    transform3.addChild( node )

    # At the scene root apply standard program 
    if  1  :
        program = osg.Program()
        main = osg.Shader( osg.Shader.FRAGMENT )

        main.setShaderSource(
            "uniform sampler2D base \n"
            "void main(void) \n"
            "\n"
            "    gl_FragColor = gl_Color * texture2DProj( base, gl_TexCoord[0] )\n"
            "    gl_FragColor *= vec4( 1.0, 1.0, 1.0, 0.5 ) \n"
            "\n"
            )
        program.addShader( main )

        main.setName( "White" ) 

        root.getOrCreateStateSet( ).setAttributeAndModes( program )

    # Now override root program with default VirtualProgram for three bottom cows
    if  1  :
        virtualProgram = VirtualProgram( )

        # Create main shader which declares and calls ColorFilter function 
        main = osg.Shader( osg.Shader.FRAGMENT )

        main.setShaderSource( 
            "vec4 ColorFilter( in vec4 color ) \n"
            "uniform sampler2D base \n"
            "void main(void) \n"
            " \n"
            "    gl_FragColor = gl_Color * texture2DProj( base, gl_TexCoord[0] ) \n"
            "    gl_FragColor = ColorFilter( gl_FragColor ) \n"
            "\n"
            )

        virtualProgram.setShader( "main", main )

        main.setName( "Virtual Main" )

        # Create filter shader which implements greem ColorFilter function 
        colorFilter = osg.Shader( osg.Shader.FRAGMENT )

        colorFilter.setShaderSource(       
            "vec4 ColorFilter( in vec4 color ) \n"
            " \n"
            "    return color * vec4( 0.0, 1.0, 0.0, 1.0 ) \n"
            "\n"
            )

        colorFilter.setName( "Virtual Green" )

        virtualProgram.setShader( "ColorFilter", colorFilter )

        group.getOrCreateStateSet( ).setAttributeAndModes( virtualProgram )

    # Create "incomplete" VirtualProgram overriding ColorFilter function
    # Lower left cow drawn will be red
    if  1  :
        virtualProgram = VirtualProgram()
      
        redFilter = osg.Shader( osg.Shader.FRAGMENT )
        redFilter.setShaderSource( 
            "vec4 ColorFilter( in vec4 color ) \n"
            " \n"
            "    return color * vec4( 1, 0, 0, 1 ) \n"
            "\n"
            )
        virtualProgram.setShader( "ColorFilter", redFilter )

        redFilter.setName( "Virtual Red" )

        transform2.getOrCreateStateSet( ).setAttribute( virtualProgram )

    # Create "incomplete" VirtualProgram overriding ColorFilter function
    # Lower right cow will be drawn with grid pattern on yellow background
    if  1  :
        virtualProgram = VirtualProgram()

        gridFilter = osg.Shader( osg.Shader.FRAGMENT )
        gridFilter.setShaderSource(         
            "vec4 ColorFilter( in vec4 color ) \n"
            " \n"
            "    vec2 grid = clamp( mod( gl_FragCoord.xy, 16.0 ), 0.0, 1.0 ) \n"
            "    return color * vec4( grid, 0.0, 1.0 ) \n"
            "\n"
            )
        virtualProgram.setShader( "ColorFilter", gridFilter )

        gridFilter.setName( "Virtual Grid" )
       
        transform3.getOrCreateStateSet( ).setAttribute( virtualProgram )

    return root
#####################

# Translated from file 'osgvirtualprogram.cpp'

#include <iostream>
#include <osg/Geode>
#include <osg/TexGen>
#include <osg/Texture2D>
#include <osg/MatrixTransform>
#include <osgDB/ReadFile>
#include <osgViewer/Viewer>
#include <osg/ShapeDrawable>
#include <osg/Material>

extern osg.Node * CreateSimpleHierarchy( osg.Node * model )
extern osg.Node * CreateAdvancedHierarchy( osg.Node * model )

########################################
osg.Node * CreateGlobe( void )
    # File not found - create textured sphere 
    geode = osg.Geode()
    hints = osg.TessellationHints()
    hints.setDetailRatio( 0.3 )

#if 1
    shape = osg.ShapeDrawable
        ( osg.Sphere(osg.Vec3(0.0, 0.0, 0.0), 4.0 ), hints.get() )
#else :
    shape = osg.ShapeDrawable
        ( osg.Box( osg.Vec3(-1.0, -1.0, -1.0), 2.0, 2.0, 2.0 ) )
#endif

    shape.setColor(osg.Vec4(0.8, 0.8, 0.8, 1.0))

    geode.addDrawable( shape.get() )

    stateSet = osg.StateSet()

    texture = osg.Texture2D( 
        osgDB.readImageFile("Images/land_shallow_topo_2048.jpg") 
    )

    material = osg.Material()

    material.setAmbient
        ( osg.Material.FRONT_AND_BACK, osg.Vec4( 0.9, 0.9, 0.9, 1.0 ) )

    material.setDiffuse
        ( osg.Material.FRONT_AND_BACK, osg.Vec4( 0.9, 0.9, 0.9, 1.0 ) )

#if 1
    material.setSpecular
        ( osg.Material.FRONT_AND_BACK, osg.Vec4( 0.7, 0.3, 0.3, 1.0 ) )

    material.setShininess( osg.Material.FRONT_AND_BACK, 25 )

#endif

    stateSet.setAttributeAndModes( material )
    stateSet.setTextureAttributeAndModes( 0,texture, osg.StateAttribute.ON )

    geode.setStateSet( stateSet )
    return geode
########################################
def main(argc, argv):
    
    # construct the viewer.
    arguments = osg.ArgumentParser( argc, argv )
    viewer = osgViewer.Viewer( arguments )

    useSimpleExample = arguments.read("-s") || arguments.read("--simple") 

    model = NULL

    if arguments.argc()>1  !arguments.isOption(1)  : 
        filename = arguments[1]
        model = osgDB.readNodeFile( filename )
        if  !model  : 
            osg.notify( osg.NOTICE ), "Error, cannot read ", filename, ". Loading default earth model instead."

    if  model == NULL  :
        model = CreateGlobe( )

    node = useSimpleExample ?        
        CreateSimpleHierarchy( model ):
        CreateAdvancedHierarchy( model )

    viewer.setSceneData( node )
    viewer.realize(  )
    viewer.run()

    return 0

# Translated from file 'VirtualProgram.cpp'

########################################
#include<osg/Shader>
#include<osg/Program>
#include<osg/State>
#include<osg/Notify>
#include<cassert>

########################################
#include "VirtualProgram.h"

using namespace osg

# If graphics board has program linking problems set MERGE_SHADERS to 1
# Merge shaders can be used to merge shaders strings into one shader. 
#define MERGE_SHADERS 0
#define NOTIFICATION_MESSAGES 0

namespace osgCandidate 
########################################
VirtualProgram.VirtualProgram( unsigned int mask ) : _mask( mask ) 
########################################
VirtualProgram.VirtualProgram
    (  VirtualProgram VirtualProgram,  osg.CopyOp copyop ):
       osg.Program( VirtualProgram, copyop ),
       _shaderMap( VirtualProgram._shaderMap ),
       _mask( VirtualProgram._mask )
########################################
VirtualProgram.~VirtualProgram( void )
########################################
osg.Shader * VirtualProgram.getShader
    (  str  shaderSemantic, osg.Shader.Type type )
    key = ShaderMap.key_type( shaderSemantic, type )

    return _shaderMap[ key ].get()
########################################
osg.Shader * VirtualProgram.setShader
(  str  shaderSemantic, osg.Shader * shader )
    if  shader.getType() == osg.Shader.UNDEFINED  : 
        return NULL

    key = ShaderMap.key_type( shaderSemantic, shader.getType() )

    shaderNew = shader
    ref_ptr< osg.Shader >  shaderCurrent = _shaderMap[ key ]

#if 0 # Good for debugging of shader linking problems. 
      # Don't do it - User could use the name for its own purposes 
    shaderNew.setName( shaderSemantic )
#endif

    if  shaderCurrent != shaderNew  : 
#if 0
       if  shaderCurrent.valid()  :
           Program.removeShader( shaderCurrent.get() )

       if  shaderNew.valid()  :
           Program.addShader( shaderNew.get() )
#endif
       shaderCurrent = shaderNew

    return shaderCurrent.get()
########################################
void VirtualProgram.apply( osg.State  state ) 
    if  _shaderMap.empty()  : # Virtual Program works as normal Program
        return Program.apply( state )

    av = state.getAttributeVec(this)

#if NOTIFICATION_MESSAGES
    os = osg.notify( osg.NOTICE )
    os, "VirtualProgram cumulate Begin"
#endif

    shaderMap = ShaderMap()
    for( State.AttributeVec.iterator i = av.begin() i != av.end() ++i )
        sa = i.first
        vp = dynamic_cast<  VirtualProgram *>( sa )
        if  vp  ( vp._mask  _mask )  : 

#if NOTIFICATION_MESSAGES
            if  vp.getName().empty()  :
                os, "VirtualProgram cumulate [ Unnamed VP ] apply"
            else : 
                os, "VirtualProgram cumulate [", vp.getName(), "] apply"
#endif

            for( ShaderMap.const_iterator i = vp._shaderMap.begin()
                                           i != vp._shaderMap.end() ++i )
                                                    shaderMap[ i.first ] = i.second

         else : 
#if NOTIFICATION_MESSAGES
            os, "VirtualProgram cumulate ( not VP or mask not match ) ignored"
#endif
            continue # ignore osg.Programs

    for( ShaderMap.const_iterator i = this._shaderMap.begin()
                                   i != this._shaderMap.end() ++i )
                                        shaderMap[ i.first ] = i.second

#if NOTIFICATION_MESSAGES
    os, "VirtualProgram cumulate End"
#endif

    if  shaderMap.size()  : 

        sl = ShaderList()
        for( ShaderMap.iterator i = shaderMap.begin() i != shaderMap.end() ++i )
            sl.push_back( i.second )

         osg.Program   program = _programMap[ sl ]

        if  !program.valid()  : 
            program = osg.Program()
#if !MERGE_SHADERS
            for( ShaderList.iterator i = sl.begin() i != sl.end() ++i )
                program.addShader( i.get() )
#else :
            strFragment = str()
            strVertex = str()
            strGeometry = str()
            
            for( ShaderList.iterator i = sl.begin() i != sl.end() ++i )
                if  i.get().getType() == osg.Shader.FRAGMENT  :
                    strFragment += i.get().getShaderSource()
                elif  i.get().getType() == osg.Shader.VERTEX  :
                    strVertex += i.get().getShaderSource()
                elif  i.get().getType() == osg.Shader.GEOMETRY  :
                    strGeometry += i.get().getShaderSource()

            if  strFragment.length() > 0  : 
                program.addShader( osg.Shader( osg.Shader.FRAGMENT, strFragment ) )
#if NOTIFICATION_MESSAGES
                os, "====VirtualProgram merged Fragment Shader:", strFragment, "===="
#endif

            if  strVertex.length() > 0   : 
                program.addShader( osg.Shader( osg.Shader.VERTEX, strVertex ) )
#if NOTIFICATION_MESSAGES
                os, "VirtualProgram merged Vertex Shader:", strVertex, "===="
#endif

            if  strGeometry.length() > 0   : 
                program.addShader( osg.Shader( osg.Shader.GEOMETRY, strGeometry ) )
#if NOTIFICATION_MESSAGES
                os, "VirtualProgram merged Geometry Shader:", strGeometry, "===="
#endif
#endif

        state.applyAttribute( program.get() )
     else : 
        Program.apply( state )

#if NOTIFICATION_MESSAGES
    os, "VirtualProgram Apply"
#endif

########################################
 # namespace osgExt

# Translated from file 'VirtualProgram.h'

#ifndef _VIRTUAL_PROGRAM__
#define _VIRTUAL_PROGRAM__ 1

#include<string>
#include<map>
#include<osg/Shader>
#include<osg/Program>

########################################
namespace osgCandidate 
########################################
class VirtualProgram (osg.Program) : 
    VirtualProgram( unsigned int mask = 0xFFFFFFFFUL )

    virtual ~VirtualProgram( void )

    VirtualProgram(  VirtualProgram VirtualProgram, 
                    copyop = osg.CopyOp.SHALLOW_COPY )

    META_StateAttribute( osgCandidate, VirtualProgram, Type( PROGRAM ) )

    #* return -1 if *this < *rhs, 0 if *this==*rhs, 1 if *this>*rhs.
    def compare(sa):
        
       # check the types are equal and then create the rhs variable
       # used by the COMPARE_StateAttribute_Parameter macros below.
       COMPARE_StateAttribute_Types(VirtualProgram,sa)

       # compare each parameter in turn against the rhs.
       COMPARE_StateAttribute_Parameter(_mask)
       COMPARE_StateAttribute_Parameter(_shaderMap)
       return 0 # passed all the above comparison macros, must be equal.

    #* If enabled, activate our program in the GL pipeline,
#     * performing any rebuild operations that might be pending. 
    virtual void  apply(osg.State state) 

    getShader = osg.Shader*(  str  shaderSemantic,
                                        osg.Shader.Type type )
    
    setShader = osg.Shader*(  str  shaderSemantic,
                                        osg.Shader * shader )
    typedef std.vector<  osg.Shader  >            ShaderList
    typedef std.pair< str, osg.Shader.Type >           ShaderSemantic
    typedef std.map< ShaderSemantic, osg.Shader > ShaderMap
    typedef std.map< ShaderList, osg.Program >    ProgramMap

    mutable ProgramMap                   _programMap
    _shaderMap = ShaderMap()
    _mask = unsigned int()
 # class VirtualProgram
########################################

 # namespace osgCandidate
########################################
#endif



if __name__ == "__main__":
    main(sys.argv)
