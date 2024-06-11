#!/bin/bash
rosdep install -i --from-path src -y
colcon build
source install/setup.bash
ros2 launch prime_calculation_timer prime_calculation_timer_launch.py