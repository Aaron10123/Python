import pygame
import sys  #關視窗的指令
import math

screen = pygame.display.set_mode((640, 320))  #視窗的寬高
pygame.display.set_caption("My Frist Game")  #視窗名
background = pygame.Surface((640, 320))  #建立畫布
background.fill((255, 255, 255))  #畫布的顏色

#畫圓形, (畫布, 顏色, 圓心, 半徑, 線寬)
# pygame.draw.circle(background, (0, 0, 255), (500, 100), 30, 0)
#畫矩形, (畫布, 顏色,[[x, y, 寬, 高], 線寬)
# pygame.draw.rect(background, (0, 255, 0), [270, 130, 60, 40], 5)
#畫橢圓, (畫布, 顏色,[[x, y, 寬, 高], 線寬)
# pygame.draw.ellipse(background, (255, 0, 0), [130, 160, 60, 35], 5)
#
# pygame.draw.line(background, (255, 0, 255), (280, 220), (320, 220), 3)
#畫多邊形
# pygame.draw.polygon(background, (100, 200, 45),
# [[100, 100], [0, 200], [200, 200]], 0)
#畫圓弧
# pygame.draw.arc(background, (255, 10, 0), [100, 10, 100, 50],
# math.radians(180), math.radians(0), 2)

while True:
    for event in pygame.event.get():  #抓取視窗事件
        if event.type == pygame.QUIT:  #判斷視窗事件
            sys.exit()  #關閉所有程式   #使用者按關閉鍵
        if event.type == pygame.MOUSEBUTTONDOWN:
            #pygame.mouse.get_pos()
            pygame.draw.circle(background, (0, 0, 255), (500, 100), 30, 0)

    print(pygame.mouse.get_pos())  #取得滑鼠座標
    screen.blit(background, (0, 0))  #繪製畫布於視窗左上角
    pygame.display.update()  #更新視窗
