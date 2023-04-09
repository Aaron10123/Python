"""
請使用者輸入華氏溫度
如果使用者輸入的不是數字，則會顯示"輸入錯誤!"
如果輸入數字則會將華氏轉換為攝氏溫度並顯示出來(轉換公式可以上網搜尋喔!)

EX:
請輸入華氏溫度:60
華氏溫度60.0F等於攝氏溫度15.555555555555555C

請輸入華氏溫度:ABC
輸入錯誤!
"""

try:
    a = int(input("請輸入華氏溫度:"))
    b = (a - 32) * 5 / 9
    print(f"華氏溫度{a}等於攝氏溫度{b}")
except:
    print("輸入錯誤!")
'''
測量你的BMI值, 確認你的體重是否正常?
* BMI公式:體重(公斤) / 身高(公尺)的平方
* BMI值正常範圍:14.8到20.7之間
* BMI值過重範圍:20.7以上

EX:
請輸入身高(公尺):1.7
請輸入體重(公斤):45
你的BMI為15.570934256055365
體重過輕

請輸入身高(公尺):1.7
請輸入體重(公斤):60
你的BMI為20.761245674740486
體重正常

請輸入身高(公尺):1.7
請輸入體重(公斤):90
你的BMI為31.14186851211073
體重過重
'''
h = float(input("請輸入身高(公尺):"))
w = float(input("請輸入體重(公斤):"))
bmi = w / h**2
print("你的BMI是" + str(bmi))
if bmi >= 21.5:
    print("體重過重")
elif bmi < 21.5 and bmi > 16.4:
    print("體重正常")
elif bmi <= 21.5:
    print("體重過輕")