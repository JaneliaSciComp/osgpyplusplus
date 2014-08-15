find_library(OSG_LIBRARY 
    NAME osg
    PATHS ${OSG_DIR}/lib
)

set(MODULE_OTHER_SRCS "")
OSGPYPP_WRAP_MODULE(osg)
target_link_libraries(osg ${OSG_LIBRARY})
