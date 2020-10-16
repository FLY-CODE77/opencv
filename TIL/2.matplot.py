# 어떤 컬러 데이터를 불러오면 bgr순서로 불러오게 되어 있음
# matplotlib 같은 경우에는 rgb순서로 가져올려는 해서 영상이 잘 못 나올수 있다
# cvtColor()함수로 rgb 순으로 변경해서 matplotlib 에 적용 해줘야 한다
# plt.imshow() 에서 grayscale 같은 경우 camp = 'gray'로 설정을 해줘야 한다

import matplotlib.pyplot as plt
import cv2


# 컬러 영상 출력
imgBGR = cv2.imread('cat.bmp')
imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB) # bgr 을 rgb 로 변환하겠다는 명시적 

plt.axis('off') # 사진에 눈금 안 만들기 위해서 하는거 
plt.imshow(imgRGB)
plt.show()

# 그레이스케일 영상 출력
imgGray = cv2.imread('cat.bmp', cv2.IMREAD_GRAYSCALE)

plt.axis('off')
plt.imshow(imgGray, cmap='gray') # grayscale 을 쓰고 싶으면 cmap = 'gray' 을 쓴다
plt.show()

# 두 개의 영상을 함께 출력
plt.subplot(121), plt.axis('off'), plt.imshow(imgRGB) # subplot  1개의 행 2개의 열 로 공간을 나눠서 1 열에 그림을 그려라 
plt.subplot(122), plt.axis('off'), plt.imshow(imgGray, cmap='gray')
plt.show()
