#########################匯入模組#########################
from umqtt.simple import MQTTClient
import sys
import time
import mcu


#########################函式與類別定義#########################
def on_message(topic, msg):
    msg = msg.decode("utf-8")
    topic = topic.decode("utf-8")
    print(f"my subscribe topic:{topic},msg:{msg}")


#########################宣告與設定#########################
wi = mcu.wifi("SingularClass", "Singular#1234")
wi.setup(ap_active=False, sta_active=True)
if wi.connect():
    print(f"IP={wi.ip}")

MQTT = mcu.MQTT("Aaron", "mqtt.singularinnovation-ai.com", "singular", "Singular#1234")

MQTT.connect()

MQTT.subscribe("YT_A", on_message)
#########################主程式#########################
while True:

    MQTT.check_msg()
    time.sleep(0.1)
