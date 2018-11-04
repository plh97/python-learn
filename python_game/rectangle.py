#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 意图设计一个 正方形, 在屏幕内部弹来弹去

import pygame,sys
from pygame.locals import *

pygame.init()

dx = 10
dy = 10
rect_x = 100
rect_y = 100
pos_x = 300
pos_y = 200
screen_width = 600
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))


pygame.display.set_caption("draw rectangle")


while True:
    for event in pygame.event.get():
        if event.type in (QUIT,KEYDOWN):
            sys.exit()

    if pos_x > screen_width-rect_x or pos_x<0:
        dx = -dx
    if pos_y > screen_height-rect_y or pos_y<0:
        dy = -dy


    pos_x += dx
    pos_y += dy


    screen.fill((0,0,200))

    color = (0, 255,0)
    pos = pos_x, pos_y, rect_x, rect_y
    print(pos)
    width = 0
    pygame.draw.rect(screen, color, pos, width)

    pygame.display.update()