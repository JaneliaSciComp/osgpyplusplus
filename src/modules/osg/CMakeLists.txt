set(MODULE_OTHER_SRCS "wrap_osg.h")
OSGPYPP_WRAP_MODULE(_osg)

find_library(OSG_OPENTHREADS_LIBRARY 
    NAME OpenThreads
    PATHS ${OSG_DIR}/lib
)
target_link_libraries(_osg ${OSG_OPENTHREADS_LIBRARY} ${OSG_LIBRARY})
