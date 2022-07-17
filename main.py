import sys, pygame
from pygame.locals import *
import food

pygame.init()
size = width, height = (640, 720)
screen = pygame.display.set_mode(size)


def main():
    pygame.display.set_caption("ONAKA GAME")
    x = width/2
    y = height-30
    chicken = food.Food(food.fried_chicken, 0, 300, 0)

    while True:
        screen.fill((0, 0, 0,))
        pygame.draw.circle(screen, (255,255,255),(x, y),30)
        pygame.draw.rect(screen, (255,255,255), (20,5,20,690), 10)
        
        chicken.draw(screen)
        chicken.fall()
        pygame.display.update()


        pressed_key = pygame.key.get_pressed()
        if pressed_key[K_LEFT] and  x > 30 +45 :
            x-=1
        if pressed_key[K_RIGHT] and x < width - 30:
            x+=1
        
    

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
   