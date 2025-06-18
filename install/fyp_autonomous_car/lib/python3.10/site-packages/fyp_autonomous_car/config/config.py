import os
import cv2

# Debug settings
debugging = True
debugging_Lane = True
debugging_L_ColorSeg = True
debugging_L_Est = True
debugging_L_Cleaning = True
debugging_L_LaneInfoExtraction = True
debugging_Signs = True
debugging_TrafficLights = True
debugging_TL_Config = True

# Video settings
vid_path = os.path.abspath("videoOutputsCar/")
if not os.path.exists(vid_path):
    os.makedirs(vid_path)
loopCount = 0

# Image dimensions
Resized_width = 320
Resized_height = 240
Ref_imgWidth = 1920
Ref_imgHeight = 1080

# Video writers
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # MP4 codec
in_q = cv2.VideoWriter(os.path.join(vid_path, "fyp_car_In.mp4"), fourcc, 30, (Resized_width, Resized_height))
out = cv2.VideoWriter(os.path.join(vid_path, "fyp_car_Out.mp4"), fourcc, 30, (Resized_width, Resized_height))

# Timing
waitTime = 1

# Frame calculations
Frame_pixels = Ref_imgWidth * Ref_imgHeight
Resize_Framepixels = Resized_width * Resized_height

# Lane detection parameters
Lane_Extraction_minArea_per = 1000 / Frame_pixels
minArea_resized = int(Resize_Framepixels * Lane_Extraction_minArea_per)

BWContourOpen_speed_MaxDist_per = 500 / Ref_imgHeight
MaxDist_resized = int(Resized_height * BWContourOpen_speed_MaxDist_per)

CropHeight = 650
CropHeight_resized = int((CropHeight / Ref_imgHeight) * Resized_height)

# Feature flags
detect = 1
Testing = True
Profiling = False
write = False
Out_write = False
enable_SatNav = False
animate_steering = False
Detect_lane_N_Draw = True
Training_CNN = False

# State variables
angle_orig = 0
angle = 0
engines_on = False
clr_seg_dbg_created = False
