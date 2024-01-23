# simple.launch.py
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess

def generate_launch_description():
    return LaunchDescription(
        [
            Node(
                package='turtlesim',
                executable='turtlesim_node',
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
                output='screen',
                ),
        ]
        )