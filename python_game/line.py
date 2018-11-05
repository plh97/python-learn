#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 画直线
import pygame,sys
from pygame.locals import *


pygame.init()
screen_width = 600
screen_height = 500
width = 10
title = 'draw line'
bg_color = (222,222,222)
screen = pygame.display.set_mode([screen_width,screen_height])
pygame.display.set_caption(title)


while True:
  for event in pygame.event.get():
    if event.type in (QUIT, KEYDOWN):
      sys.exit()


  screen.fill(bg_color)
  # here to draw something
  pygame.draw.line(screen, (200,200,222), (100,100), (500,400), width)


  pygame.display.update()