import RPi.GPIO as GPIO
import time

# GPIO 핀 번호 모드 설정
GPIO.setmode(GPIO.BCM)

try:
    # GPIO 핀 설정 (입력, 풀다운 저항 활성화)
    GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    # 감지 기준값 설정
    threshold = 0.5 

    while True:
        # 조도 센서 값 읽기
        sensor_value = GPIO.input(15)
        
        # 빛 감지 여부 판단
        if sensor_value > threshold:
            print(1) # 빛을 감지함
        else:
            print(0) # 빛을 감지하지 못함

        time.sleep(1)

finally:
    # GPIO 설정 초기화
    GPIO.cleanup()
