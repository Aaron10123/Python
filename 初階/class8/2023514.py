# book = {"書名": "a", "作者": "aa"}
# print(book["書名"])
# print(book["作者"])

# book = {}
# book["書名"] = "a"
# book["作者"] = "aa"
# print(book)

x = int(input("請輸入想興增的數量"))
book = {}  #儲存
for i in range(x):
    k = input("請輸入key名稱:")
    v = input('請輸入value:')
    book[k] = v
    print(book)

#刪除
remove = input("請輸入要刪除的key:")
book.pop(remove, '')
print(book)

for key, value in book.items():
    print(f"{key}:{value}")

search = input("請輸入要搜尋的key:")
if search in book:
    print(book[search])
else:
    print("找不到資料")

# d = {1: 'a', 2: 'b'}
# v = d.pop(1, 'c')
# print('更新後的字典：', d)
# print('移出的數值:', v)