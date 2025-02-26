import cv2
import numpy as np

# 이미지를 읽어옵니다. 예제에서는 'input.jpg' 파일을 사용했습니다.
image = cv2.imread('mountain.jpg', cv2.IMREAD_GRAYSCALE)

# 1. 평균값 필터 (Average Filter)
# 커널 생성 (3x3 평균 필터)
avg_kernel = np.ones((3, 3), np.float32) / 9
average_filtered = cv2.filter2D(image, -1, avg_kernel)

# 2. 샤프닝 필터 (Sharpening Filter)
# 샤프닝 커널 생성
sharpen_kernel = np.array([[0, -1, 0],
                           [-1, 5, -1],
                           [0, -1, 0]])
sharpened = cv2.filter2D(image, -1, sharpen_kernel)

# 3. 라플라시안 필터 (Laplacian Filter)
laplacian_filtered = cv2.Laplacian(image, cv2.CV_64F)
laplacian_filtered = cv2.convertScaleAbs(laplacian_filtered)

# 결과 출력 (윈도우로 확인)
cv2.imshow("Original Image", image)
cv2.imshow("Average Filter", average_filtered)
cv2.imshow("Sharpening Filter", sharpened)
cv2.imshow("Laplacian Filter", laplacian_filtered)

# 키 입력 대기 후 창 닫기
cv2.waitKey(0)
cv2.destroyAllWindows()

# 결과를 저장하려면 다음을 사용하세요.
# cv2.imwrite('average_filtered.jpg', average_filtered)
# cv2.imwrite('sharpened.jpg', sharpened)
# cv2.imwrite('laplacian_filtered.jpg', laplacian_filtered)