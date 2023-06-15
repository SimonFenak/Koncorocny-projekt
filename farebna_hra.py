import random
import pygame
from pygame.locals import *
import mysql.connector
SIRKA = 14
VYSKA = 11

VELKOST = 60


FARBY = {
    0: (255, 0, 0),
    1: (0, 255, 0),
    2: (255, 255, 0),
    3: (0, 0, 255),
    4: (255, 0, 255),
    5: (0, 255, 255),
}

CISLA_FARIEB = tuple(FARBY.keys())



def vytvor_pole(): #Vytvorí pole s náhodnými farbami
    pole = []
    for _ in range(VYSKA):
        pole.append(random.choices(CISLA_FARIEB, k=SIRKA))
    return pole




def stvorec(x, y): #Vráti obdĺžnik pre dané súradnice
    return pygame.Rect(x * VELKOST, y * VELKOST, VELKOST, VELKOST)




def vykresli_pole(screen, pole): #Vykreslí pole na obrazovku
    for y, riadok in enumerate(pole):
        for x, index_farby in enumerate(riadok):
            pygame.draw.rect(screen, FARBY[index_farby], stvorec(x, y))

def vylej_farbu(pole, farba_pred, farba, x, y): #Vyfarbuje pole
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
    if not (0 <= x < SIRKA and 0 <= y < VYSKA):  # opravena podmienka
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
                farba_pred = pole[0][0]
                if farba_pred != index_farby:
                    vylej_farbu2(pole, farba_pred, index_farby, 0, 0)






def zisti_koniec(pole):
    policko = pole[0][0]
    for sirka in range(SIRKA):
        for vyska in range(VYSKA):
            if policko!=pole[vyska][sirka]:
                return
    return 1

def vyhodnotenie(kroky):
    kroky=str(kroky)
    return kroky
def hra():
    kroky = 0
    screen = pygame.display.set_mode((SIRKA * VELKOST, VYSKA * VELKOST))
    pole = vytvor_pole()
    clock = pygame.time.Clock()
    vykresli_pole(screen, pole)
    pygame.display.flip()
    running = True
    tlacitko = pygame.image.load("menu-bar.png")
    mensie = pygame.transform.scale(tlacitko, (50, 50))
    zastavene = True
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
    text = nadpis.render("Farebné Štvorce!!", True, (255, 255, 255))
    text1 = font.render("Vitajte v Farebnej hre je určená ", True, (255, 255, 255))
    text2 = font.render("pre jedného hráčov. Úlohou je aby", True, (255, 255, 255))
    text3 = font.render("hráč vymaľoval celé pole jednou farbou.", True, (255, 255, 255))
    koniec = nadpis.render("Koniec!", True, (255,255,255))
    hodnot=False
    totalitnykonec=False
    pygame.display.flip()
    while running==True:
        clock.tick(60)
        if zastavene == False:
            screen.blit(mensie, (10, 10))
            vykresli_pole(screen, pole)
            screen.blit(mensie, (10, 10))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    if event.type == pygame.QUIT:
                        file = open("prihl.txt", "w")
                        file.close()
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    xpsova, ypsilonova = event.pos
                    mys_klik(pygame.mouse.get_pos(), pole)
                    if zisti_koniec(pole) == 1:
                        vyhodnotenie(kroky)
                        hodnot=True
                        running=False
                        break
                    screen.blit(mensie, (10, 10))
                    if xpsova < 60 and xpsova > 10 and ypsilonova < 60 and ypsilonova > 10:
                        zastavene = True
                        break
                    pygame.display.flip()
                    kroky+=1
            stlacene = pygame.key.get_pressed()
            if stlacene[pygame.K_ESCAPE]:
                zastavene = True
                pygame.time.wait(500)

            clock.tick(60)
        else:
            pygame.draw.rect(screen, (79, 90, 255), (330, 155, 510, 310))
            pygame.draw.rect(screen, (41, 47, 133), (335, 160, 500, 300))
            screen.blit(sidemen, (0, 0))
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
                        if event.type == pygame.QUIT:
                            file = open("subor.txt", "w")
                            file.close()
                        running = False
                        zastavene = False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        xpsova, ypsilonova = event.pos
                        if xpsova < 60 and xpsova > 10 and ypsilonova < 60 and ypsilonova > 10:
                            zastavene = False
                        if xpsova < 240 and xpsova > 60 and ypsilonova < 280 and ypsilonova > 200:
                            zastavene = False
                        if xpsova < 240 and xpsova > 60 and ypsilonova < 380 and ypsilonova > 300:
                            running = False
                            zastavene = False
                            import minihryexe
                            minihryexe.main()
                        if xpsova < 240 and xpsova > 60 and ypsilonova < 480 and ypsilonova > 400:
                            running = False
                            zastavene = False
                            pygame.quit()
                stlacene1 = pygame.key.get_pressed()
                if stlacene1[pygame.K_ESCAPE]:
                    zastavene = False
                    pygame.time.wait(500)

    if hodnot == True:
        while totalitnykonec==False:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    if event.type == pygame.QUIT:
                        file = open("prihl.txt", "w")
                        file.write("")
                        file.close()
                    totalitnykonec= True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    xpsova, ypsilonova = event.pos
                    if xpsova < 500 and xpsova > 320 and ypsilonova < 560 and ypsilonova > 505:
                        totalitnykonec=True
                    if xpsova < 500 and xpsova > 320 and ypsilonova < 490 and ypsilonova > 430:
                        import minihryexe
                        minihryexe.main()
                    if xpsova < 500 and xpsova > 320 and ypsilonova < 420 and ypsilonova > 360:
                        main()
            pygame.draw.rect(screen, (79, 90, 255), (170, 155, 510, 410))
            pygame.draw.rect(screen, (41, 47, 133), (175, 160, 500, 400))
            cislo = nadpis.render("Počet tvojich krokov " + vyhodnotenie(kroky), True, (255, 255, 255))
            screen.blit(cislo, (230, 300))
            screen.blit(koniec, (350, 250))
            screen.blit(startmen, (320, 350))
            screen.blit(minihrymen, (320, 420))
            screen.blit(ukoncitmen, (320, 490))
            pygame.display.flip()
            subor = open("prihl.txt", "r")
            cita = subor.read()
            meno = cita
            if len(cita) != 0:
                # Pripojenie k databáze
                db = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="pythonik"
                )
                cursor = db.cursor()
                query = "SELECT fareb FROM second WHERE meno = %s"
                values = (meno,)
                cursor.execute(query, values)
                result = cursor.fetchone()

                if int(vyhodnotenie(kroky)) < int(result[0]):
                    query = "UPDATE second SET fareb = %s WHERE meno = %s"
                    values = (int(vyhodnotenie(kroky)), meno)
                    cursor.execute(query, values)
                db.commit()

    clock.tick(60)
    pygame.display.flip()


def main():
    pygame.init()
    hra()
    pygame.quit()




main()
