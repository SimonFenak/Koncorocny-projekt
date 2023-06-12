import pygame
from pygame .locals import *
import time
pygame.init()

white = (255, 255, 255)
black = (0,0,0)

#SCREEN
SCREEN_WIDTH = 840
SCREEN_HEIGHT = 660
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def get_button():
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
    random3_game = pygame.image.load("tile.png").convert_alpha()
    back_to_menu = pygame.image.load("hlavnemenu.png").convert_alpha()
    end_menu = pygame.image.load("ukoncit1.png").convert_alpha()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 0
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if pong_game_rect.collidepoint(mouse_pos):
                    import pong
                    pong.main_pong()
                elif color_game_rect.collidepoint(mouse_pos):
                    import pygame_bludisko
                    pygame_bludisko.main()
                elif moon_game_rect.collidepoint(mouse_pos):
                    import raketka
                    raketka.main()
                elif random_game_rect.collidepoint(mouse_pos):
                    import farebna_hra
                    farebna_hra.main()
                elif random2_game_rect.collidepoint(mouse_pos):
                    import pexeso
                    pexeso.main()

                elif random3_game_rect.collidepoint(mouse_pos):
                    import tabulka
                    tabulka.main_menu()

                elif back_to_menu_rect.collidepoint(mouse_pos):
                    import menuexe
                    menuexe.main_menu()
                elif end_menu_rect.collidepoint(mouse_pos):
                    return 0
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
    banner = pygame.image.load("background.jpg").convert_alpha()
    background = screen.blit(banner, (0,0))
    
    
    while menu:
        button = get_button()
        if button == 0:
            menu = False
            pygame.quit()
            quit()
            
        print(button)
        pygame.display.flip()
        clock.tick(60)
                
main()
