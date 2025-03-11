# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from circleshape import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    dt = 0
    clock = pygame.time.Clock

    while True:
        #Handling events, updating game state, and drawing to screen.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        pygame.Surface.fill(screen, (0,0,0))
        pygame.display.flip()

        # Limiting the frame rate to x FPS
        clock.tick(60)
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()