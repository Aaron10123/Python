#########################匯入模組#########################
import network

#########################函式與類別定義#########################


#########################宣告與設定#########################
wlan = network.WLAN(network.STA_IF)  # 設定成STA模式
ap = network.WLAN(network.AP_IF)  # 設定成AP模式
ap.active(False)  # 關閉AP模式
wlan.active(True)  # 開啟STA模式

# wifi_list = wlan.scan()
# print("Scan result:")
# for i in range(len(wifi_list)):
#     print(wifi_list[i])

wlSSID = "SingularClass"
wlPWD = "Singular#1234"
wlan.connect(wlSSID, wlPWD)
while not (wlan.isconnected()):
    pass
print("connet successfully", wlan.ifconfig())
#########################主程式#########################
