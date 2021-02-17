import numpy as np
import sys
import cv2


src1 = cv2.imread('graf1.png', cv2.IMREAD_GRAYSCALE)
src2 = cv2.imread('graf3.png', cv2.IMREAD_GRAYSCALE)

if src1 is None or src2 is None:
    print('Image load failed!')
    sys.exit()

feature = cv2.KAZE_create()
#feature = cv2.AKAZE_create()
#feature = cv2.ORB_create()
kp1, desc1 = feature.detectAndCompute(src1, None)
kp2, desc2 = feature.detectAndCompute(src2, None)


matcher = cv2.BFMatcher_create()
matches = matcher.match(desc1, desc2)


matches = sorted(matches, key=lambda x: x.distance)
good_matches = matches[:80]

# homograpy calc
pts1 = np.array([kp1[m.queryIdx].pt for m in good_matches]).reshape(-1,1,2).astype(np.float32)
pts2 = np.array([kp2[m.trainIdx].pt for m in good_matches]).reshape(-1,1,2).astype(np.float32)


H, _ = cv2.findHomography(pts1, pts2, cv2.RANSAC)


dst = cv2.drawMatches(src1, kp1, src2, kp2, good_matches, None, flags = cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)


(h, w) = src1.shape[:2]
corners1 = np.array([[0, 0], [0, h-1], [w-1, h-1], [w-1, 0]]
                    ).reshape(-1, 1, 2).astype(np.float32)

corners2 = cv2.perspectiveTransform(corners1, H)
corners2 = corners2 + np.float32([w, 0])

cv2.polylines(dst, [np.int32(corners2)], True, (0,255,255), 2, cv2.LINE_AA)

cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()