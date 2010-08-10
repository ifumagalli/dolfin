set(DOLFIN_BOOST_INCLUDE_DIR "" CACHE PATH "Override the default location for Boost header files.")
set(DOLFIN_BOOST_LIBRARY_DIR "" CACHE PATH "Override the default location for Boost libraries.")
set(DOLFIN_BOOST_USE_MULTITHREADED OFF CACHE BOOL "Use multithreaded Boost libraries.")

set(BOOST_INCLUDEDIR ${DOLFIN_BOOST_INCLUDE_DIR})
set(BOOST_LIBRARYDIR ${DOLFIN_BOOST_LIBRARY_DIR})
set(Boost_ADDITIONAL_VERSIONS 1.43 1.43.0)
set(Boost_USE_MULTITHREADED ${DOLFIN_BOOST_USE_MULTITHREADED})
find_package(Boost 1.34 COMPONENTS ${DOLFIN_BOOST_COMPONENTS} REQUIRED)