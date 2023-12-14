numbers = [1, 2, 3]
print(numbers)  # 輸出: [1, 2, 3]
print(*numbers)  # 輸出: 1 2 3


def add(a, b, c):
    return a + b + c


numbers = [1, 2, 3]
result = add(*numbers)
print(result)  # 輸出: 6


def get_coordinates():
    return 10, 20  # 返回一個元組 (10, 20)


print(get_coordinates())  # 輸出: (10, 20)

# 一般情況下，我們會使用兩個變數來接收函式返回
x, y = get_coordinates()
print(x)  # 輸出: 10
print(y)  # 輸出: 20

print(*get_coordinates())
