import pygame
from circleshape import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, surface):
        color = "white"
        width = 2
        pygame.draw.circle(surface, color, self.position, self.radius, width)

    def update(self, dt):
        self.position += self.velocity * dt
    
