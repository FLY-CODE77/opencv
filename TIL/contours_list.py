import sys
import random
import numpy as np
import cv2

src = cv2.imread('HappyFish.jpg', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('no img')
    sys.exit()

_, src_bin = cv2.threshold(src, 0 , 255, cv2.THRESH_OTSU)
counter, _ = cv2.findContours(src_bin, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

h, w = src.shape[:2]
dst = np.zeros((h,w,3), np.uint8)

for i in range(len(counter)):
    c = (random.randint(0,255),random.randint(0,255), random.randint(0,255))
    cv2.drawContours(dst, counter, i , c, 1, cv2.LINE_AA)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.imshow('src_bin', src_bin)
cv2.waitKey()
cv2.destroyAllWindows()