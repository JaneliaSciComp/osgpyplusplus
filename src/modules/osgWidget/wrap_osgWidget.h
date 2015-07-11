/**
 * wrap_osgWidget.h
 *
 * C++ header shared by all source files used to build _osgWidget extension module in osgpyplusplus
 * OpenSceneGraph python API bindings.
 */

// default.h contains eaders shared by all osgpyplusplus modules
#include "../default.h"

// External headers needed for osgUtil classes to compile:
// <none yet>

// Full set of OSG 3.2.1 osgWidget headers:
#include <osgWidget/Box>
#include <osgWidget/Browser>
#include <osgWidget/Canvas>
#include <osgWidget/EventInterface>
#include <osgWidget/Export>
#include <osgWidget/Frame>
#include <osgWidget/Input>
#include <osgWidget/Label>
#include <osgWidget/Lua>
#include <osgWidget/PdfReader>
#include <osgWidget/Python>
#include <osgWidget/ScriptEngine>
#include <osgWidget/StyleInterface>
#include <osgWidget/StyleManager>
#include <osgWidget/Table>
#include <osgWidget/Types>
#include <osgWidget/UIObjectParent>
#include <osgWidget/Util>
#include <osgWidget/Version>
#include <osgWidget/ViewerEventHandlers>
#include <osgWidget/VncClient>
#include <osgWidget/Widget>
#include <osgWidget/Window>
#include <osgWidget/WindowManager>

// Avoid under-scoped symbols

// Instantiate template classes that will be aliased farther down

// Aliases defined within this block will influence the generated wrapper source file names for those classes
namespace pyplusplus { namespace aliases {
}}
