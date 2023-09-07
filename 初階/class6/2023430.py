# for i in range(2, 6):
#     print(i)
# else:
#     print("迴圈正常結束")

# i = 2
# while i <6:
#     print(i)
#     i += 1
# else:
#     print("迴圈正常結束")

# i = 1
# while i < 6:
#     if i == 3:
#         break
#     print(i)
#     i += 1

# for i in range(1,6):
#     if i == 3:
#         break
#     print(i)

# break #只能停止一層迴圈

# i = 1
# while i < 6:
#     if i == 3:
#         i += 1
#         continue
#     print(i)
#     i += 1

# while True:
#     x = int(input("請輸入果汁編號:"))
#     if x == 1:
#         print('蘋果汁')
#     elif x == 2:
#         print('柳橙汁')
#     elif x == 3:
#         print('葡萄汁')
#     elif x == 4:
#         print('系統關閉')
#         break

# import random

# a = random.randrange(3)
# random.randrange(0, 10, 2)
# print(a)

# import random
# random.randint(1,3)
# random.randint(1,10)

import random

x = random.randint(1, 100)
while True:
    y = int(input('請輸入一個數字'))
    if y < x:
        print('在大一點')
    elif y > x:
        print('在小一點')
    elif y == x:
        print('猜對了!!!')
        break
