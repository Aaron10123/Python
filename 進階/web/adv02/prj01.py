#######################匯入模組#######################
# 匯入 tkinter 模組
from tkinter import *
import sys
import os
from PIL import Image, ImageTk

#######################設定工作目錄#######################
# 設定工作目錄
os.chdir(sys.path[0])


#######################定義函數########################
# 定義一個函數，用來處理按鈕按下事件
def move_circle(event):
    # 取得按下的按鈕
    key = event.keysym
    print(key)
    if key == "Up":
        canvas.move(circle, 0, -10)
    elif key == "Down":
        canvas.move(circle, 0, 10)
    elif key == "Left":
        canvas.move(circle, -10, 0)
    elif key == "Right":
        canvas.move(circle, 10, 0)

    if key == "w":
        canvas.move(rect, 0, -10)
    elif key == "s":
        canvas.move(rect, 0, 10)
    elif key == "a":
        canvas.move(rect, -10, 0)
    elif key == "d":
        canvas.move(rect, 10, 0)


# 定義一個函數，用來關閉視窗
def exit_fun():
    windows.destroy()


# # def hi_fun():
# #     if display["bg"] == "red":
# #         display.config(text="green", fg="black", bg="green")
# #     else:
# #         display.config(text="red ", fg="black", bg="red")


# def hi_fun():
#     global change
#     if change == False:
#         display.config(text="green", fg="black", bg="green")
#     else:
#         display.config(text="red ", fg="black", bg="red")
#     change = not change


# change = False


# def clear_fun():
#     # 清除標籤
#     display.config(text="", fg="white", bg="#FFFFFF")
#     # # 清除按鈕
#     # btn1.config(text="")


#######################建立視窗########################
# 建立視窗
windows = Tk()
# 設定視窗名稱
windows.title("My First GUI")

# 設定視窗大小
# windows.geometry("500x500")
# # 設定視窗內容
# windows.configure(bg="white")
#######################建立畫布########################
# 建立畫布
canvas = Canvas(windows, width=500, height=500, bg="white")
# 設定畫布位置
# canvas.place(x=100, y=100)
# 設定畫布大小
# canvas.config(width=100, height=50)
#  將畫布加入視窗
canvas.pack()
#######################設定視窗圖片########################
# 設定視窗圖片
windows.iconbitmap("crocodile2.ico")
#######################載入圖片########################
# 載入圖片
# img = PhotoImage(file="crocodile2.gif")  # 只能載入gif,png格式的圖片
image = Image.open("crocodile2.gif")  # 載入圖片轉成 image 物件
# 使用 ImageTk 的 PhotoImage 建立圖片物件
img = ImageTk.PhotoImage(image)

#######################顯示圖片########################
# # 顯示圖片
my_img = canvas.create_image(300, 300, image=img)
#######################畫圖形########################
circle = canvas.create_oval(250, 150, 300, 200, fill="red")

rect = canvas.create_rectangle(220, 400, 340, 430, fill="blue")

msg = canvas.create_text(300, 100, text="Hello World", fill="black", font=("Arial", 20))

#######################綁定案件事件#########################
# 將案件綁定到畫布上，當按下指定按鈕時，執行指定的函數
canvas.bind_all("<Key>", move_circle)
#######################建立文字########################
# # 建立文字
# text = Text(windows, width=50, height=10)
# # 設定文字位置
# text.place(x=100, y=100)
# # 設定文字大小
# text.config(width=100, height=50)
# # 設定文字內容
# text.insert(0.0, "Hello World")
# # 將文字加入視窗
# text.pack()
#######################建立按鈕########################
# # 建立按鈕
# btn1 = Button(windows, text="Click Me", command=hi_fun)

# 建立一個按鈕，用來關閉視窗
quit_btn = Button(windows, text="Quit", command=windows.quit)
quit_btn.pack()


# # # 設定按鈕位置
# # btn1.place(x=100, y=100)
# # # 設定按鈕大小
# # btn1.config(width=100, height=50)
# #  將按鈕加入視窗
# btn1.pack()
#######################建立標籤########################
# # 建立標籤
# display = Label(windows, text="Hello World")  # 可打色號, fg="red", bg="#000000"
# #  將標籤加入視窗
# display.pack()
#######################運行應用程式#######################
windows.mainloop()
