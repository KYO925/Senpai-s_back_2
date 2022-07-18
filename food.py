import sys, pygame, os, random
from pygame.locals import *
from main import *

#画像の読み込み
fried_chicken = pygame.image.load(os.path.join('images', 'FriedChicken.png'))
chocolate = pygame.image.load(os.path.join('images', 'Chocolate.png'))
iceCream = pygame.image.load(os.path.join('images', 'IceCream.png'))
ramen = pygame.image.load(os.path.join('images', 'Ramen.png'))
riceBall = pygame.image.load(os.path.join('images', 'RiceBall.png'))

food_box = [
    [fried_chicken, 10],
    [chocolate, 5],
    [iceCream, 3],
    [ramen, 20],
    [riceBall, 10]
]

class Food:
    def __init__(self, img, point, x, y, G):
        self.food_img = img
        self.point = point
        self.x = x
        self.y = y
        self.G = G
        self.mask = pygame.mask.from_surface(self.food_img)
        

    def draw(self, screen):
        screen.blit(self.food_img, (self.x, self.y))
    
    def fall(self):
        self.y += self.G


def add_food(x, y, G):
    f, p = random.choice(food_box)
    return Food(f, p, x, y, G)

