# About
This is a small project built to become more familiar with fundamental ROS concepts. This project creates two nodes with a publisher/subscriber relationship. The node 'timer_node' will publish a random integer and time how long it takes the second node, 'prime_factorizer_node' to find its prime factors. The value chosen for each random number is in the range [2, `max_size_int`]. The amount of elapsed time is measured in milliseconds and the `timer_node` will log the average time taken to factor each number after a number of iterations reaches a specific value (defined by the variable `last_iteration`).

Both `max_int_size` and `last_iteration` can be modified in the file located at `/prime_calculation_timer/params/params.yaml`.

# How to use
After cloning the repo, simply use `./build_and_run.bash`. This script uses `rosdep` to install required packages (if needed), then it will build the package and run the launch file.