#!/usr/bin/python
# -*- coding: UTF-8 -*-


import pygame,sys
from pygame.locals import *
white = (255,255,255)
blue = 0,0,255
# 初始化游戏
pygame.init()
# 设置游戏屏幕宽度 600px * 500px
screen = pygame.display.set_mode([600,500])
# 设置标题
pygame.display.set_caption("Draw Circle")


running = True
width=50
dx = 5
while running:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()
    screen.fill((0,0,200))
    # 屏幕 ,  背景颜色,   位置,   半径,    宽度
    pygame.draw.circle(screen, (255,255,0), (300,250), width, 10)

    # 宽度小于30的时候,开始增大, 大于100 的时候开始减小
    if width<30:
        dx=5
    elif width>100:
        dx=-5

    width = width+dx
    pygame.display.update()