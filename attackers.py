import pygame
from pygame.sprite import Sprite
import math
import random

class Attackers(Sprite):
    def __init__(self, screen, ai_settings):
        super(Attackers, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load("images/attacker.png")
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # Initialize attacker's position and movement properties
        self.rect.right = self.screen_rect.right - self.rect.width
        self.rect.centery = random.randint(0, self.screen_rect.height)
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.speed_x = random.randint(-3, -1)
        self.amplitude = random.randint(10, 40)
        self.frequency = random.uniform(0.02, 0.06)

    def update(self):
        # Update attacker's position based on sinusoidal movement
        self.y -= self.frequency
        self.x += self.speed_x
        self.y_movement = self.amplitude * math.sin(self.frequency * self.y)
        self.x_movement = self.speed_x
        self.rect.y = self.y + self.y_movement
        self.rect.x = self.x + self.x_movement

    def draw(self):
        # Draw the attacker on the screen
        self.screen.blit(self.image, self.rect)
