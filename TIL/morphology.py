# morphology 연산

import cv2
import numpy as np
import sys 

src = cv2.imread('circuit.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('no img')
    sys.exit()

se = cv2.getStructuringElement(cv2.MORPH_RECT, (5,3))


dst = cv2.erode(src, se)
dst1 = cv2.dilate(src, se)

# dilate 영상을 보니깐 중간에 회로도 부분들이 끊김이 있다.
# 확장시키는 방법으로 어떻게 끊김 없이 영상 바꿀수 있을까!?
# 커널을 가로 1, 세로를 길게 해서 세로 방향으로 확장이 잘 일어날수 있게 해준다.\

se = cv2.getStructuringElement(cv2.MORPH_RECT, (1,7))
dst2 = cv2.dilate(src, se)


cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.waitKey()
cv2.destroyAllWindows()
