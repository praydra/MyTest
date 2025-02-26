import cv2
import numpy as np

# 캔디 이미지 읽기
image = cv2.imread('candies.png')

# BGR 이미지를 HSV 색 공간으로 변환
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# 붉은색 HSV 범위 정의 (HSV의 두 영역 필요)
lower_red1 = np.array([0, 120, 70])  # 1번째 붉은색 범위: Hue가 낮은 영역
upper_red1 = np.array([10, 255, 255])
lower_red2 = np.array([170, 120, 70])  # 2번째 붉은색 범위: Hue가 높은 영역
upper_red2 = np.array([180, 255, 255])

# 두 범위에 대한 마스크 생성
mask1 = cv2.inRange(hsv_image, lower_red1, upper_red1)
mask2 = cv2.inRange(hsv_image, lower_red2, upper_red2)

# 두 마스크를 결합
red_mask = mask1 + mask2

# 원본 이미지에서 붉은색만 추출
red_candies = cv2.bitwise_and(image, image, mask=red_mask)

# 결과 이미지 출력
cv2.imshow('Original Image', image)
cv2.imshow('Red Candies', red_candies)

# 키 입력 대기 후 종료
cv2.waitKey(0)
cv2.destroyAllWindows()