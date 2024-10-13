import requests
import datetime
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import os
import sys
from ttkbootstrap import *
from PIL import Image, ImageTk

#######################設定工作目錄########################
os.chdir(sys.path[0])  # 設定工作目錄

#######################定義常數########################
API_KEY = "892da2f13edf3c7f382637760e72d224"  # 填入你的API密鑰
BASE_URL = "https://api.openweathermap.org/data/2.5/forecast?"  # 基本URL
UNITS = "metric"  # 單位(公制)
LANG = "zh_tw"  # 語言(繁體中文)
ICON_BASE_URL = "https://openweathermap.org/img/wn/"  # 圖示URL


#######################主程式########################
def draw_graph():
    city_name = "Taipei"

    # 建立圖片
    send_url = f"{BASE_URL}appid={API_KEY}&q={city_name}&units={UNITS}&lang={LANG}"

    print(f"發送的URL: {send_url}")  # 印出發送的URL
    response = requests.get(send_url)
    response.raise_for_status()  # 檢查回應狀態碼
    info = response.json()

    Xlist = []  # 定義X軸的序列
    Ylist = []  # 定義Y軸的序列

    if "city" in info:
        # 處理並顯示天氣預報
        for forecast in info["list"]:
            dt_text = forecast["dt_txt"]  # 取得日期
            temp = forecast["main"]["temp"]  # 取得溫度
            time = datetime.strptime(dt_text, "%Y-%m-%d %H:%M:%S").strftime(
                "%m/%d %H"
            )  # 取得日期
            Xlist.append(time)  # 將日期加入序列
            Ylist.append(temp)  # 將溫度加入序列
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
    plt.close()

    image = Image.open("weather_forecast.png")
    img = ImageTk.PhotoImage(image)

    canvas.config(width=image.width, height=image.height)
    canvas.create_image(image.width // 2, image.height // 2, image=img)
    canvas.image = img


#######################建立視窗########################
Window = tk.Tk()
Window.title("天氣預報")
#######################創建畫布########################
canvas = Canvas(Window, width=0, height=0, bg="white")
canvas.grid(row=0, column=0, padx=10, pady=10)


#######################設定字型########################
font_size = 20
Window.option_add("*Font", ("Helevetica", font_size))
#######################設定主題########################
Style = Style(theme="darkly")
Style.configure("my.TButton", font=("Helevetica", font_size))

#######################建立按鈕########################
search_button = Button(
    Window, text="顯示天氣預報", command=draw_graph, style="my.TButton"
)

search_button.grid(row=0, column=2, padx=10, pady=10)
#######################運行應用程式########################
Window.mainloop()
