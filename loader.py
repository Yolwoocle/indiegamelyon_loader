import subprocess
import pygame
import sys
import random

# https://stackoverflow.com/questions/1811691/running-an-outside-program-executable-in-python
# subprocess.call(args, *, stdin=None, stdout=None, stderr=None, shell=False)
bwg_args = ["./bwg_win/bwg_v2.exe", "-windowed", "0"]
bugscraper_args = ["./bugscraper_win/bugscraper.exe"]
# subprocess.run

# initialize
pygame.init()
pygame.mixer.init()

WIDTH = 360
HEIGHT = 480
FPS = 30

# Define Colors 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

## initialize pygame and create window
displayInfo = pygame.display.Info()
screen = pygame.display.set_mode((displayInfo.current_w, displayInfo.current_h), pygame.FULLSCREEN)
pygame.display.set_caption("Birds With Guns / Bugscraper loader")
clock = pygame.time.Clock()     ## For syncing the FPS


## group all the sprites together for ease of update
all_sprites = pygame.sprite.Group()

## Game loop
running = True
while running:
    #* 1 Process input/events
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()
    
    screen.fill(WHITE)
    all_sprites.draw(screen)

    pygame.display.flip()       

pygame.quit()