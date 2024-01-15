class Bird:
    def __init__(self, color, position, pygame):
        self.radius = 20
        self.color = color
        self.speed = 5
        self.velocity = 0
        self.position = position
        self.image = pygame.image.load("red.png")
        self.image = pygame.transform.scale(self.image, (80, 80))
    

    def inBound(self, x_mouse, y_mouse):
        if (abs(self.position[0] - x_mouse)) <= self.radius:
            if(abs(self.position[1] - y_mouse)) <= self.radius:
                return True
        
        return False