import sys, pygame
from pygame.locals import *

pygame.init()
size = width, height = (1280, 720)
screen = pygame.display.set_mode(size)

def main():
    pygame.display.set_caption("ONAKA GAME")
    x = width/2
    y = height/2

    while True:
        screen.fill((0, 0, 0,))
        pygame.draw.circle(screen, (255,255,255),(x, y),30)
        pygame.display.update

        pressed_key = pygame.key.get_pressed()
        if pressed_key[K_LEFT]:
            x-=1
        if pressed_key[K_RIGHT]:
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
   