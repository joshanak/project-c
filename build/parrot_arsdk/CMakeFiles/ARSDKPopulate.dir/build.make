# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.16

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/petar/project_ws/src/parrot_arsdk

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/petar/project_ws/build/parrot_arsdk

# Utility rule file for ARSDKPopulate.

# Include the progress variables for this target.
include CMakeFiles/ARSDKPopulate.dir/progress.make

CMakeFiles/ARSDKPopulate:
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/home/petar/project_ws/build/parrot_arsdk/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Populating ARDroneSDK to devel space: /home/petar/project_ws/build/parrot_arsdk/arsdk"
	cd /home/petar/project_ws/build/parrot_arsdk/arsdk/src/ARSDKBuildUtils && /usr/bin/cmake -E make_directory /home/petar/project_ws/devel/.private/parrot_arsdk/include/parrot_arsdk
	cd /home/petar/project_ws/build/parrot_arsdk/arsdk/src/ARSDKBuildUtils && cp -rp ./out/arsdk-native/staging/usr/include/* /home/petar/project_ws/devel/.private/parrot_arsdk/include/parrot_arsdk
	cd /home/petar/project_ws/build/parrot_arsdk/arsdk/src/ARSDKBuildUtils && /usr/bin/cmake -E make_directory /home/petar/project_ws/devel/.private/parrot_arsdk/lib/parrot_arsdk
	cd /home/petar/project_ws/build/parrot_arsdk/arsdk/src/ARSDKBuildUtils && cp -rp ./out/arsdk-native/staging/usr/lib/* /home/petar/project_ws/devel/.private/parrot_arsdk/lib/parrot_arsdk
	cd /home/petar/project_ws/build/parrot_arsdk/arsdk/src/ARSDKBuildUtils && /usr/bin/cmake -E make_directory /home/petar/project_ws/devel/.private/parrot_arsdk/share/parrot_arsdk/parrot_arsdk
	cd /home/petar/project_ws/build/parrot_arsdk/arsdk/src/ARSDKBuildUtils && cp -rp ./out/arsdk-native/staging/usr/share/* /home/petar/project_ws/devel/.private/parrot_arsdk/share/parrot_arsdk/parrot_arsdk

ARSDKPopulate: CMakeFiles/ARSDKPopulate
ARSDKPopulate: CMakeFiles/ARSDKPopulate.dir/build.make

.PHONY : ARSDKPopulate

# Rule to build all files generated by this target.
CMakeFiles/ARSDKPopulate.dir/build: ARSDKPopulate

.PHONY : CMakeFiles/ARSDKPopulate.dir/build

CMakeFiles/ARSDKPopulate.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/ARSDKPopulate.dir/cmake_clean.cmake
.PHONY : CMakeFiles/ARSDKPopulate.dir/clean

CMakeFiles/ARSDKPopulate.dir/depend:
	cd /home/petar/project_ws/build/parrot_arsdk && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/petar/project_ws/src/parrot_arsdk /home/petar/project_ws/src/parrot_arsdk /home/petar/project_ws/build/parrot_arsdk /home/petar/project_ws/build/parrot_arsdk /home/petar/project_ws/build/parrot_arsdk/CMakeFiles/ARSDKPopulate.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/ARSDKPopulate.dir/depend

