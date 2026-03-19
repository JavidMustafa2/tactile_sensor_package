from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='sensor_system',
            namespace='event_talker_1',
            executable='event_talker',
            name='event_talker',
            arguments=[]
        ),
        Node(
            package='sensor_system',
            namespace='event_listener_1',
            executable='event_listener',
            name='event_listener',
            arguments=[]
        )

    ])