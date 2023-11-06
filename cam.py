import cv2

# 비디오 장치를 차례로 테스트
for i in range(31):  # 31은 테스트할 비디오 장치의 수를 의미합니다.
    cap = cv2.VideoCapture(i)
    if cap.isOpened():
        ret, frame = cap.read()
        if ret:
            cv2.imshow('Camera Test', frame)
            cv2.waitKey(0)  # 키를 누를 때까지 이미지를 표시합니다.
            cap.release()
    cv2.destroyAllWindows()
