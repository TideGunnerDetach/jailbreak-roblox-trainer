cmake_minimum_required(VERSION 3.10)
project(jailbreak-roblox-trainer)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_executable(trainer
    src/main.cpp
    src/roblox/offsets.cpp
    src/roblox/memory.cpp
)

target_include_directories(trainer PRIVATE src)
target_link_libraries(trainer PRIVATE kernel32 user32)