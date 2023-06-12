import pygame
from pygame.locals import *
import mysql.connector
import hashlib


def hash_password(password):
    # Hash hesla pomocou SHA-256
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password


def prihlasenie(username, password, cursor,db):
    if db is not None:
        query = "SELECT * FROM second WHERE meno = %s AND heslo = %s"#tu najdi chybu toto treba zmeniť bujaku heslo =...
        cursor.execute(query, (username, password))
        result = cursor.fetchone()
        if result:
            return result
        else:
            return False

def main():

    # Inicializácia Pygame
    pygame.init()
    prmeno = ''

    # Definovanie farieb
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    # Vytvorenie okna
    window_width, window_height = 840, 660
    window = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption('Formulár')

    back_to_menu = pygame.image.load("hlavnemenu.png").convert_alpha()
    to_register_menu = pygame.image.load("register.png").convert_alpha()

    # Vytvorenie textových políčok
    input_rect1 = pygame.Rect(320, 300, 230, 50)
    input_active1 = False
    input_text1 = ''

    input_rect2 = pygame.Rect(320, 380, 230, 50)
    input_active2 = False
    input_text2 = ''

    # Pripojenie k databáze
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="pythonik"
    )
    cursor = db.cursor()
    banner = pygame.image.load("background.jpg").convert_alpha()

    # Hlavná slučka hry
    running = True
    warningovanie = False
    font_nadpis = pygame.font.Font(None, 72)
    f_nick = pygame.font.Font(None, 45)
    warning = f_nick.render("Zlé prihlasovacie údaje!", True, (255, 255, 255))

    while running:
        back_to_menu_rect = window.blit(back_to_menu, (170, 500))
        to_register_menu_rect = window.blit(to_register_menu, (470,500))

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if back_to_menu_rect.collidepoint(mouse_pos):
                    import menuexe
                    menuexe.main_menu()
                if to_register_menu_rect.collidepoint(mouse_pos):
                    import regis
                if event.key == K_RETURN:
                    if input_text1 == '' or input_text2 == '':
                        warningovanie = True
                        continue
                    # Overenie mena a hesla
                    username = input_text1
                    password = input_text2
                    hashed_password = hash_password(password)
                    exists = prihlasenie(username, hashed_password, cursor,db)
                    if exists:
                        print("Prihlásenie úspešné.")
                        input_text1 = ''
                        input_text2 = ''
                        prmeno = exists[0]
                        subor = open("prihl.txt", "w")
                        subor.write(prmeno)
                        subor.close()
                        warningovanie = False
                        import menuexe
                        menuexe.main_menu()
                        pygame.quit()
                        continue
                    else:
                        print("Nesprávne prihlasovacie údaje.")
                        input_text2 = ''
                        continue
                elif event.key == K_BACKSPACE:
                    if input_active1:
                        input_text1 = input_text1[:-1]
                    elif input_active2:
                        input_text2 = input_text2[:-1]
                else:
                    if input_active1:
                        input_text1 += event.unicode
                    elif input_active2:
                        input_text2 += event.unicode
            elif event.type == MOUSEBUTTONDOWN:
                if input_rect1.collidepoint(event.pos):
                    input_active1 = True
                    input_active2 = False
                elif input_rect2.collidepoint(event.pos):
                    input_active1 = False
                    input_active2 = True
                else:
                    input_active1 = False
                    input_active2 = False
                xpsova, ypsilonova = event.pos
                if xpsova < 324 and xpsova > 170 and ypsilonova < 577 and ypsilonova > 500:
                    import menuexe
                    menuexe.main_menu()
                if xpsova < 654 and xpsova > 470 and ypsilonova < 647 and ypsilonova > 500:
                    import regis
                    regis.main()
                    pygame.quit()

        # Vykreslenie pozadia
        window.fill(WHITE)

        # Vykreslenie textových políčok
        background = window.blit(banner, (0, 0))
        nadpis = font_nadpis.render("Prihlásenie", True, (255, 255, 255))
        nick = f_nick.render("Nick:", True, (255, 255, 255))
        heslo = f_nick.render("Heslo:", True, (255, 255, 255))
        window.blit(nadpis, (290, 200))
        window.blit(nick, (200, 310))
        window.blit(heslo, (200, 390))
        back_to_menu_rect = window.blit(back_to_menu, (170, 500))
        to_register_menu_rect = window.blit(to_register_menu, (470,500))

        if warningovanie:
            window.blit(warning, (260, 260))

        pygame.draw.rect(window, (255, 255, 255), input_rect1, 2)
        pygame.draw.rect(window, (255, 255, 255), input_rect2, 2)

        font = pygame.font.Font(None, 52)
        text_surface1 = font.render(input_text1, True, (255, 255, 255))
        text_surface2 = font.render(input_text2, True, (255, 255, 255))
        window.blit(text_surface1, (input_rect1.x + 5, input_rect1.y + 5))
        window.blit(text_surface2, (input_rect2.x + 5, input_rect2.y + 5))
        pygame.display.update()

    # Uzavretie spojenia s databázou
    cursor.close()
    db.close()

    # Ukončenie Pygame
    pygame.quit()

main()
