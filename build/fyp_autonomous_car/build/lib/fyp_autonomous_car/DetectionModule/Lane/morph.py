import cv2
import time
import math
import numpy as np
from ...config import config

def Distance(a,b):
    a_y = a[0,0]
    a_x = a[0,1]
    b_y = b[0,0]
    b_x = b[0,1]
    distance = math.sqrt( ((a_x-b_x)**2)+((a_y-b_y)**2) )
    return distance

def Distance_(a,b):
    return math.sqrt( ( (a[1]-b[1])**2 ) + ( (a[0]-b[0])**2 ) )


def BwareaOpen(img,MinArea):
    treshhold = cv2.threshold(img,0,255,cv2.THRESH_BINARY)[1]
    #remove noise by filtering contoured areas
    contours = cv2.findContours(treshhold,cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[1]
    contours_small = []
    for index, controur in enumerate(contours):
        area = cv2.contourArea(controur)
        if area < MinArea:
            contours_small.append(controur)

    treshhold = cv2.drawContours(treshhold,contours_small,-1,0,-1) 
    return treshhold


