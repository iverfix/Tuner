cmake_minimum_required(VERSION 4.3.2)

project(Tuner)
add_executable(Tuner)

target_sources(Tuner PRIVATE main.cpp)
target_compile_features(Tuner PRIVATE cxx_std_23)
