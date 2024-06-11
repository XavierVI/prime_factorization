#!/bin/bash

rosdep install -i --from-path src -y

colcon build

source install/setup.bash