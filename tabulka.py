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


query = "SELECT meno,bludisko  FROM main ORDER BY bludisko "
cursor.execute(query)
bludiskores = cursor.fetchmany(3)
cursor.fetchall()

query = "SELECT meno,fareb FROM main ORDER BY fareb "
cursor.execute(query)
farebres = cursor.fetchmany(3)
cursor.fetchall()

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

        games_menu_rect = screen.blit(games_menu, (320, 550))
        pygame.display.update()


def main_menu():
    menu = True
    prihlaseny = False
    clock = pygame.time.Clock()
    banner = pygame.image.load("background.jpg").convert_alpha()
    background = screen.blit(banner, (0, 0))
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
