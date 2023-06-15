import pygame
import random

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)

# SCREEN
SCREEN_WIDTH = 840
SCREEN_HEIGHT = 660
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Load images
card_images = []
for i in range(1, 16):
    image = pygame.image.load(f"pexesopics/{i}.png")  # Adjust the file name pattern
    card_images.append(image)

# Load background image
background_image = pygame.image.load("pexesobackground.png")
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Cards
cards = random.sample(range(1, len(card_images) + 1), len(card_images)) * 2
random.shuffle(cards)
revealed = [False for _ in cards]
matching_pairs = 0

# Card dimensions
NUM_COLS = 6
NUM_ROWS = 5
GAP = 20

CARD_WIDTH = (SCREEN_WIDTH - (NUM_COLS + 1) * GAP) // NUM_COLS
CARD_HEIGHT = (SCREEN_HEIGHT - (NUM_ROWS + 1) * GAP) // NUM_ROWS

# Create cards
cards_rects = []
for row in range(NUM_ROWS):
    for col in range(NUM_COLS):
        x = GAP + col * (CARD_WIDTH + GAP)
        y = GAP + row * (CARD_HEIGHT + GAP)
        rect = pygame.Rect(x, y, CARD_WIDTH, CARD_HEIGHT)
        cards_rects.append(rect)

selected_cards = []

def check_matching_cards():
    global selected_cards, matching_pairs
    if len(selected_cards) == 2:
        card1, card2 = selected_cards
        if cards[card1] == cards[card2]:
            matching_pairs += 1
            if matching_pairs == len(cards) // 2:

                return True
        else:
            pygame.time.delay(1000)
            for i in selected_cards:
                revealed[i] = False
        selected_cards.clear()


def draw_cards():
    for i, rect in enumerate(cards_rects):
        if revealed[i]:
            pygame.draw.rect(screen, white, rect)
            pygame.draw.rect(screen, black, rect, 2)
            image = card_images[cards[i] - 1]
            resized_image = pygame.transform.scale(image, (CARD_WIDTH - 2 * GAP, CARD_HEIGHT - 2 * GAP))
            image_rect = resized_image.get_rect(center=rect.center)
            screen.blit(resized_image, image_rect)
        else:
            pygame.draw.rect(screen, black, rect)

def main():
    clock = pygame.time.Clock()
    running = True
    zastavene = False
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
    hodnot = False
    nadpis = pygame.font.Font(None, 50)
    koniec = nadpis.render("Koniec!", True, (255, 255, 255))
    totalitnykonec = False
    maly = pygame.font.Font(None, 25)
    nadpis = pygame.font.Font(None, 50)
    text = nadpis.render("Raketka!!", True, (255, 255, 255))
    text1 = font.render("Vitajte v hre raketka, hra je určená ", True, (255, 255, 255))
    text2 = font.render("pre jedného hráča. Úlohou je dopraviť", True, (255, 255, 255))
    text3 = font.render("raketku na bielu plošinu čo najviackrát", True, (255, 255, 255))
    text5 = font.render("za dvadsať sekúnd!", True, (255, 255, 255))
    text4 = maly.render("(Hru pauzneš pomocou ESC)", True, (255, 255, 255))
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    pos = pygame.mouse.get_pos()
                    for i, rect in enumerate(cards_rects):
                        if rect.collidepoint(pos) and not revealed[i]:
                            revealed[i] = True
                            draw_cards()
                            pygame.display.flip()
                            selected_cards.append(i)
                            if len(selected_cards) == 2:
                                hodnot=check_matching_cards()
            stlacenne = pygame.key.get_pressed()
            if stlacenne[pygame.K_ESCAPE]:
                zastavene = True

        if zastavene==False:
            screen.blit(background_image, (0, 0))
            draw_cards()
            pygame.display.flip()
            clock.tick(60)
        else:
            pygame.draw.rect(screen, (79, 90, 255), (330, 155, 510, 310))
            pygame.draw.rect(screen, (41, 47, 133), (335, 160, 500, 300))
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

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        xpsova, ypsilonova = event.pos

                        if xpsova < 240 and xpsova > 60 and ypsilonova < 280 and ypsilonova > 200:
                            zastavene=False

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
                            pygame.quit()
                        if xpsova < 500 and xpsova > 320 and ypsilonova < 490 and ypsilonova > 430:
                            import minihryexe
                            minihryexe.main()
                pygame.draw.rect(screen, (79, 90, 255), (170, 155, 510, 410))
                pygame.draw.rect(screen, (41, 47, 133), (175, 160, 500, 400))
                hlaska = nadpis.render("Si frajer dal si to!!", True, (255, 255, 255))
                screen.blit(hlaska, (270, 300))
                screen.blit(koniec, (350, 250))
                screen.blit(minihrymen, (320, 420))
                screen.blit(ukoncitmen, (320, 490))
                pygame.display.flip()
            pygame.display.flip()


    pygame.quit()

def main_hlavny():
    main()
main_hlavny()