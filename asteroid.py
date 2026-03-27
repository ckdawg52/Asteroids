import random

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            vel = self.velocity
            new_v = random.uniform(20, 50)
            v1 = self.velocity.rotate(new_v)
            v2 = self.velocity.rotate(-new_v)
            new_r = self.radius - ASTEROID_MIN_RADIUS
            a1 = Asteroid(self.position.x, self.position.y, new_r)
            a2 = Asteroid(self.position.x, self.position.y, new_r)
            a1.velocity = v1 * 1.2
            a2.velocity = v2 * 1.2
