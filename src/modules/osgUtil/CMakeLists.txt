find_library(OSGUTIL_LIBRARY 
    NAME osgUtil
    PATHS ${OSG_DIR}/lib
)

set(MODULE_OTHER_SRCS "")
OSGPYPP_WRAP_MODULE(osgUtil)
target_link_libraries(osgUtil
    ${OSG_LIBRARY}
    ${OPENTHREADS_LIBRARY})
