cmake_minimum_required(VERSION 3.28)

project(bulbasaur LANGUAGES CXX)
include(GNUInstallDirs)


find_package(Charmander REQUIRED)

set(CMAKE_WINDOWS_EXPORT_ALL_SYMBOLS TRUE)

add_library(bulbasaur bulbasaur.cpp)

target_include_directories(bulbasaur
    PUBLIC
        $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
        $<INSTALL_INTERFACE:include> # see below
)

target_link_libraries(bulbasaur PRIVATE Charmander::charmander)

# add_executable(hello-bulbasaur hello-bulbasaur.cpp)
# target_link_libraries(hello-bulbasaur PRIVATE bulbasaur)

target_sources(bulbasaur
    PUBLIC
    FILE_SET HEADERS
    BASE_DIRS include
    FILES include/bulbasaur.h)


install(TARGETS bulbasaur
    EXPORT BulbasaurExports
    FILE_SET HEADERS
    INCLUDES DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
)

install(EXPORT BulbasaurExports
    DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/bulbasaur
    NAMESPACE Bulbasaur::
)

include(CMakePackageConfigHelpers)

configure_package_config_file(
    BulbasaurConfig.cmake.in BulbasaurConfig.cmake
    INSTALL_DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/bulbasaur
    NO_SET_AND_CHECK_MACRO
    NO_CHECK_REQUIRED_COMPONENTS_MACRO
)
install(FILES ${CMAKE_CURRENT_BINARY_DIR}/BulbasaurConfig.cmake
        DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/bulbasaur)
