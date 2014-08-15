// This file has been generated by Py++.

#include "boost/python.hpp"

#include "__convenience.pypp.hpp"

#include "__call_policies.pypp.hpp"

#include "wrap_osg.h"

#include "f:/users/cmbruns/git/osgpyplusplus/src/modules/osg/generated_code/atomic.pypp.hpp"

#include "f:/users/cmbruns/git/osgpyplusplus/src/modules/osg/generated_code/atomicptr.pypp.hpp"

#include "f:/users/cmbruns/git/osgpyplusplus/src/modules/osg/generated_code/deletehandler.pypp.hpp"

#include "f:/users/cmbruns/git/osgpyplusplus/src/modules/osg/generated_code/mutex.pypp.hpp"

#include "f:/users/cmbruns/git/osgpyplusplus/src/modules/osg/generated_code/observer.pypp.hpp"

#include "f:/users/cmbruns/git/osgpyplusplus/src/modules/osg/generated_code/observerset.pypp.hpp"

#include "f:/users/cmbruns/git/osgpyplusplus/src/modules/osg/generated_code/osg_free_functions.pypp.hpp"

#include "f:/users/cmbruns/git/osgpyplusplus/src/modules/osg/generated_code/osg_global_variables.pypp.hpp"

#include "f:/users/cmbruns/git/osgpyplusplus/src/modules/osg/generated_code/quat.pypp.hpp"

#include "f:/users/cmbruns/git/osgpyplusplus/src/modules/osg/generated_code/referenced.pypp.hpp"

#include "f:/users/cmbruns/git/osgpyplusplus/src/modules/osg/generated_code/vec2d.pypp.hpp"

#include "f:/users/cmbruns/git/osgpyplusplus/src/modules/osg/generated_code/vec2f.pypp.hpp"

#include "f:/users/cmbruns/git/osgpyplusplus/src/modules/osg/generated_code/vec3d.pypp.hpp"

#include "f:/users/cmbruns/git/osgpyplusplus/src/modules/osg/generated_code/vec3f.pypp.hpp"

#include "f:/users/cmbruns/git/osgpyplusplus/src/modules/osg/generated_code/vec4d.pypp.hpp"

#include "f:/users/cmbruns/git/osgpyplusplus/src/modules/osg/generated_code/vec4f.pypp.hpp"

namespace bp = boost::python;

BOOST_PYTHON_MODULE(osg){
    register_Atomic_class();

    bp::implicitly_convertible< OpenThreads::Atomic, unsigned int >();

    register_AtomicPtr_class();

    register_Mutex_class();

    register_DeleteHandler_class();

    register_Observer_class();

    register_Referenced_class();

    register_ObserverSet_class();

    register_Quat_class();

    register_Vec2d_class();

    bp::implicitly_convertible< osg::Vec2d, osg::Vec2f >();

    register_Vec2f_class();

    register_Vec3d_class();

    bp::implicitly_convertible< osg::Vec3d, osg::Vec3f >();

    register_Vec3f_class();

    register_Vec4d_class();

    bp::implicitly_convertible< osg::Vec4d, osg::Vec4f >();

    register_Vec4f_class();

    register_global_variables();

    register_free_functions();
}

