import random
from math import hypot,atan2,cos,sin,pi,sqrt,degrees
import pygame, sys
from pygame.locals import *
import time


def betterArc(surf, color, rect, start, end, width=1):
    (x,y,w,h) = rect
    trans = [0,0,0,0]
    tmpSurf = pygame.Surface((w,h),SRCALPHA)
    pygame.draw.ellipse(tmpSurf,color,(0,0,w,h))
    if width:#Hollow the ellipse if needed.
        pygame.draw.ellipse(tmpSurf,trans,(width,width,w-width*2,h-width*2))
    
    #rotate backwards to line start up with 0, then chop off the bottom half, giving arc: start->start+pi
    rotSurf = pygame.transform.rotate(tmpSurf,-degrees(start))
    pygame.draw.rect(rotSurf,trans,(0,rotSurf.get_height()/2,rotSurf.get_width(),rotSurf.get_height()))
    rotSurf = pygame.transform.rotate(rotSurf,degrees(start))
    
    if end-start > pi:#we need more than 180 degrees
    
        #Draw the half arc we have. (start->start+pi)
        transx = (rotSurf.get_width()-w)/2
        transy = (rotSurf.get_height()-h)/2
        surf.blit(rotSurf,(x-transx,y-transy))
        
        #Cut off the remaning arc from the half we have.
        rotAngle = degrees(pi - end)
        rotSurf = pygame.transform.rotate(rotSurf,rotAngle)
        pygame.draw.rect(rotSurf,trans,(0,0,rotSurf.get_width(),rotSurf.get_height()/2))
        rotSurf = pygame.transform.rotate(rotSurf,180-rotAngle)
        
        #Draw the second part.
        transx = (rotSurf.get_width()-w)/2
        transy = (rotSurf.get_height()-h)/2
        surf.blit(rotSurf,(x-transx,y-transy))
        
    else:#We don't need all of this arc
        #Cut off the end point to end+pi (leaving you with start->end)
        rotAngle = degrees(pi-end)
        rotSurf = pygame.transform.rotate(rotSurf,rotAngle)
        pygame.draw.rect(rotSurf,trans,(0,rotSurf.get_height()/2,rotSurf.get_width(),rotSurf.get_height()/2))
        rotSurf = pygame.transform.rotate(rotSurf,-rotAngle)
        
        #Draw our arc.
        transx = (rotSurf.get_width()-w)/2
        transy = (rotSurf.get_height()-h)/2
        surf.blit(rotSurf,(x-transx,y-transy))


pygame.init()
fpsClock = pygame.time.Clock()
window = pygame.display.set_mode((400,400))
pygame.display.set_caption("ArcTest")
arc = 0
start = 0
while True:
    for event in pygame.event.get():
        if event.type == QUIT or event.type == MOUSEBUTTONDOWN:
                pygame.quit()
                sys.exit()
    window.fill([0,255,0])
    
    #Arc with a width
    betterArc(window,[0,0,255],(0,0,100,200),start,start+arc,20)
    pygame.draw.arc(window,[0,0,0],(100,0,100,200),start,start+arc,20)
    
    #Defaults to a width of 1, like pygames
    betterArc(window,[255,0,0],(0,0,100,200),start,start+arc)
    pygame.draw.arc(window,[255,255,255],(100,0,100,200),start,start+arc)
    
    #Also, if 0 or None, etc. It fills the entire arc
    betterArc(window,[255,0,0],(30,30,40,140),start,start+arc,0)
    pygame.draw.arc(window,[255,0,0],(130,30,40,140),start,start+arc,20)

    #Update stuff    
    pygame.display.update()
    dt = fpsClock.tick(30)/1000.0
    arc = (arc+dt*1.5)%(pi*2)
    start = (start + dt)%(pi*2)
