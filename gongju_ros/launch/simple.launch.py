# simple.launch.py
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription(
        [
            Node(
                package='gongju_ros',
                executable='simple_pub',
                output='screen',
                namespace='csk'
                ), 
            Node(
                package='gongju_ros',
                executable='simple_sub',
                output='screen',
                namespace='csk'
                ),
            Node(
                package='gongju_ros',
                executable='simple_time_pub',
                output='screen',
                namespace='csk'
                ),
            Node(
                package='gongju_ros',
                executable='simple_time_sub',
                output='screen',
                namespace='csk'
                )
        ]
        )