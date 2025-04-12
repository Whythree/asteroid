import pygame
from constants import *

def main():
    print("Starting Asteroids!")
    pygame.init()

    dt = 0
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        print(dt)
        screen.fill((0,0,0))
        dt = clock.tick(60) / 1000
        pygame.display.flip()





if __name__ == "__main__":
    main()
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
