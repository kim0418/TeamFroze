import cv2

cap = cv2.VideoCapture(0) #0,14,15,21,22
if cap.isOpened():
    ret, frame = cap.read()
    cv2.imshow('Captured Image', frame)
    cv2.waitKey(0)  # 사용자가 키를 누를 때까지 기다립니다.
    cv2.destroyAllWindows()  # 모든 창을 닫습니다.
else:
    print('Unable to open video source: /dev/video0')
cap.release()
