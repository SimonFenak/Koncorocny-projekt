import pygame
from pygame import mixer
import time
from pygame.locals import *
import mysql.connector
def kresli(screen,panak,labyrint):
    screen.fill((0, 0, 0))
    for i in range(len(labyrint)):
        for j in range(len(labyrint[i])):
            if labyrint[i][j] == "#":
                pygame.draw.rect(screen,(255, 255, 50), pygame.Rect(j * 20,i * 20,20,20))
    pygame.draw.circle(screen, (0,0,255), (panak[0]*20+10,panak[1]*20+10), 10)
    pygame.display.flip()  #komentar
def main():
    panak = [1,1]
    mixer.init()
    pygame.init()
    sound = mixer.Sound("ough-47202.mp3")
    screen = pygame.display.set_mode((840, 660))
    f = open("labyrint.txt", "r")
    labyrint = f.read().split("\n")
    running= True
    cas =  time.time()
    tlacitko = pygame.image.load("menu-bar.png")
    mensie = pygame.transform.scale(tlacitko, (50, 50))
    zastavene = False
    minihry = pygame.image.load("minihry1.png").convert_alpha()
    minihrymen = pygame.transform.scale(minihry, (180, 80))
    ukoncit = pygame.image.load("ukoncit1.png").convert_alpha()
    ukoncitmen = pygame.transform.scale(ukoncit, (180, 80))
    start = pygame.image.load("start.png").convert_alpha()
    startmen = pygame.transform.scale(start, (180, 80))
    side = pygame.image.load("sidebar.png").convert_alpha()
    sidemen = pygame.transform.scale(side, (300, 660))
    font = pygame.font.Font(None, 36)
    vyhodnotenie=False
    totalitnykonec=False
    nadpis = pygame.font.Font(None, 50)
    text = nadpis.render("Bludisko!", True, (255, 0, 0))
    text1 = font.render("Vitajte v hre blusko hra je určená ", True, (255, 0, 0))
    text2 = font.render("pre jedného hráča. Ulohou je aby", True, (255, 0, 0))
    text3 = font.render("sa hráč dostal na koniec bludiska.", True, (255, 0, 0))
    koniec = nadpis.render("Koniec!", True, (255, 255, 255))
    while running==True:
        cas = time.time()
        for event in pygame.event.get():
            pressed = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                running = False
                file = open("prihl.txt", "w")
                file.write("")
                file.close()
        if pressed[pygame.K_RIGHT]:
            if labyrint[panak[1]][panak[0]+1]=="#":sound.play()
            elif labyrint[panak[1]][panak[0]+1]=="U":
                vyhodnotenie=True
                zastavene=True
            else: panak[0] += 1
            time.sleep(0.1)
        if pressed[pygame.K_LEFT]:
            if labyrint[panak[1]][panak[0] - 1] == "#":
                sound.play()
            elif labyrint[panak[1] + 1][panak[0]] == "U":
                Vyhodnotenie=True
            else:
                panak[0] -= 1
            time.sleep(0.1)
        if pressed[pygame.K_UP]:
            if labyrint[panak[1]-1][panak[0]] == "#":
                sound.play()
            elif labyrint[panak[1] + 1][panak[0]] == "U":
                Vyhodnotenie = True
            else:
                panak[1] -= 1
            time.sleep(0.1)
        if pressed[pygame.K_DOWN]:
            if labyrint[panak[1]+1][panak[0]] == "#":
                sound.play()
            elif labyrint[panak[1]+1][panak[0]] == "U":
                Vyhodnotenie = True
            else:
                panak[1] += 1
            time.sleep(0.1)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            xpsova, ypsilonova = event.pos
            if xpsova < 110 and xpsova > 10 and ypsilonova < 110 and ypsilonova > 10:
                zastavene = True
        stlacene = pygame.key.get_pressed()
        if stlacene[pygame.K_ESCAPE]:
            zastavene = True
        if zastavene == False and vyhodnotenie==False:
            kresli(screen,panak,labyrint)
        elif zastavene==True and vyhodnotenie==False:
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
                            import minihryexe
                            minihryexe.main()
                            running = False
                            zastavene = False
                        if xpsova < 240 and xpsova > 60 and ypsilonova < 480 and ypsilonova > 400:
                            running = False
                            zastavene = False
                            pygame.quit()
                    stlacene1 = pygame.key.get_pressed()
                    if stlacene1[pygame.K_ESCAPE]:
                        zastavene = False

        else:
            casik=cas/100000000
            casik=round(casik,2)
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
                query = "SELECT bludisko FROM second WHERE meno = %s"
                values = (meno,)
                cursor.execute(query, values)
                result = cursor.fetchone()

                if casik < int(result[0]) or int(result[0])==0.0:
                    query = "UPDATE second SET bludisko = %s WHERE meno = %s"
                    values = (casik, meno)
                    cursor.execute(query, values)
                db.commit()
            while totalitnykonec == False:

                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        file = open("prihl.txt", "w")
                        file.write("")
                        file.close()
                        totalitnykonec = True
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        xpsova, ypsilonova = event.pos
                        if xpsova < 500 and xpsova > 320 and ypsilonova < 560 and ypsilonova > 505:
                            totalitnykonec = True
                        if xpsova < 500 and xpsova > 320 and ypsilonova < 490 and ypsilonova > 430:
                            import minihryexe
                            minihryexe.main()
                        if xpsova < 500 and xpsova > 320 and ypsilonova < 420 and ypsilonova > 360:
                            main()
                cislo = nadpis.render("Tvoj čas:"+str(casik) , True, (255, 0, 0))
                screen.blit(cislo, (230, 300))
                screen.blit(koniec, (350, 250))
                screen.blit(startmen, (320, 350))
                screen.blit(minihrymen, (320, 420))
                screen.blit(ukoncitmen, (320, 490))
                pygame.display.flip()
            pygame.display.flip()
main()
