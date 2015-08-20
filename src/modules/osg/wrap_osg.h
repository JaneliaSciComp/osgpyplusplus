#include "../default.h"

// Full set of OSG 3.2.1 osg headers below
#include <osg/AlphaFunc>
#include <osg/AnimationPath>
#include <osg/ApplicationUsage>
#include <osg/ArgumentParser>
#include <osg/Array>
#include <osg/ArrayDispatchers>
#include <osg/AudioStream>
#include <osg/AutoTransform>
#include <osg/Billboard>
#include <osg/BlendColor>
#include <osg/BlendEquation>
#include <osg/BlendFunc>
#include <osg/BoundingBox>
#include <osg/BoundingSphere>
#include <osg/BoundsChecking>
#include <osg/buffered_value>
#include <osg/BufferIndexBinding>
#include <osg/BufferObject>
#include <osg/Camera>
#include <osg/CameraNode>
#include <osg/CameraView>
#include <osg/ClampColor>
#include <osg/ClearNode>
#include <osg/ClipNode>
#include <osg/ClipPlane>
#include <osg/ClusterCullingCallback>
#include <osg/CollectOccludersVisitor>
#include <osg/ColorMask>
#include <osg/ColorMatrix>
#include <osg/ComputeBoundsVisitor>
#include <osg/Config>
#include <osg/ConvexPlanarOccluder>
#include <osg/ConvexPlanarPolygon>
#include <osg/CoordinateSystemNode>
#include <osg/CopyOp>
#include <osg/CullFace>
#include <osg/CullingSet>
#include <osg/CullSettings>
#include <osg/CullStack>
#include <osg/DeleteHandler>
#include <osg/Depth>
#include <osg/DisplaySettings>
#include <osg/Drawable>
#include <osg/DrawPixels>
#include <osg/Endian>
#include <osg/Export>
#include <osg/fast_back_stack>
#include <osg/Fog>
#include <osg/FragmentProgram>
#include <osg/FrameBufferObject>
#include <osg/FrameStamp>
#include <osg/FrontFace>
#include <osg/Geode>
#include <osg/Geometry>
#include <osg/GL>
#include <osg/GL2Extensions>
#include <osg/GLBeginEndAdapter>
#include <osg/GLExtensions>
#include <osg/GLObjects>
#include <osg/GLU>
#include <osg/GraphicsContext>
#include <osg/GraphicsCostEstimator>
#include <osg/GraphicsThread>
#include <osg/Group>
#include <osg/Hint>
#include <osg/Image>
#include <osg/ImageSequence>
#include <osg/ImageStream>
#include <osg/ImageUtils>
#include <osg/io_utils>
#include <osg/KdTree>
#include <osg/Light>
#include <osg/LightModel>
#include <osg/LightSource>
#include <osg/LineSegment>
#include <osg/LineStipple>
#include <osg/LineWidth>
#include <osg/LOD>
#include <osg/LogicOp>
#include <osg/Material>
#include <osg/Math>
#include <osg/Matrix>
#include <osg/Matrixd>
#include <osg/Matrixf>
#include <osg/MatrixTransform>
#include <osg/MixinVector>
#include <osg/Multisample>
#include <osg/Node>
#include <osg/NodeCallback>
#include <osg/NodeTrackerCallback>
#include <osg/NodeVisitor>
#include <osg/Notify>
#include <osg/Object>
#include <osg/Observer>
#include <osg/observer_ptr>
#include <osg/ObserverNodePath>
#include <osg/OccluderNode>
#include <osg/OcclusionQueryNode>
#include <osg/OperationThread>
#include <osg/PagedLOD>
#include <osg/PatchParameter>
#include <osg/Plane>
#include <osg/Point>
#include <osg/PointSprite>
#include <osg/PolygonMode>
#include <osg/PolygonOffset>
#include <osg/PolygonStipple>
#include <osg/Polytope>
#include <osg/PositionAttitudeTransform>
#include <osg/PrimitiveRestartIndex>
#include <osg/PrimitiveSet>
#include <osg/Program>
#include <osg/Projection>
#include <osg/ProxyNode>
#include <osg/Quat>
#include <osg/ref_ptr>
#include <osg/Referenced>
#include <osg/RenderInfo>
#include <osg/SampleMaski>
#include <osg/Scissor>
#include <osg/Sequence>
#include <osg/ShadeModel>
#include <osg/Shader>
#include <osg/ShaderAttribute>
#include <osg/ShaderComposer>
#include <osg/ShadowVolumeOccluder>
#include <osg/Shape>
#include <osg/ShapeDrawable>
#include <osg/State>
#include <osg/StateAttribute>
#include <osg/StateAttributeCallback>
#include <osg/StateSet>
#include <osg/Stats>
#include <osg/Stencil>
#include <osg/StencilTwoSided>
#include <osg/Switch>
#include <osg/TemplatePrimitiveFunctor>
#include <osg/TexEnv>
#include <osg/TexEnvCombine>
#include <osg/TexEnvFilter>
#include <osg/TexGen>
#include <osg/TexGenNode>
#include <osg/TexMat>
#include <osg/Texture>
#include <osg/Texture1D>
#include <osg/Texture2D>
#include <osg/Texture2DArray>
#include <osg/Texture2DMultisample>
#include <osg/Texture3D>
#include <osg/TextureBuffer>
#include <osg/TextureCubeMap>
#include <osg/TextureRectangle>
#include <osg/Timer>
#include <osg/TransferFunction>
#include <osg/Transform>
#include <osg/TriangleFunctor>
#include <osg/TriangleIndexFunctor>
#include <osg/Uniform>
#include <osg/UserDataContainer>
#include <osg/ValueObject>
#include <osg/Vec2>
#include <osg/Vec2b>
#include <osg/Vec2d>
#include <osg/Vec2f>
#include <osg/Vec2i>
#include <osg/Vec2s>
#include <osg/Vec2ub>
#include <osg/Vec2ui>
#include <osg/Vec2us>
#include <osg/Vec3>
#include <osg/Vec3b>
#include <osg/Vec3d>
#include <osg/Vec3f>
#include <osg/Vec3i>
#include <osg/Vec3s>
#include <osg/Vec3ub>
#include <osg/Vec3ui>
#include <osg/Vec3us>
#include <osg/Vec4>
#include <osg/Vec4b>
#include <osg/Vec4d>
#include <osg/Vec4f>
#include <osg/Vec4i>
#include <osg/Vec4s>
#include <osg/Vec4ub>
#include <osg/Vec4ui>
#include <osg/Vec4us>
#include <osg/Version>
#include <osg/VertexProgram>
#include <osg/View>
#include <osg/Viewport>


