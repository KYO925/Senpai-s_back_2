import sys, pygame, random
from pygame.locals import *
from food import *

pygame.init()
size = width, height = (640, 720)
screen = pygame.display.set_mode(size)


def main():
    pygame.display.set_caption("ONAKA GAME")
    x = width/2
    y = height-30
    foods = []
    clock = pygame.time.Clock()
    FPS = 60
    food_amount = 30

    while True:
        clock.tick(FPS)
        screen.fill((0, 0, 0,))
        pygame.draw.circle(screen, (255,255,255),(x, y),30)
        pygame.draw.rect(screen, (255,255,255), (20,5,20,690), 10)
        
        if len(foods) <= 15:
            for i in range(food_amount):
                food = Food(random.choice(food_box), 0, random.randrange(45, width), random.randrange(-3000, -10))
                foods.append(food)

        for food in foods:
            food.draw(screen)
            food.fall()

            if food.y > height + 50:#foodが画面外にあったら
                foods.remove(food)
               




        pygame.display.update()


        pressed_key = pygame.key.get_pressed()
        if pressed_key[K_LEFT] and  x > 30 +45 :
            x-=10
        if pressed_key[K_RIGHT] and x < width - 30:
            x+=10
        
    

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

def main_menu():
    titlefont = pygame.font.SysFont(None, 32)
    while True:
        screen.fill((0,0,0))
        titletext = titlefont.render('PRESS SPACE TO START', True, (200,200,0))
        screen.blit(titletext, (int(width/2) -int(titletext.get_width()/2),400))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.key == K_SPACE:
                    main()

if __name__ == "__main__":
    main_menu()
   