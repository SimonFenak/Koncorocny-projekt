import pygame
import random
import subprocess

WIDTH = 850
HEIGHT = 660
BALL_SIZE = 20
BALL_SPEED = 4


def stvorec(x, y):
    return pygame.Rect(int(x), int(y), BALL_SIZE, BALL_SIZE)

def plosky(x, y):
    return pygame.Rect(int(x), int(y), 10, 100)
def menu():
    return pygame.Rect(100, 100, 50, 50)
def pause():
    return pygame.Rect(0, 0, 300,660)

def pong():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    my_font = pygame.font.SysFont("Consolas", 30)
    clock = pygame.time.Clock()
    hrac1_body = 0
    hrac2_body = 0

    running = True
    choices=[[10,HEIGHT / 2 - 50],[WIDTH - 30, HEIGHT / 2 - 50]]
    vyber=random.randint(0,1)
    ball_x = choices[vyber][0]
    ball_y = choices[vyber][1]
    ploska1_y = HEIGHT / 2 - 50
    ploska1_x = 0
    ploska2_y = HEIGHT / 2 - 50
    ploska2_x = WIDTH - 10

    movement = [random.choice([-1, 1]), random.choice([1, -1])]
    tlacitko = pygame.image.load("menu-bar.png")
    mensie =pygame.transform.scale(tlacitko, (50, 50))
    zastavene=True
    minihry = pygame.image.load("minihry1.png").convert_alpha()
    minihrymen = pygame.transform.scale(minihry, (180, 80))
    ukoncit = pygame.image.load("ukoncit1.png").convert_alpha()
    ukoncitmen = pygame.transform.scale(ukoncit, (180, 80))
    start = pygame.image.load("start.png").convert_alpha()
    startmen = pygame.transform.scale(start, (180, 80))
    side = pygame.image.load("sidebar.png").convert_alpha()
    sidemen = pygame.transform.scale(side, (300, 660))
    font = pygame.font.Font(None, 36)
    nadpis = pygame.font.Font(None, 50)
    text = nadpis.render("Ping Pong!!", True, (255, 255, 255))
    text1= font.render("Vitajte v hre ping pong hra je určená ", True, (255, 255, 255))
    text2 = font.render("pre dvoch hráčov. Ulohou je aby", True, (255, 255, 255))
    text3=font.render("hráči dostali kocku za protivníka.",True, (255, 255, 255))
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                xpsova, ypsilonova = event.pos
                if xpsova < 110 and xpsova > 10 and ypsilonova < 110 and ypsilonova > 10  :
                        zastavene=True

        if zastavene==False:
            pressed = pygame.key.get_pressed()
            if ploska1_y > 0:
                if pressed[pygame.K_w]:
                    ploska1_y -= 4
            if ploska1_y < (HEIGHT - 100):
                if pressed[pygame.K_s]:
                    ploska1_y += 4
            if ploska2_y > 0:
                if pressed[pygame.K_UP]:
                    ploska2_y -= 4
            if ploska2_y < (HEIGHT - 100):
                if pressed[pygame.K_DOWN]:
                    ploska2_y += 4


            if ball_x < 0:
                movement = [0, 0]
                hrac2_body += 1
                ball_x = 10
                ball_y = ploska1_y + 30
                movement = [random.choice([-1, 1]), random.choice([1, -1])]
            if ball_y < 0:
                movement[1] = 1
            if ball_x > (WIDTH - BALL_SIZE):
                movement = [0, 0]
                hrac1_body += 1
                ball_x = WIDTH - 30
                ball_y =  ploska2_y + 30
                movement=[random.choice([-1, 1]), random.choice([1, -1])]
            if ball_y > (HEIGHT - BALL_SIZE):
                movement[1] = -1
            ball_x += BALL_SPEED * movement[0]
            ball_y += BALL_SPEED * movement[1]
            screen.fill((0,0,0))

            lopta = pygame.draw.rect(screen, (255, 255, 255), stvorec(ball_x, ball_y))

            hrac1 = pygame.draw.rect(screen, (255,255,255), plosky(ploska1_x, ploska1_y))
            hrac2 = pygame.draw.rect(screen, (255, 255, 255), plosky(ploska2_x, ploska2_y))
            screen.blit(mensie, (10, 10))
            if pygame.Rect.colliderect(lopta, hrac1):
                movement[0] = 1
            if pygame.Rect.colliderect(lopta, hrac2):
                movement[0] = - 1

            text_surface = my_font.render(f"{hrac1_body} : {hrac2_body}", True, (255, 0, 0))
            screen.blit(text_surface, ((WIDTH - text_surface.get_width()) / 2, 0))

            pygame.display.flip()
            clock.tick(60)
        else:
            screen.blit(sidemen, (0, 0))
            screen.blit(startmen, (60, 200))
            screen.blit(startmen, (60, 200))
            screen.blit(minihrymen, (60, 300))
            screen.blit(ukoncitmen, (60, 400))
            screen.blit(mensie, (10, 10))
            screen.blit(text, (350, 200))
            screen.blit(text1, (350, 250))
            screen.blit(text2, (350, 300))
            screen.blit(text3, (350, 350))
            pygame.display.flip()
            while zastavene == True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        zastavene = False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        xpsova, ypsilonova = event.pos
                        if xpsova < 110 and xpsova > 10 and ypsilonova < 110 and ypsilonova > 10:
                            zastavene = False
                        if xpsova < 240 and xpsova > 60 and ypsilonova < 280 and ypsilonova > 200:

                            zastavene = False
                        if xpsova < 240 and xpsova > 60 and ypsilonova < 380 and ypsilonova > 300:
                            subprocess.call(['python', './menu.py'])
                            running = False
                            zastavene = False
                        if xpsova < 240 and xpsova > 60 and ypsilonova < 480 and ypsilonova > 400:
                            running = False
                            zastavene = False

        pygame.display.flip()

def main():
    pygame.init()
    pong()
    pygame.quit()

if __name__ == '__main__':
    main()
