#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist
import cv2
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
import os

#the imports above are the necessary libraries and the ros2 python client

#this is the class for the video output node which is the main node for the autonomous car that saves the video feed to a file
class SaveVideoOutput(Node):

    def __init__(self):
        super().__init__('videoOutput_node') #this is the node name and below is the subscriber which subscribes to the camera feed and processes the data
        self.subscriber_ = self.create_subscription(Image, '/camera/image_raw', self.process_data, 10) 
        
        # if the video output folder doesnt exist, the following will create it 
        vid_path = os.path.abspath("videoOutputsCar")
        if not os.path.exists(vid_path):
            os.makedirs(vid_path)
            
        # videos are saved in the mp4 format which is the most widely compatible format
        fourcc = cv2.VideoWriter_fourcc(*'mp4v') 
        self.videoOut = cv2.VideoWriter(os.path.join(vid_path, 'fyp_car.mp4'), fourcc, 30, (1280,720)) #resolution is set to 720p

        self.get_logger().info('Subscribe video feed and record camera') #terminal feedback
        self.cvbridge = CvBridge() 

    def process_data(self, data): #this function will processes the data from the camera feed and saves it to the video file
        frame = self.cvbridge.imgmsg_to_cv2(data, 'bgr8') 
        self.videoOut.write(frame) #write the frame to the video file
        cv2.imshow('frame', frame)
        cv2.waitKey(1)


def main(args=None): 
    rclpy.init(args=args) #initialises and spins the node

    video_output_node = SaveVideoOutput() #class instance for the SaveVideoOutput class

#error handling for the node so that will run until the node is interrupted by the user keyboard 
    try:
        rclpy.spin(video_output_node) 
    except KeyboardInterrupt:
        pass
    finally:
        video_output_node.videoOut.release() 
        cv2.destroyAllWindows() #if the user click control+c, the video is saved and windows are closed 
        video_output_node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()