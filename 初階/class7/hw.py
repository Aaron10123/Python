l = ['蘋果汁', '柳橙汁', '葡萄汁']
option = ['1.新增餐點', '2.移除餐點', '3.提交菜單']
user = []

while True:
    print(f"目前已點的餐:{user}")
    for o in option:
        print(o)
    ans = input("請輸入功能:")
    if ans == "1":
        for index in range(len(l)):
            print(f"{index+1}. {l[index]}")
        x = int(input('請輸入菜單編號:'))
        user.append(l[x - 1])

    elif ans == "2":
        x = input('請輸入要刪除的菜單名稱:')
        while x in user:
            user.remove(x)

    elif ans == "3":
        print('您點的餐點為')
        # print(f"{'蘋果汁'}:{user.count('蘋果汁')}")
        # print(f"{'柳橙汁'}:{user.count('柳橙汁')}")
        # print(f"{'葡萄汁'}:{user.count('葡萄汁')}")
        for i in l:
            if i in user:
                print(f"{i}:{user.count(i)}")
        break