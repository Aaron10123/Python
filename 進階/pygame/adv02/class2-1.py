import pygame
import sys  #關視窗的指令
import math


def check_click(pos, x_0, y_0, x_639, y_319):
    x_match = x_0 < pos[0] < x_639
    y_match = y_0 < pos[1] < y_319
    if x_match and y_match:
        return True
    else:
        return False


pygame.init()
screen = pygame.display.set_mode((640, 320))  #視窗的寬高
pygame.display.set_caption("My Frist Game")  #視窗名
background = pygame.Surface((640, 320))  #建立畫布
background.fill((255, 255, 255))  #畫布的顏色
####################設定文字######################
typeface = pygame.font.get_default_font()
font = pygame.font.Font(typeface, 24)
title = font.render("Start", True, (0, 0, 0))
tit_w = title.get_width()
tit_h = title.get_height()

# #畫多邊形
# pygame.draw.polygon(background, (100, 200, 45),
#                     [[100, 100], [0, 200], [200, 200]], 0)
# #畫圓弧
# pygame.draw.arc(background, (255, 10, 0), [100, 10, 100, 50],
#                 math.radians(180), math.radians(0), 2)

paint = False

while True:
    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():  #抓取視窗事件
        if event.type == pygame.QUIT:  #判斷視窗事件
            sys.exit()  #關閉所有程式   #使用者按關閉鍵
        if event.type == pygame.MOUSEBUTTONDOWN:
            if check_click(mouse_pos, 0, 0, tit_w, tit_h):
                paint = not paint
            #pygame.mouse.get_pos()
    if paint:
        pygame.draw.circle(background, (0, 0, 255), (400, 100), 30, 0)

        #畫圓形, (畫布, 顏色, 圓心, 半徑, 線寬)
        pygame.draw.circle(background, (0, 0, 255), (200, 100), 30, 0)
        #畫矩形, (畫布, 顏色,[[x, y, 寬, 高], 線寬)
        pygame.draw.rect(background, (0, 255, 0), [270, 130, 60, 40], 5)
        #畫橢圓, (畫布, 顏色,[[x, y, 寬, 高], 線寬)
        pygame.draw.ellipse(background, (255, 0, 0), [130, 160, 60, 35], 5)
        pygame.draw.ellipse(background, (255, 0, 0), [400, 160, 60, 35], 5)
        pygame.draw.line(background, (255, 0, 255), (280, 220), (320, 220), 3)
    else:
        background.fill((255, 255, 255))

    print(pygame.mouse.get_pos())  #取得滑鼠座標
    screen.blit(background, (0, 0))  #繪製畫布於視窗左上角
    screen.blit(title, (0, 0))
    pygame.display.update()  #更新視窗
