import pygame
from pygame.sprite import Sprite
import pygame.mixer
class Bullet (Sprite):
    def __init__(self, screen,player,scale=1.0):
        super(Bullet,self).__init__()
        self.screen=screen
        self.image=pygame.image.load("images/bullettt.png")
        self.bullet_sound = pygame.mixer.Sound("audio/bullet_sound.wav.mp3")  # Load bullet sound
        self.rect=self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.rect.centery=player.rect.centery
        self.rect.left = player.rect.left + player.rect.width
        self.x=float(player.rect.x)
        self.bullet_speed=10

    def update(self):
        self.x += self.bullet_speed
        self.rect.x = self.x

    def draw(self):

        self.screen.blit(self.image, self.rect)

    def fire_sound(self):
        self.bullet_sound.play()