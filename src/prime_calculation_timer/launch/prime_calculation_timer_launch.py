from launch import LaunchDescription
from launch_ros.actions import Node
import os

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='prime_calculation_timer',
            executable='prime_factorizer_node',
            name='prime_factorizer_node',
            output='screen',
            emulate_tty=True,
            parameters=[
            ]
        ),
        Node(
            package='prime_calculation_timer',
            executable='timer_node',
            name='timer_node',
            output='screen',
            emulate_tty=True,
            parameters=[
            ]
        )
    ])
