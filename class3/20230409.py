# try:
#     num = int(input('請輸入一個數字'))
#     total = num + 1
#     print(total)
# except ValueError:
#     print('請輸入數字')
# except:
#     print("發生錯誤")
# else:
#     print('成功執行')
# finally:
#     print("程式結束")
# except:             可以有多個, 第二個開始,可要可不要
#     print("發生錯誤")
# else:               只能有一個,可要可不要
#     print('成功執行')
# finally:            只能有一個,可要可不要
#     print("程式結束")
#比較運算子 運算  範例 結果(布林)
#  ==      相等    1==1 True
#  !=      不相等  1!=0 True
#  >=      大於等於1>=2 False
#  <=      小於等於1<=2 True
#  >         大於  1>2  False
#  <         小於  1<2  True
# password = input('輸入密碼')
# if password == "1234":
#     print("歡迎光臨")
# elif password == "vip1":
#     print('大佬請進')
# elif password == "5487":
#     print("87請進")
# elif password =="7777":
#     print("主人好")
# else:
#     print("笑死,進不去吧!")
a = int(input("請輸入成績"))
if a >= 90:
    print("你是等第A")
elif a >= 80 and a <= 89.9:
    print("你是等第B")
elif a >= 70 and a <= 79.9:
    print("你是等第C")
elif a >= 60 and a <= 69.9:
    print("你是等第D")
else:
    print("你是等第E")