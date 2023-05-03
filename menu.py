import pygame
pygame.init()

white = (255, 255, 255)
black = (0,0,0)

#SCREEN
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def display_button(img, x, y):
    obr = pygame.image.load(img)
    obr1=obr.get_rect()
    screen.blit(obr, (x, y))
    return obr1


def main_menu():
    menu = True
    clock = pygame.time.Clock()
    
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu = False
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if games_menu.collidepoint(mouse_pos):
                    print("Ukáže menu s minihrami")
                if about_menu.collidepoint(mouse_pos):
                    print("ukáže info o nás")
                if end_menu.collidepoint(mouse_pos):
                    pygame.quit()
                    quit()
        
        games_menu = display_button("minihry.png", 320, 300)
        about_menu = display_button("onas.png", 320, 380) 
        end_menu = display_button("ukoncit.png", 320, 460) 


        pygame.display.flip()
        clock.tick(60)
        pygame.display.update()
                
main_menu()
