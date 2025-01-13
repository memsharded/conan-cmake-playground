cmake_minimum_required(VERSION 3.28)

project(pikachu LANGUAGES CXX)
include(GNUInstallDirs)

set(CMAKE_WINDOWS_EXPORT_ALL_SYMBOLS TRUE)

add_library(pikachu pikachu.cpp)

target_include_directories(pikachu
    PUBLIC
        $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
        $<INSTALL_INTERFACE:include> # see below
)

target_sources(pikachu
    PUBLIC
    FILE_SET HEADERS
    BASE_DIRS include
    FILES include/pikachu.h)


install(TARGETS pikachu
    EXPORT PikachuExports
    FILE_SET HEADERS
    INCLUDES DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
)

install(EXPORT PikachuExports
    DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/pikachu
    NAMESPACE Pikachu::
)

include(CMakePackageConfigHelpers)

configure_package_config_file(
    PikachuConfig.cmake.in PikachuConfig.cmake
    INSTALL_DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/pikachu
    NO_SET_AND_CHECK_MACRO
    NO_CHECK_REQUIRED_COMPONENTS_MACRO
)
install(FILES ${CMAKE_CURRENT_BINARY_DIR}/PikachuConfig.cmake
        DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/pikachu)
