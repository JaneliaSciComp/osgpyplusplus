#include "../default.h"

// TODO wrap more classes
#include <osg/Array>
// StateAttribute classes
#include <osg/StateAttribute>
#include <osg/AlphaFunc>
#include <osg/Billboard>
#include <osg/BlendColor>
#include <osg/BlendEquation>
#include <osg/BlendFunc>
#include <osg/BufferIndexBinding>
#include <osg/CameraView>
#include <osg/ClampColor>
#include <osg/ClipNode>
#include <osg/ClipPlane>
#include <osg/CoordinateSystemNode>
#include <osg/ColorMask>
#include <osg/ColorMatrix>
#include <osg/CullFace>
#include <osg/Depth>
#include <osg/Drawable>
#include <osg/DrawPixels>
#include <osg/Fog>
#include <osg/FragmentProgram>
#include <osg/FrameBufferObject>
#include <osg/FrontFace>
#include <osg/Geode>
#include <osg/Geometry> // OK
#include <osg/Hint>
#include <osg/Light>
#include <osg/LightModel>
#include <osg/LineStipple>
#include <osg/LineWidth>
#include <osg/LOD>
#include <osg/LogicOp>
#include <osg/Material>
#include <osg/MatrixTransform>
#include <osg/Multisample>
#include <osg/Object> // OK
#include <osg/OcclusionQueryNode>
#include <osg/PagedLOD>
#include <osg/PatchParameter>
#include <osg/Point>
#include <osg/PointSprite>
#include <osg/PolygonMode>
#include <osg/PolygonOffset>
#include <osg/PolygonStipple>
#include <osg/PositionAttitudeTransform>
#include <osg/PrimitiveRestartIndex>
#include <osg/Program>
#include <osg/ProxyNode>
#include <osg/Referenced> // OK excluded copy methods
#include <osg/SampleMaski>
#include <osg/Scissor>
#include <osg/Sequence>
#include <osg/ShadeModel>
#include <osg/ShaderAttribute>
#include <osg/ShapeDrawable>
#include <osg/Stencil>
#include <osg/StencilTwoSided>
#include <osg/TexEnv>
#include <osg/TexEnvCombine>
#include <osg/TexEnvFilter>
#include <osg/TexGen>
#include <osg/TexGenNode>
#include <osg/TexMat>
#include <osg/Texture>
#include <osg/VertexProgram>
#include <osg/Viewport>
// NodeVisitor classes
#include <osg/NodeVisitor>
#include <osg/CollectOccludersVisitor>
#include <osg/ComputeBoundsVisitor>
#include <osg/KdTree>
// 
#include <osg/Fog>
#include <osg/Vec4>
#include <osg/Vec3>
#include <osg/Vec2>
#include <osg/GL>
#include <osg/Texture2D> // OK
#include <osg/PositionAttitudeTransform> // OK
#include <osg/Sequence> // OK
#include <osg/Switch> // OK
#include <osg/CameraView> // OK
#include <osg/LightSource> // OK
#include <osg/CoordinateSystemNode> // OK
#include <osg/Projection> // OK
#include <osg/ClipNode> // OK
#include <osg/OccluderNode> // OK
#include <osg/TexGenNode> // OK
#include <osg/OcclusionQueryNode> // OK
#include <osg/Billboard> // OK
#include <osg/LOD> // OK
#include <osg/MatrixTransform> // OK
#include <osg/PagedLOD> // OK
#include <osg/ProxyNode> // OK
#include <osg/Uniform> // OK
#include <osg/Geode> // OK
#include <osg/View> // OK
#include <osg/Quat> // OK
#include <osg/Vec2f> // OK
#include <osg/CopyOp> // OK
#include <osg/UserDataContainer> // OK
#include <osg/Node> // OK
#include <osg/StateSet> // OK
#include <osg/Notify> // OK
#include <osg/Stats> // OK excluded getAttribute methods
#include <osg/Observer> // OK
#include <osg/DeleteHandler> // OK
#include <osg/Export> // OK
#include <osg/Version> // OK
#include <osg/io_utils>

// Disambiguate aliases for file names
template class std::vector<osg::Group*>;
template class std::vector<osg::Object*>;
template class std::vector<osg::Node*>;
template class std::vector<osg::StateSet*>;

template class osg::TemplateArray< osg::Vec4, osg::Array::Vec4ArrayType, 4, GL_FLOAT >;
template class osg::TemplateArray< osg::Vec3, osg::Array::Vec3ArrayType, 3, GL_FLOAT >;
template class osg::TemplateArray< osg::Vec2, osg::Array::Vec2ArrayType, 2, GL_FLOAT >;

template class osg::TemplateArray< unsigned int, osg::Array::UIntArrayType, 4, 4 >;

template class osg::BoundingSphereImpl< osg::Vec3f >;

// template class std::map<std::pair<osg::StateAttribute::Type, unsigned int>, std::pair<osg::ref_ptr<osg::StateAttribute>, unsigned int>, std::less<std::pair<osg::StateAttribute::Type, unsigned int> >, std::allocator<std::pair<std::pair<osg::StateAttribute::Type, unsigned int> const, std::pair<osg::ref_ptr<osg::StateAttribute>, unsigned int> > > >;
namespace pyplusplus { namespace aliases {
    typedef std::vector<osg::Group*> std_vector_osgGroupPtr;
    typedef std::vector<osg::Node*> std_vector_osgNodePtr;
    typedef std::vector<osg::Object*> std_vector_osgObjectPtr;
    typedef std::vector<osg::StateSet*> std_vector_osgStateSetPtr;
    typedef std::map<std::pair<osg::StateAttribute::Type, unsigned int>, std::pair<osg::ref_ptr<osg::StateAttribute>, unsigned int>, std::less<std::pair<osg::StateAttribute::Type, unsigned int> >, std::allocator<std::pair<std::pair<osg::StateAttribute::Type, unsigned int> const, std::pair<osg::ref_ptr<osg::StateAttribute>, unsigned int> > > > longClassName1;
	
	typedef osg::TemplateArray< osg::Vec4, osg::Array::Vec4ArrayType, 4, GL_FLOAT > Vec4Array;
	typedef osg::TemplateArray< osg::Vec3, osg::Array::Vec3ArrayType, 3, GL_FLOAT > Vec3Array;
	typedef osg::TemplateArray< osg::Vec2, osg::Array::Vec2ArrayType, 2, GL_FLOAT > Vec2Array;

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

// #include <osg/Matrixf>

