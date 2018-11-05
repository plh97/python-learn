#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 画????
import pygame,sys,math
from pygame.locals import *


pygame.init()
screen_width = 600
screen_height = 500
title = 'The Pie Game - Press 1,2,3,4'
bg_color = (222,222,222)
screen = pygame.display.set_mode([screen_width,screen_height])
pygame.display.set_caption(title)

myfont = pygame.font.Font(None, 60)

color = 200,80,60
width=4
y=300
x=250
radius=200

position = x-radius, y-radius, radius*2, radius*2

piece1 = False
piece2 = False
piece3 = False
piece4 = False



while True:
  for event in pygame.event.get():
    if event.type in (QUIT):
      sys.exit()
    elif event.type in KEYUP:
      if event.key == pygame.K_ESCAPE:
        sys.exit()
      elif event.type == pygame.K_1:
        piece1 = True
      elif event.type == pygame.K_2:
        piece2 = True
      elif event.type == pygame.K_3:
        piece3 = True
      elif event.type == pygame.K_4:
        piece4 = True


  # clear the screen
  screen.fill(bg_color)
  # here to draw something
  # draw the four numbers
  textImg1 = myfont.render("1", True, color)
  screen.blit(textImg1, (x+radius/2-20, y-radius/2))
  textImg2 = myfont.render("2", True, color)
  screen.blit(textImg1, (x-radius/2-20, y-radius/2))
  textImg1 = myfont.render("3", True, color)
  screen.blit(textImg1, (x+radius/2-20, y+radius/2))
  textImg1 = myfont.render("4", True, color)
  screen.blit(textImg1, (x-radius/2-20, y+radius/2))

  # should the pieces be drawn?
  if piece1:
    start_angle = math.randians(0)
    end_angle = math.radians(180)
    pygame.draw.arc(screen,color,(x,y),(x,y-radius), width)
    pygame.draw.line(screen,color,(x,y), (x,y-radius), width)
    pygame.draw.line(screen,color,(x,y), (x+radius,y), width)
    




  pygame.display.update()