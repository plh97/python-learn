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
# 控制字体大小 100px 大小
myFont = pygame.font.Font(None, 100)
# 渲染字体 Hello World
textImage = myFont.render("Hello world", True, white)

running = True
while running:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()
    screen.fill(blue)
    screen.blit(textImage, (100, 100))
    pygame.display.update()