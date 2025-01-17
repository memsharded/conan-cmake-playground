# conan-cmake-playground
Some examples of Conan + CMakeDeps generators to troubleshoot linking issues


## static libraries

### old CMakeDeps

```
[100%] Linking CXX executable hello
/opt/cmake-3.30.5-linux-x86_64/bin/cmake -E cmake_link_script CMakeFiles/hello.dir/link.txt --verbose=1
/usr/bin/c++ -m64 -O3 -DNDEBUG -m64 CMakeFiles/hello.dir/print_hello.cpp.o -o hello   
-L/home/memsharded/.conan2/p/b/bulba9a72ce3ac2fc9/p/lib  
-L/home/memsharded/.conan2/p/b/charmed871fdc987c6/p/lib  
-L/home/memsharded/.conan2/p/b/pikacee1c4113186ed/p/lib  
-Wl,-rpath,/home/memsharded/.conan2/p/b/bulba9a72ce3ac2fc9/p/lib:/home/memsharded/.conan2/p/b/charmed871fdc987c6/p/lib:/home/memsharded/.conan2/p/b/pikacee1c4113186ed/p/lib 
/home/memsharded/.conan2/p/b/bulba9a72ce3ac2fc9/p/lib/libbulbasaur.a 
/home/memsharded/.conan2/p/b/charmed871fdc987c6/p/lib/libcharmander.a 
/home/memsharded/.conan2/p/b/pikacee1c4113186ed/p/lib/libpikachu.a
```

```
Dynamic section at offset 0x2d48 contains 30 entries:
  Tag        Type                         Name/Value
 0x0000000000000001 (NEEDED)             Shared library: [libstdc++.so.6]
 0x0000000000000001 (NEEDED)             Shared library: [libgcc_s.so.1]
 0x0000000000000001 (NEEDED)             Shared library: [libc.so.6]
 0x000000000000001d (RUNPATH)            Library runpath: [/home/memsharded/.conan2/p/b/bulba9a72ce3ac2fc9/p/lib:/home/memsharded/.conan2/p/b/charmed871fdc987c6/p/lib:/home/memsharded/.conan2/p/b/pikacee1c4113186ed/p/lib]
```

### pure CMake

```
[100%] Linking CXX executable hello
/opt/cmake-3.30.5-linux-x86_64/bin/cmake -E cmake_link_script CMakeFiles/hello.dir/link.txt --verbose=1
/usr/bin/c++ -O3 -DNDEBUG CMakeFiles/hello.dir/print_hello.cpp.o -o hello  
/mnt/c/Users/Diego/conanws/conan-cmake-playground/install/linux/bulbasaur/lib/libbulbasaur.a 
/mnt/c/Users/Diego/conanws/conan-cmake-playground/install/linux/charmander/lib/libcharmander.a 
/mnt/c/Users/Diego/conanws/conan-cmake-playground/install/linux/pikachu/lib/libpikachu.a
```

```
Dynamic section at offset 0x2d58 contains 29 entries:
  Tag        Type                         Name/Value
 0x0000000000000001 (NEEDED)             Shared library: [libstdc++.so.6]
 0x0000000000000001 (NEEDED)             Shared library: [libgcc_s.so.1]
 0x0000000000000001 (NEEDED)             Shared library: [libc.so.6]
 0x000000000000000c (INIT)               0x1000
 0x000000000000000d (FINI)               0x1650
```


### incubating CMakeDeps

```
[100%] Linking CXX executable hello
/opt/cmake-3.30.5-linux-x86_64/bin/cmake -E cmake_link_script CMakeFiles/hello.dir/link.txt --verbose=1
/usr/bin/c++ -m64 -O3 -DNDEBUG -m64 CMakeFiles/hello.dir/print_hello.cpp.o -o hello  
/home/memsharded/.conan2/p/b/bulba9a72ce3ac2fc9/p/lib/libbulbasaur.a 
/home/memsharded/.conan2/p/b/charmed871fdc987c6/p/lib/libcharmander.a 
/home/memsharded/.conan2/p/b/pikacee1c4113186ed/p/lib/libpikachu.a
```

```
Dynamic section at offset 0x2d58 contains 29 entries:
  Tag        Type                         Name/Value
 0x0000000000000001 (NEEDED)             Shared library: [libstdc++.so.6]
 0x0000000000000001 (NEEDED)             Shared library: [libgcc_s.so.1]
 0x0000000000000001 (NEEDED)             Shared library: [libc.so.6]
 0x000000000000000c (INIT)               0x1000
 0x000000000000000d (FINI)               0x1650
```



## shared libraries

### old CMakeDeps

```
[100%] Linking CXX executable hello
/opt/cmake-3.30.5-linux-x86_64/bin/cmake -E cmake_link_script CMakeFiles/hello.dir/link.txt --verbose=1
/usr/bin/c++ -m64 -O3 -DNDEBUG -m64 CMakeFiles/hello.dir/print_hello.cpp.o -o hello   
-L/home/memsharded/.conan2/p/b/bulbac8139c5804aac/p/lib  
-L/home/memsharded/.conan2/p/b/charma6ae9001b3b66/p/lib  
-L/home/memsharded/.conan2/p/b/pikaccddcbcddba2f9/p/lib  
-Wl,-rpath,/home/memsharded/.conan2/p/b/bulbac8139c5804aac/p/lib:/home/memsharded/.conan2/p/b/charma6ae9001b3b66/p/lib:/home/memsharded/.conan2/p/b/pikaccddcbcddba2f9/p/lib /home/memsharded/.conan2/p/b/bulbac8139c5804aac/p/lib/libbulbasaur.so
```

