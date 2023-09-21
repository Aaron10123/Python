######################匯入模組######################
import pygame
import sys
import os
import random


####################定義函式######################
def check_click(pos, x_min, y_min, x_max, y_max):
    """判斷滑鼠是否點擊在指定的區域內"""
    x_match = x_min < pos[0] < x_max
    y_match = y_min < pos[1] < y_max
    if x_match and y_match:
        return True
    else:
        return False


def snow_fall():
    """下雪"""

    for snow in snow_list:
        # 畫出雪花
        pygame.draw.circle(screen, WHITE, (snow["x_site"], snow["y_site"]),
                           snow["radius"])

        # 計算雪花下次顯示的座標
        snow["x_site"] += snow["x_shift"]
        snow["y_site"] += snow["radius"]

        # 如果雪花落出畫面，重設位置
        if snow["y_site"] > bg_y or snow["x_site"] > bg_x:
            snow["y_site"] = random.randint(-bg_y, -1)
            snow["x_site"] = random.randint(0, bg_x)


####################初始化######################
os.chdir(sys.path[0])  # 設定程式執行路徑
pygame.init()
bg_img = "snow.jpg"
bg = pygame.image.load(bg_img)

bg_x = bg.get_width()  # 640
bg_y = bg.get_height()  # 400
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

######################建立視窗######################
screen = pygame.display.set_mode((bg_x, bg_y))
pygame.display.set_caption("Snow")

####################撥放音樂######################
mp3_path = "snow-dream.mp3"
pygame.mixer.music.load(mp3_path)  # 音樂載入程式
pygame.mixer.music.play()  # 播放音樂
pygame.mixer.music.fadeout(600000)  # 設定音樂撥放時間單位毫秒
pygame.mixer.music.pause()

####################設定文字######################
typeface = pygame.font.get_default_font()
font = pygame.font.Font(typeface, 24)
title = font.render("Stop", True, BLACK)
tit_w = title.get_width()
tit_h = title.get_height()

####################設定雪花基本參數######################
snow_list = []

for i in range(150):
    x_site = random.randrange(0, bg_x)
    y_site = random.randrange(-bg_y, -1)
    x_shift = random.randint(-1, -1)
    radius = random.randint(4, 6)

    snow_list.append({
        "x_site": x_site,
        "y_site": y_site,
        "x_shift": x_shift,
        "radius": radius,
    })
####################新增fps######################
clock = pygame.time.Clock()

######################循環偵測######################
paint = False  # 是否要下雪
cnt = 0

while True:
    clock.tick(20)  # 設定每秒20幀執行

    # 取得滑鼠位置
    mouse_pos = pygame.mouse.get_pos()

    # 取得事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if check_click(mouse_pos, 0, 0, tit_w, tit_h):
                paint = not paint

    if cnt > 10:
        cnt = 0
        for snow in snow_list:
            snow["x_shift"] = random.randint(-3, 3)
    else:
        cnt += 1

    screen.blit(bg, (0, 0))
    screen.blit(title, (0, 0))
    if paint:
        title = font.render("Start", True, BLACK)
        pygame.mixer.music.unpause()
        snow_fall()
    else:
        title = font.render("Stop", True, BLACK)
        pygame.mixer.music.pause()

    # 更新繪圖視窗
    pygame.display.update()