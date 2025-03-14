from circleshape import *
from constants import *
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(0, 0)
        self.position = pygame.Vector2(x, y)


    def draw(self, screen):
        if not isinstance(self.radius, (int, float)):
            raise TypeError(f"Expected self.radius to be a number, got {type(self.radius)} instead.")
        pygame.draw.circle(
            screen, 
            (255, 255, 255), 
            (int(self.position.x), 
             int(self.position.y)), 
             self.radius, 
             2)

    def split(self):
        random_angle = random.uniform(20, 50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        velocity_1 = self.velocity.rotate(random_angle) * 1.2
        velocity_2 = self.velocity.rotate(-random_angle) * 1.2
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return
        self.kill()
        new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_1.velocity = velocity_1

        new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_2.velocity = velocity_2

    def update(self, dt):
        self.position += (self.velocity * dt)