```
Dynamic section at offset 0x2d50 contains 31 entries:
  Tag        Type                         Name/Value
 0x0000000000000001 (NEEDED)             Shared library: [libbulbasaur.so]
 0x0000000000000001 (NEEDED)             Shared library: [libstdc++.so.6]
 0x0000000000000001 (NEEDED)             Shared library: [libgcc_s.so.1]
 0x0000000000000001 (NEEDED)             Shared library: [libc.so.6]
 0x000000000000001d (RUNPATH)            Library runpath: [/home/memsharded/.conan2/p/b/bulbac8139c5804aac/p/lib:/home/memsharded/.conan2/p/b/charma6ae9001b3b66/p/lib:/home/memsharded/.conan2/p/b/pikaccddcbcddba2f9/p/lib]
```


### pure CMake

```
[100%] Linking CXX executable hello
/opt/cmake-3.30.5-linux-x86_64/bin/cmake -E cmake_link_script CMakeFiles/hello.dir/link.txt --verbose=1
/usr/bin/c++ -O3 -DNDEBUG CMakeFiles/hello.dir/print_hello.cpp.o -o hello 

-Wl,-rpath,/mnt/c/Users/Diego/conanws/conan-cmake-playground/install/linux/bulbasaur/lib:/mnt/c/Users/Diego/conanws/conan-cmake-playground/install/linux/charmander/lib:/mnt/c/Users/Diego/conanws/conan-cmake-playground/install/linux/pikachu/lib 

/mnt/c/Users/Diego/conanws/conan-cmake-playground/install/linux/bulbasaur/lib/libbulbasaur.so 

-Wl,-rpath-link,/mnt/c/Users/Diego/conanws/conan-cmake-playground/install/linux/charmander/lib:/mnt/c/Users/Diego/conanws/conan-cmake-playground/install/linux/pikachu/lib
```

```
Dynamic section at offset 0x2d50 contains 31 entries:
  Tag        Type                         Name/Value
 0x0000000000000001 (NEEDED)             Shared library: [libbulbasaur.so]
 0x0000000000000001 (NEEDED)             Shared library: [libstdc++.so.6]
 0x0000000000000001 (NEEDED)             Shared library: [libgcc_s.so.1]
 0x0000000000000001 (NEEDED)             Shared library: [libc.so.6]
 0x000000000000001d (RUNPATH)            Library runpath: [/mnt/c/Users/Diego/conanws/conan-cmake-playground/install/linux/bulbasaur/lib:/mnt/c/Users/Diego/conanws/conan-cmake-playground/install/linux/charmander/lib:/mnt/c/Users/Diego/conanws/conan-cmake-playground/install/linux/pikachu/lib]
 0x000000000000000c (INIT)               0x1000
 0x000000000000000d (FINI)               0x130c
```


### incubating CMakeDeps


```
[100%] Linking CXX executable hello
/opt/cmake-3.30.5-linux-x86_64/bin/cmake -E cmake_link_script CMakeFiles/hello.dir/link.txt --verbose=1
/usr/bin/c++ -m64 -O3 -DNDEBUG -m64 CMakeFiles/hello.dir/print_hello.cpp.o -o hello  
-Wl,-rpath,/home/memsharded/.conan2/p/b/bulbac8139c5804aac/p/lib:/home/memsharded/.conan2/p/b/charma6ae9001b3b66/p/lib:/home/memsharded/.conan2/p/b/pikaccddcbcddba2f9/p/lib 
/home/memsharded/.conan2/p/b/bulbac8139c5804aac/p/lib/libbulbasaur.so 
/home/memsharded/.conan2/p/b/charma6ae9001b3b66/p/lib/libcharmander.so 
/home/memsharded/.conan2/p/b/pikaccddcbcddba2f9/p/lib/libpikachu.so
```

```
Dynamic section at offset 0x2d50 contains 31 entries:
  Tag        Type                         Name/Value
 0x0000000000000001 (NEEDED)             Shared library: [libbulbasaur.so]
 0x0000000000000001 (NEEDED)             Shared library: [libstdc++.so.6]
 0x0000000000000001 (NEEDED)             Shared library: [libgcc_s.so.1]
 0x0000000000000001 (NEEDED)             Shared library: [libc.so.6]
 0x000000000000001d (RUNPATH)            Library runpath: [/home/memsharded/.conan2/p/b/bulbac8139c5804aac/p/lib:/home/memsharded/.conan2/p/b/charma6ae9001b3b66/p/lib:/home/memsharded/.conan2/p/b/pikaccddcbcddba2f9/p/lib]
 0x000000000000000c (INIT)               0x1000
 0x000000000000000d (FINI)               0x130c
```
