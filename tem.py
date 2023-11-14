# import Adafruit_DHT as dht
# import time

# timea = int(time.time())
# sumH = 0.0
# sumT = 0.0

# while True:
#     if timea != int(time.time()):
#         humidity, temperature = dht.read_retry(dht.DHT22, 4)
#         tm = time.localtime(time.time())
#         print("Temperature={0:0.1f}*C    Humidity={1:0.1f}%    time={2:d}:{3:d}:{4:d}({5:d}/{6:d})".format(temperature, humidity, tm.tm_hour + 9, tm.tm_min, tm.tm_sec, tm.tm_mon, tm.tm_mday))
#         timea = int(time.time())
#         sumH += humidity
#         sumT += temperature
#         if 0 == int(time.time()) % 60:
#             print("Temperature={0:0.1f}*C    Humidity={1:0.1f}%    time={2:d}:{3:d}({4:d}/{5:d})\n".format(sumT / 60, sumH / 60, tm.tm_hour + 9, tm.tm_min, tm.tm_mon, tm.tm_mday))
#             sumH=0.0
#             sumT=0.0


import cv2
import os
import Adafruit_DHT as dht
import time
import subprocess
#from /usr.src.app.lights

timea = int(time.time())
sumH = 0.0
sumT = 0.0
yolo_offset = 0

while True:
    if timea != int(time.time()):
        if(cv2.waitKey(1) % 0xFF==27):
            break
        humidity, temperature = dht.read_retry(dht.DHT22, 4)
        tm = time.localtime(time.time())
        #print("Temperature={0:0.1f}*C    Humidity={1:0.1f}%    time={2:d}:{3:d}:{4:d}({5:d}/{6:d})".format(temperature, humidity, tm.tm_hour + 9, tm.tm_min, tm.tm_sec, tm.tm_mon, tm.tm_mday))
        timea = int(time.time())
        sumH += humidity
        sumT += temperature
        if 0 == int(time.time()) % 10:
            print("Temperature={0:0.1f}*C    Humidity={1:0.1f}%    time={2:d}:{3:d}({4:d}/{5:d})\n".format(sumT / 10, sumH / 10, tm.tm_hour + 9, tm.tm_min, tm.tm_mon, tm.tm_mday))
            if((sumT/10)>=23):
                if(yolo_offset==0):
                    yolo_offset=1
                    process = subprocess.Popen(["python3", "detect.py", "--source", "0", "--weights", "best.pt","--conf","0.25"])
                #os.system(' "python3 detect.py --source 0 --weights best.pt & echo $! > /tmp/detect_pid"')
                #os.system('sudo docker exec -it yolo_container /bin/bash -c "python3 detect.py --source 0 --weights yolov5s.pt"')
                if((sumT/10)<23):
                    if(yolo_offset==1):
                        yolo_offset=0
                        process.terminate()
                        process = None
                    #os.system(' "kill -SIGINT $(cat /tmp/detect_pid)"')
                    #os.system('sudo docker exec -it yolo_container /bin/bash -c "^C"')
            sumH=0.0
            sumT=0.0
