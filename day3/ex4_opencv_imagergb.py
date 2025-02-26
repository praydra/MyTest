import cv2

# 이미지 읽기
image = cv2.imread('Lenna.png')

# 이미지가 제대로 로드되었는지 확인
if image is None:
    print("이미지를 로드할 수 없습니다. 경로를 확인하세요.")
else:
    # 이미지 크기 출력
    print(f"Image Shape: {image.shape}")

    # BGR 채널 분리
    blue, green, red = cv2.split(image)

    # 각 성분 출력
    print("Blue Channel:\n", blue)
    print("Green Channel:\n", green)
    print("Red Channel:\n", red)



    # 각 채널 출력
    cv2.imshow("Original Image", image)  # 원본 이미지
    cv2.imshow("Blue Channel", blue)  # Blue 채널
    cv2.imshow("Green Channel", green)  # Green 채널
    cv2.imshow("Red Channel", red)  # Red 채널

    # 키 입력 대기
    cv2.waitKey(0)

    # 모든 창 닫기
    cv2.destroyAllWindows()