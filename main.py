# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from circleshape import *
from player import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    #Creating groups to declutter
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updateable, drawable)

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

        # Draw the player
        for obj in drawable:
            obj.draw(screen)

        # Motion granted to the player
        updateable.update(dt)

        # Update the displayd
        pygame.display.flip()

        # Limit the frame rate and calculate delta time
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()