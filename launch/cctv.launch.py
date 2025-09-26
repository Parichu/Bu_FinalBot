from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='bu_fire_bot',
            executable='cctv_node.py',
            name='cctv_node',
            output='screen'
        ),
        Node(
            package='bu_fire_bot',
            executable='robot_nav.py',
            name='robot_nav',
            output='screen'
        )
    ])


