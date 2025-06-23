from circleshape import CircleShape
import pygame
from constants import *
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_timer = 0
        

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        self.shot_timer -= dt#decrease shot timer by 'dt' everytime update is called on player
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)#move left
        if keys[pygame.K_d]:
            self.rotate(dt)#move right
        if keys[pygame.K_w]:
            self.move(dt)#move forward
        if keys[pygame.K_s]:
            self.move(-dt)#move backward
        if keys[pygame.K_SPACE]:
            self.shoot()

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):#shoot bullets
        if self.shot_timer > 0:
            return#prevent player from shooting if shot_timer > 0
        self.shot_timer = PLAYER_SHOT_COOLDOWN
        shot = Shot(self.position.x, self.position.y)#create new shot object at players position
        shot.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOT_SPEED#set shot velocity to player rotation * shot speed

        