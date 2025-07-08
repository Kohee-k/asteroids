import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        color = "white"
        points = self.triangle()
        line_width = 2
        pygame.draw.polygon(screen, color, points, line_width)
    
    def collision(self, othershape):
        return pygame.math.Vector2.distance_to(self.position, othershape.position) <= (self.radius + othershape.radius)

    def update(self, dt):
        # sub-classes must override
        pass