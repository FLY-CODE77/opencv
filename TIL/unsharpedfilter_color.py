# 언샤프 컬러
import cv2
import numpy as np
import sys

src = cv2.imread('rose.bmp')

if src is None:
    print(1)
    sys.exit()

src_ycrcb = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)

# np.float32 로하는 이유
# uint8 로 나오는 경우 가우시안 블러에 의 해서 소수점들이 짤리는 경우가 생긴다
# 미묘한 차이가 있기 때문에 float로 변경해서 해준다!
src_f = src_ycrcb[:,:,0].astype(np.float32)
blr = cv2.GaussianBlur(src_f, (0,0), 2.0)
# 최종 버전으로 나올때 np.unit8 로 변 경시켜 준다.
src_ycrcb [:,:,0] = np.clip(2. * src_f  - blr, 0, 255).astype(np.uint8)

dst = cv2.cvtColor(src_ycrcb,cv2.COLOR_YCrCb2BGR)

cv2.imshow('src',src)
cv2.imshow('dst',dst)
cv2.waitKey()
cv2.destroyAllWindows()
