import cv2
import numpy as np

# Lenna 이미지를 읽어오기
image = cv2.imread("Lenna.png")

# 이미지를 BGR에서 HSV 색 공간으로 변환
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# HSV 채널 분리
h, s, v = cv2.split(hsv_image)

# 각 성분 출력
print("Hue Channel:\n", h)
print("\nSaturation Channel:\n", s)
print("\nValue Channel:\n", v)

# 결과를 시각적으로 확인하기 위해 각 채널을 표시
cv2.imshow("Hue", h)
cv2.imshow("Saturation", s)
cv2.imshow("Value", v)

# 원본 이미지와 HSV 이미지를 확인
cv2.imshow("Original Image", image)
cv2.imshow("HSV Image", hsv_image)

# 키 입력 대기 후 창 닫기
cv2.waitKey(0)
cv2.destroyAllWindows()