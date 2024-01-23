# simple.launch.py
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess, DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    param_dir = LaunchConfiguration(
        'param_dir',
        default=os.path.join(get_package_share_directory('gongju_ros'), 'param', 'turtlesim.yaml')
    )
    myparam =  LaunchConfiguration(
        'myparam',
        default=os.path.join(get_package_share_directory('gongju_ros'), 'param', 'myparam.yaml')
    )

    return LaunchDescription(
        [
            DeclareLaunchArgument(
                'param_dir',
                default_value=param_dir
            ),
            DeclareLaunchArgument(
                'myparam',
                default_value=myparam
            ),
            Node(
                package='turtlesim',
                executable='turtlesim_node',
                parameters=[param_dir],
                output='screen',
                ),
            ExecuteProcess(
                cmd=['ros2 service call',
                     '/spawn',
                     'turtlesim/srv/Spawn',
                     '"{x: 3, y: 7, theta: 0.2}"'],
                shell=True,
            ),
            Node(
                package='gongju_ros',
                executable='move_turtlesim',
                parameters=[myparam],
                output='screen',
                ),
        ]
        )