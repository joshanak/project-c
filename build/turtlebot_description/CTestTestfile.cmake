# CMake generated Testfile for 
# Source directory: /home/petar/project_ws/src/turtlebot/turtlebot_description
# Build directory: /home/petar/project_ws/build/turtlebot_description
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(_ctest_turtlebot_description_gtest_turtlebot_description_test_urdf "/home/petar/project_ws/build/turtlebot_description/catkin_generated/env_cached.sh" "/usr/bin/python3" "/opt/ros/noetic/share/catkin/cmake/test/run_tests.py" "/home/petar/project_ws/build/turtlebot_description/test_results/turtlebot_description/gtest-turtlebot_description_test_urdf.xml" "--return-code" "/home/petar/project_ws/devel/.private/turtlebot_description/lib/turtlebot_description/turtlebot_description_test_urdf --gtest_output=xml:/home/petar/project_ws/build/turtlebot_description/test_results/turtlebot_description/gtest-turtlebot_description_test_urdf.xml")
set_tests_properties(_ctest_turtlebot_description_gtest_turtlebot_description_test_urdf PROPERTIES  _BACKTRACE_TRIPLES "/opt/ros/noetic/share/catkin/cmake/test/tests.cmake;160;add_test;/opt/ros/noetic/share/catkin/cmake/test/gtest.cmake;98;catkin_run_tests_target;/opt/ros/noetic/share/catkin/cmake/test/gtest.cmake;37;_catkin_add_google_test;/home/petar/project_ws/src/turtlebot/turtlebot_description/CMakeLists.txt;25;catkin_add_gtest;/home/petar/project_ws/src/turtlebot/turtlebot_description/CMakeLists.txt;0;")
subdirs("gtest")
