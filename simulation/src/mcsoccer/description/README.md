# Simulation Tuning
## Torque

change motor_torque (Nm) and motor_velocity (Rad/s) on mcsoccer.urdf.xacro
```xml
<xacro:property name="motor_torque" value="0.5"/> 

<xacro:property name="motor_velocity" value="20.0"/>
```

## Acceleration
find on mcsoccer.gazebo

```xml
<max_linear_acceleration>1.0</max_linear_acceleration>

<max_angular_acceleration>2.0</max_angular_acceleration>
```
