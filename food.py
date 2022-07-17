import sys, pygame, os
from pygame.locals import *

#画像の読み込み
fried_chicken = pygame.image.load(os.path.join('images', 'FriedChicken.png'))

class Food:
    def __init__(self, img, point, x, y):
        self.food_img = img
        self.food_point = point
        self.x = x
        self.y = y

    def draw(self, screen):
        screen.blit(self.food_img, (self.x, self.y))
    
    def fall(self):
        self.y += 1
            

