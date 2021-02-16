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

kp1, desc1 = feature.detectAndCompute(src1, None)
kp2, desc2 = feature.detectAndCompute(src2, None)

matcher = cv2.BFMatcher_create()
#matcher = cv2.BFMatcher_create(cv2.NORM_HAMMING)

matches = matcher.match(desc1, desc2)

print('# of kp1:', len(kp1))
print('# of kp2:', len(kp2))
print('# of matches:', len(matches))

dst  = cv2.drawMatches(src1, kp1, src2, kp2, matches, None)

cv2.namedWindow('dst', cv2.WINDOW_NORMAL)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()