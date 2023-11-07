import cv2
import torch
import numpy as np

path='/home/froze/yolov5/detect.py'
model = torch.hub.load('ultralytics/yolov5','custom',path, force_reload=true)

def realtime_object_detection():
  cpa=cv2.VideoCapture(0)

  while true:
    ret,frame=cap.read()

    while ret==False:
      cap.release())
      cap.cv.VideoCapture(0)
      ret, frame = cap.read()

    cv2.imshow('image_jpg',frame)
    if cv.waitKey(1)==ord('q'):
      break
  cap.release()
