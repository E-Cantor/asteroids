# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Creating Asteroid Field group
    asteroid_field_updateable = pygame.sprite.Group()
    AsteroidField.containers = (asteroid_field_updateable,)

    # Initializing Asteroid Field
    asteroid_field = AsteroidField()

    # Creating player groups to declutter
    p_updateable = pygame.sprite.Group()
    p_drawable = pygame.sprite.Group()
    Player.containers = (p_updateable, p_drawable)

    # Creating asteroid groups to declutter
    a_updateable = pygame.sprite.Group()
    a_drawable = pygame.sprite.Group()
    Asteroid.containers = (a_updateable, a_drawable)

    #creating shots groups to declutter
    s_updateable = pygame.sprite.Group()
    s_drawable = pygame.sprite.Group()
    Shot.containers = (s_updateable, s_drawable)

    # Create the player at the center of the screen
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)

    dt = 0
    clock = pygame.time.Clock()

    while True:
        # Handle events, update game state, and draw to the screen
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Clear the screen with black
        screen.fill((0, 0, 0))

        # Update asteroid field objects
        asteroid_field_updateable.update(dt)

        # Update and draw player-related objects
        p_updateable.update(dt)
        for obj in p_drawable:
            obj.draw(screen)

        # Update and draw asteroid-related objects
        a_updateable.update(dt)
        for obj in a_drawable:
            obj.draw(screen)

        # Detecting collision between Asteroid and Player
        for asteroid in a_drawable.sprites():  # assuming 'asteroids' is your asteroid group
            if player.collision(asteroid):  # assuming 'player' is your player object
                print("Game over!")
                import sys
                sys.exit()  # immediately exit the program

        # Update the display
        pygame.display.flip()

        # Limit the frame rate and calculate delta time
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()