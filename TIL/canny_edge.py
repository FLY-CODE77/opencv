# 케니 엣지 검출

import cv2
import sys
import numpy as np


src = cv2.imread('HappyFish.jpg', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exi()

dst = cv2.Canny(src , 50 , 150)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()

