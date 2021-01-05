# 허브 변환 원 검출

import cv2
import sys
import numpy as np

src = cv2.imread('HappyFish.jpg')

if src is None:
    print('no img')
    sys.exit()

gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

# 블러링 하고 약간 디테일을 둑이면 잘됨
# 블러링을 잘해줘야 한다

blr = cv2.GaussianBlur(gray, (0,0), 1.0)

def on_trackbar(pos):
    rmin = cv2.getTrackbarPos('minRadius', 'img')
    rmax = cv2.getTrackbarPos('maxRadius', 'img')
    th = cv2.getTrackbarPos('threshold', 'img')

    circles =   cv2.HoughCircles(blr, cv2.HOUGH_GRADIENT, 1, 50 , param1= 120, param2=th, minRadius=rmin, maxRadius=rmax)
    
    dst = src.copy()
    for i in range(circles.shape[1]):
        cx, cy, radius = circles[0][i]
        cv2.circle(dst, (cx,cy), int(radius), (0,0,255), 2, cv2.LINE_AA)
    
    return cv2.imshow('img', dst)

cv2.imshow('img', src)
cv2.createTrackbar('minRadius', 'img', 0, 100, on_trackbar)
cv2.createTrackbar('maxRadius', 'img', 0, 150, on_trackbar)
cv2.createTrackbar('threshold', 'img', 0, 100, on_trackbar)
cv2.setTrackbarPos('minRadius', 'img', 10)
cv2.setTrackbarPos('maxRadius', 'img', 20)
cv2.setTrackbarPos('threshold', 'img', 10)
cv2.waitKey()

cv2.destroyAllWindows()
