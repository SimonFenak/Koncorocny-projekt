import random
import pygame
import time
from pygame.locals import *
import mysql.connector
GRAVITY=0.04
SIRKA = 840
VYSKA = 660
VELKOST = 60
bullkit=[]
ACCEL_Y=0.1
ACCEL_X=0.07
pocet = 0
cas = time.time()

def stvorec(x, y):
    return pygame.Rect(int(x) , int(y) , VELKOST, VELKOST)

def plocha(poziciar):
    return pygame.Rect(poziciar, VYSKA-5, 50,5 )

def volny_pad(pocet,cas):
    poziciar = random.randint(0, 790)
    color = (0, 0, 255)
    rychlost_y = 0.0
    konec=0
    rychlost_x = 0.0
    pos_x=SIRKA/2-VELKOST/2
    pos_y=VYSKA-VELKOST
    screen = pygame.display.set_mode((SIRKA, VYSKA))
    my_font=pygame.font.SysFont("Arial",25)
    clock = pygame.time.Clock()
    running = True
    zastavene= False
    tlacitko = pygame.image.load("menu-bar.png")
    mensie = pygame.transform.scale(tlacitko, (50, 50))
    minihry = pygame.image.load("minihry1.png").convert_alpha()
    minihrymen = pygame.transform.scale(minihry, (180, 80))
    ukoncit = pygame.image.load("ukoncit1.png").convert_alpha()
    ukoncitmen = pygame.transform.scale(ukoncit, (180, 80))
    start = pygame.image.load("start.png").convert_alpha()
    startmen = pygame.transform.scale(start, (180, 80))
    side = pygame.image.load("sidebar.png").convert_alpha()
    sidemen = pygame.transform.scale(side, (300, 660))
    raketka = pygame.image.load("raketkabezohna.png").convert_alpha()
    upravenaraketka = pygame.transform.scale(raketka, (60, 60))
    raketkaohen = pygame.image.load("raketkazohonom.png").convert_alpha()
    upravenaraketkaohen = pygame.transform.scale(raketkaohen, (60, 60))
    font = pygame.font.Font(None, 36)
    hodnot=False
    nadpis = pygame.font.Font(None, 50)
    koniec = nadpis.render("Koniec!", True, (255, 255, 255))
    totalitnykonec=False
    maly=pygame.font.Font(None, 25)
    nadpis = pygame.font.Font(None, 50)
    text = nadpis.render("Raketka!!", True, (255, 255, 255))
    text1 = font.render("Vitajte v hre raketka hra je určená ", True, (255, 255, 255))
    text2 = font.render("pre jedného hráča. Ulohou je dopraviť", True, (255, 255, 255))
    text3 = font.render("raketku na bielu plošinku čo najviackrát", True, (255, 255, 255))
    text5 = font.render("za dvadsať sekúnd!", True, (255, 255, 255))
    text4 = maly.render("(Hru pauzneš pomocou ESC)", True, (255, 255, 255))
    while running:
        caspotom = time.time()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                file = open("prihl.txt", "w")
                file.write("")
                file.close()
                running = False


            stlacenne = pygame.key.get_pressed()
            if stlacenne[pygame.K_ESCAPE]:
                zastavene = True

                print("stavujem")
                pygame.time.wait(500)
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            rychlost_y +=ACCEL_Y
            screen.blit(upravenaraketkaohen, (pos_x, pos_y))
            pygame.display.flip()
        if pressed[pygame.K_RIGHT] and konec==0:
            rychlost_x += ACCEL_X
        if pressed[pygame.K_LEFT] and konec==0:
            rychlost_x -= ACCEL_X



        if zastavene== False:
            pos_x += rychlost_x
            pos_y-=rychlost_y
            rychlost_y-=GRAVITY
            if pos_y>=VYSKA-VELKOST-1 and int(rychlost_y)<-1:
                print("Ši še rozbil")
                rychlost_x=0
                rychlost_y=0
                konec=1
                screen.blit(upravenaraketka, (pos_x, pos_y))
                pygame.display.flip()
                pygame.time.wait(500)
            if konec==1:
                text_surface = my_font.render("ROZBITY ŠI", False, (255, 127, 0))
                screen.blit(text_surface, (0, 0))
                pos_y=VYSKA-VELKOST
                pos_x=pos_x
                rychlost_x = 0
                rychlost_y = 0
                main(pocet,cas)
            if pos_y > VYSKA-VELKOST:
                pos_y=VYSKA-VELKOST
                rychlost_y=0
                rychlost_x/=1.2
            if pos_y <= 0:
                rychlost_y=-0.2
                pos_y=0
            if pos_x <=0 :
                pos_x = 0
                rychlost_x =0
            if pos_x>=SIRKA-VELKOST:
                rychlost_x -= rychlost_x+1

                pos_x=SIRKA-VELKOST
            if pos_x >= poziciar-50 and pos_x <poziciar+50 and pos_y>595:
                pocet += 1
                if caspotom-cas>20:
                    hodnot=True
                    running=False
                pos_y=625
                rychlost_y=0
                konec=1

            screen.fill((0,0,0))
            text_surface=my_font.render(f"SPEED X:{rychlost_x:6.1f} Y:{rychlost_y:6.1f}",False,(255,127,0))
            vyhri = my_font.render(f"Počet výhier:{pocet}", False, (255, 255, 255))
            kolkocas=font.render(f"Tvoj čas:{caspotom-cas:6.1f}", False, (255, 255, 255))
            screen.blit(kolkocas,(650,5))
            screen.blit(vyhri, (700, 630))
            screen.blit(text_surface,(0,0))
            screen.blit(upravenaraketka, (pos_x, pos_y))
            pygame.draw.rect(screen, (255,255,255), plocha(poziciar))
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
            screen.blit(text5, (350, 400))
            screen.blit(text4, (350, 430))
            pygame.display.flip()
            while zastavene == True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        file = open("prihl.txt", "w")
                        file.write("")
                        file.close()
                        running = False
                        zastavene = False
                    stlacene1 = pygame.key.get_pressed()
                    if stlacene1[pygame.K_ESCAPE]:
                        zastavene = False
                        print("ZASTAVUJEME")

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        xpsova, ypsilonova = event.pos
                        if xpsova < 60 and xpsova > 10 and ypsilonova < 60 and ypsilonova > 10:
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
                pygame.display.flip()
    if hodnot==True:
        subor=open("prihl.txt","r")
        cita=subor.read()
        meno=cita
        if len(cita)!=0:
            # Pripojenie k databáze
            db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="pythonik"
            )
            cursor = db.cursor()
            query = "SELECT raketka FROM main WHERE meno = %s"
            values = (meno,)
            cursor.execute(query, values)
            result = cursor.fetchone()

            if pocet>int(result[0]):
                query = "UPDATE main SET raketka = %s WHERE meno = %s"
                values = (pocet,meno)
                cursor.execute(query, values)
            db.commit()
        while totalitnykonec==False:
            for event in pygame.event.get():
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
                        pocet = 0
                        cas = time.time()
                        main(pocet, cas)
            cislo = nadpis.render("Počet úspešnych pokusov:" + str(pocet), True, (255, 255, 255))
            screen.blit(cislo, (200, 300))
            screen.blit(koniec, (350, 250))
            screen.blit(startmen, (320, 350))
            screen.blit(minihrymen, (320, 420))
            screen.blit(ukoncitmen, (320, 490))
            pygame.display.flip()
        pygame.display.flip()
def main(pocet,cas):
    pygame.init()
    pygame.font.init()
    volny_pad(pocet,cas)
    pygame.quit()
main(pocet,cas)
