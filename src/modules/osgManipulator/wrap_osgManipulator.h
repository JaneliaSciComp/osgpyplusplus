/**
 * wrap_osgManipulator.h
 *
 * C++ header shared by all source files used to build _osgManipulator extension module in osgpyplusplus
 * OpenSceneGraph python API bindings.
 */

// default.h contains eaders shared by all osgpyplusplus modules
#include "../default.h"

// External headers needed for osgUtil classes to compile:
// <none yet>

// Full set of OSG 3.2.1 osgManipulator headers:
#include <osgManipulator/AntiSquish>
#include <osgManipulator/Command>
#include <osgManipulator/CommandManager>
#include <osgManipulator/Constraint>
#include <osgManipulator/Dragger>
#include <osgManipulator/Export>
#include <osgManipulator/Projector>
#include <osgManipulator/RotateCylinderDragger>
#include <osgManipulator/RotateSphereDragger>
#include <osgManipulator/Scale1DDragger>
#include <osgManipulator/Scale2DDragger>
#include <osgManipulator/ScaleAxisDragger>
#include <osgManipulator/Selection>
#include <osgManipulator/TabBoxDragger>
#include <osgManipulator/TabBoxTrackballDragger>
#include <osgManipulator/TabPlaneDragger>
#include <osgManipulator/TabPlaneTrackballDragger>
#include <osgManipulator/TrackballDragger>
#include <osgManipulator/Translate1DDragger>
#include <osgManipulator/Translate2DDragger>
#include <osgManipulator/TranslateAxisDragger>
#include <osgManipulator/TranslatePlaneDragger>
#include <osgManipulator/Version>

// Instantiate template classes that will be aliased farther down

// Aliases defined within this block will influence the generated wrapper source file names for those classes
namespace pyplusplus { namespace aliases {
}}
