import sys
import numpy as np
import cv2

src1 = cv2.imread('graf1.png', cv2.IMREAD_GRAYSCALE)
src3 = cv2.imread('graf3.png', cv2.IMREAD_GRAYSCALE)

if src1 is None or src3 is None:
    print('img load fail')
    sys.exit()

feature = cv2.KAZE_create()

kp1 = feature.detect(src1)
kp3 = feature.detect(src3)

print("# of kp1 :", len(kp1))
print("# of kp3 :", len(kp3))

dst1 = cv2.drawKeypoints(src1, kp1, None, flags = cv2.DrawMatchesFlags_DRAW_RICH_KEYPOINTS)
dst3 = cv2.drawKeypoints(src3, kp3, None, flags = cv2.DrawMatchesFlags_DRAW_RICH_KEYPOINTS)

cv2.imshow('dst1', dst1)
cv2.imshow('dst3', dst3)
cv2.waitKey()
cv2.destroyAllWindows()