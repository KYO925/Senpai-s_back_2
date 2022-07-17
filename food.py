import sys, pygame, os
from pygame.locals import *

#画像の読み込み
fried_chicken = pygame.image.load(os.path.join('images', 'FriedChicken.png'))
chocolate = pygame.image.load(os.path.join('images', 'Chocolate.png'))
iceCream = pygame.image.load(os.path.join('images', 'IceCream.png'))
ramen = pygame.image.load(os.path.join('images', 'Ramen.png'))
riceBall = pygame.image.load(os.path.join('images', 'RiceBall.png'))

food_box = [fried_chicken,
            chocolate,
            iceCream,
            ramen,
            riceBall]



class Food:
    def __init__(self, img, point, x, y):
        self.food_img = img
        self.food_point = point
        self.x = x
        self.y = y

    def draw(self, screen):
        screen.blit(self.food_img, (self.x, self.y))
    
    def fall(self):
        self.y += 10

            

