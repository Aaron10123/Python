import requests
import datetime
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import os
import sys
from ttkbootstrap import *
from PIL import Image, ImageTk

#######################定義常數########################
API_KEY = "892da2f13edf3c7f382637760e72d224"  # 填入你的API密鑰
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"  # 基本URL
FORECAST_URL = "https://api.openweathermap.org/data/2.5/forecast?"  # 基本URL
UNITS = "metric"  # 單位(公制)
LANG = "zh-tw"  # 語言(繁體中文)
ICON_BASE_URL = "https://openweathermap.org/img/wn/"  # 圖示URL


#######################定義函數########################
def on_switch_change():
    global UNITS, current_temperature
    UNITS = "metric" if check_type.get() else "imperial"

    if temperature_labal["text"] != "溫度: ???°C":
        if UNITS == "metric":
            current_temperature = round((current_temperature - 32) * 5 / 9, 2)
        else:
            current_temperature = round(current_temperature * 9 / 5 + 32, 2)
        temperature_labal.config(
            text=f"溫度: {current_temperature}°{'C' if UNITS == 'metric' else 'F'}"
        )


def get_weather_info():
    global UNITS, current_temperature
    city_name = city_name_entry.get()
    send_url = f"{BASE_URL}appid={API_KEY}&q={city_name}&units={UNITS}&lang={LANG}"

    response = requests.get(send_url)
    info = response.json()

    if "weather" in info and "main" in info:
        current_temperature = info["main"]["temp"]
        weather_description = info["weather"][0]["description"]
        icon_code = info["weather"][0]["icon"]
        icon_url = f"{ICON_BASE_URL}{icon_code}@2x.png"
        icon_response = requests.get(icon_url)  # 取得圖片
        if icon_response.status_code == 200:
            with open(f"{icon_code}.png", "wb") as icon_file:
                icon_file.write(icon_response.content)  # 將圖片寫入檔案
        image = Image.open(f"{icon_code}.png")  # 開啟圖片檔案
        tk_image = ImageTk.PhotoImage(image)  # 將圖片轉換成PhotoImage
        icon_labal.config(image=tk_image)  # 將圖片設為圖示
        icon_labal.image = tk_image

        temperature_labal.config(
            text=f"溫度: {current_temperature}°{'C' if UNITS == 'metric' else 'F'}"
        )
        description_labal.config(text=f"描述: {weather_description}")
    else:
        description_labal.config(text="查詢失敗")

    city_name = "Taipei"

    # 建立圖片
    send_url = f"{FORECAST_URL}appid={API_KEY}&q={city_name}&units={UNITS}&lang={LANG}"

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


#######################設定工作目錄########################
os.chdir(sys.path[0])  # 設定工作目錄
#######################建立視窗########################
Window = tk.Tk()
Window.title("Wheather")

#######################設定字型########################
font_size = 20
Window.option_add("*Font", ("Helevetica", font_size))
#######################設定主題########################
Style = Style(theme="darkly")
Style.configure("my.TButton", font=("Helevetica", font_size))
Style.configure("my.TCheckbutton", font=("Helevetica", font_size))

#######################建立變數########################
check_type = BooleanVar()
check_type.set(True)
#######################建立標籤########################
# Entry物件
city_name_labal = Label(Window, text="請輸入要查詢的城市名稱")
city_name_labal.grid(row=0, column=0, padx=10, pady=10)

icon_labal = Label(Window, text="天氣圖示")
icon_labal.grid(row=1, column=0, padx=10, pady=10)

temperature_labal = Label(Window, text="溫度: ???°C")
temperature_labal.grid(row=1, column=1, padx=10, pady=10)

description_labal = Label(Window, text="描述: ???")
description_labal.grid(row=1, column=2, padx=10, pady=10)

#######################建立Entry物件########################
city_name_entry = Entry(Window, width=20)
city_name_entry.grid(row=0, column=1)
#######################建立checkbutton########################
check = Checkbutton(
    Window,
    variable=check_type,
    onvalue=True,
    offvalue=False,
    command=on_switch_change,
    style="my.TCheckbutton",
    text="溫度單位(°C/°F)",
)
check.grid(row=2, column=1, padx=10, pady=10)


#######################建立按鈕########################
search_button = Button(
    Window, text="獲得天氣資訊", command=get_weather_info, style="my.TButton"
)

search_button.grid(row=0, column=2)
#######################創建畫布########################
canvas = Canvas(Window, width=0, height=0, bg="white")
canvas.grid(row=3, column=0, columnspan=3, padx=10, pady=10)
#######################運行應用程式########################
Window.mainloop()
