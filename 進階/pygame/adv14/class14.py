
######################載入套件######################
import pygame
import sys
import os
from pygame.locals import *
######################定義函式區######################
def bg_update():
    """更新背景"""
    global roll_y

    roll_y = (roll_y - 10) % bg_y
    screen.blit(img, (0, roll_y - bg_y))  #(x , y)
    screen.blit(img, (0, roll_y))
######################初始化設定######################
os.chdir(sys.path[0])
pygame.init()
LIMIT_LOW = 140
PTERA_LIMIT_LOW = 110
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
clock = pygame.time.Clock()
######################載入圖片######################
img = pygame.image.load("space.png")


######################遊戲視窗設定######################
bg_x = img.get_width()
bg_y = img.get_height()
bg_size = (bg_x, bg_y)
pygame.display.set_caption("Galaxy Lancer")
screen = pygame.display.set_mode([bg_x, bg_y])
roll_y = 0
######################玩家設定######################

######################主程式######################

while True:
    clock.tick(20)  # 設定每秒20幀執行
    mouse_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    bg_update()

    pygame.display.update()
