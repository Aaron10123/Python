'''
當使用者輸入數值時，程式不僅提示再大再小還需要提示縮小過後的輸入範圍
EX:
請輸入0~100的整數:50
再小一點
請輸入0~50的整數:25
再小一點
請輸入0~25的整數:15
再大一點
請輸入15~25的整數:30
再小一點
請輸入15~25的整數:10
再大一點
請輸入15~25的整數:20
再大一點
請輸入20~25的整數:23
再大一點
請輸入23~25的整數:24
恭喜猜中!
'''

import random

x = random.randint(1, 100)
min = 0
max = 100
while True:
    y = int(input(f'請輸入一個數字{min}~{max}:'))
    if y < x:
        print('在大一點')
        if min < y:
            min = y
    elif y > x:
        print('在小一點')
        if max > y:
            max = y
    elif y == x:
        print('猜對了!!!')
        break
