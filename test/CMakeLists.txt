include(UsePythonTest)

# Value of PYTHONPATH variable for in-build-area testing.
set(TEST_PATH "${STAGING_FOLDER}")
file(TO_NATIVE_PATH TEST_PATH ${TEST_PATH})
set(TEST_PYTHON_PATH ${TEST_PATH} $ENV{PYTHONPATH})

# Run all the testWhatever.py programs
file(GLOB TEST_PROGS "*.py")
foreach(TEST_PROG ${TEST_PROGS})
    get_filename_component(TEST_ROOT ${TEST_PROG} NAME_WE)
    set_source_files_properties(${TEST_PROG} PROPERTIES PYTHONPATH "${TEST_PYTHON_PATH}")
    ADD_PYTHON_TEST("${TEST_ROOT}" ${TEST_PROG})
endforeach(TEST_PROG ${TEST_PROGS})
