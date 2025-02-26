import cv2
import numpy as np

# Candies.png 이미지 읽기
image = cv2.imread("Candies.png")

if image is None:
    print("이미지를 찾을 수 없습니다. 파일 경로를 확인해주세요.")
else:
    # 이미지에서 BGR 채널 분리
    b, g, r = cv2.split(image)

    # Red 채널이 50 이상인 범위 설정
    lower_bound = np.array([0, 0, 200])  # BGR에서 R 값 최소 50
    upper_bound = np.array([255, 255, 255])  # 최대값

    # 범위 내에 있는 값들만 마스크 처리
    mask = cv2.inRange(image, lower_bound, upper_bound)

    # 마스크를 사용해 원본 이미지에서 원하는 색만 추출
    red_extracted = cv2.bitwise_and(image, image, mask=mask)

    # 결과 이미지 출력
    cv2.imshow("Original Image", image)
    cv2.imshow("Red Extracted", red_extracted)

    # 결과 저장 (필요시 사용)
    # cv2.imwrite("Red_Extracted.png", red_extracted)

    cv2.waitKey(0)
    cv2.destroyAllWindows()