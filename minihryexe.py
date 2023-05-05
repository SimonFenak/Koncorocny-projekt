import pygame
pygame.init()

white = (255, 255, 255)
black = (0,0,0)

#SCREEN
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def get_button():
    pong_game = pygame.image.load("pongy.png").convert_alpha()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 0
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if pong_game_rect.collidepoint(mouse_pos):
                    import pong
                    pong.main_pong()   
        pong_game_rect = screen.blit(pong_game, (50, 50))
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