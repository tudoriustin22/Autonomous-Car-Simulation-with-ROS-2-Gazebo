#this file contains the global configuration for the autonomous car project which can be used in any file in the project

import os
import cv2

# the following are a list of debugging flags which can be used to enable or disable debugging for the parts of the code
debugging = True  
debugging_Lane = True 
debugging_L_ColorSeg = True  
debugging_L_Est = True 
debugging_L_Cleaning = True 
debugging_L_LaneInfoExtraction = True  
debugging_Signs = True 
debugging_TrafficLights = True 
debugging_TL_Config = True 

# the following are the paths to the video outputs folder and the counter for video loops
vid_path = os.path.abspath("videoOutputsCar/")  # path to the video outputs folder where recordings from the car are stored
if not os.path.exists(vid_path):
    os.makedirs(vid_path)  
loopCount = 0  

# these are the original and reduced image dimensions for video processing
Resized_width = 320 
Resized_height = 240 
Ref_imgWidth = 1920 
Ref_imgHeight = 1080 

# this is the configuration for the mp4 video codec and writers for input and output video
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # mp4v is the MP4 codec
in_q = cv2.VideoWriter(os.path.join(vid_path, "fyp_car_In.mp4"), fourcc, 30, (Resized_width, Resized_height)) 
out = cv2.VideoWriter(os.path.join(vid_path, "fyp_car_Out.mp4"), fourcc, 30, (Resized_width, Resized_height)) 

# this is the delay between frame processing in the camera feed in milliseconds
waitTime = 1

#these are the calculations for the number of pixels in the original and resized frames
Frame_pixels = Ref_imgWidth * Ref_imgHeight  
Resize_Framepixels = Resized_width * Resized_height 

# these are the parameters for the lane extraction algorithm
Lane_Extraction_minArea_per = 1000 / Frame_pixels  
minArea_resized = int(Resize_Framepixels * Lane_Extraction_minArea_per)  

BWContourOpen_speed_MaxDist_per = 500 / Ref_imgHeight  # Maximum distance percentage for contour processing
MaxDist_resized = int(Resized_height * BWContourOpen_speed_MaxDist_per)  # Maximum distance in resized frame

CropHeight = 650  # Height for image cropping
CropHeight_resized = int((CropHeight / Ref_imgHeight) * Resized_height)  # Cropped height in resized frame
# Feature flags
detect = 1  
Testing = True 
Profiling = False  
write = False  
Out_write = False  
animate_steering = False  

# these are the state variables for the car
angle_orig = 0  
angle = 0 
engines_on = False  
clr_seg_dbg_created = False  

