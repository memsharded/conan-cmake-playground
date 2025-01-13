cmake_minimum_required(VERSION 3.28)

project(charmander LANGUAGES CXX)
include(GNUInstallDirs)


find_package(Pikachu REQUIRED)

set(CMAKE_WINDOWS_EXPORT_ALL_SYMBOLS TRUE)

if(CHARMANDER_HEADER_ONLY)
    add_compile_definitions(CHARMANDER_HEADER_ONLY)
    add_library(charmander INTERFACE)
    target_link_libraries(charmander INTERFACE Pikachu::pikachu)
else()
    add_library(charmander charmander.cpp)

    target_include_directories(charmander
        PUBLIC
            $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
            $<INSTALL_INTERFACE:include> # see below
    )

    target_link_libraries(charmander PRIVATE Pikachu::pikachu)
endif()

target_sources(charmander
    PUBLIC
    FILE_SET HEADERS
    BASE_DIRS include
    FILES include/charmander.h)


install(TARGETS charmander
    EXPORT CharmanderExports
    FILE_SET HEADERS
    INCLUDES DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
)

install(EXPORT CharmanderExports
    DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/charmander
    NAMESPACE Charmander::
)

include(CMakePackageConfigHelpers)

configure_package_config_file(
    CharmanderConfig.cmake.in CharmanderConfig.cmake
    INSTALL_DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/charmander
    NO_SET_AND_CHECK_MACRO
    NO_CHECK_REQUIRED_COMPONENTS_MACRO
)
install(FILES ${CMAKE_CURRENT_BINARY_DIR}/CharmanderConfig.cmake
        DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/charmander)
