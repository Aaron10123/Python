#######################匯入模組#######################
# 匯入 tkinter 模組
from tkinter import *
import random


#######################定義函數########################
def hi_fun():
    # 顯示訊息
    print("Hello World")
    # # 將訊息輸出到視窗
    # windows.messagebox.showinfo("Hello", "Hello World")
    # display.config(text="Hello World", fg="red", bg="#000000")
    # 隨機變色
    # display.config(text="Hello World", fg=random.choice(color))
    COLORS = "#" + "".join([random.choice("0123456789ABCDEF") for i in range(6)])
    display.config(text="Hello World", fg=COLORS)


color = ["red", "green", "blue"]


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

# 設定文字大小
windows.option_add("*Font", "Helvetica 28")
# 設定視窗大小
# windows.geometry("500x500")
# # 設定視窗內容
# windows.configure(bg="white")
#######################建立按鈕########################
# 建立按鈕
btn1 = Button(windows, text="Click Me", command=hi_fun)
btn2 = Button(windows, text="Clean Screen", command=clear_fun)

# # 設定按鈕位置
# btn1.place(x=100, y=100)
# # 設定按鈕大小
# btn1.config(width=50, height=20)
#  將按鈕加入視窗
btn1.pack()
btn2.pack()
#######################建立標籤########################
# 建立標籤
display = Label(windows, text="Hello World")  # 可打色號, fg="red", bg="#000000"
# # 設定標籤位置
# display.place(x=100, y=200)
# # 設定標籤大小
# display.config(width=100, height=50)
#  將標籤加入視窗
display.pack()
#######################運行應用程式#######################
windows.mainloop()
