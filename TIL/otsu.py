#otsu 자동 이진화 코드

import numpy as np
import sys
import cv2

src = cv2.imread('field.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('no img')
    sys,exit()


th, dst = cv2.threshold(src, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
print("otsu's threshold:" ,th)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()