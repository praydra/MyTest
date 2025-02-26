import cv2

# 카메라 열기 (기본 카메라의 인덱스는 0)
cap = cv2.VideoCapture(0)

# 카메라가 정상적으로 열렸는지 확인
if not cap.isOpened():
    print("카메라를 열 수 없습니다.")
else:
    print("카메라를 실행합니다. 'ESC' 키를 눌러 종료하세요.")

    while True:
        # 프레임 읽기
        ret, frame = cap.read()

        # 프레임 읽기에 실패하면 루프 종료
        if not ret:
            print("프레임을 읽을 수 없습니다. 종료합니다.")
            break

        # 현재 프레임 화면에 출력
        cv2.imshow("Camera", frame)

        # ESC 키(27)를 누르면 종료
        if cv2.waitKey(1) & 0xFF == 27:
            print("사용자에 의해 종료되었습니다.")
            break

    # 자원 해제
    cap.release()
    cv2.destroyAllWindows()