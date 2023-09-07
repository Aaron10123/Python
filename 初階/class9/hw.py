def add_score():
    global book
    k = input("請輸入科目名稱:")
    while True:
        try:
            v = int(input('請輸入分數:'))
        except:
            print("發生錯誤")
        else:
            book[k] = v
            break


def remove_score():
    global book
    remove = input("請輸入要刪除的科目:")
    if remove in book:
        book.pop(remove, '')
    else:
        print('此科目尚未新增!')


def summit_score():
    print(f'您的平均為:{sum(book.values())/len(book)}')


option = ['1.新增科目成績', '2.移除科目成績', '3.提交所有成績並顯示平均']
command = [add_score, remove_score, summit_score]
book = {}

while True:
    for key, value in book.items():
        print(f'{key}:{value}')
    for o in option:
        print(o)
    ans = int(input("請輸入功能:"))
    if ans > len(command):
        print('錯誤')
    else:
        command[ans - 1]
        if ans == len(command):
            break

    # if ans == "1":
    #     add_score()

    # elif ans == "2":
    #     remove_score()

    # elif ans == "3":
    #     summit_score()
    #     break

    # else:
    #     print('錯誤')
