#!/usr/bin/python
# -*- coding: utf-8 -*-
# 画曲线

import pygame
import sys
pygame.init()
screen = pygame.display.set_mode([640,480])
screen.fill([255,255,255])
my_ball = pygame.image.load('image/ball.png')
my_ball = pygame.transform.scale(my_ball, (100,100))

screen.blit(my_ball, [50,50])
pygame.display.flip()
pygame.time.delay(2000)
screen.fill([255,255,255])
screen.blit(my_ball,[150,50])
pygame.display.flip()


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    