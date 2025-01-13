#pragma once
#include <string>
#if defined(CHARMANDER_HEADER_ONLY)
#include "pikachu.h"
#include <iostream>
#include <string>
#endif

namespace charmander {
    #if defined(CHARMANDER_HEADER_ONLY)
    void say_hello(const std::string& name) {
        std::cout << "Hello, " << name << "! - Charmander" << std::endl;
        pikachu::say_hello(name);       
    }
    #else
    void say_hello(const std::string& name);
    #endif
}
