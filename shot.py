import circleshape
import constants
import pygame

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(0, 0)
        self.position = pygame.Vector2(x, y)
        SHOT_RADIUS = 5