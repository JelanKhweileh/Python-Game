import pygame

class Player():
    def __init__(self, screen: object, scale: object = 1.0) -> object:
        # Initialize player properties
        self.shield_timer = None
        self.screen = screen
        self.image = pygame.image.load("images/playerr.png")
        self.original_image = self.image.copy()
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.rect.centery = self.screen_rect.centery
        self.rect.left = self.screen_rect.left
        self.scale = scale

        # Initialize movement flags
        self.moving_top = False
        self.moving_bottom = False
        self.moving_right = False
        self.moving_left = False

    def update(self):
        # Update player's position based on movement flags
        if self.moving_top and self.rect.top > 0:
            self.rect.centery -= 30
        elif self.moving_bottom and self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery += 30
        elif self.moving_right and self.rect.right <= self.screen_rect.right:
            self.rect.right += 30
        elif self.moving_left and self.rect.left > 0:
            self.rect.left -= 30

    def draw(self):
        # Scale and draw the player's image on the screen
        scaled_image = pygame.transform.scale(self.original_image, (
            int(self.rect.width * self.scale), int(self.rect.height * self.scale)
        ))
        self.screen.blit(scaled_image, self.rect)


