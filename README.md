# Computational Physics Final Project

## 3D Projectile Motion with and without Air Resistance

### Project Overview

This project simulates three-dimensional projectile motion using Python and the fourth-order Runge-Kutta (RK4) numerical method.

The simulation allows users to investigate the effects of gravity and air resistance on projectile trajectories while adjusting various physical parameters such as initial speed, launch angle, initial height, and drag coefficient.

The project demonstrates how computational physics techniques can be applied to solve physical problems that are difficult to analyze analytically.

---

## Objectives

- Simulate horizontal projectile motion.
- Simulate oblique projectile motion.
- Compare trajectories with and without air resistance.
- Analyze the influence of physical parameters.
- Apply the RK4 numerical integration method.
- Visualize projectile motion in three-dimensional space.

---

## Features

### Motion Types

- Horizontal Projectile Motion
- Oblique Projectile Motion

### Resistance Models

- Without Air Resistance
- With Air Resistance

### Adjustable Parameters

- Initial Height
- Initial Speed
- Launch Angle
- Azimuth Angle
- Mass
- Radius
- Drag Coefficient
- Air Density
- Time Step

### Visualization

- 3D Trajectory Plot
- Height vs Time
- Speed vs Time
- Height vs Horizontal Distance
- Trajectory Comparison

---

## Physical Model

The projectile is represented by:

\[
\vec r = (x,y,z)
\]

\[
\vec v = (v_x,v_y,v_z)
\]

### Without Air Resistance

\[
\frac{d\vec v}{dt}=(0,0,-g)
\]

### With Air Resistance

\[
\vec F_d=-\frac12\rho C_d A |\vec v|\vec v
\]

where:

- \( \rho \) = air density
- \( C_d \) = drag coefficient
- \( A=\pi r^2 \) = cross-sectional area

---

## Numerical Method

The simulation uses the Fourth-Order Runge-Kutta (RK4) method.

Advantages:

- High accuracy
- Stable numerical solution
- Suitable for nonlinear differential equations
- Widely used in computational physics

---

## Program Workflow

```text
Start
 ↓
Input Parameters
 ↓
Select Motion Type
 ↓
Select Drag Model
 ↓
Initialize Position and Velocity
 ↓
RK4 Numerical Integration
 ↓
Update State Variables
 ↓
Ground Collision Detection
 ↓
Generate Results
 ↓
Visualization
 ↓
End
```

## Parameter Analysis

The project investigates how different parameters affect projectile motion.

| Parameter | Effect on Motion |
|------------|------------|
| Initial Speed | Increases range and maximum height |
| Launch Angle | Changes trajectory shape and flight time |
| Initial Height | Increases flight time and range |
| Drag Coefficient | Reduces range and velocity |
| Air Density | Increases drag force |
| Mass | Reduces drag influence |
| Radius | Increases drag force |
| Gravity | Reduces flight time and height |

---

## Example Experiments

| Experiment | Initial Speed | Launch Angle | Initial Height | Cd |
|------------|------------|------------|------------|------------|
| Baseline | 20 m/s | 45° | 10 m | 0.47 |
| Test 1 | 40 m/s | 45° | 10 m | 0.47 |
| Test 2 | 20 m/s | 30° | 10 m | 0.47 |
| Test 3 | 20 m/s | 60° | 10 m | 0.47 |
| Test 4 | 20 m/s | 45° | 50 m | 0.47 |
| Test 5 | 20 m/s | 45° | 10 m | 0 |
| Test 6 | 20 m/s | 45° | 10 m | 1.0 |

---

## Results

The simulation demonstrates that:

- Air resistance reduces projectile range.
- Air resistance reduces maximum height.
- Air resistance reduces flight time.
- Higher initial velocity increases range.
- Launch angle significantly affects trajectory shape.
- RK4 provides stable and accurate numerical results.

---

## Future Improvements

Possible extensions include:

- Wind effects
- Variable air density
- Magnus effect (ball spin)
- Real-time interactive simulation
- Enhanced 3D visualization

---

## Technologies Used

- Python
- NumPy
- Matplotlib
- Jupyter Notebook

---

## Author

YIYANG LIU

Computational Physics Final Project
