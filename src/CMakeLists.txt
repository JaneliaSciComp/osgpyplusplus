# Copy python source modules to staging area
file(COPY osgpyplusplus 
    DESTINATION ${STAGING_FOLDER})
# Copy binary exension modules into second level staging folder
set(MODULE_STAGING_FOLDER ${STAGING_FOLDER}/osgpyplusplus)
add_subdirectory(modules)
