import sys
import numpy as np
import cv2

src = cv2.imread("symbols.png", cv2.IMREAD_GRAYSCALE)
if src is None:
    print('image fail')
    sys.exit()

tm = cv2.TickMeter()

# GFTT
tm.start()

corners = cv2.goodFeaturesToTrack(src , 400, 0.01, 10)
tm.stop()
print('GFTT: {}ms'.format(tm.getTimeMilli()))

dst1 = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)

if corners is not None:
    for i in range(corners.shape[0]):
        pt = (int(corners[i,0,0]), int(corners[i,0,1]))
        cv2.circle(dst1, pt, 5, (0,0,255),2)

tm.reset()
tm.start()

fast = cv2.FastFeatureDetector_create(60)
keypoint = fast.detect(src)

tm.stop()
print('Fast : {} ms.'.format(tm.getTimeMilli()))

dst2 = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)

for kp in keypoint:
    pt = (int(kp.pt[0]), int(kp.pt[1]))
    cv2.circle(dst2 , pt, 5, (0,0,255), 2)

cv2.imshow('GFTT', dst1)
cv2.imshow('FAST', dst2)
cv2.waitKey()
cv2.destroyAllWindows()