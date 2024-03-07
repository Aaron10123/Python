#########################匯入模組#########################
from machine import Pin, PWM
from time import sleep
import mcu

#########################函式與類別定義#########################


#########################宣告與設定#########################
frequency = 1000
duty_cycle = 0
led = PWM(Pin(2), freq=frequency, duty=duty_cycle)
gpio = mcu.gpio()
RED = PWM(Pin(gpio.D5, Pin.OUT), freq=frequency, duty=duty_cycle)
GREEN = PWM(Pin(gpio.D6, Pin.OUT), freq=frequency, duty=duty_cycle)
BLUE = PWM(Pin(gpio.D7, Pin.OUT), freq=frequency, duty=duty_cycle)
#########################主程式#########################
while True:
    for i in range(1023, -1, -1):
        RED.duty(i)
        BLUE.duty(1023 - i)
        sleep(0.002)
    for i in range(1023, -1, -1):
        RED.duty(i)
        GREEN.duty(1023 - i)
        sleep(0.002)
    for i in range(1023, -1, -1):
        BLUE.duty(i)
        GREEN.duty(1023 - i)
        sleep(0.002)
