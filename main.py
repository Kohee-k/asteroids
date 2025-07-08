# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group ()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    player = Player(x, y)
    asteroidfield = AsteroidField()


    while True:
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                return
            
        screen.fill("black")

        updatable.update(dt)
        for sprite in drawable:
            sprite.draw(screen)
        
        pygame.display.flip()

        #Framelimiter
        dt = clock.tick(60) / 1000
    

if __name__ == "__main__":
    main()