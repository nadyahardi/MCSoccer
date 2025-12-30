import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from launch.substitutions import Command

def generate_launch_description():
    pkg_name = 'soccer_bot'
    
    # 1. SETUP LOKASI FILE
    pkg_share = get_package_share_directory(pkg_name)
    urdf_file = os.path.join(pkg_share, 'urdf', 'robot.urdf.xacro')
    ros_gz_sim_pkg = get_package_share_directory('ros_gz_sim')

    # 2. PROSES URDF
    # Kita proses file xacro menjadi XML robot yang siap spawn
    robot_desc = Command(['xacro ', urdf_file])

    # 3. NODE: ROBOT STATE PUBLISHER
    # Agar ROS tahu bentuk robot kita
    node_robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description': robot_desc, 'use_sim_time': True}]
    )

    # 4. MEMBUKA GAZEBO (GZ SIM)
    # Kita panggil launch file bawaan Gazebo untuk membuka dunia kosong
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(ros_gz_sim_pkg, 'launch', 'gz_sim.launch.py')
        ),
        launch_arguments={'gz_args': '-r empty.sdf'}.items(),
    )

    # 5. SPAWN ROBOT
    # Memasukkan robot ke dalam dunia Gazebo
    spawn_entity = Node(
        package='ros_gz_sim',
        executable='create',
        arguments=['-topic', 'robot_description',
                   '-name', 'soccer_bot',
                   '-z', '0.1'], # Munculkan agak tinggi (10cm) biar gak nyangkut
        output='screen'
    )

    # 6. JEMBATAN KOMUNIKASI (BRIDGE)
    # Ini yang paling penting: Menerjemahkan topik ROS <-> Gazebo
    bridge = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        arguments=[
            # Jembatan untuk Perintah Gerak (ROS -> Gazebo)
            '/cmd_vel@geometry_msgs/msg/Twist@gz.msgs.Twist',
            # Jembatan untuk Odometry/Posisi (Gazebo -> ROS)
            '/odom@nav_msgs/msg/Odometry@gz.msgs.Odometry',
        ],
        output='screen'
    )

    return LaunchDescription([
        node_robot_state_publisher,
        gazebo,
        spawn_entity,
        bridge
    ])

