# 이진화 트랙바로 이용해서 조정해서 최적값 찾기

import cv2
import sys
import numpy as numpy


src = cv2.imread('HappyFish.jpg', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('no img')
    sys.exit()

def on_threshold(pos):
    _, dst = cv2.threshold(src, pos, 255, cv2.THRESH_BINARY)
    cv2.imshow('dst', dst)


cv2.imshow('src', src)
cv2.namedWindow('dst')
# 윈도우 사이즈는 생각을 해봐야 할듯
cv2.createTrackbar('THR', 'dst', 0, 255, on_threshold)
cv2.setTrackbarPos('THR', 'dst', 128)

cv2.waitKey()
cv2.destroyAllWindows()