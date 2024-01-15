import sys
import pygame
import math
from bird import Bird
from pig import Pig

pygame.init()

width = 1200
height = 800
screen = pygame.display.set_mode((width, height))
bird = Bird('red', [200, 400])
pig = Pig([800, 400])
gravity = 1
sling = False
shoot = False
initial_position = []
max_length = 100
def slingshotInbound(position, mos_position):
    x, y = pygame.mouse.get_pos()
    bird_pos = position
    distance = math.hypot(x - initial_position[0], y - initial_position[1])
    if distance > max_length:
        angle = math.atan2(y - position[1], x - position[0])
        bird_pos = [int(position[0] + max_length * math.cos(angle)), 
                    int(position[1] + max_length * math.sin(angle))]
        return bird_pos
    if distance < max_length:
        return mos_position
    

while True:
    x, y = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: # Left Click
                if sling == True:
                    break
                if(bird.inBound(x, y)):
                    sling = True
                    initial_position = bird.position
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1: # Left Click
                initial_position = []
                sling = False
                shoot = True

    if sling == True:
        bird.position = slingshotInbound(initial_position, [x, y])

    if shoot == True:
        bird.velocity += gravity
        bird.position[1] += bird.velocity
        if bird.position[1] > 800:
            bird.velocity = 0
            bird.position[1] = 400
            bird.position[0] = 200
            shoot = False
    
    screen.fill((255, 255, 255))

    pygame.draw.circle(screen, bird.color, (int(bird.position[0]), int(bird.position[1])), bird.radius)
    pygame.draw.circle(screen, pig.color, (int(pig.position[0]), int(pig.position[1])), pig.radius)
    pygame.display.flip()
    pygame.time.Clock().tick(60)
