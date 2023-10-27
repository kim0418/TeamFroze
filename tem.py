import Adafruit_DHT as dht
import time

timea = int(time.time())
sumH = 0.0
sumT = 0.0

while True:
    if timea != int(time.time()):
        humidity, temperature = dht.read_retry(dht.DHT22, 4)
        tm = time.localtime(time.time())
        print("Temperature={0:0.1f}*C    Humidity={1:0.1f}%    time={2:d}:{3:d}:{4:d}({5:d}/{6:d})".format(temperature, humidity, tm.tm_hour + 9, tm.tm_min, tm.tm_sec, tm.tm_mon, tm.tm_mday))
        timea = int(time.time())
        sumH += humidity
        sumT += temperature
        if 0 == int(time.time()) % 60:
            print("Temperature={0:0.1f}*C    Humidity={1:0.1f}%    time={2:d}:{3:d}({4:d}/{5:d})\n".format(sumT / 60, sumH / 60, tm.tm_hour + 9, tm.tm_min, tm.tm_mon, tm.tm_mday))
            sumH=0.0
            sumT=0.0
