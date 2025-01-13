import os
import platform
import shutil

############# CONFIGURATION ###########################
shared = False
charmander_header = False
#######################################################

def run(cmd):
    ret = os.system(cmd)
    if ret != 0:
        raise Exception(f"Failed CMD: {cmd}")

platform = platform.system().lower()

build_dir = os.path.join( os.path.dirname(os.path.realpath(__file__)), "build", platform)
install_dir = os.path.join( os.path.dirname(os.path.realpath(__file__)), "install", platform)
shutil.rmtree(build_dir, ignore_errors=True)
shutil.rmtree(install_dir, ignore_errors=True)

os.makedirs(build_dir, exist_ok=True)
os.makedirs(install_dir, exist_ok=True)

# Strict dependency order (pikachu <- charmander <- bulbasaur <- squirtle)
projects = ["pikachu", "charmander", "bulbasaur", "squirtle"]
project_base_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "projects")

dep_dirs = [f'-D{project.capitalize()}_ROOT="{install_dir}/{project}"' for project in projects]


shared_cmake = "-DBUILD_SHARED_LIBS=ON" if shared else ""
shared_conan = '-o "*:shared=True"' if shared else ""

charmander_header_cmake = "-DCHARMANDER_HEADER_ONLY=ON" if charmander_header else ""
charmander_header_conan = '-o "*:header_only=True"' if charmander_header else ""

print("***********************************************************")
print("********************** CMakeDeps **************************")
print("***********************************************************")
# Build using Conan CMakeDeps
for project in projects:
    run(f"conan create projects/{project} {shared_conan} {charmander_header_conan}")


print("***********************************************************")
print("********************** Pure CMAKE *************************")
print("***********************************************************")
# Build projects and use vanilla CMake-generated config and targets (no Conan involved)
for project in projects:
    defines = " ".join(dep_dirs)
    print(f"-----------------Project: {project}-----------------")
    run(f"cmake --fresh -S {project_base_dir}/{project} -B {build_dir}/{project} -DCMAKE_BUILD_TYPE=Release "
        f"-DCMAKE_INSTALL_PREFIX={install_dir}/{project} {defines} {shared_cmake} {charmander_header_cmake}")
    run(f"cmake --build {build_dir}/{project} --config Release")
    run(f"cmake --install {build_dir}/{project} --config Release")


print("***********************************************************")
print("******************** NEW CMakeDeps ************************")
print("***********************************************************")
# Build using Conan new experimental CMakeDeps
for project in projects:
    run(f"conan create projects/{project} {shared_conan} {charmander_header_conan} -c tools.cmake.cmakedeps:new=will_break_next")
