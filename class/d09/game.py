import sys
import pygame
import math
from bird import Bird
from pig import Pig


class Game:
    def __init__(self):
        pygame.init()
        self.width = 1200
        self.height = 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background = pygame.image.load("background.png")
        self.bird = Bird('red', [160, 360], pygame)
        self.pig = Pig([800, 200], pygame)
        self.brown = (123, 63, 0)
        self.gravity = 1
        self.ground = 500
        self.slingshot()

    def slingshot(self):
        self.sling = False
        self.shoot = False
        self.max_length = 100
        self.slingshot_velocity = 1
        self.slingshot_image = pygame.image.load("slingshot.png")
        self.slingshot_image = pygame.transform.scale(self.slingshot_image,
                                                            (int(self.slingshot_image.get_width() / 4), 
                                                             int(self.slingshot_image.get_height() / 4)))

    def slingshotInbound(self, position, mouse_position):
        x, y = pygame.mouse.get_pos()
        bird_pos = position
        distance = math.hypot(x - self.bird.initial_position[0], y - self.bird.initial_position[1])
        if distance > self.max_length:
            angle = math.atan2(y - position[1], x - position[0])
            bird_pos = [int(position[0] + self.max_length * math.cos(angle)), 
                        int(position[1] + self.max_length * math.sin(angle))]
            return bird_pos
        if distance < self.max_length:
            return mouse_position
        
    def check_collision(self):

        distance = math.hypot((self.bird.position[0] - 40) - self.pig.position[0],
                              (self.bird.position[1] - 40) - self.pig.position[1])
        if distance < self.bird.radius + self.pig.radius:
            self.bird.velocity = 0
            self.bird.position[1] = 360
            self.bird.position[0] = 160
            self.slingshot_velocity = 0
    
    def get_velocity(self):

        distance = math.hypot(self.bird.position[0] - self.bird.initial_position[0], 
                              self.bird.position[1] - self.bird.initial_position[1])
        angle = math.atan2(self.bird.position[1] - self.bird.initial_position[1], 
                           self.bird.position[0] - self.bird.initial_position[0])

        self.bird.velocity = - distance * math.sin(angle) * 0.6
        self.slingshot_velocity = - distance * math.cos(angle) * 0.2
        self.bird.velocity = min(self.bird.velocity, 50)
        self.slingshot_velocity = min(self.slingshot_velocity, 50)
    
    def control(self):
            x, y = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Left Click
                        if self.sling == True:
                            break
                        if self.bird.inBound(x, y):
                            self.sling = True
                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:  # Left Click
                        self.get_velocity()
                        self.gravity = min(self.gravity, 50)
                        self.slingshot_velocity = min(self.slingshot_velocity, 50)
                        self.sling = False
                        self.shoot = True

    def physics(self):

        x, y = pygame.mouse.get_pos()
        
        if self.pig.position[1] > self.ground - self.pig.image.get_height():
            self.pig.velocity = 0
        else:
            self.pig.velocity += self.gravity
            self.pig.position[1] += self.pig.velocity
        
        if self.sling == True:
            self.bird.position = self.slingshotInbound(self.bird.initial_position, [x, y])

        if self.shoot == True:
            self.bird.velocity += self.gravity
            self.bird.position[1] += self.bird.velocity
            self.bird.position[0] += self.slingshot_velocity

            if self.bird.position[1] > self.ground:
                self.bird.velocity = 0
                self.bird.position[1] = self.bird.initial_position[1]
                self.bird.position[0] = self.bird.initial_position[0]
                
                self.shoot = False

    def render(self):
        self.screen.fill((255, 255, 255))
        self.screen.blit(self.background, (0, 0))
        if(int(abs(self.bird.position[0] - self.bird.initial_position[0])) < 105 
        and int(abs(self.bird.position[1] - self.bird.initial_position[1]) < 105)):
            pygame.draw.line(self.screen, self.brown, (180, 340), 
                                  (int(self.bird.position[0]), int(self.bird.position[1])), 20)
            pygame.draw.line(self.screen, self.brown, (140, 360), 
                                  (int(self.bird.position[0]), int(self.bird.position[1])), 20)
            
        self.screen.blit(self.slingshot_image, (100, 300))
        pygame.draw.circle(self.screen, self.bird.color, (int(self.bird.position[0]), 
                                                               int(self.bird.position[1])), self.bird.radius)
        # pygame.draw.rect(self.screen, self.brown, self.woodPlatform)

        self.screen.blit(self.bird.image, (int(self.bird.position[0] - 40), int(self.bird.position[1] - 40)))
        self.screen.blit(self.pig.image, (int(self.pig.position[0]), int(self.pig.position[1])))
        self.check_collision();

        pygame.display.flip()
        pygame.time.Clock().tick(60)
        while True:
            self.control()
            self.physics()
            self.render()


        