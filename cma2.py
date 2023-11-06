import cv2

cap = cv2.VideoCapture(0)  # /dev/video14 장치를 사용
cap.set(cv2.CAP_PROP_FPS,30)
if cap.isOpened():
    ret, frame = cap.read()
    if ret:  # 비디오 캡처가 제대로 되었는지 확인
        cv2.imshow('Captured Image', frame)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print('Failed to capture video.')
        cap.release()  # 비디오 소스를 닫습니다.
else:
    print('Unable to open video source: /dev/video14')
cap.release()
