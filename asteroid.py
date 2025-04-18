from circleshape import CircleShape
import pygame
import random

from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius, velocity=pygame.Vector2(0,0)):
        super().__init__(x,y,radius)
        self.velocity = velocity

    def draw(self, screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        random_angle = random.uniform(20,50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_spawn_velocity = self.velocity.rotate(random_angle)
        asteroid_spawn_velocity_negative = self.velocity.rotate(-random_angle)

        new_asteroid = Asteroid(self.position.x, self.position.y, new_radius, asteroid_spawn_velocity * 1.2)
        new_asteroid = Asteroid(self.position.x, self.position.y, new_radius, asteroid_spawn_velocity_negative * 1.2)
