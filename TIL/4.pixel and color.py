import sys
import cv2
# 영상 속성과 픽셀 값 처리

# OPenCv는 영상 데이터를 numpy.ndarray로 표현된다
# ndarray는 주요한 feature를 가지고 있는데
# ndim : 차원 수 (len(img.shape))
# shape : 각 차원의 크기 (h,x) # 그레이 스케일 , (h,w,3) # 컬러 스케일 
# size : 전체 원소 갯수
# dtype : 원소의 데이터 타입 : 영상 데이터 같은 경우 uint8 로 구성됨 1beat = 1byte 를 가지고 있다 - 부호가 없는 8 비트 정수 

# 영상 불러오기
img1 = cv2.imread('cat.bmp',cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('cat.bmp',cv2.IMREAD_COLOR)

print((img1.shape)) # 이 차원으로 잡히고 
print((img2.shape)) # 삼 차원으로 잡힌다 


if img1 is None or img2 is None:
    print('Image load failed')
    sys.exit()

# 사진 픽셀 단위로 색 변경 시키는 방법

# h,w = img1.shape
# h,w = img2.shape[:2]

# for y in range(h):
#     for x in range(w):
#         img1[y,x] = 0
#         img2[y,x] = (0,255,255)
# # 역시 for 문 딜레이가 존재 한다 .. 
# # 별로 안 좋은 코드 --> opencv, numpy 로 제공하는 기능으로 사용한다
# img1[:,:] = 0
# img2[:,:] = (0,255,255)


cv2.imshow('img1',img1)
cv2.imshow('img2',img2)
cv2.waitKey()


cv2.destroyAllWindows()

# grayscale 인지 확인하는 방법
if img1.ndim ==2: # ndim - > 차원이 몇 차원인지 표현스
    print('img is a grayscale')

if img2.ndim ==3 :
    print('img2 is a colorscale')

# 영상에서 픽셀 값 참조하는 코드
# img 영상에 X=20 , Y=10 에 존제하는 픽셀 값을 알고 싶을때는

# 그레이스 스케일 일 때는 한 평면에만 존재 하니깐 하나의 값만 나온다
x = 20 
y = 10
p = img1[y,x]
print(p)

# color 성분일때는 3개의 평면이 겹쳐 있는것이니깐 각 각의 위치에 있는 성분값이 나온다 - > 리스트 형으로 [a,b,c]
p2 = img2[y,x]
print(p2)

