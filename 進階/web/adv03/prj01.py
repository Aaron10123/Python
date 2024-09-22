from ttkbootstrap import *
import sys
import os


#######################定義函數########################
def show_result():
    entry_text = entry.get()
    try:
        result = eval(entry_text)
    except:
        result = "計算錯誤"
    label.config(text=result)


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
# Entry物件
label = Label(Window, text="計算結果")
label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

#######################建立Entry物件########################
entry = Entry(Window, width=20)
entry.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
#######################建立按鈕########################
button = Button(Window, text="計算", command=show_result, style="my.TButton")
button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
#######################運行應用程式########################
Window.mainloop()
