# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a ROS2-based multi-sensor SLAM system designed to integrate LiDAR, Camera, IMU, and GPS data for accurate mapping and localization. The project is in early development with a modular architecture.

## Build Commands

```bash
# Build all packages
cd ~/multi_sensor_slam_ws
colcon build --symlink-install

# Build specific package
colcon build --packages-select multi_sensor_slam_core --symlink-install

# Clean build
rm -rf build/ install/ log/
colcon build --symlink-install

# Source the workspace (required after building)
source install/setup.bash
```

## Development Commands

```bash
# Run linting checks (configured in each package)
colcon test --packages-select <package_name>
colcon test-result --verbose

# Check for missing dependencies
rosdep check --from-paths src --ignore-src -r

# Format C++ code (when clang-format is configured)
find . -name '*.cpp' -o -name '*.hpp' | xargs clang-format -i
```

## Architecture

The system consists of three main ROS2 packages:

1. **multi_sensor_slam_core**: Central SLAM implementation
   - Handles sensor fusion and SLAM algorithms
   - Manages TF2 transformations
   - Publishes map and odometry data

2. **multi_sensor_slam_lidar**: LiDAR processing
   - Point cloud preprocessing
   - Feature extraction from LiDAR data
   - LiDAR odometry estimation

3. **multi_sensor_slam_camera**: Camera/visual processing
   - Image preprocessing with OpenCV
   - Visual feature extraction
   - Visual odometry estimation

## Key Dependencies

- **ROS2 Humble**: Target distribution
- **Essential ROS2 packages**: rclcpp, sensor_msgs, geometry_msgs, nav_msgs, tf2_*, visualization_msgs
- **Camera-specific**: cv_bridge, image_transport
- **Planned integrations**: PCL, OpenCV, Eigen3, GTSAM, Ceres Solver

## Important Notes

1. **Calibration Package**: The `direct_visual_lidar_calibration` package is temporarily excluded from the build due to Eigen/GTSAM compatibility issues. It's listed in .gitignore.

2. **Include Directories**: CMakeLists.txt files reference include directories that don't exist yet. Create them when adding header files.

3. **Package Descriptions**: All package.xml files need proper descriptions and license information (currently marked as TODO).

4. **No Launch Files**: Launch files haven't been created yet. They should be placed in `launch/` directories within each package.

5. **C++ Standard**: The project uses C++17 as configured in CMakeLists.txt.

## Current Implementation Status

- All packages contain minimal "hello world" implementations
- No actual SLAM algorithms implemented
- No sensor driver integrations
- No configuration files or parameters
- Testing infrastructure exists but no tests written

## When Making Changes

1. Follow the existing package structure
2. Add new nodes as separate executables in CMakeLists.txt
3. Update package.xml when adding new dependencies
4. Create launch files for new nodes
5. Place configuration files in `config/` directories
6. Use ROS2 parameter system for configurable values