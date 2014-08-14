find_path(OSG_DIR "include/osg/Vec2f")
find_path(OSG_INCLUDE_DIR "osg/Vec2f"
    PATHS ${OSG_DIR})
include_directories(${OSG_INCLUDE_DIR})
find_library(OSG_LIBRARY 
    NAME osg
    PATHS ${OSG_DIR}/lib
)

set(MODULE_OTHER_SRCS "")
OSGPYPP_WRAP_MODULE(osg)
target_link_libraries(osg ${OSG_LIBRARY})
