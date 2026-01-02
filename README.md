# MicroClub's Soccer Bot

This repository contains arduino code for the robot's esp and simulation using Gazebo Harmonic on ROS2 Jazzy Jalisco Distribution

## Directory structure
```text
.
├── mcu/                  
│   ├── mcsoccer_esp32/      # Arduino program for ESP
│   └── utils/               # getmacadress()
│
└── simulation/          
    └── src/
        └── mcsoccer/        
            ├── config/      # Joystick & RViz configuration
            ├── description/ # URDF
            └── launch/   
```

## Simulation Tuning
see 
>simulation/src/mcsoccer --> description --> README.md
