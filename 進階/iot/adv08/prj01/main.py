#########################匯入模組###############################
from umqtt.simple import MQTTClient
import sys
import time
import mcu
from machine import Pin, ADC, PWM
from time import sleep
import mcu

#########################函式與類別定義#########################


def on_message(topic, msg):
    global m
    msg = msg.decode("utf-8")  # Byte to str
    topic = topic.decode("utf-8")
    print(f"mt subscribe topic:{topic}, msg:{msg}")
    m = msg


#########################宣告與設定#############################

wi = mcu.wifi("SingularClass", "Singular#1234")
wi.setup(ap_active=False, sta_active=True)
if wi.connect():
    print(f"IP = {wi.ip}")

mq_server = "mqtt.singularinnovation-ai.com"
mqttClientId = "cringe"
mqtt_username = "singular"
mqtt_password = "Singular#1234"
mqClient0 = MQTTClient(
    mqttClientId, mq_server, user=mqtt_username, password=mqtt_password, keepalive=30
)

try:
    mqClient0.connect()

except:
    sys.exit()
finally:
    print("connected MQTT server")

mqClient0.set_callback(on_message)
mqClient0.subscribe("cringe")
gpio = mcu.gpio()
light_sensor = ADC(0)  # 建立ADC物件
frequency = 1000
duty_cycle = 0
m = ""
RED = PWM(Pin(gpio.D5), freq=frequency, duty=duty_cycle)
#########################主程式#################################

while True:
    light_sensor_reading = light_sensor.read()
    mqClient0.check_msg()
    mqClient0.ping()
    if m == "on":
        RED.duty(1023)
    elif m == "off":
        RED.duty(0)
    elif m == "auto":
        if light_sensor_reading > 900:
            RED.duty(1023)
        else:
            RED.duty(0)

    time.sleep(0.1)
