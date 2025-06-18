import numpy as np
import cv2
#these imports are the necessary libraries and the numpy library

#the following are the global variables for the white and yellow masks determined using the trackbars during development
#they were first initialised as 0 and then the trackbars were used to change the values to the optimal values manually 

# White
h_l = 0          
lit_l = 200    
sat_l = 0        

# Yellow
hue_l_yellow = 20    
hue_h_yellow = 40    
lit_l_yellow = 100  
sat_l_yellow = 100   


def extractMask(frame):#this function will extract the mask from the frame with the white and yellow masks
    global src #
    src = frame
    global hls_convertion #this is the hls convertion of the frame which is used to segment the lane and convert the frame to the hls color space
    hls_convertion = cv2.cvtColor(frame, cv2.COLOR_BGR2HLS) #the frame is converted to hls which is read by openCV
    
    mask = segmentColors(hls_convertion,(h_l, lit_l, sat_l),(255,255,255))# this is the mask for the white lane and the 255,255,255 is the upper limit for the white lane
    mask_yellow = segmentColors(hls_convertion,(hue_l_yellow, lit_l_yellow, sat_l_yellow),(hue_h_yellow,255,255)) #this is the mask for the yellow lane and the hue_h_yellow is the upper limit for the yellow lane
    mask = mask != 0 #this is the mask for the white lane and the mask is not 0
    dst = src * (mask[:,:,None].astype(src.dtype)) #this is the destination image which is the source image from the frame  multiplied by the mask

    mask_yellow = mask_yellow != 0 
    dst_yellow = src * (mask_yellow[:,:,None].astype(src.dtype)) #this is the destination image which is the source image from the frame  multiplied by the yellow mask

    cv2.imshow("White Mask",dst) #the window displaying the white mask
    cv2.imshow("Yellow Mask",dst_yellow) #the window displaying the yellow mask
    cv2.waitKey(1)

#the following are the functions for the trackbars which are used to change the values of the white and yellow masks
#for each trackbar, the value is changed and the extractMask function is called to update the mask
def on_sat_low_yellow_change(val):
    global sat_l_yellow
    sat_l_yellow = val 
    if 'src' in globals(): 
        extractMask(src) 

def on_lit_low_yellow_change(val):
    global lit_l_yellow
    lit_l_yellow = val
    if 'src' in globals():
        extractMask(src)

def on_hue_high_yellow_change(val):
    global hue_h_yellow
    hue_h_yellow = val
    if 'src' in globals():
        extractMask(src)

def on_hue_low_yellow_change(val):
    global hue_l_yellow
    hue_l_yellow = val
    if 'src' in globals():
        extractMask(src)

def on_sat_low_change(val):
    global sat_l
    sat_l = val
    if 'src' in globals():
        extractMask(src)

def on_lit_low_change(val):
    global lit_l
    lit_l = val
    if 'src' in globals():
        extractMask(src)

def on_hue_low_change(val):
    global h_l
    h_l = val
    if 'src' in globals():
        extractMask(src)



#the following are the functions for the trackbars which are used to change the values of the white and yellow masks
#for each trackbar, the value is changed and the extractMask function is called to update the mask with a max value being 255

def init_windows():
    cv2.namedWindow("White Mask")
    cv2.namedWindow("Yellow Mask")

    #these are using the saturation, lightness and hue values for the yellow mask
    cv2.createTrackbar("sat_low_yellow","Yellow Mask",sat_l_yellow,255,on_sat_low_yellow_change)
    cv2.createTrackbar("lit_low_yellow","Yellow Mask",lit_l_yellow,255,on_lit_low_yellow_change)
    cv2.createTrackbar("hue_high_yellow","Yellow Mask",hue_h_yellow,255,on_hue_high_yellow_change)
    cv2.createTrackbar("hue_low_yellow","Yellow Mask",hue_l_yellow,255,on_hue_low_yellow_change)

 #these are using the saturation, lightness and hue values for the white mask
    cv2.createTrackbar("sat_low","White Mask",sat_l,255,on_sat_low_change)
    cv2.createTrackbar("lit_low","White Mask",lit_l,255,on_lit_low_change)
    cv2.createTrackbar("hue_low","White Mask",h_l,255,on_hue_low_change)



#the segmentColors function is used to segment the colors in the frame
def segmentColors(hls_convertion, low_range, upper_range):  #it takes the hls convertion of the frame, the lower range and the upper range as input
    mask_range = cv2.inRange(hls_convertion, low_range, upper_range) 
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3)) #the kernel is the structure element for the morphological operation which is an ellipse
    #the ellipse is used to create a kernel of size 3x3
    dilatedMask = cv2.morphologyEx(mask_range, cv2.MORPH_DILATE, kernel) #the dilated mask is the morphological operation which is dilation and is re

    return dilatedMask

#
def segmentLane(frame, min_area):
    hls_convertion = cv2.cvtColor(frame, cv2.COLOR_BGR2HLS) #the frame is converted to hls which is read by open CV

    # White Segmentation 
    white_mask = segmentColors(hls_convertion,         #the white mask is segmented using the segmentColors function
                            np.array([h_l, lit_l, sat_l]), #the lower range and the upper range are the values of the trackbars
                            np.array([255, 255, 255])) #the upper range
    
    # Yellow Segmentation 
    yellow_mask = segmentColors(hls_convertion,#
                             np.array([hue_l_yellow, lit_l_yellow, sat_l_yellow]), #the lower range and the upper range are the values of the trackbars
                             np.array([hue_h_yellow, 255, 255]))
    
    #the following will be resizing the windows so they dont take up too much space on the screen once the simulation is running
    display_width = white_mask.shape[1] // 2  # 640
    display_height = white_mask.shape[0] // 2  # 360
    white_mask_display = cv2.resize(white_mask, (display_width, display_height))
    yellow_mask_display = cv2.resize(yellow_mask, (display_width, display_height)) #the yellow mask is resized to the same size as the white mask
    
    # the following will show the resized masks in the new windows
    cv2.imshow("White Mask", white_mask_display)
    cv2.imshow("Yellow Mask", yellow_mask_display)
    cv2.waitKey(1) 
    
    return white_mask, yellow_mask

    