#########################匯入模組#########################
import mcu

#########################函式與類別定義#########################


#########################宣告與設定#########################
wi = mcu.wifi("SingularClass", "Singular#1234")
wi.setup(ap_active=False, sta_active=True)

wi.scan()
if wi.connect():
    print(f"IP={wi.ip}")
#########################主程式#########################
