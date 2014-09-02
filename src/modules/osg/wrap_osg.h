#include "../default.h"

// TODO wrap more classes
#include <osg/Object> // OK
#include <osg/Referenced> // OK excluded copy methods
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
#include <osg/OcclusionQueryNode> // OK
#include <osg/TexGenNode> // OK
#include <osg/OcclusionQueryNode> // OK
#include <osg/Billboard> // OK
#include <osg/LOD> // OK
#include <osg/MatrixTransform> // OK
#include <osg/PagedLOD> // OK
#include <osg/ProxyNode> // OK
#include <osg/Geometry> // OK
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

// Disambiguate aliases for file names
template class std::vector<osg::Group*>;
template class std::vector<osg::Object*>;
template class std::vector<osg::Node*>;
template class std::vector<osg::StateSet*>;

// TODO - instantiate more VecXArray types
template class osg::TemplateArray< osg::Vec4, osg::Array::Vec4ArrayType, 4, GL_FLOAT >;
template class osg::TemplateArray< osg::Vec3, osg::Array::Vec3ArrayType, 3, GL_FLOAT >;

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

	typedef osg::BoundingSphereImpl< osg::Vec3f > BoundingSphereVec3f;
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

