import sys
import pygame
from constants import *
#from circleshape import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()#create empty update group
    drawable = pygame.sprite.Group()#create empty drawable group
    asteroids = pygame.sprite.Group()#create asteroids group
    shots = pygame.sprite.Group()#create shots group to hold all shots

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()
    Player.containers = (updatable, drawable)#add Player (from player.py class Player) to both groups then create player object
    
    player = Player((SCREEN_WIDTH / 2),(SCREEN_HEIGHT / 2))#instantiate the player object to the middle of the screen
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updatable.update(dt)#player controls for movement 

        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game Over!")
                sys.exit()
            for bullet in shots:
                if asteroid.collision(bullet):
                    asteroid.split()
                    bullet.kill()

        screen.fill("black")
        
        
        for obj in drawable:
            obj.draw(screen)#draw player on the screen using the draw method of player.py

        pygame.display.flip()

        dt = clock.tick(60) / 1000#limit fps to 60

if __name__ == "__main__":
    main()