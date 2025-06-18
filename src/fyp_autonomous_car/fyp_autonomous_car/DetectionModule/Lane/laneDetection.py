from .segmentColor import segmentLane
from ...config import config
#the imports above import the segmentLane function from the segmentColor module and the config module


def lane_detection(img): #this function will detect the lane in the image frame
    # and it will crop below the horizon in the car view using the config.CropHeight_resized variable in the config file with global variables
    croppedImage = img[config.CropHeight_resized:,:]

    segmentLane(croppedImage,config.minArea_resized) #this will segment the lane in the cropped image and the minimum area of the lane