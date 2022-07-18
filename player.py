import sys, pygame, os
from pygame.locals import *

player_img = pygame.image.load(os.path.join('images', 'Player.png'))

class Player:
    def __init__(self, img, x, y):
        self.player_img = img
        self.x = x
        self.y = y
        self.point = 0
        self.mask = pygame.mask.from_surface(self.player_img)

    def draw(self, screen):
        screen.blit(self.player_img, (self.x, self.y))
        pygame.draw.rect(screen, (255,255,255), (5,5,30,700), 2)
        pygame.draw.rect(screen, (255,128,128), (10,700-700*self.point/100,20,700*self.point/100), 0)

    def move(self, horizontal):
        self.x += horizontal

    def add_point(self, p):
        self.point += p


