#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist


class DrivingNode(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

        self.get_logger().info('Publishing: cmd_vel')
        self.command_velocity_msg = Twist()

    def timer_callback(self):
        self.command_velocity_msg.linear.x = 1.0;
        self.command_velocity_msg.angular.z = 0.2;

        self.publisher_.publish(self.command_velocity_msg)



def main(args=None):
    rclpy.init(args=args)

    cmd_vel_publisher = DrivingNode()

    rclpy.spin(cmd_vel_publisher)

    cmd_vel_publisher.destroy_node()
    rclpy.shutdown()
 

if __name__ == '__main__':
    main()