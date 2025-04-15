import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    print("Starting Asteroids!")
    pygame.init()

    #Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    dt = 0
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT/2)

    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    #GameLoop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0,0,0))

        for item in drawable:
            item.draw(screen)

        for asteroid in asteroids:
            if asteroid.collide(player):
                print("Game Over!")
                sys.exit()

        updatable.update(dt)

        dt = clock.tick(60) / 1000
        pygame.display.flip()


if __name__ == "__main__":
    main()
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
