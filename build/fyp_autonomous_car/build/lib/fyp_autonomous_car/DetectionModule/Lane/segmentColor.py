import numpy as np
import cv2


# White
h_l = 0          
lit_l = 200    
sat_l = 0        

# Yellow
hue_l_yellow = 20    
hue_h_yellow = 40    
lit_l_yellow = 100  
sat_l_yellow = 100   


def extractMask(frame):
    global src
    src = frame
    global hls_convertion
    hls_convertion = cv2.cvtColor(frame, cv2.COLOR_BGR2HLS)
    
    mask = segmentColors(hls_convertion,(h_l, lit_l, sat_l),(255,255,255))
    mask_yellow = segmentColors(hls_convertion,(hue_l_yellow, lit_l_yellow, sat_l_yellow),(hue_h_yellow,255,255))
    mask = mask != 0
    dst = src * (mask[:,:,None].astype(src.dtype))

    mask_yellow = mask_yellow != 0
    dst_yellow = src * (mask_yellow[:,:,None].astype(src.dtype))

    cv2.imshow("White Mask",dst)
    cv2.imshow("Yellow Mask",dst_yellow)
    cv2.waitKey(1)


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

def init_windows():
    cv2.namedWindow("White Mask")
    cv2.namedWindow("Yellow Mask")

    cv2.createTrackbar("sat_low_yellow","Yellow Mask",sat_l_yellow,255,on_sat_low_yellow_change)
    cv2.createTrackbar("lit_low_yellow","Yellow Mask",lit_l_yellow,255,on_lit_low_yellow_change)
    cv2.createTrackbar("hue_high_yellow","Yellow Mask",hue_h_yellow,255,on_hue_high_yellow_change)
    cv2.createTrackbar("hue_low_yellow","Yellow Mask",hue_l_yellow,255,on_hue_low_yellow_change)

    cv2.createTrackbar("sat_low","White Mask",sat_l,255,on_sat_low_change)
    cv2.createTrackbar("lit_low","White Mask",lit_l,255,on_lit_low_change)
    cv2.createTrackbar("hue_low","White Mask",h_l,255,on_hue_low_change)


def mask_edge(frame, mask, min_area):
    #remove noise from the mask (small objects) by keeping the objects larger than min_area
    maskedFrame = cv2.bitwise_and(frame, frame, mask=mask)
    frameGrey = cv2.cvtColor(maskedFrame, cv2.COLOR_BGR2GRAY)
    maskLarge = BwareaOpen(frameGrey, min_area)
    frameGrey = cv2.bitwise_and(frameGrey, maskLarge)
    frameSmooth = cv2.GaussianBlur(frameGrey, (11,11), 1)
    edges = cv2.Canny(frameSmooth, 50, 150)
    return maskLarge, edges


def segmentMiddleLane(frame, white_mask, min_area):
    middleLaneMask, middleLaneEdges = mask_edge(frame, white_mask, min_area)
    return middleLaneMask, middleLaneEdges

def segmentOuterLanes(frame, yellow_mask, min_area):
    outerLanesMask, outerLanesEdges = mask_edge(frame, yellow_mask, min_area)
    return outerLanesMask, outerLanesEdges



def segmentColors(hls_convertion, low_range, upper_range):
    mask_range = cv2.inRange(hls_convertion, low_range, upper_range)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
    dilatedMask = cv2.morphologyEx(mask_range, cv2.MORPH_DILATE, kernel)
    return dilatedMask


def segmentLane(frame, min_area):
    hls_convertion = cv2.cvtColor(frame, cv2.COLOR_BGR2HLS)

    # White Segmentation
    white_mask = segmentColors(hls_convertion,
                            np.array([h_l, lit_l, sat_l]),
                            np.array([255, 255, 255]))
    
    # Yellow Segmentation
    yellow_mask = segmentColors(hls_convertion,
                             np.array([hue_l_yellow, lit_l_yellow, sat_l_yellow]),
                             np.array([hue_h_yellow, 255, 255]))
    
    #Resize the windows so they dont take up too much space on the screen
    display_width = white_mask.shape[1] // 2  # 640
    display_height = white_mask.shape[0] // 2  # 360
    white_mask_display = cv2.resize(white_mask, (display_width, display_height))
    yellow_mask_display = cv2.resize(yellow_mask, (display_width, display_height))
    
    # Show the resized masks
    cv2.imshow("White Mask", white_mask_display)
    cv2.imshow("Yellow Mask", yellow_mask_display)
    cv2.waitKey(1)
    
    return white_mask, yellow_mask

    