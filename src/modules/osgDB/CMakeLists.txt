find_library(OSGDB_LIBRARY 
    NAME osgDB
    PATHS ${OSG_DIR}/lib
)

set(MODULE_OTHER_SRCS "")
OSGPYPP_WRAP_MODULE(osgDB)
target_link_libraries(osgDB 
    ${OSG_LIBRARY}
    ${OPENTHREADS_LIBRARY}
    ${OSGDB_LIBRARY})
