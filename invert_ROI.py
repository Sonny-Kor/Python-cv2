from __future__ import print_function
import argparse
import cv2
import numpy as np
from display_image2 import display_image

def invert_image_m1(img,rect):
    dst = img.copy()
    length = len(dst.shape)
    if length == 3:
        for y in range(rect[1],rect[3]):
            for x in range(rect[0],rect[2]):
                dst[y,x,0] = 255 - dst[y, x, 0]
                if dst[y,x,0] < 0:
                    dst[y,x,0] = 0
                dst[y,x,1] = 255 - dst[y, x, 1]
                if dst[y,x,1] < 0:
                    dst[y,x,1] = 0
                dst[y,x,2] = 255 - dst[y, x, 2]
                if dst[y,x,2] < 0:
                    dst[y,x,2] = 0
    elif length == 2:
        for y in range(rect[1], rect[3]):
            for x in range(rect[0], rect[2]):
                dst[y, x] = 255 - dst[y, x]


    return dst

def invert_image_m2(img, rect):
    dst = img.copy()
    dst[rect[1]:rect[3],rect[0]:rect[2]] = 255- dst[rect[1]:rect[3],rect[0]:rect[2]]
    
    return dst

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True, help="Path to the input image")
    ap.add_argument("-s", "--start_point", type = int, nargs='+',default=[0,0],help = "Start point of the rectangle")
    ap.add_argument("-e", "--end_point", type=int, nargs='+',default=[150,150],help = "end point of the rectangle")
    args = vars(ap.parse_args())

    filename = args["image"]
    sp = args["start_point"]
    ep = args["end_point"]

    image = cv2.imread(filename, cv2.IMREAD_UNCHANGED)
    rect = sp + ep
    e1 = cv2.getTickCount()
    inverted = invert_image_m1(image,rect)
    e2 = cv2.getTickCount()
    time = (e2-e1)/cv2.getTickFrequency()
    print("[정보] 방법1 소요 시간 : {}".format(time))
    display_image(inverted)

    e1= cv2.getTickCount()
    inverted = invert_image_m2(image,rect)
    e2 = cv2.getTickCount()
    time = (e2-e1)/cv2.getTickFrequency()
    print("[정보]방법 2 소요시간: {}".format(time))

    display_image(inverted)