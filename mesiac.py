import pygame

SIRKA = 400
VYSKA = 400
VELKOST = 30
GRAVITY = 0.03
ACCEL_Y = 0.1
ACCEL_X = 0.01
BRZDENIE = 1.2
MAX_TOUCH_SPEED = -1.0

def stvorec(x, y):
    return pygame.Rect(int(x), int(y), VELKOST, VELKOST)


def volny_pad():
    rychlost_y = 0.0
    rychlost_x = 0.0
    pos_x = (SIRKA - VELKOST) / 2
    pos_y = VYSKA - VELKOST
    screen = pygame.display.set_mode((SIRKA, VYSKA))
    my_font = pygame.font.SysFont("Comic Sans MS", 15)
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            rychlost_y += ACCEL_Y
        if pressed[pygame.K_RIGHT]:
            rychlost_x += ACCEL_X
        if pressed[pygame.K_LEFT]:
            rychlost_x -= ACCEL_X
        rychlost_y -= GRAVITY
        if pos_y > VYSKA - VELKOST:
            pos_y = VYSKA - VELKOST
            rychlost_y = 0.0
            rychlost_x /= BRZDENIE
        pos_y -= rychlost_y
        pos_x += rychlost_x

        screen.fill((0 ,0, 0))
        text_surface = my_font.render(
            f"SPEED X:{rychlost_x:6.1f} Y:{rychlost_y:6.1f}", True, (255, 127, 0))
        screen.blit(text_surface, (0,0))
        pygame.draw.rect(screen, (255, 255, 255), stvorec(pos_x, pos_y))

        pygame.display.flip()
        clock.tick(60)


def main():
    pygame.init()
    pygame.font.init()
    volny_pad()
    pygame.quit()


main()
