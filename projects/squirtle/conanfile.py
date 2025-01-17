import os

from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout, CMakeDeps
from conan.tools.microsoft import VCVars


class pikachuRecipe(ConanFile):
    name = "squirtle"
    version = "1.0"
    package_type = "application"
    exports_sources = "CMakeLists.txt", "*.cpp"

    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"


    def layout(self):
        cmake_layout(self)
    
    def generate(self):
        deps = CMakeDeps(self)
        deps.generate()
        tc = CMakeToolchain(self)
        tc.generate()
        VCVars(self).generate(scope="run")

    def requirements(self):
        self.requires("bulbasaur/1.0")

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        exe = os.path.join(self.cpp.build.bindir, "hello")
        self.run(exe, env="conanrun")
        if self.settings.os == "Linux":
            self.run(f"readelf -d {exe}")
        if self.settings.os == "Windows":
            self.run(f"dumpbin /DEPENDENTS {exe}.exe", env="conanrun")
