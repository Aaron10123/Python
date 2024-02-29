#########################匯入模組#########################
from machine import Pin, PWM
from time import sleep

#########################函式與類別定義#########################
frequency = 1000
duty_cycle = 0
led = PWM(Pin(2), freq=frequency, duty=duty_cycle)

#########################宣告與設定#########################
while True:
    led.duty(0)
    sleep(2)
    led.duty(800)
    sleep(2)
    led.duty(1023)
    sleep(2)
#########################主程式#########################
