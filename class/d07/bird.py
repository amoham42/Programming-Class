class Bird:
    def __init__(self, color, position):
        self.radius = 20
        self.color = color
        self.speed = 5
        self.velocity = 0
        self.position = position
    

    def inBound(self, x_mouse, y_mouse):
        if (abs(self.position[0] - x_mouse)) <= self.radius:
            if(abs(self.position[1] - y_mouse)) <= self.radius:
                return True
        
        return False