#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

#import the ros2 client and the Twist message type from the geometry_msgs package
from geometry_msgs.msg import Twist

#this is the class for the driving node which is the main node for the autonomous car and which sends cmd_vel messages to the car
class DrivingNode(Node):

    def __init__(self): #initializes the node and creates the publisher and timer
        super().__init__('minimal_publisher') #name for the node
        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10) #publisher for the cmd_vel topic
        timer_period = 0.5  # in seconds
        self.timer = self.create_timer(timer_period, self.timer_callback) #this is a timer that calls the timer_callback function every 0.5 seconds

        self.get_logger().info('Publishing: cmd_vel') #this is the terminal feedback given when the node is started
        self.command_velocity_msg = Twist()

    def timer_callback(self): #this is the function that is called every 0.5 seconds to publish the command velocity to the car
        self.command_velocity_msg.linear.x = 1.0; #this is the linear velocity which means the car will move forward at 1 m/s
        self.command_velocity_msg.angular.z = 0.2; #this is the angular velocity which means the car will turn at 0.2

        self.publisher_.publish(self.command_velocity_msg) #this publisher simply publishes the command velocity to the car making it move



def main(args=None): #this is the main function that initializes and spins the node
    rclpy.init(args=args) #initialise the ros2 node

    cmd_vel_publisher = DrivingNode() #create a class instance

    rclpy.spin(cmd_vel_publisher) #the node will run until it is interrupted by the user

    cmd_vel_publisher.destroy_node() 
    rclpy.shutdown() #the ros2 node is then destroyed and shutdown ending the program
 

if __name__ == '__main__':
    main()