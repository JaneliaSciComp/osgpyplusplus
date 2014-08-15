set(MODULE_OTHER_SRCS "")
OSGPYPP_WRAP_MODULE(osg)

find_library(OSG_OPENTHREADS_LIBRARY 
    NAME OpenThreads
    PATHS ${OSG_DIR}/lib
)
target_link_libraries(osg ${OSG_OPENTHREADS_LIBRARY})
