#########################匯入模組#########################
from machine import Pin, I2C
import dht
import time
import mcu
import ssd1306


#########################函式與類別定義#########################
def on_message(topic, msg):
    global m
    msg = msg.decode("utf-8")
    topic = topic.decode("utf-8")
    print(f"my subscribe topic:{topic},msg:{msg}")
    m = msg


#########################宣告與設定#########################
gpio = mcu.gpio()
servo = mcu.servo(gpio.D8)
i2c = I2C(scl=Pin(gpio.D1), sda=Pin(gpio.D2))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

wi = mcu.wifi("SingularClass", "Singular#1234")
wi.setup(ap_active=False, sta_active=True)
if wi.connect():
    print(f"IP={wi.ip}")

mqtt_client = mcu.MQTT(
    "Aaron", "mqtt.singularinnovation-ai.com", "singular", "Singular#1234"
)
mqtt_client.connect()
mqtt_client.subscribe("YT_A", on_message)
m = "0"
#########################主程式#########################
while True:
    mqtt_client.check_msg()
    oled.text("topic:hello", 0, 0)  # 顯示文字, x座標, y座標
    oled.text(f"servo angle:{m}", 0, 10)  # 顯示文字, x座標, y座標
    oled.show()
    try:
        servo.angle(int(m))
    except:
        pass
    time.sleep(0.1)