// Non-osg classes needed
template struct std::pair<double,double>; // needed by osg::GraphicsCostEstimator

// Disambiguate aliases for file names
template class std::vector<osg::Group*>;
template class std::vector<osg::Object*>;
template class std::vector<osg::Node*>;
template class std::vector<osg::StateSet*>;

template class osg::TemplateArray< osg::Vec4, osg::Array::Vec4ArrayType, 4, GL_FLOAT >;
template class osg::TemplateArray< osg::Vec3, osg::Array::Vec3ArrayType, 3, GL_FLOAT >;
template class osg::TemplateArray< osg::Vec2, osg::Array::Vec2ArrayType, 2, GL_FLOAT >;
// template class std::vector< osg::TemplateArray< osg::Vec3, osg::Array::Vec3ArrayType, 3, GL_FLOAT > >;

template class osg::TemplateArray< unsigned int, osg::Array::UIntArrayType, 4, 4 >;

template class osg::BoundingSphereImpl< osg::Vec3f >;

// template class std::map<std::pair<osg::StateAttribute::Type, unsigned int>, std::pair<osg::ref_ptr<osg::StateAttribute>, unsigned int>, std::less<std::pair<osg::StateAttribute::Type, unsigned int> >, std::allocator<std::pair<std::pair<osg::StateAttribute::Type, unsigned int> const, std::pair<osg::ref_ptr<osg::StateAttribute>, unsigned int> > > >;
namespace pyplusplus { namespace aliases {
	typedef std::pair<double,double> pair_double; // needed by osg::GraphicsCostEstimator

    typedef std::vector<osg::Group*> std_vector_osgGroupPtr;
    typedef std::vector<osg::Node*> std_vector_osgNodePtr;
    typedef std::vector<osg::Object*> std_vector_osgObjectPtr;
    typedef std::vector<osg::StateSet*> std_vector_osgStateSetPtr;
    typedef std::map<std::pair<osg::StateAttribute::Type, unsigned int>, std::pair<osg::ref_ptr<osg::StateAttribute>, unsigned int>, std::less<std::pair<osg::StateAttribute::Type, unsigned int> >, std::allocator<std::pair<std::pair<osg::StateAttribute::Type, unsigned int> const, std::pair<osg::ref_ptr<osg::StateAttribute>, unsigned int> > > > longClassName1;
	
	typedef osg::TemplateArray< osg::Vec4, osg::Array::Vec4ArrayType, 4, GL_FLOAT > Vec4Array;
	typedef osg::TemplateArray< osg::Vec3, osg::Array::Vec3ArrayType, 3, GL_FLOAT > Vec3Array;
	typedef osg::TemplateArray< osg::Vec2, osg::Array::Vec2ArrayType, 2, GL_FLOAT > Vec2Array;
    
    // typedef std::vector< osg::TemplateArray< osg::Vec3, osg::Array::Vec3ArrayType, 3, GL_FLOAT > > vector_Vec3Array;

	typedef osg::TemplateArray< unsigned int, osg::Array::UIntArrayType, 4, 4 > UIntArray;

	typedef osg::BoundingSphereImpl< osg::Vec3f > BoundingSphereVec3f;

	// Avoid multiply defined aliases
	typedef osg::FragmentProgram::MatrixList FragmentProgram_MatrixList;
	// typedef osg::CullStack::MatrixList CullStack_MatrixList;
	typedef osg::VertexProgram::MatrixList VertexProgram_MatrixList;
}}

// function(s) needed by indexing suite
namespace osg {

	inline bool operator==(
			const osg::GraphicsContext::ScreenSettings& lhs, 
			const osg::GraphicsContext::ScreenSettings& rhs) 
	{
		if (lhs.width != rhs.width) return false;
		if (lhs.height != rhs.height) return false;
		if (lhs.refreshRate != rhs.refreshRate) return false;
		if (lhs.colorDepth != rhs.colorDepth) return false;
		return true;
	}

	inline bool operator==(
			const osg::ConvexPlanarPolygon& lhs, 
			const osg::ConvexPlanarPolygon& rhs) 
	{
		if (lhs.getVertexList() != rhs.getVertexList()) return false;
		return true;
	}	
}
