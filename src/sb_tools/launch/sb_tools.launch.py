from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
            Node(
                package='sb_tools',
                executable='color_publisher'
            ), 
            Node(
                package='sb_tools',
                namespace='color_publisherBlack',
                executable='color_publisher',
                parameters=[{'led_color_param':'Black'}]
            )
    ])

