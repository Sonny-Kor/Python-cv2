from __future__ import print_function
import argparse
import cv2

def display_image(img):
    # 영상 정보 출력
    print("(rows,cols,ch): {}".format(img.shape))

    # 영상 출력 윈도우 생성
    cv2.namedWindow('image',cv2.WINDOW_NORMAL)
    # 윈도우에 영상 출력
    cv2.imshow('image',img)

    # 사용자 입력 대기
    cv2.waitKey(0)
    # 윈도우 파괴
    cv2.destroyAllWindows()

def handle_ROI(img, rect):
    [sx, sy, ex, ey] = rect
    if(sx<0 or sy<0 or ex>=img.shape[1] or ey>= img.shape[0]):
        print("invalid coord")
        return None
    crop = img[sy:ey, sx:ex]
    return crop

def split_channel(img):
    b, g, r = cv2.split(img)

    return r,g,b

def merge_channel(r,g,b):
    img = cv2.merge((b,g,r))
    return img

def get_pixel(img, x, y):
    # 좌표 유효성 확인
    if( x>= img.shape[1] or y>= img.shape[0]):
        print("Invalid coord. ({}, {})".format(x,y))
        return None
    return img[y,x]

def put_pixel(img, x, y, value):
    if (x >= img.shape[1] or y>= img.shape[0]):
        print("Invalid coord. ({}, {})".format(x,y))
    img[y, x] = value

if __name__ == '__main__':
    
    filename = "images\\1920x1280\\cat.jpg"

    image = cv2.imread(filename, cv2.IMREAD_COLOR)
    value = get_pixel(image, 30, 20)
    print("[Before] value : {}".format(value))

    put_pixel(image, 30, 20, 0)
    value = get_pixel(image, 30, 20)
    print("[After] value : {}".format(value))

    if(image is None):
        print('{}: reading error'.format(filename))
    else:
        display_image(image)

    