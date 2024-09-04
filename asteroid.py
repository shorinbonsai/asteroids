import pygame
from constants import *
from circleshape import CircleShape
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        rand_angle = random.uniform(20, 50)

        first = self.velocity.rotate(rand_angle)
        second = self.velocity.rotate(-rand_angle)

        radius_new = self.radius - ASTEROID_MIN_RADIUS
        asteroid = Asteroid(self.position.x, self.position.y, radius_new)
        asteroid.velocity = first * 1.2
        asteroid = Asteroid(self.position.x, self.position.y, radius_new)
        asteroid.velocity = second * 1.2
