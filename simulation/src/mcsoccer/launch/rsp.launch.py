import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.substitutions import Command
from launch_ros.actions import Node

def generate_launch_description():
    pkg_name = 'mcsoccer' 
    file_subpath = 'description/mcsoccer.urdf.xacro'

    # find xacro file location
    xacro_file = os.path.join(get_package_share_directory(pkg_name), file_subpath)

    # xacro to urdf
    robot_description_raw = Command(['xacro ', xacro_file])

    # Setup Node Robot State Publisher
    node_robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description': robot_description_raw,
                     'use_sim_time': True}] # Gazebo time sinc
    )

    # Return Launch Description
    return LaunchDescription([
        node_robot_state_publisher
    ])
