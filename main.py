import sys, pygame, random
from pygame.locals import *
from food import *
from player import *

pygame.init()
size = width, height = (640, 720)
screen = pygame.display.set_mode(size)

#衝突判定
def collide(obj1, obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None

def main():
    pygame.display.set_caption("ONAKA GAME")
    clock = pygame.time.Clock()
    FPS = 60
    speed = 10
    foods = []
    food_amount = 10
    player = Player(player_img, width/2, height-150)

    while True:
        clock.tick(FPS)
        screen.fill((0, 0, 0,))
        player.draw(screen)
        
        if len(foods) <= 5:
            for i in range(food_amount):
                foods.append(add_food(random.randrange(45, width-50), random.randrange(-3000, -10), random.randrange(5, 15)))

        for food in foods:
            food.draw(screen)
            food.fall()

            if food.y > height + 50:#foodが画面外にあったら
                foods.remove(food)

            if collide(player, food):
                foods.remove(food)
                player.add_point(food.point)
                if player.point >= 120:
                    player.point = 120
                    game_over(player.point)
               

        pygame.display.update()


        pressed_key = pygame.key.get_pressed()
        if pressed_key[K_LEFT] and  player.x > 50 :
            player.move(-speed)
        if pressed_key[K_RIGHT] and player.x < width - 100:
            player.move(speed)
        
    

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == K_SPACE:
                    game_over(player.point)

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

def game_over(score):
    gameoverfont = pygame.font.SysFont(None, 32)
    while True:
        screen.fill((0,0,0))
        if 80 == score:
            ptext = "Perfect!!!!!"
        elif 80 <= score < 90: 
            ptext = "Good"
        elif 80 > score:
            ptext = "I'm hungry."
        elif 90 <= score:
            ptext = "Overeating!!!!!"

        gameovertext = gameoverfont.render(ptext, True, (200,200,0))
        gameoverscore = gameoverfont.render(f'{score}%', True, (200,200,0))
        screen.blit(gameovertext, (int(width/2) -int(gameovertext.get_width()/2),300))
        screen.blit(gameoverscore, (int(width/2) -int(gameoverscore.get_width()/2),350))
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
                    main_menu()

if __name__ == "__main__":
    main_menu()
   