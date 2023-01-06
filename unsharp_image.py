from __future__ import print_function
import argparse
import cv2
import numpy as np
from display_image2 import display_image

def unsharp_image(img, alpha=1.5, beta = 0.5):
    dst = img.copy()
    dst = cv2.GaussianBlur(dst, ksize = (9,9), sigmaX= 1.5)
    dst = cv2.addWeighted(img,alpha,dst,-beta,0)
    
    return dst


if __name__ == '__main__':
    # 명령 행 인자 처리
    ap = argparse.ArgumentParser()
    ap.add_argument("-i","--input", required= True, help = "Path to the input image")
    ap.add_argument("-o", "--output", required= True, help = "Path to the output image")
    args = vars(ap.parse_args())
    
    infile = args["input"]
    outfile = args["output"]

    image = cv2.imread(infile, cv2.IMREAD_UNCHANGED)
    filterd = unsharp_image(image,1.4,0.5)
    display_image(filterd)
    
    print("Saved to {}".format(outfile))
    cv2.imwrite(outfile,filterd)