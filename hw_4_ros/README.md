# HW4 – ROS 2 Jazzy: pub/sub + service/client

ROS 2 Jazzy is installed through [RoboStack](https://robostack.github.io) (conda) because ROS has no native macOS binaries.

```sh
# one-time setup
mamba create -n ros_jazzy -c conda-forge -c robostack-jazzy \
  python=3.12 ros-jazzy-desktop colcon-common-extensions "setuptools<80" compilers cmake pkg-config make ninja

# build
conda activate ros_jazzy
cd ros2_ws && colcon build --symlink-install
source install/setup.zsh   # in every new terminal
```

## Publisher / Subscriber (`py_pubsub`)

```sh
ros2 run py_pubsub talker     # terminal 1
ros2 run py_pubsub listener   # terminal 2
```

## Service / Client (`py_srvcli`)

```sh
ros2 run py_srvcli service    # terminal 1
ros2 run py_srvcli client 2 3 # terminal 2 -> "2 + 3 = 5"
```
