"""
輸入一數字n為尋找的區間範圍, 找出區間範圍
3,7的倍數顯示在螢幕上, 其餘不顯示

hint:可以使用%取餘數進行判斷

EX
請輸入正整數:20
3
6
7
9
12
14
15
18
"""
x = int(input('請輸入一個數字'))
for i in range(3, x, 3):
    print(i)
for y in range(7, x, 7):
    print(y)
"""
請輸入要印出的箭頭大小

hint:
可利用字串乘法
val="*" * 3
print(val)
***

EX:
請輸入要印出的箭頭大小:3
  *  
 *** 
*****
  *  
  *  
  * 
"""
x = int(input('請輸入要印出的箭頭大小'))
y = -1
z = x
for i in range(x):
    z -= 1
    y += 2
    val = " " * z + "*" * y
    print(val)
x -= 1
for z in range(x + 1):
    a = " " * x + "*" * 1
    print(a)
