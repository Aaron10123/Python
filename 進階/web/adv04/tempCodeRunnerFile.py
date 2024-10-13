
#######################建立按鈕########################
search_button = Button(
    Window, text="獲得天氣資訊", command=get_weather_info, style="my.TButton"
)

search_button.grid(row=0, column=2)
#######################運行應用程式########################
Window.mainloop()
