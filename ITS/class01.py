# 1E=float
l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(4 in l)  # True
# eval 是函数，可以在字串中進行計算或判斷型態是int or float

# 0 or 5 = 5 #從做到右，第一個非零的數字或空字串就是結果


# is 是從嚴比較，== 是弱比較
# 括弧->指數->正數、負數與反位元->乘法和除法->加法和減法->且
# def
# 新增一個函數要用 def 開頭，後面接著函數名稱，再加上小括號，最後加上冒號。
# 小括號裡面可以放入傳入函數的參數也可以不放。
def hello():
    print("Hello, World!")


for i in range(10):
    hello()


# 有傳入參數的函數
# 這個函數有一個參數 name，當呼叫這個函數時，可以傳入一筆資料給 name。
def hello(name):
    print(f"Hello, {name}!")


hello("Alice")
hello("Bob")
hello("Charlie")
for i in range(10):
    hello(i)  # 這裡的 i 會被當作 name 的值


# 有回傳值的函數
# 這個函數會回傳一個值，當呼叫這個函數時，可以把回傳的值存起來。
# 在指令當中只要執行return，就會回傳值，並結束函數。
def add(a, b):  # 可以允許多個傳入參數
    return a + b


print(add(1, 2))
print(add("Hello, ", "World!"))
sum = add(3, 4)  # 可以將回傳值存到變數中
print(sum)


# 有多個回傳值的函數
# 這個函數會回傳兩個值，當呼叫這個函數時，可以把回傳的值存起來。
def add_sub(a, b):
    return a + b, a - b


sum, sub = add_sub(5, 6)  # 可以將回傳值存到多個變數中
print(f"sum = {sum}, sub = {sub}")


# 多個return
def add_sub(a, b):
    if a > b:
        return a + b
    else:
        return a - b


print(add_sub(5, 6))
print(add_sub(6, 5))


# 預設參數
# 可以在函數的參數中設定預設值，當呼叫這個函數時，如果沒有傳入參數，就會使用預設值。
# 多個參數時，有預設值的參數要放在沒有預設值的參數後面。
def hello(name, message="Hello"):
    print(f"{message}, {name}!")


hello("Alice")
hello("Bob", "Good Morning")


# 限制傳入參數型態
# 可以在函數的參數中設定型態，當呼叫這個函數時，可以提示使用者要傳入的參數型態。
# 變數: 型態=預設值
# -> 型態，代表回傳值的型態
def add(a: int, b: int = 0) -> int:
    return a + b


print(add(1, 2))
print(add("Hello, ", "World!"))


try:  # try必須要有最少一個except, 也可以有多個
    pass
except ValueError:  # except至少要有一個, 也可以有多個
    pass
except Exception as e:  # except至少要有一個, 也可以有多個
    pass
else:  # 可有可無, 但如果有的話, 必須要有except, else只能有一個
    pass
finally:  # 可有可無, 但如果有的話, 必須要有except, finally只能有一個
    pass


def hello(name, age=10, grade=5):
    print("Hello", name, "you are", age, "years old and in grade", grade)


hello("Alice")
hello("Bob", 12)
hello("Charlie", 11, 6)


import random

print(random.randint(1, 10))  # 一定要設定開始與結束, 範圍會包含結束的數字
print(random.randrange(10))  # 0~9
print(random.randrange(10, 20))  # 10~19
print(random.randrange(10, 20, 2))  # 10~19, 間隔2
a = "abcdefghij"
print(a[1:3])  # bc
print(a[1:3:2])  # b
print(a[::2])  # acegi


from random import randint  # 只引入randint, 不用再打random.

try:  # try必須要有最少一個except, 也可以有多個
    a = int(input("Enter a number: "))
    b = randint(1, 10)
    print("You entered", a)
    print("Random number is", b)
    print("Sum is", a + b)
except ValueError:  # except至少要有一個, 也可以有多個
    print("Please enter a number")
except Exception as e:
    print("Error:", e)
else:  # 可有可無, 但如果有的話, 必須要有except, else只能有一個
    print("No error")
finally:  # 可有可無, 但如果有的話, 必須要有except, finally只能有一個
    print("End of program")

# 檔案讀寫模式
# r: 讀取, 檔案必須存在, 檔案不存在則發生錯誤
# r+: 讀取與寫入, 檔案必須存在, 檔案不存在則發生錯誤
# w: 寫入, 檔案不存在則建立, 檔案存在則清空
# w+: 讀取與寫入, 檔案不存在則建立, 檔案存在則清空
# a: 寫入, 檔案不存在則建立, 檔案存在則接續寫入
# a+: 讀取與寫入, 檔案不存在則建立, 檔案存在則接續寫入


# math module
# math.fabs(x): 取絕對值, 把有正負號的數字轉成正數
# math.ceil(x): 無條件進位到最接近的整數
# math.floor(x): 無條件捨去到最接近的整數
# math.fmod(x, y): 小數取餘數, 會回傳浮點數
# math.frexp(x): 回傳一個tuple, 第一個是小數, 第二個是次方，例如: math.frexp(10) 回傳 (0.625, -1)
# tuple長這樣: (0.625, -1), 資料看起來像list, 但是tuple是不可變的


# assertis(x, y): x is y, 如果x和y是同一個物件, 則回傳True, 否則回傳False
# assertin(x, y): x in y, 如果x是y的元素, 則回傳True, 否則回傳False
# assertequal(x, y): x == y, 如果x等於y, 則回傳True, 否則回傳False
# assertisinstance(x, y): isinstance(x, y), 如果x是y的實例, 則回傳True, 否則回傳False

# 指令傳入值有無預設值的規則
# 1. 有預設值的變數必須放在沒有預設值的變數後面
# 2. 有預設值的變數可以不用傳入值, 會使用預設值
# 3. 有預設值的變數可以傳入值, 會使用傳入值
# 4. 沒有預設值的指令必須傳入值

# 字串格式化%的使用方法
# %s: 字串
print("I'm %s." % ("Ray"))
# %d: 十進位整數
# %02d: 保留兩位數，不足補0
print("I'm %s. I'm %d year old" % ("Ray", 18))
print("I'm %s. I'm %02d year old" % ("Ray", 8))
# %f: 浮點數
# %.2f: 保留兩位小數
print("I'm %s. I'm %.2f year old" % ("Ray", 18.123456))

# format()的使用方法
print("I'm {}. I'm {} year old".format("Ray", 18))
print("I'm {}. I'm {} year old".format("Ray", 18.123456))
# 保留兩位小數
print("I'm {}. I'm {:.2f} year old".format("Ray", 18.123456))
# 保留兩位整數，不足補0
print("I'm {}. I'm {:02d} year old".format("Ray", 18))
print("I'm {}. I'm {:02d} year old".format("Ray", 8))
print("I'm {}. I'm {:02d} year old".format("Ray", 18.123456))

print("I'm {1:s}. I'm {0:d} year old".format(18, "Ray"))
print("I'm {name:s}. I'm {age:d} year old".format(age=18, name="Ray"))
print("I'm {name:s}. I'm {age:02d} year old".format(age=18, name="Ray"))
