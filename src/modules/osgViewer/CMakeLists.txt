find_library(OSGVIEWER_LIBRARY 
    NAME osgViewer
    PATHS ${OSG_DIR}/lib
)

set(MODULE_OTHER_SRCS "")
OSGPYPP_WRAP_MODULE(osgViewer)
target_link_libraries(osgViewer 
    ${OSG_LIBRARY}
    ${OPENTHREADS_LIBRARY}
    ${OSGVIEWER_LIBRARY})
