# 猜字游戏

import pygame
import sys
import random

skier_images = [
    'image/tree.png',
    'image/crash.png',
    'image/down.png',
    'image/man.png',
    'image/snow.png',
]

skier_arr = [
    'image/skier_down.png',
    'image/skier_right1.png',
    'image/skier_right2.png',
    'image/skier_left2.png'
    'image/skier_left1.png',
]


class SkierClass(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('image/skier_down.png')
        self.rect = self.image.get_rect()
        self.rect.center = (320, 100)
        self.angle = 0

    def turn(self, direction):
        self.angle = self.angle + direction
        if self.angle < -2: 
            self.angle = -2
        if self.angle >  2: 
            self.angle =  2
        center = self.rect.center
        self.image = pygame.image.load(skier_arr[self.angle])

        self.rect = self.image.get_rect()
        self.rect.center = center
        speed = [self.angle, 6 - abs(self.angle) * 2]
        return speed
    
    def move(self, speed):
        self.rect.centerx = self.rect.centerx + speed[0]
        if self.rect.centerx < 20: 
            self.rect.centerx = 20
        if self.rect.centerx > 620: 
            self.rect.centerx = 60


class ObstacleClass(pygame.sprite.Sprite):
    def __init__(self, image_file, location, type):
        pygame.sprite.Sprite.__init__(self)
        self.image_file = image_file
        self.image = pygame.image.load(image_file)
        self.image = pygame.transform.scale(self.image, (40,40))

        self.rect = self.image.get_rect()
        self.rect.center = location
        self.type = type
        self.passed = False

    def update(self):
        global speed
        self.rect.centery -= speed[1]
        if self.rect.centery < -32:
            self.kill()


def create_map():
    global obstacleClass
    locations = []
    for i in range(10):
        row = random.randint(0, 9)
        col = random.randint(0, 9)
        location = [col * 64 + 20, row * 64 + 20 + 640]
        if not (location in locations):
            locations.append(location)
            type = random.choice(['tree','flag'])
            if type == 'tree': 
                img = skier_images[0]
            elif type == 'flag':
                img = 'image/skier_crash.png'
            obstacle = ObstacleClass(img, location, type)
            obstacles.add(obstacle)

def animate():
    screen.fill([255,255,255])
    obstacles.draw(screen)
    screen.blit(skier.image, skier.rect)
    screen.blit(score_text, [10, 10])
    pygame.display.flip()

pygame.init()
screen = pygame.display.set_mode([640, 640])
clock = pygame.time.Clock()
skier = SkierClass()
speed = [0, 6]
obstacles = pygame.sprite.Group()
map_position = 0
points = 0
create_map()
font = pygame.font.Font(None, 50)

running = True
while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed = skier.turn(-1)
            elif event.key == pygame.K_RIGHT:
                speed = skier.turn(1)
    skier.move(speed)

    map_position += speed[1]

    if map_position >= 640:
        create_map()
        map_position = 0

    hit = pygame.sprite.spritecollide(skier, obstacles, False)

    if hit:
        if hit[0].type == 'tree' and not hit[0].passed:
            points = points - 100
            skier.image = pygame.image.load(skier_images[0])
            animate()
            pygame.time.delay(1000)
            skier.image = pygame.image.load(skier_images[1])
            skier.image = pygame.transform.scale(skier.image, (100,100))

            skier.angle = 0
            speed = [0, 6]
            hit[0].passed = True
        elif hit[0].passed == 'flag' and not hit[0].passed:
            points += 10
            hit[0].kill()

    obstacles.update()
    score_text = font.render("Score: " + str(points), 1, (0,0,0))
    animate()
pygame.quit()