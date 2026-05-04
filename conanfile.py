from conan import ConanFile
from conan.tools.cmake import cmake_layout


class TunerRecipie(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeDeps", "CMakeToolchain"

    def requirements(self):
        self.requires("portaudio/19.7")

    def layout(self):
        cmake_layout(self)
