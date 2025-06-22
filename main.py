import pygame
from constants import *
from player import *

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
    Player.containers = (updatable, drawable)#add Player (from player.py class Player) to both groups then create player object
    player = Player((SCREEN_WIDTH / 2),(SCREEN_HEIGHT / 2))#instantiate the player object to the middle of the screen
    game_running = True
    while game_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)#player controls for movement
        for sprites in drawable:
            sprites.draw(screen)#draw player on the screen using the draw method of player.py
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()