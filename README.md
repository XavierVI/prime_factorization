# About
This is a small project built to become more familiar with fundamental ROS concepts. This project creates two nodes with a publisher/subscriber relationship. The node 'timer_node' will publish a random integer and time how long it takes the second node, 'prime_factorizer_node' to find its prime factors. The amount of elapsed time is measured in milliseconds.

# How to use
After cloning the repo, run the following commands:
- `./build.bash`
- `ros2 launch prime_calculation_timer prime_calculation_timer_launch.py`