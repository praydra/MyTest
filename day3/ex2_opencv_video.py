import cv2

# 동영상 파일 읽기
video_path = "test_video.mp4"
cap = cv2.VideoCapture(video_path)

# 동영상이 제대로 열렸는지 확인
if not cap.isOpened():
    print("동영상을 열 수 없습니다. 경로를 확인하세요.")
else:
    # 동영상 프레임 출력
    while True:
        # 프레임 읽기
        ret, frame = cap.read()

        # 동영상이 끝나면 루프 종료
        if not ret:
            print("동영상 재생이 완료되었습니다.")
            break

        # 프레임 화면에 출력
        cv2.imshow("Video", frame)

        # 키 입력 대기 (25ms 대기, 약 40 FPS에 해당)
        # Esc 키(27)를 누르면 종료
        if cv2.waitKey(25) & 0xFF == 27:
            print("사용자에 의해 종료되었습니다.")
            break

    # 모든 자원 해제
    cap.release()
    cv2.destroyAllWindows()