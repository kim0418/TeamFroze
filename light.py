# import RPi.GPIO as GPIO
# import time

# # GPIO 핀 번호 모드 설정
# GPIO.setmode(GPIO.BCM)

# # GPIO 핀 설정 (입력, 풀다운 저항 활성화)
# light_pin = 22
# GPIO.setup(light_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# try:
#     while True:
#         # 조도 센서 값 읽기
#         sensor_value = GPIO.input(light_pin)
        
#         # 빛 감지 여부 출력
#         if sensor_value == 0:
#             print("Light Detected")
#         else:
#             print("Light Not Detected")

#         time.sleep(1)

# finally:
#     # GPIO 설정 초기화
#     GPIO.cleanup()



import RPi.GPIO as GPIO
import time
import os

# GPIO 핀 번호 모드 설정
GPIO.setmode(GPIO.BCM)

# GPIO 핀 설정 (입력, 풀다운 저항 활성화)
light_pin = 22
GPIO.setup(light_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# 도커 컨테이너에 대한 명령을 실행하는 함수
def run_command_in_container(container_name, command):
    os.system(f'sudo docker exec -it {container_name} {command}')

# 도커 컨테이너 이름
container_name = 'yolo_container'

# 실행 중인지 여부를 추적하는 플래그
running = False

try:
    while True:
        # 조도 센서 값 읽기
        sensor_value = GPIO.input(light_pin)

        # 빛 감지 여부에 따라 도커 컨테이너 내의 스크립트 실행
        if sensor_value == 0 and not running:
            print("Light Detected, Starting Script")
            run_command_in_container(container_name, 'python3 detect.py --source 0 --weights best.pt --conf 0.25 &')
            running = True
        elif sensor_value != 0 and running:
            print("Light Not Detected, Stopping Script")
            run_command_in_container(container_name, 'pkill -f "python3 detect.py --source 0 --weights best.pt --conf 0.25"')
            running = False

        time.sleep(1)

finally:
    # GPIO 설정 초기화
    GPIO.cleanup()
