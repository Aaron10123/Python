#########################匯入模組#########################
import paho.mqtt.client as mqtt
import time
import getpass
import os
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage


#########################函式與類別定義#########################
def on_publish(client, userdata, mid, reason_code, properties):
    print(f"Message {mid} has been published.")


os.environ["OPENAI_API_KEY"] = getpass.getpass()
model = ChatOpenAI(model="gpt-4o", temperature=0.1)
#########################宣告與設定#########################
client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
client.on_publish = on_publish
client.username_pw_set("singular", "Singular#1234")
client.connect("mqtt.singularinnovation-ai.com", 1883, 60)
client.loop_start()

#########################主程式#########################
while True:
    ans = input("請輸入想跟AI說的話:")

    msg = model.invoke(
        [
            HumanMessage(
                content="""
                你是一個控制室內燈光開關以及車庫門的居家管理員
                你可以根據使用者說的話來控制燈光,關燈,開車庫門,關車庫門
                請回答'on'或'off'或'None'或'open'或'close'
                可同時回答多個指令
                'open'代表開車庫門
                'close'代表關車庫門
                'on'代表開燈
                'off'代表關燈
                'None'代表不要做任何事
                不能回答其他的字串
                """
            ),
            HumanMessage(content=ans),
        ]
    )
    result = client.publish("YT_A", msg.content)  # 發布訊息
    result.wait_for_publish()  # 等待發布完成
    # 檢查發布是否成功
    if result.rc == mqtt.MQTT_ERR_SUCCESS:
        print("Message published successfully")
    else:
        print("Failed to publish message")
    time.sleep(0.1)
# 這裡有點暗，我需要一些光線。
