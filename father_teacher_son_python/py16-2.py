#!/usr/bin/python
# -*- coding: utf-8 -*-
# 随机画100个大小不等的正方形

import sys,random

import pygame,time

from pygame.color import THECOLORS
pygame.init()
screen = pygame.display.set_mode([640,480])
screen.fill([255,255,255])

running = True


def randomGraph():
    screen.fill((0,0,0))
    for i in range(100):
        width = random.randint( 0, 250)
        height = random.randint( 0, 100)
        top = random.randint(0, 400)
        left = random.randint(0, 500)
        color_name = random.choice(THECOLORS.keys())
        color = THECOLORS[color_name]
        line_width = random.randint(1, 3)
        pygame.draw.rect(screen, color, [left, top, width, height], line_width)
    pygame.display.flip()


randomGraph()


running = True


while running:
    print('刷新')
    randomGraph()
    time.sleep(1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()