#pragma once
#include <string>
#ifdef CHARMANDER_HEADER_ONLY
#endif

namespace charmander {
    #ifdef CHARMANDER_HEADER_ONLY
    void say_hello(const std::string& name) {
        std::cout << "Hello, " << name << "! - Charmander" << std::endl;
        pikachu::say_hello(name);       
    }
    #else
    void say_hello(const std::string& name);
    #endif
}
