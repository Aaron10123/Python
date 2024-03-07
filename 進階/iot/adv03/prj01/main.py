#########################匯入模組#########################
from machine import Pin, PWM
from time import sleep

#########################函式與類別定義#########################


#########################宣告與設定#########################
frequency = 1000
duty_cycle = 0
led = PWM(Pin(2), freq=frequency, duty=duty_cycle)

#########################主程式#########################
while True:
    for i in range(1023, -1, -1):
        led.duty(i)
        sleep(0.002)
    for x in range(-1, 1023):
        led.duty(x)
        sleep(0.002)
