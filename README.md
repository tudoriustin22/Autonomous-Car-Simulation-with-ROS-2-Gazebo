# Autonomous Car Simulation with ROS 2 & Gazebo

A lightweight and modular autonomous driving simulator built with ROS 2 Humble and Gazebo Classic, focused on vision-based lane detection and manual teleoperation. Designed for efficient simulation and testing on machines with limited resources.

## 🚗 Project Overview

This project demonstrates the development of a modular autonomous driving system with the following core features:

- 3D simulation environment with custom roads and signs.
- A Prius vehicle model with Ackerman steering and onboard camera.
- Vision-based lane detection using traditional computer vision techniques.
- Manual and autonomous control modes.
- Modular ROS 2 architecture for scalable and testable development.

---

## 📋 Requirements

### Functional (MoSCoW Prioritization)

**Must Have**
- 3D simulation environment with roads
- Vehicle with steering and camera sensor
- Basic lane detection via computer vision
- Manual control (teleoperation)

**Should Have**
- Real-time lane detection display
- Recording camera feed

**Could Have**
- Traffic sign detection
- More advanced autonomous behaviors

**Won’t Have**
- Deep learning systems
- Multi-sensor fusion
- Multi-agent simulation

### Non-Functional

**Must Have**
- Modular ROS 2 node architecture
- Runs on Ubuntu 22.04 with ROS 2 Humble
- Documented system setup

**Should Have**
- Clean, reusable codebase

**Could Have**
- Configurable simulation parameters

---

## 🛠️ System Design

### Architecture

- **Simulator**: Gazebo Classic for 3D world and physics.
- **Vehicle**: Prius model with Ackerman drive, camera sensor.
- **ROS 2 Nodes**:
  - `driving_node`: Basic movement control
  - `carVision_node`: Lane detection via OpenCV
  - `videoOutput_node`: Camera recording
- **Detection Module**:
  - Color segmentation for lane detection
  - Real-time visualization of segmentation

### Folder Structure

