import pygame
import random

WIDTH = 850
HEIGHT = 660
BALL_SIZE = 20
BALL_SPEED = 4


def stvorec(x, y):
    return pygame.Rect(int(x), int(y), BALL_SIZE, BALL_SIZE)


def plosky(x, y):
    return pygame.Rect(int(x), int(y), 10, 100)


def pong():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    my_font = pygame.font.SysFont("Consolas", 15)
    clock = pygame.time.Clock()
    running = True
    ball_x = 200
    ball_y = 200
    ploska1_y = HEIGHT / 2 - 50
    ploska1_x = 0
    ploska2_y = HEIGHT / 2 - 50
    ploska2_x = WIDTH - 10
    hrac1_body = 0
    hrac2_body = 0
    movement = [1, 1]
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


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
        if pressed[pygame.K_SPACE]:
            ball_x = WIDTH / 2
            ball_y = HEIGHT / 2
            movement = [random.choice([-1, 1]), random.choice([1, -1])]


        if ball_x < 0:
            movement = [0, 0]
            hrac1_body += 1
        if ball_y < 0:
            movement[1] = 1
        if ball_x > (WIDTH - BALL_SIZE):
            movement = [0, 0]
            hrac2_body += 1
        if ball_y > (HEIGHT - BALL_SIZE):
            movement[1] = -1
        ball_x += BALL_SPEED * movement[0]
        ball_y += BALL_SPEED * movement[1]
        screen.fill((0,0,0))

        lopta = pygame.draw.rect(screen, (255, 255, 255), stvorec(ball_x, ball_y))

        hrac1 = pygame.draw.rect(screen, (255,255,255), plosky(ploska1_x, ploska1_y))
        hrac2 = pygame.draw.rect(screen, (255, 255, 255), plosky(ploska2_x, ploska2_y))

        if pygame.Rect.colliderect(lopta, hrac1):
            movement[0] = 1
        if pygame.Rect.colliderect(lopta, hrac2):
            movement[0] = - 1

        text_surface = my_font.render(f"{hrac1_body} : {hrac2_body}", True, (255, 0, 0))
        screen.blit(text_surface, ((WIDTH - text_surface.get_width()) / 2, 0))

        pygame.display.flip()
        clock.tick(60)


def main():
    pygame.init()
    pong()
    pygame.quit()

if __name__ == '__main__':
    main()
