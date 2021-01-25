import cv2
import sys
import numpy as np 

src = cv2.imread("HappyFish.jpg")

if src is None:
    print('no img')
    sys.exit()


rc = cv2.selectROI(src)
mask = np.zeros(src.shape[:2], np.uint8)
cv2.grabCut(src, mask, rc, None, None, 5, cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask == 0)| (mask == 2), 0, 1).astype('uint8')

dst = src * mask2[:, :, np.newaxis]
mask = mask * 64 

cv2.imshow('mask', mask)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()