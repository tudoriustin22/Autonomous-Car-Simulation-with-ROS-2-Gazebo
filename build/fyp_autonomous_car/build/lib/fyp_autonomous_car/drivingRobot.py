from .DetectionModule.Lane.laneDetection import lane_detection
from .DetectionModule.Lane.segmentColor import init_windows
import cv2

class AutonomousCar():
    def __init__(self):
        self.windows_initialized = False
        
    def driveCar(self,frame):
        if not self.windows_initialized:
            init_windows()
            self.windows_initialized = True
            
        lane_detection(frame)
        
    def cleanup(self):
        cv2.destroyWindow("White Mask")
        cv2.destroyWindow("Yellow Mask")    