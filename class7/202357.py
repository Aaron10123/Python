# 用中括號表示,逗號分隔
# 串列[起始值:終止值]
# 串列[起始值:終止值:]
# i= ['a','b','c']
# for index in range(len(i)):
#     print(i[index])
# print(range(3))
# print(list(range(3)))
# l = ['a', 'b', 'c']
# a = l.copy()
# a[0] = 1
# print(a, l)

# list = ['蘋果汁', '柳橙汁', '葡萄汁','可樂', '系統關閉']
# while True:
#     x = int(input("請輸入果汁編號:"))
#     if x >= len(list):
#         break
#     else:
#         print(list[x - 1])

# juices = ["蘋果汁", "柳橙汁", "葡萄汁", "系統關閉"]

# while True:
#     for j in range(len(juices)):
#         print(f"{j+1}. {juices[j]}")

#     try:
#         ans = int(input("請輸入編號:"))
#     except:
#         print("請輸入數字編號")
#     else:
#         if ans == len(juices):
#             print("~~系統關閉~~")
#             break
#         elif ans > len(juices):
#             print("輸入錯誤查無此果汁，請重新輸入編號")
#         else:
#             print(f"您點的商品是{juices[ans-1]}")

# l = []
# while True:
#     x = input('請輸入資料')
#     l.append(x)
#     print(l)
#     if x == 'e':
#         break

# while True:
#     x = input('請輸入要刪除的資料')
#     while x in l:
#         l.remove(x)
#         print(l)
#     if x == 'e':
#         break
# while True:
#     x = input('請輸入要查詢資料數量')
#     print(l.count(x))
#     if x == 'e':
#         break