import pygame
from pygame .locals import *
from pygame import mixer
import time
pygame.init()

white = (255, 255, 255)
black = (0,0,0)

#SCREEN
SCREEN_WIDTH = 840
SCREEN_HEIGHT = 660
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def get_button(sound): #Načítanie obrázkov a tlačidiel
    pong_game = pygame.image.load("pong-logo.png").convert_alpha()
    pong_game=pygame.transform.scale(pong_game, (200, 200))
    color_game = pygame.image.load("bludisko-logo.png").convert_alpha()
    color_game = pygame.transform.scale(color_game, (180,180))
    moon_game = pygame.image.load("raketkazohonom.png").convert_alpha()
    moon_game = pygame.transform.scale(moon_game, (200, 200))
    random_game = pygame.image.load("farebna-logo.png").convert_alpha()
    random_game = pygame.transform.scale(random_game, (180, 180))
    random2_game = pygame.image.load("My project.png").convert_alpha()
    random2_game = pygame.transform.scale(random2_game, (180, 180))
    random3_game = pygame.image.load("tabulkadomenu.png").convert_alpha()
    back_to_menu = pygame.image.load("hlavnemenu.png").convert_alpha()
    end_menu = pygame.image.load("ukoncit1.png").convert_alpha()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                file = open("prihl.txt", "w")
                file.write("")
                file.close()
                sound.stop()
                return 0
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if pong_game_rect.collidepoint(mouse_pos):
                    sound.stop()
                    # Spustenie hry Pong
                    import pong
                    pong.main_pong()
                    pygame.quit()
                elif color_game_rect.collidepoint(mouse_pos):
                    sound.stop()
                    pygame.time.wait(500)
                    # Spustenie hry s farbami
                    import pygame_bludisko
                    pygame_bludisko.main()
                    pygame.quit()
                elif moon_game_rect.collidepoint(mouse_pos):
                    sound.stop()
                    # Spustenie hry Raketka
                    import raketka
                    raketka.main()
                    pygame.quit()
                elif random_game_rect.collidepoint(mouse_pos):
                    sound.stop()
                    # Spustenie náhodnej hry
                    import farebna_hra
                    farebna_hra.main()
                    pygame.quit()

                elif random2_game_rect.collidepoint(mouse_pos):
                    sound.stop()
                    # Spustenie hry Pexeso
                    import pexeso
                    pexeso.main()
                    pygame.quit()

                elif random3_game_rect.collidepoint(mouse_pos):
                    sound.stop()
                    # Spustenie tabuľky s možnosťou menu
                    import tabulka
                    tabulka.main_menu()
                    pygame.quit()

                elif back_to_menu_rect.collidepoint(mouse_pos):
                    sound.stop()
                    # Návrat do hlavného menu
                    import menuexe
                    menuexe.main_menu()
                    pygame.quit()

                elif end_menu_rect.collidepoint(mouse_pos):
                    file = open("prihl.txt", "w")
                    file.write("")
                    file.close()
                    return 0
        # Nastavenie pozícií tlačidiel
        pong_game_rect = screen.blit(pong_game, (50, 50))
        color_game_rect = screen.blit(color_game, (300, 50))
        moon_game_rect = screen.blit(moon_game, (550, 50))
        random_game_rect = screen.blit(random_game, (50, 300))
        random2_game_rect = screen.blit(random2_game, (300, 300))
        random3_game_rect = screen.blit(random3_game, (550, 300))
        back_to_menu_rect = screen.blit(back_to_menu, (170, 500))
        end_menu_rect = screen.blit(end_menu, (470, 500))

        pygame.display.flip()


def main():
    menu = True
    clock = pygame.time.Clock()
    sound = mixer.Sound("backgroundsong.wav")
    sound.play()
    banner = pygame.image.load("background.jpg").convert_alpha()
    background = screen.blit(banner, (0,0))


    while menu:
        button = get_button(sound)
        if button == 0:
            menu = False
            pygame.quit()
            quit()

        pygame.display.flip()
        clock.tick(60)

main()
