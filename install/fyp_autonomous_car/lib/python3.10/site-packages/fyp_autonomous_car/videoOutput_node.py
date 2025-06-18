#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist
import cv2
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
import os


class SaveVideoOutput(Node):

    def __init__(self):
        super().__init__('videoOutput_node')
        self.subscriber_ = self.create_subscription(Image, '/camera/image_raw', self.process_data, 10)
        
        # Create output directory if it doesn't exist
        vid_path = os.path.abspath("videoOutputsCar")
        if not os.path.exists(vid_path):
            os.makedirs(vid_path)
            
        # Use MP4 format
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        self.videoOut = cv2.VideoWriter(os.path.join(vid_path, 'fyp_car.mp4'), fourcc, 30, (1280,720))

        self.get_logger().info('Subscribe video feed and record camera')
        self.cvbridge = CvBridge()

    def process_data(self, data):
        frame = self.cvbridge.imgmsg_to_cv2(data, 'bgr8')
        self.videoOut.write(frame)
        cv2.imshow('frame', frame)
        cv2.waitKey(1)


def main(args=None):
    rclpy.init(args=args)

    video_output_node = SaveVideoOutput()

    try:
        rclpy.spin(video_output_node)
    except KeyboardInterrupt:
        pass
    finally:
        video_output_node.videoOut.release()
        cv2.destroyAllWindows()
        video_output_node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()