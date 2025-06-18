#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist
import cv2
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
from .drivingRobot import AutonomousCar


class carVision(Node):

    def __init__(self):
        super().__init__('carVision_node')

        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)
        self.subscriber_ = self.create_subscription(Image, '/camera/image_raw', self.process_data, 10)

        self.get_logger().info('Subscribing to the camera')
        self.cvbridge = CvBridge()
        self.command_velocity_msg = Twist()
        self.AutonomousCarDrive = AutonomousCar()

    def sent_command_velocity(self):
        self.publisher_.publish(self.command_velocity_msg) 

    def process_data(self, data):
        frame = self.cvbridge.imgmsg_to_cv2(data, 'bgr8')
        self.AutonomousCarDrive.driveCar(frame)        

        cv2.imshow('frame', frame)
        cv2.waitKey(1)


def main(args=None):
    rclpy.init(args=args)

    car_vision_node = carVision()

    try:
        rclpy.spin(car_vision_node)
    except KeyboardInterrupt:
        pass
    finally:
        car_vision_node.AutonomousCarDrive.cleanup()
        cv2.destroyAllWindows()
        car_vision_node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()