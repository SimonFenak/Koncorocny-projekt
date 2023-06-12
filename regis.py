import pygame
from pygame.locals import *
import mysql.connector
import hashlib

def hash_password(password):
    # Vytvorenie objektu pre hashovanie
    hash_object = hashlib.sha256()
    # Konverzia hesla na bajty
    password_bytes = password.encode('utf-8')
    # Aktualizácia objektu hashu s heslom
    hash_object.update(password_bytes)
    # Získanie zahashovaného reťazca
    hashed_password = hash_object.hexdigest()
    return hashed_password

def check_username(username, hashed_password, cursor, db):
    cursor = db.cursor()
    if db is not None:
        query = "SELECT * FROM second WHERE meno = %s"
        cursor.execute(query, (username,))
        result = cursor.fetchone()
        cursor.close()
        if result:
            return True
        else:
            return False
    else:
        print("Chyba: Nie je pripojené k databáze.")
        return False

def main():

    # Inicializácia Pygame
    pygame.init()

    # Definovanie farieb
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    # Vytvorenie okna
    window_width, window_height = 840, 660
    window = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption('Formulár')

    back_to_menu = pygame.image.load("hlavnemenu.png").convert_alpha()
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
    warningovanie=False
    overenie=False
    uspech=False
    font_nadpis= pygame.font.Font(None, 72)
    f_nick = pygame.font.Font(None, 45)
    warning = f_nick.render("Zlé prihlasovacie údaje!", True, (255, 255, 255))
    over=f_nick.render("Prihlasovacie meno už existuje.", True, (255, 255, 255))
    uspes_text=f_nick.render("Úspešne si sa registroval", True, (255, 255, 255))
    while running:
        back_to_menu_rect = window.blit(back_to_menu, (350, 500))
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

            elif event.type == KEYDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if back_to_menu_rect.collidepoint(mouse_pos):
                    import menuexe
                    menuexe.main_menu()
                    pygame.quit()
                if event.key == K_RETURN:
                    if  input_text1 == '' or input_text2 == '':
                        warningovanie=True
                        overenie=False
                        continue
                    #Overenie mena
                    username = input_text1
                    password = input_text2
                    hashed_password = hash_password(password)
                    exists = check_username(username, hashed_password, cursor, db)
                    if exists:
                        overenie=True
                        warningovanie = False
                        input_text2 = ''
                        continue
                    overenie=False
                    # Vloženie informácií do databázy
                    warningovanie = False
                    query = "INSERT INTO second (meno, heslo, bludisko, fareb) VALUES (%s, %s, %s, %s)"
                    values = (input_text1, hashed_password, 100.0, 50)
                    cursor.execute(query, values)
                    db.commit()
                    uspech=True
                    input_text1 = ''
                    input_text2 = ''

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
                if xpsova < 504 and xpsova > 350 and ypsilonova < 577 and ypsilonova > 500:
                    import menuexe
                    menuexe.main_menu()

        # Vykreslenie pozadia
        window.fill(WHITE)

        # Vykreslenie textových políčok
        background = window.blit(banner, (0, 0))

        nadpis = font_nadpis.render("Registruj sa!!", True, (255, 255, 255))
        nick = f_nick.render("Nick:", True, (255, 255, 255))
        heslo = f_nick.render("Heslo:", True, (255, 255, 255))
        window.blit(nadpis, (270, 200))
        window.blit(nick, (200, 310))
        window.blit(heslo, (200, 390))
        back_to_menu_rect = window.blit(back_to_menu, (350, 500))
        if warningovanie==True:
            window.blit(warning, (260, 260))
        if overenie == True:
            window.blit(over, (240, 260))
        if uspech==True:
            window.blit(uspes_text, (240, 260))

        pygame.draw.rect(window, (255,255,255), input_rect1, 2)
        pygame.draw.rect(window, (255,255,255), input_rect2, 2)

        font = pygame.font.Font(None, 52)

        text_surface1 = font.render(input_text1, True, (255,255,255))
        text_surface2 = font.render(input_text2, True, (255,255,255))

        window.blit(text_surface1, (input_rect1.x + 5, input_rect1.y + 5))
        window.blit(text_surface2, (input_rect2.x + 5, input_rect2.y + 5))
        pygame.display.update()

    # Uzavretie spojenia s databázou
    cursor.close()
    db.close()

    # Ukončenie Pygame
    pygame.quit()
main()