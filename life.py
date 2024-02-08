import pygame
from pygame.sprite import Sprite


class Life(Sprite):
    def __init__(self, screen, x, y):
        # Initialize a life object with its position
        super(Life, self).__init__()
        self.screen = screen
        self.image = pygame.image.load("images/heart.png")  # Load the image for a life
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self):
        # Draw the life image on the screen
        self.screen.blit(self.image, self.rect)


def check_collisions(player, attackerss,player_lives):
    # Check for collisions between player and attackers
    collisions = pygame.sprite.spritecollide(player, attackerss, True)

    if collisions:
        # Return a life object if lives remain
        if len(player_lives) > 0:
            lost_life = player_lives.sprites()[0]  # Get the first (and only) sprite from the lives group
            return lost_life

    return None
