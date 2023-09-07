'''
1.	請問Python有哪五種形態:
答案:int,str,float,bool,none
2.	請問使用什麼function可以顯示出形態
答案:type
3.	請問 a = int('1'), a的形態是什麼
答案:整數
4.	請問 b = str(1), b的形態是什麼
答案:字串
5.	請問 c = float(1), c的形態是什麼
答案:浮點數
6.	請問 d = bool(1), d的形態是什麼
答案:布林值
7.	請列出Python加、減、乘、除表示符號
答案:+,-,*,/
8. 請問今天學了哪一些function(函式)?
答案:# max() 
# len() 
# type() 
# int() 
# float() 
# bool() 
# str() 
# print()
# input()
9. 延續上題, 請嘗試描述每個function的功能各別是什麼?
答案:取最大值,取長度,取型態,取整數,取浮點數,取布林值,取字串,終端機顯示,終端機輸入

'''
"""
Topic:請使用input and print打造對話機器人
e.g.
old = input("How old are you?")
print("I am " + old)

1.Show:How old are you?
2.input:12
3.Output:I am 12
"""
a = input("請輸入你的年齡: ")
print("你的年齡是" + a)
"""
請使用者輸入身高(公尺)h以及體重(公斤)w
透過下面公式計算出BMI數值並顯示計算結果

bmi = w/h**2

EX:
請輸入身高:1.7
請輸入體重:50
你的BMI為17.301038062283737
"""
h = float(input("請輸入身高(公尺):"))
w = float(input("請輸入體重(公斤):"))
bmi = w / h**2
print("你的BMI是" + str(bmi))
