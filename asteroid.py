import pygame
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)  # Pass all required arguments to parent
        self.rotation = 0
        self.velocity = pygame.Vector2(0, 0)

    def draw(self, screen):
        # Draw the asteroid using its actual attributes
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius, 2)

    def update(self, dt):
        # sub-classes must override
        self.position += (self.velocity*dt)