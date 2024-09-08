#######################匯入模組#######################
# 匯入 tkinter 模組
from tkinter import *


#######################定義函數########################
# def hi_fun():
#     if display["bg"] == "red":
#         display.config(text="green", fg="black", bg="green")
#     else:
#         display.config(text="red ", fg="black", bg="red")


def hi_fun():
    global change
    if change == False:
        display.config(text="green", fg="black", bg="green")
    else:
        display.config(text="red ", fg="black", bg="red")
    change = not change


change = False


def clear_fun():
    # 清除標籤
    display.config(text="", fg="white", bg="#FFFFFF")
    # # 清除按鈕
    # btn1.config(text="")


#######################建立視窗########################
# 建立視窗
windows = Tk()
# 設定視窗名稱
windows.title("My First GUI")

# 設定視窗大小
# windows.geometry("500x500")
# # 設定視窗內容
# windows.configure(bg="white")
#######################建立按鈕########################
# 建立按鈕
btn1 = Button(windows, text="Click Me", command=hi_fun)


# # 設定按鈕位置
# btn1.place(x=100, y=100)
# # 設定按鈕大小
# btn1.config(width=100, height=50)
#  將按鈕加入視窗
btn1.pack()
#######################建立標籤########################
# 建立標籤
display = Label(windows, text="Hello World")  # 可打色號, fg="red", bg="#000000"
#  將標籤加入視窗
display.pack()
#######################運行應用程式#######################
windows.mainloop()
