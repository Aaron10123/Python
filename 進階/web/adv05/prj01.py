import requests
import datetime
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import os
import sys


#######################設定工作目錄########################
os.chdir(sys.path[0])  # 設定工作目錄

#######################定義常數########################
API_KEY = "892da2f13edf3c7f382637760e72d224"  # 填入你的API密鑰
BASE_URL = "https://api.openweathermap.org/data/2.5/forecast?"  # 基本URL
UNITS = "metric"  # 單位(公制)
LANG = "zh_tw"  # 語言(繁體中文)
ICON_BASE_URL = "https://openweathermap.org/img/wn/"  # 圖示URL

#######################主程式########################
city_name = "Taipei"
send_url = f"{BASE_URL}appid={API_KEY}&q={city_name}&units={UNITS}&lang={LANG}"
print(f"發送的URL: {send_url}")
response = requests.get(send_url)
response.raise_for_status()
info = response.json()

Xlist = []
Ylist = []

if "city" in info:
    for forecast in info["list"]:
        dt_text = forecast["dt_txt"]
        temp = forecast["main"]["temp"]
        time = datetime.datetime.strptime(dt_text, "%Y-%m-%d %H:%M:%S").strftime(
            "%m/%d %H"
        )
        Xlist.append(time)
        Ylist.append(temp)
        print(f"日期: {time} - 溫度: {temp}°C")

        wreather_description = forecast["weather"][0]["description"]
        print(f"日期: {dt_text} - 溫度: {temp}°C - 描述: {wreather_description}")
else:
    print("查詢失敗")

#######################繪製圖表########################
font = FontProperties(fname="LXGWWenKaiTC-Light.ttf", size=14)
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(Xlist, Ylist)
ax.set_xlabel("日期", fontproperties=font)
ax.set_ylabel("溫度", fontproperties=font)
ax.set_title("天氣預報", fontproperties=font)
plt.xticks(rotation=45)
plt.tight_layout()
fig.savefig("weather_forecast.png")
plt.show()
