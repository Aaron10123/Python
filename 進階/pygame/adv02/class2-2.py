######################匯入模組######################
import pygame
import sys  #關視窗的指令
import math
import os
####################定義函式######################


def check_click(pos, x_0, y_0, x_639, y_319):
    x_match = x_0 < pos[0] < x_639
    y_match = y_0 < pos[1] < y_319
    if x_match and y_match:
        return True
    else:
        return False


####################初始化######################
os.chdir(sys.path[0])  #設定程式執行路線
pygame.init()
bg_img = "snow.jpg"
bg = pygame.image.load(bg_img)

bg_x = bg.get_width()  #640
bg_y = bg.get_height()  #400
screen = pygame.display.set_mode((bg_x, bg_y))
pygame.display.set_caption("My Frist Game")
######################建立視窗######################

####################撥放音樂######################
mp3_path = "snow-dream.mp3"
pygame.mixer.music.load(mp3_path)
pygame.mixer.music.play()
pygame.mixer.fadeout(600000)
####################設定文字######################
typeface = pygame.font.get_default_font()
font = pygame.font.Font(typeface, 24)
title = font.render("Start", True, (0, 0, 0))
tit_w = title.get_width()
tit_h = title.get_height()

####################設定雪花基本參數######################

####################新增fps######################
clock = pygame.time.Clock()

######################循環偵測######################
paint = False

while True:
    clock.tick(20)
    mouse_pos = pygame.mouse.get_pos()
    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():  #抓取視窗事件
        if event.type == pygame.QUIT:  #判斷視窗事件
            sys.exit()  #關閉所有程式   #使用者按關閉鍵
        if event.type == pygame.MOUSEBUTTONDOWN:
            if check_click(mouse_pos, 0, 0, tit_w, tit_h):
                paint = not paint
    if paint:
        title = font.render("Stop", True, (0, 0, 0))

    else:
        title = font.render("Start", True, (0, 0, 0))

    screen.blit(bg, (0, 0))  #繪製畫布於視窗左上角
    screen.blit(title, (0, 0))
    pygame.display.update()  #更新視窗
