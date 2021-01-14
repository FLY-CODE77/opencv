import cv2
import sys
import numpy as np


src = cv2.imread('circuit.bmp', cv2.IMREAD_GRAYSCALE)


if src is None:
    print('no img')
    sys.exit()

# 이진화 
_, src_bin = cv2.threshold(src, 0, 255, cv2.THRESH_OTSU)

# 레이블링
cnt, labels, stats, centroids = cv2.connectedComponentsWithStats(src_bin)


# 각각의 객체 정보 받아서 빨간색 사각형 그리기

# 0 이 아닌 1 부터 시작인 이유는 배경은 제외 하겠다
dst = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)

for i in range(1, cnt):
    x, y, w, h, a = stats[i]
    if a < 20: # 작은점 걸러버리기
        continue
    
    cv2.rectangle(dst, (x, y, w, h), (0, 0, 255), 2)

cv2.imshow('src', src)
cv2.imshow('src_bin', src_bin)
cv2.imshow('dst', dst)

cv2.waitKey()
cv2.destroyAllWindows()