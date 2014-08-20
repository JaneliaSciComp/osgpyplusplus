find_library(OSGGA_LIBRARY 
    NAME osgGA
    PATHS ${OSG_DIR}/lib
)

set(MODULE_OTHER_SRCS "")
OSGPYPP_WRAP_MODULE(osgGA)
target_link_libraries(osgGA 
    ${OSG_LIBRARY}
    ${OPENTHREADS_LIBRARY}
    ${OSGGA_LIBRARY})
