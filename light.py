import RPi.GPIO as GPIO
import time

# GPIO 핀 번호 모드 설정
GPIO.setmode(GPIO.BCM)

# GPIO 핀 설정 (입력, 풀다운 저항 활성화)
light_pin = 22
GPIO.setup(light_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
    while True:
        # 조도 센서 값 읽기
        sensor_value = GPIO.input(light_pin)
        
        # 빛 감지 여부 출력
        if sensor_value == 0:
            print("Light Detected")
        else:
            print("Light Not Detected")

        time.sleep(1)

finally:
    # GPIO 설정 초기화
    GPIO.cleanup()
