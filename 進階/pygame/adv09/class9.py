######################匯入模組######################
import pygame
import sys
import os
from pygame.locals import *


####################定義函式######################
def bg_update():
    """更新背景"""
    global bg_roll_x

    bg_roll_x = (bg_roll_x - 10) % bg_x
    screen.blit(img, (bg_roll_x - bg_x, 0))
    screen.blit(img, (bg_roll_x, 0))


def move_dinosaur():
    """移動恐龍"""
    global ds_y, jumpState, jumpValue, ds_index, ds_center_y, ds_center_x

    if jumpState:
        if ds_y >= LIMIT_LOW:
            jumpValue = -jump_height
        if ds_y <= 0:
            jumpValue = jump_height
        ds_y += jumpValue

        if jumpValue < 0:
            jumpValue += 1
        else:
            jumpValue += 1

        if ds_y >= LIMIT_LOW:
            jumpState = False
            ds_y = LIMIT_LOW

    ds_index = (ds_index - 1) % len(img_dinosaur)
    ds_center_x = ds_x + img_dinosaur[ds_index].get_width() / 2
    ds_center_y = ds_y + img_dinosaur[ds_index].get_height() / 2
    screen.blit(img_dinosaur[ds_index], (ds_x, ds_y))


def move_cacti():
    """移動仙人掌"""
    global cacti_x, score, cacti_center_x, cacti_center_y

    cacti_x = (cacti_x - cacti_shift) % (bg_x - 100)
    cacti_center_x = cacti_x + img_cacti.get_width() / 2
    cacti_center_y = cacti_y + img_cacti.get_height() / 2
    screen.blit(img_cacti, (cacti_x, cacti_y))

    if cacti_x <= 0:
        score += 1


def score_update():
    """更新分數"""
    score_sur = score_font.render(str(score), False, RED)
    screen.blit(score_sur, (10, 10))


def is_hit(x1, y1, x2, y2, r):
    """圓形碰撞偵測"""
    if ((x1 - x2)**2 + (y1 - y2)**2) < (r * r):
        return True
    else:
        return False


def game_over():
    """遊戲結束"""
    screen.blit(img_gg, ((bg_x - gg_w) / 2, (bg_y - gg_h) / 2))


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
img_cacti = pygame.image.load("cacti.png")
img_gg = pygame.image.load("gameover.png")
bg_x = img.get_width()
bg_y = img.get_height()
bg_roll_x = 0
######################建立視窗######################
screen = pygame.display.set_mode([bg_x, bg_y])
pygame.display.set_caption("小恐龍")
######################分數物件######################
score = 0
typeface = pygame.font.get_default_font()
score_font = pygame.font.Font(typeface, 24)
######################恐龍物件######################
ds_x = 50
ds_y = LIMIT_LOW
ds_index = 0
jumpState = False
jumpValue = 0
jump_height = 13
ds_center_x = ds_x + img_dinosaur[0].get_width() / 2
ds_center_y = ds_y + img_dinosaur[0].get_height() / 2
######################仙人掌物件######################
cacti_x = bg_x - 100
cacti_y = LIMIT_LOW
cacti_shift = 10
cacti_center_x = cacti_x + img_cacti.get_width() / 2
cacti_center_y = cacti_y + img_cacti.get_height() / 2
cacti_detect_r = max(img_cacti.get_width(), img_cacti.get_height()) / 2

######################遊戲結束物件####################
gg = False
gg_w = img_gg.get_width()
gg_h = img_gg.get_height()
######################循環偵測######################

cnt = 0

while True:
    clock.tick(20)  # 設定每秒20幀執行
    mouse_pos = pygame.mouse.get_pos()

    # 取得事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE and ds_y <= LIMIT_LOW:
                jumpState = True
            if event.key == K_RETURN and gg:
                score = 0
                gg = False
                cacti_x = bg_x - 100
                ds_y = LIMIT_LOW
                jumpState = False
    if gg:
        game_over()
    else:
        bg_update()
        move_dinosaur()
        move_cacti()
        score_update()
        gg = is_hit(ds_center_x, ds_center_y, cacti_center_x, cacti_center_y,
                    cacti_detect_r)
        pygame.draw.circle(screen, RED,
                           (int(cacti_center_x), int(cacti_center_y)),
                           cacti_detect_r, 1)

    # 更新繪圖視窗
    pygame.display.update()
