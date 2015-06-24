find_library(OSGUTIL_LIBRARY 
    NAME osgUtil
    PATHS ${OSG_DIR}/lib
)

set(MODULE_OTHER_SRCS "wrap_osgUtil.h")
OSGPYPP_WRAP_MODULE(_osgUtil)
target_link_libraries(_osgUtil
    ${OSG_LIBRARY}
    ${OPENTHREADS_LIBRARY}
    ${OSGUTIL_LIBRARY})

# Establish a linear chain of wrapper dependencies
# osg<-osgDB<-osgGA<-osgUtil<-osgViewer<-?
if(OSGPYPP_REGENERATE_BINDINGS)
	add_dependencies(Generate__osgUtil_WrapperSources Generate__osg_WrapperSources)
endif()
