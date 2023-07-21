# Imports
from niryo_robot_python_ros_wrapper import *
import rospy

# Initializing ROS node
rospy.init_node('niryo_ned_example_python_ros_wrapper')

niryo_robot = NiryoRosWrapper()

# - Constants
workspace_name = "conveyorkejriwal"  # Robot's Workspace Name

# The observation pose
observation_pose = (0.164, -0.021, 0.153, -3.062, 1.333, -3.027)
# Place pose
green_place_pose = (-0.069, -0.266, 0.079, -2.934, 1.226, 1.607)
red_place_pose = (0.01, -0.247, 0.084, 3.134, 1.368, 1.643)
blue_place_pose = (0.028, 0.274, 0.076, -0.33, 1.443, 1.209)

# - Main Program
# Calibrate robot if robot needs calibration
niryo_robot.calibrate_auto()
# Changing tool
niryo_robot.update_tool()

count = 0
while count < 3:
	niryo_robot.move_pose(*observation_pose) #set a proper pose by manually moving the robot

	obj_found, shape_ret, color_ret = niryo_robot.vision_pick(workspace_name,
                                                                  height_offset=-0.01,
                                                                  shape=ObjectShape.ANY,
                                                                  color=ObjectColor.ANY)
	

	niryo_robot.move_pose(*observation_pose)

	if obj_found:
	
		if color_ret == 'GREEN':
			niryo_robot.place_from_pose(*green_place_pose)
			count += 1
		elif color_ret == 'RED':
			niryo_robot.place_from_pose(*red_place_pose)
			count += 1
		elif color_ret == 'BLUE':
			niryo_robot.place_from_pose(*blue_place_pose)
			count += 1
		

#niryo_robot.set_learning_mode(True)

niryo_robot.end()
