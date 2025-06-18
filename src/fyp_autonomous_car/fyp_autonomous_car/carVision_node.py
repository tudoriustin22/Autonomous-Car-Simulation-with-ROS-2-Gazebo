#!/usr/bin/env python3
#import the necessary libraries and the ros2 python client
import rclpy 
from rclpy.node import Node

from geometry_msgs.msg import Twist 
import cv2
from cv_bridge import CvBridge
from sensor_msgs.msg import Image 
from .drivingRobot import AutonomousCar #this is the class for the autonomous car which is created the drivingRobot.py file

#the following class is the main node for the autonomous car which subscribes to the camera feed and publishes the command velocity to the car
class carVision(Node):
#initializes the node and creates the publisher and subscriber
    def __init__(self):
        super().__init__('carVision_node') #name of the ros2 node

        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10) #publisher for the command velocity which uses the Twist message type same as teleoperating the car
        self.subscriber_ = self.create_subscription(Image, '/camera/image_raw', self.process_data, 10) #subscriber for the camera feed w

        self.get_logger().info('Subscribing to the camera') #printing a log status message to the terminal
        self.cvbridge = CvBridge() #this converts the standard ros2 image from bgr8 to opencv format
        self.command_velocity_msg = Twist() #this is the twist message for command velocity, same one used for teleoperation
        self.AutonomousCarDrive = AutonomousCar() #this is an object of the AutonomousCar class
 

 #the following function publishes the command velocity to the car
    def sent_command_velocity(self):
        self.publisher_.publish(self.command_velocity_msg) 

#the following function processes the camera feed, converts it to cv2 format and drives the car
    def process_data(self, data):
        frame = self.cvbridge.imgmsg_to_cv2(data, 'bgr8') 
        self.AutonomousCarDrive.driveCar(frame)       #this is the function call to drive the car

        cv2.imshow('frame', frame) #imshow will open a new window to display the frame from the camera feed, as a video stream
        cv2.waitKey(1) #delay between frames

#the following function is the main function that initializes and spins the node
def main(args=None): 
    rclpy.init(args=args) #initialise the ros2 carVision node

    car_vision_node = carVision() #create an instance of the class itself

#error handling for the node that will run until the node is interrupted by the user
    try: 
        rclpy.spin(car_vision_node)
    except KeyboardInterrupt:
        pass
    finally:
        car_vision_node.AutonomousCarDrive.cleanup()
        cv2.destroyAllWindows() #this is a function call to the cleanup method in the AutonomousCar class and close all windows
        car_vision_node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main() #caling the main function to run the node 