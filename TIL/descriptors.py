import sys
import numpy as np
import cv2

src1 = cv2.imread('graf1.png', cv2.IMREAD_GRAYSCALE)
src2 = cv2.imread('graf3.png', cv2.IMREAD_GRAYSCALE)

if src1 is None or src2 is None:
    print('img load error')
    sys.exit()

feature = cv2.KAZE_create()
#feature = cv2.AKAZE_create()
#featrue = cv2.ORB_create()

kp1 = feature.detect(src1)

_, desc1 = feature.compute(src1, kp1)

kp2, desc2 = feature.detectAndCompute(src2, None)

print('desc1.shape', desc1.shape)
print('desc1.dtype', desc1.dtype)
print('desc2.shape', desc2.shape)
print('desc2.dtype', desc2.dtype)

dst1 = cv2.drawKeypoints(src1, kp1, None, flags = cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
dst2 = cv2.drawKeypoints(src2, kp2, None, flags = cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.waitKey()
cv2.destroyAllWindows()