from __future__ import print_function
import argparse
import cv2
import numpy as np
from display_image2 import display_image

def smoothing_image(img, type='mean', ksize = 3):
    # 영상 평활화
    if(type == 'mean'):
        dst = cv2.blur(img, (ksize,ksize))
    elif(type == 'Gaussian'):
        dst = cv2.GaussianBlur(img, (ksize,ksize),0)
    elif(type == 'median'):
        dst = cv2.medianBlur(img, ksize)
    else:
        print("[에러] 잘못된 type 지정")
        return None
    return dst

def gradient_image(img, type="Sobel", dir = 'all'):
    if(type == "Sobel"):
        if (dir == 'x'):
            dst = cv2.Sobel(img, cv2.CV_64F,1,0)
            dst = np.uint8(np.absolute(dst))
        elif(dir == 'y'):
            dst = cv2.Sobel(img, cv2.Sobel,0,1)
            dst = np.uint8(np.absolute(dst))
        elif(dir == 'all'):
            dstx = cv2.Sobel(img,cv2.CV_64F,1,0)
            dstx = np.uint8(np.absolute(dstx))
            dsty = cv2.Sobel(img,cv2.CV_64F,0,1)
            dsty = np.uint8(np.absolute(dsty))
            # gradient = max(|gradientx| , |gradienty|)
            dst = cv2.bitwise_or(dstx, dsty)
    elif(type == "Laplacian"):
        dst = cv2.Laplacian(img,cv2.CV_64F)
        dst = np.uint8(np.absolute(dst))
    else:
        print("[에러] 잘못된 type 지정")
        return None
    return dst


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('-i', '--image',required=True, help = "Path to the input image")
    args = vars(ap.parse_args())
    filename = args['image']

    image = cv2.imread(filename,cv2.IMREAD_UNCHANGED)
    display_image(image)

    smoothing = smoothing_image(image,'Gaussian',5)
    if(smoothing is not None):
        display_image(smoothing)

    gradient = gradient_image(image,'Laplacian','all')
    if(gradient is not None):
        display_image(gradient)
