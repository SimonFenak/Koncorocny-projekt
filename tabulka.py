import pygame
from pygame.locals import *
import mysql.connector
pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)

# SCREEN
SCREEN_WIDTH = 840
SCREEN_HEIGHT = 660
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# Pripojenie k databáze
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="pythonik"
)
cursor = db.cursor()

query = "SELECT meno, raketka FROM main ORDER BY raketka DESC LIMIT 3"
cursor.execute(query)
raketkares = cursor.fetchmany(3)
cursor.fetchall()
raketprv=raketkares[0]
raketdru=raketkares[1]
rakettre=raketkares[2]

query = "SELECT meno,bludisko  FROM main ORDER BY bludisko DESC"
cursor.execute(query)
bludiskores = cursor.fetchmany(3)
cursor.fetchall()
bludisprv=bludiskores[0]
bludisdru=bludiskores[1]
bludistre=bludiskores[2]

query = "SELECT meno,fareb FROM main ORDER BY fareb "
cursor.execute(query)
farebres = cursor.fetchmany(3)
cursor.fetchall()
farebprv=farebres[0]
farebdru=farebres[1]
farebtre=farebres[2]
def get_button(prihlaseny):
    games_menu = pygame.image.load("minihry1.png").convert_alpha()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                file = open("prihl.txt", "w")
                file.write("")
                file.close()
                return 0
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if games_menu_rect.collidepoint(mouse_pos):
                    return "Minihry"
                else:
                    break

        games_menu_rect = screen.blit(games_menu, (50, 550))
        pygame.display.update()


def main_menu():
    menu = True
    prihlaseny = False
    clock = pygame.time.Clock()
    banner = pygame.image.load("background.jpg").convert_alpha()
    tabulka=pygame.image.load("table.png").convert_alpha()
    nadpis = pygame.font.Font(None, 50)
    raketka =nadpis.render("Raketka", True, (255, 255, 255))
    bludisko = nadpis.render("Bludisko", True, (255, 255, 255))
    fareb= nadpis.render("Štvorce", True, (255, 255, 255))
    raketv1=nadpis.render(str(raketprv).strip('('')'','),True,(255,255,255))
    raketv2 = nadpis.render(str(raketdru).strip('('')'','), True, (255, 255, 255))
    raketv3 = nadpis.render(str(rakettre).strip('('')'','), True, (255, 255, 255))
    bludv1 = nadpis.render(str(bludisprv).strip('('')'','),True,(255,255,255))
    bludv2 = nadpis.render(str(bludisdru).strip('('')'','), True, (255, 255, 255))
    bludv3 = nadpis.render(str(bludistre).strip('('')'','), True, (255, 255, 255))
    farebv1 = nadpis.render(str(farebprv).strip('('')'','), True, (255, 255, 255))
    farebv2 = nadpis.render(str(farebdru).strip('('')'','), True, (255, 255, 255))
    farebv3 = nadpis.render(str(farebtre).strip('('')'','), True, (255, 255, 255))
    tabulkaupr = pygame.transform.scale(tabulka, (300, 280))
    background = screen.blit(banner, (0, 0))
    screen.blit(tabulkaupr,(80,70))
    screen.blit(raketv1,(100,165))
    screen.blit(raketv2, (100, 235))
    screen.blit(raketv3, (100, 285))
    screen.blit(farebv1, (480, 165))
    screen.blit(farebv2, (480, 235))
    screen.blit(farebv3, (480,285 ))
    screen.blit(bludv1, (290, 400))
    screen.blit(bludv2, (290, 460))
    screen.blit(bludv3, (290, 520))
    screen.blit(tabulkaupr, (460, 70))
    screen.blit(tabulkaupr, (270, 300))
    screen.blit(raketka,(160,30))
    screen.blit(fareb, (540, 30))
    screen.blit(bludisko, (350, 580))
    pygame.display.flip()
    clock.tick(60)

    while menu:
        button = get_button(prihlaseny)
        if button==0:
            menu=False
        print(button)
        pygame.display.flip()
        clock.tick(60)

main_menu()
