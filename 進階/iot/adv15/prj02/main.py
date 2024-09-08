#########################匯入模組#########################

import mcu
import time
from machine import Pin, I2C
import ssd1306


#########################函式與類別定義#########################
def on_message(topic, msg):
    global m
    msg = msg.decode("utf-8")  # Byte to str
    topic = topic.decode("utf-8")
    print(f"my subscribe topic:{topic}, msg:{msg}")
    m = msg


#########################宣告與設定#########################
gpio = mcu.gpio()
servo = mcu.servo(gpio.D8)
i2c = I2C(scl=Pin(gpio.D1), sda=Pin(gpio.D2))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
LED = mcu.LED(gpio.D5, gpio.D6, gpio.D7)

wi = mcu.wifi("SingularClass", "Singular#1234")
wi.setup(ap_active=False, sta_active=True)
if wi.connect():
    print(f"IP={wi.ip}")

mqtt_client = mcu.MQTT("Ray", "mqtt.singularinnovation-ai.com", "singular", "Singular#1234")
mqtt_client.connect()
mqtt_client.subscribe("hello", on_message)
m = "no message"

#########################主程式#########################
while True:
    mqtt_client.check_msg()  # 等待已訂閱的主題發送資料
    oled.fill(0)  # 清除螢幕
    oled.text("topic : hello", 0, 0)
    oled.text(f"servo angle: {m}", 0, 10)
    oled.show()
    if "ON" in m:
        LED.BLUE.value(1)
        LED.GREEN.value(1)
        LED.RED.value(1)
    if "OFF" in m:
        LED.BLUE.value(0)
        LED.GREEN.value(0)
        LED.RED.value(0)
    if "None" in m:
        pass
    if "open" in m:
        servo.angle(180)
    if "close" in m:
        servo.angle(90)
    time.sleep(1)