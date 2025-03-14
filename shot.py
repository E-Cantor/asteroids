from circleshape import CircleShape
from constants import SHOT_RADIUS, SCREEN_WIDTH, SCREEN_HEIGHT
import pygame

class Shot(CircleShape):
    def __init__(self, position, velocity):
        super().__init__(position.x, position.y, SHOT_RADIUS)
        self.velocity = velocity

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (int(self.position.x), int(self.position.y)), self.radius, 1)

    def update(self, dt):
        self.position += self.velocity * dt
        self.x = self.position.x
        self.y = self.position.y
        # Remove shot if it goes off-screen
        if (self.position.x < 0 or 
            self.position.x > SCREEN_WIDTH or 
            self.position.y < 0 or 
            self.position.y > SCREEN_HEIGHT):
            self.kill()  # Removes from all sprite groups