import numpy as np
import sys
import cv2

# to synthesis
src = cv2.imread('airplane.bmp',cv2.IMREAD_COLOR)
mask = cv2.imread('mask_palne.bmp',cv2.IMREAD_GRAYSCALE)
dst = cv2.imread('field.bmp',cv2.IMREAD_COLOR)

# synthesis cv2.copyTo
cv2.copyTo(src,mask,dst)

# src : plane img
# mask : grayscale mask!
# dst : green field 

# dst[mask>0] = src[mask>0]
cv2.imshow('dst',dst)
cv2.waitKey()
cv2.destroyAllWindows()

