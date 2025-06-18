from .segmentColor import segmentLane
from ...config import config


def lane_detection(img):
    #crop below the horizon in the car view
    croppedImage = img[config.CropHeight_resized:,:]

    segmentLane(croppedImage,config.minArea_resized)