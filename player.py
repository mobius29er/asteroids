import pygame
from circleshape import *
from constants import *
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)  # Pass all required arguments to parent
        self.rotation = 0
        self.velocity = pygame.Vector2(0, 0)
        self.shots = pygame.sprite.Group()
        self.shoot_cooldown = 0 


    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        # sub-classes must override
        pygame.draw.polygon(screen, "white", self.triangle(),2)

    def update(self, dt):
        # sub-classes must override
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)

        if keys[pygame.K_d]:
            self.rotate(dt)
        
        if keys[pygame.K_w]:
            self.move(dt)

        if keys[pygame.K_s]:
            self.move(-dt)
        
        # Update cooldown
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= dt

        # Check for spacebar and cooldown
        if keys[pygame.K_SPACE] and self.shoot_cooldown <= 0:
            self.shoot(dt)
            self.shoot_cooldown = 0.3  # Add 300ms cooldown between shots

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED*dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    
    def shoot(self, dt):
        # Create velocity vector
        velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        # Create new shot at player's position
        shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
        shot.velocity = velocity
        # The containers will automatically add it to the right groups