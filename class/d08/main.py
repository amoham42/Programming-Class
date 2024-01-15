import sys
import pygame
import math
from bird import Bird
from pig import Pig

pygame.init()

width = 1200
height = 600
screen = pygame.display.set_mode((width, height))
bird = Bird('red', [160, 360], pygame)
pig = Pig([800, 400], pygame)
gravity = 1
slingshot_velocity = 1
sling = False
shoot = False
initial_position = []
max_length = 100
background = pygame.image.load("background.png")
slingshot_image = pygame.image.load("slingshot.png")
slingshot_image = pygame.transform.scale(slingshot_image, (int(slingshot_image.get_width() / 4), slingshot_image.get_height() / 4))
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
                gravity -= 1
                slingshot_velocity += 1
                initial_position = []
                sling = False
                shoot = True

    if sling == True:
        bird.position = slingshotInbound(initial_position, [x, y])

    if shoot == True:
        bird.velocity += gravity
        bird.position[1] += bird.velocity
        bird.position[0] += slingshot_velocity

        if bird.position[1] > 800:
            bird.velocity = 0
            bird.position[1] = 360
            bird.position[0] = 160
            slingshot_velocity = 0
            shoot = False
    
    screen.fill((255, 255, 255))
    screen.blit(background, (0, 0))
    pygame.draw.line(screen, (123, 63, 0), (180, 340), (int(bird.position[0]), int(bird.position[1])), 20)
    pygame.draw.line(screen, (123, 63, 0), (140, 360), (int(bird.position[0]), int(bird.position[1])), 20)
    screen.blit(slingshot_image, (100, 300))
    pygame.draw.circle(screen, bird.color, (int(bird.position[0]), int(bird.position[1])), bird.radius)
    
    screen.blit(bird.image, (int(bird.position[0] - 40), int(bird.position[1] - 40)))
    screen.blit(pig.image, (int(pig.position[0]), int(pig.position[1])))
    


    pygame.display.flip()
    pygame.time.Clock().tick(60)
