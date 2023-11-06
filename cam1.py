import cv2

for i in range(31):
    cap = cv2.VideoCapture(i)
    if cap is None or not cap.isOpened():
        print('Warning: unable to open video source: /dev/video{}'.format(i))
    else:
        print('/dev/video{} is open.'.format(i))
        cap.release()  # 장치를 다시 닫습니다.
