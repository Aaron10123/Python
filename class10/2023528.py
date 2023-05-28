# def add_score():
#     global score_dict
#     sj = input("請輸入想新增的科目:")
#     if sj in score_dict:
#         print('此科目已經新增過囉!')
#     else:
#         while True:
#             try:
#                 score_dict[sj] = int(input("請輸入分數:"))
#             except:
#                 print("輸入錯誤，請重新輸入")
#             else:
#                 break

# def edit_score():
#     global score_dict
#     sj = input("請輸入想修改的科目:")
#     if sj in score_dict:
#         while True:
#             try:
#                 score_dict[sj] = int(input("請輸入分數:"))
#             except:
#                 print("輸入錯誤，請重新輸入")
#             else:
#                 break
#     else:
#         print('此科目尚未新增!')

# def del_score():
#     global score_dict
#     sj = input('請輸入想刪除的科目:')
#     if sj in score_dict:
#         score_dict.pop(sj)
#         print('刪除成功!')
#     else:
#         print('此科目尚未新增!')

# def submit_score():
#     global score_dict
#     if len(score_dict) == 0:
#         print('目前沒有登記成績喔!')
#     else:
#         for k, v in score_dict.items():
#             print(f'{k}:{v}')
#         print(f'總平均為:{sum(score_dict.values())/len(score_dict)}')

# score_dict = {}
# func_dict = {
#     '1': add_score,
#     '2': del_score,
#     '3': submit_score,
#     '5': edit_score
# }
# while True:
#     for k, v in score_dict.items():
#         print(f'{k}:{v}')
#     print("1. 新增科目成績")
#     print("2. 刪除科目成績")
#     print("3. 提交所有成績並顯示平均")
#     print('5. 修改科目成績')
#     ans = input("請輸入功能編號:")
#     print("==========================")
#     if ans in func_dict:
#         func_dict[ans]()
#     else:
#         print('查無此功能請重新輸入!')

#     if ans == '3':
#         break
#     print("==========================")
import turtle
import random

# a = int(input("請輸入座標x:"))
# c = int(input("請輸入座標y:"))


def tree(x: int, y: int):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color("green")
    turtle.begin_fill()
    turtle.circle(20)
    turtle.end_fill()
    turtle.goto(x - 5, y)
    turtle.color("brown")
    turtle.begin_fill()
    turtle.right(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(10)
    turtle.end_fill()
    turtle.penup()


turtle.speed(0)
for i in range(100):
    tree(random.randint(1, 250), random.randint(1, 250))
turtle.done()
