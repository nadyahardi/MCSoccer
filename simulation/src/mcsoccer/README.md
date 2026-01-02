# Simulation Setup
## Prerequisites

- Install Jazzy Jalisco:  
  [ROS2 Jazzy Jalisco Installation](https://docs.ros.org/en/jazzy/Installation/Ubuntu-Install-Debs.html)

  [Instalation video guide by *Alexandar Habar PhD* on youtube](https://youtu.be/08o46x5SfJM?si=HDDDF1KCSMPI0PHD)

- Install Depedencies
  ```bash
  sudo apt install ros-jazzy-xacro 
  ```
  ```bash
  sudo apt install ros-jazzy-joint-state-publisher
  ```
  ```bash
  sudo apt install ros-jazzy-teleop-twist-joy
  ```
## Cloning the Repository
 ### Clone the repository
  ```bash
  git clone https://github.com/nadyahardi/MCSoccer.git
 ```
    
Then pull the submodules with:
    
```bash
git submodule update --init --recursive --remote
```
### Pulling Commits from the Repository
    
```bash
git pull --rebase
```

## Installation
- Build
  ```bash
  cd simulation
  colcon build --symlink-install

  source install/setup.bash
  ```

## Running the Simulation
>simulation using Gazebo Harmonic (gz-sim)
- open terminal 1 for running Gazebo and Rviz(Rviz in development)
  ```bash
  ros2 launch mcsoccer sim.launch.py
  ```

- Open second terminal for PS4 Controller
  ```bash
  source install/setup.bash
  ros2 launch mcsoccer joystick.launch.py
  ```
