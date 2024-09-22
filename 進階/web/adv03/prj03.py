import requests
import os
import sys

#######################定義常數########################
API_KEY = "892da2f13edf3c7f382637760e72d224"  # 填入你的API密鑰
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"  # 基本URL
UNITS = "metric"  # 單位(公制)
LANG = "zh-tw"  # 語言(繁體中文)
ICON_BASE_URL = "https://openweathermap.org/img/wn/"  # 圖示URL

#######################主程式########################
os.chdir(sys.path[0])  # 設定工作目錄

city = input("請輸入要查詢的城市名稱: ")

send_url = f"{BASE_URL}appid={API_KEY}&q={city}&units={UNITS}&lang={LANG}"
print(send_url)
response = requests.get(send_url)
info = response.json()


if "weather" in info and "main" in info:
    current_temperature = info["main"]["temp"]
    weather_description = info["weather"][0]["description"]
    icon_code = info["weather"][0]["icon"]

    print(f"城市名稱: {city}")
    print(f"當前溫度: {current_temperature}°C")
    print(f"天氣描述: {weather_description}")

    icon_url = f"{ICON_BASE_URL}{icon_code}@2x.png"
    print(f"天氣圖示: {icon_url}")
    icon_response = requests.get(icon_url)

    if icon_response.status_code == 200:
        with open(f"{icon_code}.png", "wb") as icon_file:
            icon_file.write(icon_response.content)
        print(f"圖片已保存至{icon_code}.png")
    else:
        print(f"圖片下載失敗")

else:
    print("查詢失敗")
