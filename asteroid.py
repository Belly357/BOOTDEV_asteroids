import pygame  # type: ignore
import random
from circleshape import *
from constants import ASTEROID_MIN_RADIUS

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
        
        ran_angle = random.uniform(20, 50)
        rotation_one = self.velocity.rotate(ran_angle)
        rotation_two = self.velocity.rotate(-ran_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_one = Asteroid(self.position[0], self.position[1], new_radius)
        asteroid_two = Asteroid(self.position[0], self.position[1], new_radius)
        asteroid_one.velocity = rotation_one * 1.2
        asteroid_two.velocity = rotation_two * 1.2
        