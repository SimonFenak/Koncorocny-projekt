import random
import pygame
GRAVITY=0.04
SIRKA = 840
VYSKA = 660
VELKOST = 30
bullkit=[]
ACCEL_Y=0.1
ACCEL_X=0.07
poziciar = random.randint(0, 350)
somarina=[]
#pisem random komentar
for m in range(poziciar,poziciar+50):
    somarina.append(m)
def random():
    poziciar = random.randint(0, 350)

def stvorec(x, y):
    return pygame.Rect(int(x) , int(y) , VELKOST, VELKOST)

def plocha():
    return pygame.Rect(poziciar, VYSKA-5, 50,5 )
def volny_pad():
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
    zastavene= True
    tlacitko = pygame.image.load("menu-bar.png")
    mensie = pygame.transform.scale(tlacitko, (50, 50))
    minihry = pygame.image.load("minihry.png").convert_alpha()
    minihrymen = pygame.transform.scale(minihry, (180, 80))
    ukoncit = pygame.image.load("ukoncit.png").convert_alpha()
    ukoncitmen = pygame.transform.scale(ukoncit, (180, 80))
    start = pygame.image.load("start.png").convert_alpha()
    startmen = pygame.transform.scale(start, (180, 80))
    side = pygame.image.load("sidebar.png").convert_alpha()
    sidemen = pygame.transform.scale(side, (300, 660))
    font = pygame.font.Font(None, 36)
    nadpis = pygame.font.Font(None, 50)
    text = nadpis.render("Ping Pong!!", True, (255, 255, 255))
    text1 = font.render("Vitajte v hre ping pong hra je určená ", True, (255, 255, 255))
    text2 = font.render("pre dvoch hráčov. Ulohou je aby", True, (255, 255, 255))
    text3 = font.render("hráči dostali kocku za protivníka.", True, (255, 255, 255))
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            rychlost_y +=ACCEL_Y
        if pressed[pygame.K_RIGHT] and konec==0:
            rychlost_x += ACCEL_X
        if pressed[pygame.K_LEFT] and konec==0:
            rychlost_x -= ACCEL_X
        if pressed[pygame.K_ESCAPE] and konec==0:
            zastavene=True
            pygame.time.wait(500)


        if zastavene== False:
            pos_x += rychlost_x
            pos_y-=rychlost_y
            rychlost_y-=GRAVITY
            if pos_y>=VYSKA-VELKOST-1 and int(rychlost_y)<-1:
                print("Ši še rozbil")
                color=(255,0,0)
                rychlost_x=0
                rychlost_y=0
                konec=1
            if konec==1:
                text_surface = my_font.render("ROZBITY ŠI", False, (255, 127, 0))
                screen.blit(text_surface, (0, 0))
                pos_y=VYSKA-VELKOST
                pos_x=pos_x
                rychlost_x = 0
                rychlost_y = 0
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
            if pos_x >= poziciar-50 and pos_x <poziciar+50 and pos_y>625:
                pos_y=625
                rychlost_y=0
                konec=1
                print("Výhra")
                break
            screen.fill((0,0,0))
            text_surface=my_font.render(f"SPEED X:{rychlost_x:6.1f} Y:{rychlost_y:6.1f}",False,(255,127,0))
            screen.blit(text_surface,(0,0))
            pygame.draw.rect(screen,color,stvorec(pos_x,pos_y))
            pygame.draw.rect(screen, (255,255,255), plocha())
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
                stlacene1 = pygame.key.get_pressed()
                if stlacene1[pygame.K_ESCAPE]:
                    zastavene = False
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        zastavene = False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        xpsova, ypsilonova = event.pos
                        if xpsova < 60 and xpsova > 10 and ypsilonova < 60 and ypsilonova > 10:
                            zastavene = False
                        if xpsova < 240 and xpsova > 60 and ypsilonova < 280 and ypsilonova > 200:
                            zastavene = False


                        if xpsova < 240 and xpsova > 60 and ypsilonova < 380 and ypsilonova > 300:
                            import menu
                            menu.main_menu()
                            running = False
                            zastavene = False
                        if xpsova < 240 and xpsova > 60 and ypsilonova < 480 and ypsilonova > 400:
                            running = False
                            zastavene = False


        pygame.display.flip()



def main():
    pygame.init()
    pygame.font.init()
    volny_pad()
    pygame.quit()


main()