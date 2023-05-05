import random
import pygame


SIRKA = 20
VYSKA = 15

VELKOST = 40

FARBY = {
    0: (255, 0, 0),
    1: (0, 255, 0),
    2: (255, 255, 0),
    3: (0, 0, 255),
    4: (255, 0, 255),
    5: (0, 255, 255),
}

CISLA_FARIEB = tuple(FARBY.keys())

tahy = []

def vytvor_pole():
    pole = []
    for _ in range(VYSKA):
        pole.append(random.choices(CISLA_FARIEB, k=SIRKA))
    return pole


def stvorec(x, y):
    return pygame.Rect(x * VELKOST, y * VELKOST, VELKOST, VELKOST)


def vykresli_pole(screen, pole):
    for y, riadok in enumerate(pole):
        for x, index_farby in enumerate(riadok):
            pygame.draw.rect(screen, FARBY[index_farby], stvorec(x, y))

def vylej_farbu(pole, farba_pred, farba, x, y):
    if farba_pred != pole[y][x]:
        return
    pole[y][x] = farba
    if y > 0:
        vylej_farbu(pole, farba_pred, farba, x, y - 1)
    if y < VYSKA - 1:
        vylej_farbu(pole, farba_pred, farba, x, y + 1)
    if x > 0:
        vylej_farbu(pole, farba_pred, farba, x - 1, y)
    if x < SIRKA - 1:
        vylej_farbu(pole, farba_pred, farba, x + 1, y)


def vylej_farbu2(pole, farba_pred, farba, x, y):
    if not (0 <= x < SIRKA and 0 <= y < VYSKA):  # oprevena podmienka
        return
    if farba_pred != pole[y][x]:
        return
    pole[y][x] = farba
    for dx, dy in ((0, -1), (0, 1), (-1, 0), (1, 0)):
        vylej_farbu2(pole, farba_pred, farba, x + dx, y + dy)


def mys_klik(mys_pos, pole):
    for y, riadok in enumerate(pole):
        for x, index_farby in enumerate(riadok):
            if stvorec(x, y).collidepoint(mys_pos):
                farba_pred = pole[0][0]  # pred zavolanim vyliatia farby,
                # kontrolujem, ci som neklikol na tu istu farbu
                if farba_pred != index_farby:
                    vylej_farbu2(pole, farba_pred, index_farby, 0, 0)


def hra():
    screen = pygame.display.set_mode((SIRKA * VELKOST, VYSKA * VELKOST))
    pole = vytvor_pole()
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mys_klik(pygame.mouse.get_pos(), pole)
                tahy.append(1)
        vykresli_pole(screen, pole)
        pygame.display.flip()
        if pole[0] and pole[1] and pole[2] and pole[3] and pole[4] and pole[5] and pole[6] and pole[7] and pole[8] and pole[9] and pole[10] and pole[11] and pole[12] and pole[13] and pole[14] == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] or pole[0] and pole[1] and pole[2] and pole[3] and pole[4] and pole[5] and pole[6] and pole[7] and pole[8] and pole[9] and pole[10] and pole[11] and pole[12] and pole[13] and pole[14] == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1] or pole[0] and pole[1] and pole[2] and pole[3] and pole[4] and pole[5] and pole[6] and pole[7] and pole[8] and pole[9] and pole[10] and pole[11] and pole[12] and pole[13] and pole[14] == [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2] or pole[0] and pole[1] and pole[2] and pole[3] and pole[4] and pole[5] and pole[6] and pole[7] and pole[8] and pole[9] and pole[10] and pole[11] and pole[12] and pole[13] and pole[14] == [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3] or pole[0] and pole[1] and pole[2] and pole[3] and pole[4] and pole[5] and pole[6] and pole[7] and pole[8] and pole[9] and pole[10] and pole[11] and pole[12] and pole[13] and pole[14] == [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4] or pole[0] and pole[1] and pole[2] and pole[3] and pole[4] and pole[5] and pole[6] and pole[7] and pole[8] and pole[9] and pole[10] and pole[11] and pole[12] and pole[13] and pole[14] == [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]:
            return
        clock.tick(60)


def main():
    pocitadlo = 0
    pygame.init()
    hra()
    for _ in tahy:
        pocitadlo += 1
    return pocitadlo


print(f"Zabralo ti to:{main()}ťahov")
pygame.quit()
