
import pygame

pygame.init()

display_x = 600
display_y = 500
display = pygame.display.set_mode((display_x, display_y))
pygame.display.set_caption('Прыг Скок')

display.fill((255, 255, 255))


clock = pygame.time.Clock()
pers = pygame.image.load('ptigc.png')
bytilki = pygame.image.load('бутылка.png')
fon = pygame.image.load('fon.png')
display.blit(fon, (display_x - 600, display_y- 500))
user_x = 40
user_y = 60
x = display_x / 2 - user_x*2
y = display_y - (user_y*2)


byt_x_raz = 30
byt_y_raz = 70
x_byt = display_x - byt_x_raz
y_byt = display_y - (user_y*2) -10

make_jump = False
jumper = 30

def draw():
    #display.fill((255, 255, 255))
    display.blit(fon, (display_x - 600, display_y - 500))

    #pygame.draw.rect(display, (247, 240, 22), (x, y, user_x, user_y),)
    display.blit(pers, (x, y))
    bytilka()
    pygame.display.update()
    clock.tick(60)

def run_game():
    global make_jump, pers, bytilki
    game = True
    while game:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
                pygame.quit()
                quit()
        draw()
        keus = pygame.key.get_pressed()
        if keus[pygame.K_SPACE]:
            make_jump = True

        if make_jump:
            jump()



        #draw()

def check_position():
    pass


def jump():
    global make_jump, y, jumper
    if jumper >= -30:
        y -= jumper /3
        jumper -= 1
    else:
        jumper = 30
        make_jump = False

def bytilka():
    global byt_x_raz, byt_y_raz, x_byt, y_byt
    if byt_x_raz >= -x_byt:

        pygame.draw.rect(display, (50, 205, 50), (x_byt, y_byt, byt_x_raz, byt_y_raz))
        display.blit(bytilki, (x_byt, y_byt))
        x_byt -= 4
    else:
        x_byt = display_x



run_game()