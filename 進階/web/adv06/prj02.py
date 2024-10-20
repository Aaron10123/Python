# 認識裝飾器
# 定義一個函式
def greet():
    print("Hello!")


# 定義一個函式,接收一個函式作為參數
def welcome(func):  # 將指令名稱當作參數傳入
    print("Welcome!")  # 執行 Welcome!
    func()  # 呼叫傳入的函式


# 執行welcome函式,傳入greet函式
welcome(greet)


def decorator(func):  # 定義裝飾器
    # 定義包裹函數
    def wrapper():  # 定義包裹函式
        print("Before")  # 在函數前執行 Before
        func()  # 執行原函數
        print("After")  # 在函數後執行 After

    return wrapper  # 回傳包裹函式


# 使用裝飾器裝飾函數
@decorator
def greet():
    print("Hello!")


# 執行裝飾器的函數
greet()


def decorator(func):  # 定義裝飾器
    # 定義包裹函數
    def wrapper(name):  # 定義包裹函式
        print("Before")  # 在函數前執行 Before
        func(name)  # 執行原函數
        print("After")  # 在函數後執行 After

    return wrapper  # 回傳包裹函式


# 使用裝飾器裝飾函數
@decorator
def greet(name):
    print(f"Hello, {name}!")  # 印出名字


# 執行裝飾器的函數
greet("Alice")


def decorator(func):  # 定義裝飾器
    # 定義包裹函數
    def wrapper(*args, **kwargs):  # 定義包裹函式
        print("Before")  # 在函數前執行 Before
        result = func(*args, **kwargs)  # 執行原函數
        print("After")  # 在函數後執行 After
        return result  # 回傳原函數的回傳值

    return wrapper  # 回傳包裹函式


# 使用裝飾器裝飾函數,greet會接收任意數量的參數
@decorator
def greet(name=None):
    if name:
        print(f"Hello, {name}!")  # 如果有名字則印出名字
    else:
        print("Hello!")  # 如果沒有名字則印出問候語


# 呼叫函數,沒有傳入參數
greet()

# 呼叫函數,傳入參數
greet("Alice")


def decorator_with_args(greeting):  # 定義裝飾器
    def decorator(func):  # 定義裝飾器
        # 定義包裹函數
        def wrapper(*args, **kwargs):  # 定義包裹函式
            print(f"{greeting}Before")  # 在函數前執行 Before
            result = func(*args, **kwargs)  # 執行原函數
            print(f"{greeting}After")  # 在函數後執行 After
            return result  # 回傳原函數的回傳值

        return wrapper  # 回傳包裹函式


# 使用裝飾器裝飾函數,greet會接收任意數量的參數
@decorator
def greet(name=None):
    if name:
        print(f"Hello, {name}!")  # 如果有名字則印出名字
    else:
        print("Hello!")  # 如果沒有名字則印出問候語


greet()

greet("Alice")


class Repeat:
    def times(self, n):
        def decorator(func):
            def wrapper(*args, **kwargs):
                for _ in range(n):
                    result = func(*args, **kwargs)
                return result

            return wrapper

        return decorator


# 需要先實例化Repeat類
repeat = Repeat()


@repeat.times(3)  # 重複3次
def say_hi(name):
    print(f"Hi, {name}!")


say_hi("Alice")
