cmake_minimum_required(VERSION 2.8.3)
project(recognize)

## Find catkin macros and libraries
find_package(catkin REQUIRED COMPONENTS pcl_ros rospy visualization_msgs)
find_package(Boost REQUIRED)
#find_package(PCL)
#dynamics_reconfigure nodeles

include_directories(${catkin_INCLUDE_DIRS})
 
catkin_package(
  INCLUDE_DIRS
  LIBRARIES turtlebot_teleop
  CATKIN_DEPENDS rospy geometry_msgs pcl_ros rospy visualization_msgs turtlebot_msgs dynamic_reconfigure
  DEPENDS
)

###########
## Build ##
###########

#############
## Install ##
#############

## Mark executable scripts (Python etc.) for installation
install(PROGRAMS
  scripts/recognize
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

## Mark executables and/or libraries for installation
install(TARGETS
  RUNTIME DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

## Mark all other useful stuff for installation
install(DIRECTORY launch
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)
