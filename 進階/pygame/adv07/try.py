######################匯入模組######################
import pygame
import sys
import os

####################定義函式######################

####################初始化######################
os.chdir(sys.path[0])
pygame.init()
LIMIT_LOW = 140
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
clock = pygame.time.Clock()

####################載入圖片物件######################
img = "bg.png"
bg = pygame.image.load(img)
bg_x = bg.get_width()
bg_y = bg.get_height()
bg_roll_x = 0
######################建立視窗######################
screen = pygame.display.set_mode([bg_x, bg_y])
pygame.display.set_caption("小恐龍")
######################分數物件######################

######################恐龍物件######################

######################仙人掌物件######################

######################循環偵測######################

cnt = 0

while True:
    clock.tick(10)  # 設定每秒20幀執行
    mouse_pos = pygame.mouse.get_pos()

    # 取得事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # 更新繪圖視窗
    pygame.display.update()
