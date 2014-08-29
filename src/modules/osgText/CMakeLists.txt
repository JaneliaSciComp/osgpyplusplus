find_library(OSGTEXT_LIBRARY 
    NAME osgText
    PATHS ${OSG_DIR}/lib
)

set(MODULE_OTHER_SRCS "wrap_osgText.h")
OSGPYPP_WRAP_MODULE(osgText)
target_link_libraries(osgText 
    ${OPENTHREADS_LIBRARY}
    ${OSG_LIBRARY}
    ${OSGDB_LIBRARY}
    ${OSGTEXT_LIBRARY})

# Establish a linear chain of wrapper dependencies
# osg<-osgDB<-osgGA<-osgUtil<-osgText<-?
if(OSGPYPP_REGENERATE_BINDINGS)
	add_dependencies(Generate_osgText_WrapperSources Generate_osg_WrapperSources)
	add_dependencies(Generate_osgText_WrapperSources Generate_osgDB_WrapperSources)
endif()
