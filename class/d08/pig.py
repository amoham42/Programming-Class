class Pig:
    def __init__(self, position, pygame):
        self.radius = 20
        self.color = (0, 255, 0)
        self.size = 50
        self.position = position
        self.image = pygame.image.load("pig.png")
        self.image = pygame.transform.scale(self.image, (100, 100))

