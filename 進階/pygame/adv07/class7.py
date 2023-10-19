######################匯入模組######################
import pygame
import sys
import os


####################定義函式######################
def bg_update():
    """更新背景"""
    global bg_roll_x

    bg_roll_x = (bg_roll_x - 10) % bg_x
    screen.blit(img, (bg_roll_x - bg_x, 0))
    screen.blit(img, (bg_roll_x, 0))


def move_dinosaur():
    """移動恐龍"""
    global ds_y, ds_index
    ds_index = (ds_index - 1) % len(img_dinosaur)
    screen.blit(img_dinosaur[ds_index], (ds_x, ds_y))


####################初始化######################
os.chdir(sys.path[0])
pygame.init()
LIMIT_LOW = 140
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
clock = pygame.time.Clock()

####################載入圖片物件######################
img = pygame.image.load("bg.png")
dinosaur1 = pygame.image.load("小恐龍1.png")
dinosaur2 = pygame.image.load("小恐龍2.png")
img_dinosaur = [dinosaur1, dinosaur2]
bg_x = img.get_width()
bg_y = img.get_height()
bg_roll_x = 0
######################建立視窗######################
screen = pygame.display.set_mode([bg_x, bg_y])
pygame.display.set_caption("小恐龍")
######################分數物件######################

######################恐龍物件######################
ds_x = 50
ds_y = LIMIT_LOW
ds_index = 0
jumpState = False
jumpValue = 0
jump_height = 13
######################仙人掌物件######################

######################循環偵測######################

cnt = 0

while True:
    clock.tick(20)  # 設定每秒20幀執行
    mouse_pos = pygame.mouse.get_pos()

    # 取得事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    bg_update()
    move_dinosaur()

    # 更新繪圖視窗
    pygame.display.update()
