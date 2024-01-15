import sys
import pygame
from bird import Bird
from pig import Pig

pygame.init()

width = 1200
height = 800
screen = pygame.display.set_mode((width, height))
bird = Bird('red', [200, 400])
pig = Pig([800, 400])
gravity = 1

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    bird.power += gravity
    bird.position[1] += bird.power
    if bird.position[1] > 800:
        bird.power = 0
        bird.position[1] = 400
    
    screen.fill((255, 255, 255))

    pygame.draw.circle(screen, bird.color, (int(bird.position[0]), int(bird.position[1])), bird.radius)
    pygame.draw.circle(screen, pig.color, (int(pig.position[0]), int(pig.position[1])), pig.radius)
    pygame.display.flip()
    pygame.time.Clock().tick(60)
