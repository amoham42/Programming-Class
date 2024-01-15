class Snake:
    def __init__(self):
        self.length = 1
        self.positions = [((width // 2), (height // 2))]
        self.direction = random.choice([pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT])
        self.color = GREEN

    def get_head_position(self):
        return self.positions[0]

    def turn(self, point):
        # Add code to change direction
        pass

    def move(self):
        # Add code to move the snake
        pass

    def reset(self):
        # Add code to reset the snake
        pass

    def draw(self, surface):
        for p in self.positions:
            r = pygame.Rect((p[0], p[1]), (gridsize, gridsize))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, BLACK, r, 1)
