#include "../default.h"

// 2>C:\boost\include\boost-1_56\boost/type_traits/is_polymorphic.hpp(51) : error C2504: 'osg::ProxyNode' : base class undefined
#include <osg/CameraView>
#include <osg/ClipNode>
#include <osg/OcclusionQueryNode>
#include <osg/PositionAttitudeTransform>
#include <osg/ProxyNode>
#include <osg/Sequence>
#include <osg/TexGenNode>

// DONE - all osgAnimation include files included
// #include <osgAnimation/MorphGeometry> // compile errors on Win7

#include <osgAnimation/Action>
#include <osgAnimation/ActionAnimation>
#include <osgAnimation/ActionBlendIn>
#include <osgAnimation/ActionBlendOut>
#include <osgAnimation/ActionCallback>
#include <osgAnimation/ActionStripAnimation>
#include <osgAnimation/ActionVisitor>
#include <osgAnimation/Animation>
#include <osgAnimation/AnimationManagerBase>
#include <osgAnimation/AnimationUpdateCallback>
#include <osgAnimation/BasicAnimationManager>
#include <osgAnimation/Bone>
#include <osgAnimation/BoneMapVisitor>
#include <osgAnimation/Channel>
#include <osgAnimation/CubicBezier>
#include <osgAnimation/EaseMotion>
#include <osgAnimation/Export>
#include <osgAnimation/FrameAction>
#include <osgAnimation/Interpolator>
#include <osgAnimation/Keyframe>
#include <osgAnimation/LinkVisitor>
#include <osgAnimation/RigGeometry>
#include <osgAnimation/RigTransform>
#include <osgAnimation/RigTransformHardware>
#include <osgAnimation/RigTransformSoftware>
#include <osgAnimation/Sampler>
#include <osgAnimation/Skeleton>
#include <osgAnimation/StackedMatrixElement>
#include <osgAnimation/StackedQuaternionElement>
#include <osgAnimation/StackedRotateAxisElement>
#include <osgAnimation/StackedScaleElement>
#include <osgAnimation/StackedTransform>
#include <osgAnimation/StackedTransformElement>
#include <osgAnimation/StackedTranslateElement>
#include <osgAnimation/StatsHandler>
#include <osgAnimation/StatsVisitor>
#include <osgAnimation/Target>
#include <osgAnimation/Timeline>
#include <osgAnimation/TimelineAnimationManager>
#include <osgAnimation/UpdateBone>
#include <osgAnimation/UpdateMaterial>
#include <osgAnimation/UpdateMatrixTransform>
#include <osgAnimation/Vec3Packed>
#include <osgAnimation/VertexInfluence>


namespace pyplusplus { namespace aliases {
    // RuntimeError: `Py++` is going to write different content to the same file(F:\Users\cmbruns\git\osgpyplusplus\src\modules\osgAnimation\generated_code\_BoneWeight__value_traits.pypp.hpp).
    typedef osgAnimation::RigTransformSoftware::BoneWeight RTSBoneWeight;
    typedef osgAnimation::VertexInfluenceSet::BoneWeight VISBoneWeight;
}}

