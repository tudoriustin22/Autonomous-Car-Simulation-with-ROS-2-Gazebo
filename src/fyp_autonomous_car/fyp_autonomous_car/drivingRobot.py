from .DetectionModule.Lane.laneDetection import lane_detection
from .DetectionModule.Lane.segmentColor import init_windows
import cv2

#these lines import the lane detection and segment color functions from the laneDetection and segmentColor modules
#
class AutonomousCar():
    def __init__(self):
        self.windows_initialized = False #this checks is the windows have been initialized or not
        
    def driveCar(self,frame): #this function will drive the car
        if not self.windows_initialized: #if the windows are not yet initialised, they are initialised
            init_windows()
            self.windows_initialized = True 
            
        lane_detection(frame) #this function will detect the lane
        
    def cleanup(self): #after which the windows are destroyed if the user presses ctrl+c or command+c
        cv2.destroyWindow("White Mask")
        cv2.destroyWindow("Yellow Mask")    