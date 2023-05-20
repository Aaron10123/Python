option = ['1.新增科目成績', '2.移除科目成績', '3.提交所有成績並顯示平均']
book = {}

while True:
    for key, value in book.items():
        print(f'{key}:{value}')
    for o in option:
        print(o)
    ans = input("請輸入功能:")
    if ans == "1":
        k = input("請輸入科目名稱:")
        while True:
            try:
                v = int(input('請輸入分數:'))
            # except ValueError:
            #     print('錯誤')
            except:
                print("發生錯誤")
            else:
                book[k] = v
                break

    elif ans == "2":
        remove = input("請輸入要刪除的科目:")
        if remove in book:
            book.pop(remove, '')
        else:
            print('此科目尚未新增!')

    elif ans == "3":
        print(f'您的平均為:{sum(book.values())/len(book)}')
        break

    else:
        print('錯誤')
