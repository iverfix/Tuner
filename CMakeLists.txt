cmake_minimum_required(VERSION 4.3.2)

project(Tuner)

find_package(portaudio REQUIRED)

add_executable(${PROJECT_NAME})
target_link_libraries(${PROJECT_NAME} portaudio)
target_sources(${PROJECT_NAME} PRIVATE main.cpp)
target_compile_features(${PROJECT_NAME} PRIVATE cxx_std_23)
