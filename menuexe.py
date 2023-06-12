import pygame
pygame.init()

white = (255, 255, 255)
black = (0,0,0)

#SCREEN
SCREEN_WIDTH = 840
SCREEN_HEIGHT = 660
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def get_button(prihlaseny):

    games_menu = pygame.image.load("minihry1.png").convert_alpha()
    about_menu = pygame.image.load("onas1.png").convert_alpha()
    end_menu = pygame.image.load("ukoncit1.png").convert_alpha()
    if prihlaseny == True:
        login_menu = pygame.image.load("prihlaseny.png").convert_alpha()
    elif prihlaseny == False:
        login_menu = pygame.image.load("login.png").convert_alpha()


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
                elif about_menu_rect.collidepoint(mouse_pos):
                    return "O nás"
                elif login_menu_rect.collidepoint(mouse_pos):
                    return "Login"
                elif end_menu_rect.collidepoint(mouse_pos):
                    return 0
                else:
                    break
        
        games_menu_rect = screen.blit(games_menu, (320, 300))
        about_menu_rect = screen.blit(about_menu, (320, 380))
        end_menu_rect = screen.blit(end_menu, (320, 460))
        login_menu_rect = screen.blit(login_menu, (740,50))

        pygame.display.update()


def main_menu():
    menu = True
    prihlaseny = False
    clock = pygame.time.Clock()
    banner = pygame.image.load("background.jpg").convert_alpha()
    background = screen.blit(banner, (0,0))
    subor = open("prihl.txt")
    log = subor.read()
    print(len(log))
    if len(log)!=0:
        prihlaseny = True
    
    while menu:
        button = get_button(prihlaseny)
        if button == 0:
            menu = False
            pygame.quit()
            quit()
        elif button == "Minihry":
            import minihryexe
            minihryexe.main()
            pygame.quit()
        elif button == "Login" and prihlaseny==False:
            import login
        elif button == "Login" and prihlaseny==True:
            print("už si prihlásený")
        elif button == "O nás":
            import o_nas
            o_nas.main()
        print(button)
        pygame.display.flip()
        clock.tick(60)
                
main_menu()
