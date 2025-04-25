import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node 


def generate_launch_description():
    config_filepath = os.path.join(
        get_package_share_directory('bringup'),
        'config',
        'config.yaml'
    )

    joy_node = Node(
            package='joy',
            executable='joy_node',
            name='joy_node',
            parameters=[{
                'device_id': 0,
                'deadzone': 0.05,
                'autorepeat_rate': 20.0,
            }]
    )

    teleop_twist_joy_adv = Node(
        package='teleop_twist_joy',
        executable='teleop_node',
        name='teleop_twist_joy_adv',
        parameters=[config_filepath],
        remappings={('/cmd_vel', '/cmd_vel')},
        output='screen'
    )

    return LaunchDescription([
        joy_node,
        teleop_twist_joy_adv,
    ])