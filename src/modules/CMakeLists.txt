# Python
find_package(PythonLibs REQUIRED)
mark_as_advanced(CLEAR PYTHON_INCLUDE_DIRS)
mark_as_advanced(CLEAR PYTHON_LIBRARIES)
include_directories(${PYTHON_INCLUDE_DIRS})
message(STATUS "Python version: ${PYTHONLIBS_VERSION_STRING}")
message(STATUS "Python library: ${PYTHON_LIBRARY_RELEASE}")

# Boost is required because we need boost python to build bindings
set(Boost_USE_STATIC_LIBS OFF)
set(Boost_USE_MULTITHREADED ON)
set(Boost_ADDITIONAL_VERSIONS 1.56 1.56.0)
find_package(Boost COMPONENTS python REQUIRED)
# Avoid exposing confusing Cmake variables
mark_as_advanced(Boost_DIR)
mark_as_advanced(Boost_LIB_DIAGNOSTIC_DEFINITIONS)
mark_as_advanced(CLEAR Boost_INCLUDE_DIR)
mark_as_advanced(CLEAR Boost_PYTHON_LIBRARY_DEBUG)
mark_as_advanced(CLEAR Boost_PYTHON_LIBRARY_RELEASE)

include_directories(${Boost_INCLUDE_DIR})

set(OSGPYPP_REGENERATE_BINDINGS FALSE CACHE BOOL "Whether to regenerate boost python C++ binding source code")

# For initial testing and debugging only...
add_subdirectory(greet)
