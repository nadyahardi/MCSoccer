import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import Command, LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    pkg_name = 'soccer_bot'
    file_subpath = 'urdf/robot.urdf.xacro'

    # Cari lokasi file xacro di sistem
    xacro_file = os.path.join(get_package_share_directory(pkg_name), file_subpath)

    # Proses file xacro menjadi urdf murni
    robot_description_raw = Command(['xacro ', xacro_file])

    # Node 1: Robot State Publisher (Penyiar bentuk robot)
    node_robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description': robot_description_raw}]
    )

    # Node 2: Joint State Publisher GUI (Slider untuk putar roda manual)
    node_joint_state_publisher = Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
        name='joint_state_publisher_gui'
    )

    # Node 3: RViz (Visualizer)
    node_rviz = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen'
    )

    return LaunchDescription([
        node_robot_state_publisher,
        node_joint_state_publisher,
        node_rviz,
    ])
