from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    pkg_path = get_package_share_directory('prime_calculation_timer')
    yaml_path = os.path.join(pkg_path, 'params.yaml')
    print(yaml_path)
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
            parameters=[yaml_path]
        )
    ])
