import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    
    # Ambil lokasi file konfigurasi joystick.yaml
    joy_params = os.path.join(get_package_share_directory('mcsoccer'), 'config', 'joystick.yaml')

    # 1. Node Driver Joystick (Membaca hardware)
    joy_node = Node(
        package='joy',
        executable='joy_node',
        parameters=[joy_params],
    )

    # 2. Node Teleop (Menerjemahkan tombol jadi cmd_vel)
    teleop_node = Node(
        package='teleop_twist_joy',
        executable='teleop_node',
        name='teleop_twist_joy_node',
        parameters=[joy_params],
        remappings=[('/cmd_vel', '/cmd_vel')] # Pastikan topiknya sesuai dengan plugin Gazebo
    )

    return LaunchDescription([
        joy_node,
        teleop_node
    ])
