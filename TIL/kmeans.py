import sys
import numpy as np 
import cv2

src = cv2.imread("2.jpg")

if src is None:
    print("image load fail")
    sys.exit()

data = src.reshape((-1, 3)).astype(np.float32)

criteria = (cv2.TERM_CRITERIA_EPS|cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)

for K in range(2, 10):
    print('K;', K)
    ret, label, center = cv2.kmeans(data, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

    center = np.uint8(center)
    dst = center[label.flatten()]
    dst = dst.reshape((src.shape))

    cv2.imshow('src', src)
    cv2.imshow('dst', dst)
    cv2.waitKey()

cv2.destroyAllWindows()