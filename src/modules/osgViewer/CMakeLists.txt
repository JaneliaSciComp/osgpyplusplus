find_library(OSGVIEWER_LIBRARY 
    NAME osgViewer
    PATHS ${OSG_DIR}/lib
)

set(MODULE_OTHER_SRCS "")
OSGPYPP_WRAP_MODULE(osgViewer)
target_link_libraries(osgViewer 
    ${OPENTHREADS_LIBRARY}
    ${OSG_LIBRARY}
    ${OSGGA_LIBRARY}
    ${OSGVIEWER_LIBRARY})
