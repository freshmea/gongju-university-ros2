# simple.launch.py
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription(
        [
            Node(
                package="arithmetic",
                executable="main",
                output="screen",
            ),
            Node(
                package="arithmetic",
                executable="arg",
                output="screen",
            ),
        ]
    )
