'''Snowflake Blizard'''

import pygame
import random

RED=(255, 0, 0)
REDORANGE=(230, 50, 0)
ORANGE=(230, 120, 0)
YELLOWORANGE=(250, 160, 0)
YELLOW=(250, 210, 0)
YELLOWGREEN=(230, 230, 0)
GREEN=(0,255 , 0)
DARKGREEN=(0, 100, 0)
BLUEGREEN=(0, 150, 100)
CYAN=(0, 255, 225)
SKYBLUE=(100, 150, 255)
BLUE=(0, 0, 255)
INDIGO=(30, 0, 100)
LIGHTPURPLE=(160, 100, 255)
PURPLE=(130, 0, 220)
DARKPURPLE=(40, 0, 100)
MAGENTA=(200, 0, 200)
PINK=(250, 0, 250)
WHITE=(255, 255, 255)
BLACK=(0,0,0)
colors=[GREEN, DARKGREEN,BLUEGREEN, CYAN, SKYBLUE, BLUE, INDIGO]

pygame.init()

size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Snow")


class SnowFlake():
    def __init__(self):
        self.y_speed=random.randint(-3, -1)
        self.x_location=random.randint(0, 700)
        self.size=random.randint(2, 15)
        self.color=((random.randint(0, 255)), (random.randint(0, 255)), (random.randint(0, 255)) )
        self.y_location=random.randint(490, 500)
    def fall(self, screen):
        pygame.draw.circle(screen, self.color, [self.x_location, self.y_location], self.size)
        self.y_location += self.y_speed



done = False

clock = pygame.time.Clock()

snow_list = []


while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(BLACK)

    snow_list.append(SnowFlake())

    for flake in snow_list:
        flake.fall(screen)

    pygame.display.flip()

    clock.tick(30)


pygame.quit()
exit()
