from circleshape import *
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED
from shot import *

class Player(CircleShape):
    def __init__(self, x, y, s_updateable):
        super().__init__(x, y, PLAYER_RADIUS)
        self.position = pygame.Vector2(x, y)
        self.rotation = 0
        self.shots_group = s_updateable
        # Add these lines:
        self.shot_cooldown = 0.2  # seconds between shots
        self.time_since_last_shot = 0  # start with no cooldown

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    # Drawing player sprite on game board.
    def draw(self, screen):
        pygame.draw.polygon(screen,(255,255,255), self.triangle(), 2)

    # Rotating player sprite in game.
    def rotate(self, dt):
        self.rotation = (PLAYER_TURN_SPEED * dt) + self.rotation
    
    def update(self, dt):
        keys = pygame.key.get_pressed()

        self.time_since_last_shot += dt

        # Defining rotation
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)

        # Defining forward and backwards movement
        if keys[pygame.K_w]:
            self.move_forward(dt)
        if keys[pygame.K_s]:
            self.move_backward(dt)

        # Handle spacebar for shooting with cooldown
        if keys[pygame.K_SPACE] and self.time_since_last_shot >= self.shot_cooldown:
            self.shoot()
            self.time_since_last_shot = 0  # Reset the timer

    # Moving the player sprite
    def move_forward(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def move_backward(self, dt):
        backwards = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += backwards * -PLAYER_SPEED * dt

    # Granting the shooting ability to player

    def shoot(self):
        # Use the same direction as defined by the player's triangle for consistency
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        bullet_velocity = forward * PLAYER_SHOOT_SPEED
    
        # Create position at the tip of the triangle to start the bullet
        bullet_start = self.position + forward * self.radius
    
        # Create a new shot at the tip of the player's triangle
        new_shot = Shot(bullet_start, bullet_velocity)
    
        # The Shot should automatically be added to Shot.containers
        # But adding explicitly to the shots_group doesn't hurt
        self.shots_group.add(new_shot)