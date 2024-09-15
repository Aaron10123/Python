from ttkbootstrap import *
import sys
import os
from tkinter import filedialog
from PIL import Image, ImageTk

#######################定義函數########################


def open_file():
    global file_path
    file_path = filedialog.askopenfilename(initialdir=sys.path[0])
    labal2.config(text=file_path)


def show_image():
    global file_path
    image = Image.open(file_path)
    image = image.resize((canvas.winfo_width(), canvas.winfo_height()))
    photo = ImageTk.PhotoImage(image)
    canvas.create_image(0, 0, image=photo, anchor="nw")
    canvas.image = photo


#######################設定工作目錄########################
os.chdir(sys.path[0])  # 設定工作目錄
#######################建立視窗########################
Window = tk.Tk()
Window.title("My GUI")

#######################設定字型########################
font_size = 20
Window.option_add("*Font", ("Helevetica", font_size))
#######################設定主題########################
Style = Style(theme="darkly")
Style.configure("my.TButton", font=("Helevetica", font_size))

#######################建立標籤########################
label = Label(Window, text="選擇檔案")
label.grid(row=0, column=0, sticky="E")

labal2 = Label(Window, text="無")
labal2.grid(row=0, column=1, sticky="E")
#######################建立按鈕########################
button = Button(Window, text="瀏覽", command=open_file, style="my.TButton")
button.grid(row=0, column=2, sticky="W")
button2 = Button(Window, text="顯示", command=show_image, style="my.TButton")
button2.grid(row=1, column=0, columnspan=3, sticky="EW")

canvas = Canvas(Window, width=600, height=600)
canvas.grid(
    row=2,
    column=0,
    columnspan=3,
)
#######################運行應用程式########################
Window.mainloop()



