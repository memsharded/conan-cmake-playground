set(CMAKE_VERBOSE_MAKEFILE ON)

cmake_minimum_required(VERSION 3.28)

project(squirtle LANGUAGES CXX)

find_package(Bulbasaur REQUIRED)
add_executable(hello print_hello.cpp)

target_link_libraries(hello PRIVATE Bulbasaur::bulbasaur)