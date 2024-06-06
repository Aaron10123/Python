import getpass
import os

os.environ["OPENAI_API_KEY"] = getpass.getpass()

from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-4o", temperature=0.1)
from langchain_core.messages import HumanMessage

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
    print(msg.content)
