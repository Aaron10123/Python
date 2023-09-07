# def hello():
#     print("hello")
# def hello(name):
#     print(f"hello {name}")

# # hello("a")

# apple = 10

# def my_min(a: int, s: int):
#     """比較兩個數字哪一個比較小"""
#     global apple
#     print(apple)
#     apple = 100
#     if a < s:
#         return a
#     else:
#         return s

# print(my_min(1, 2))
# print(apple)

import random


def roll_dice(once: int):
    x = []
    for y in range(once):
        x.append(random.randint(1, 6))

    return x


o = int(input('請輸入擲骰子的次數:'))
print(roll_dice(o))
