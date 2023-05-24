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
    image = pygame.image.load(f"pexesopics\{i}.png")  # Adjust the file name pattern
    card_images.append(image)



# Cards
cards = [i // 2 for i in range(len(card_images))] * 2
random.shuffle(cards)
revealed = [False] * len(cards)
selected_card = None
matching_pairs = 0

# Card dimensions
CARD_WIDTH = 100
CARD_HEIGHT = 150
GAP = 10
NUM_COLS = 6
NUM_ROWS = 5
GRID_X = (SCREEN_WIDTH - (CARD_WIDTH + GAP) * NUM_COLS) // 2
GRID_Y = (SCREEN_HEIGHT - (CARD_HEIGHT + GAP) * NUM_ROWS) // 2

# Create cards
cards_rects = []
for row in range(NUM_ROWS):
    for col in range(NUM_COLS):
        x = GRID_X + col * (CARD_WIDTH + GAP)
        y = GRID_Y + row * (CARD_HEIGHT + GAP)
        rect = pygame.Rect(x, y, CARD_WIDTH, CARD_HEIGHT)
        cards_rects.append(rect)

def check_matching_cards():
    global selected_card, matching_pairs
    matching = [i for i, rev in enumerate(revealed) if rev]
    if len(matching) == 2:
        if cards[matching[0]] == cards[matching[1]]:
            matching_pairs += 1
            if matching_pairs == len(cards) // 2:
                print("You won!")
        else:
            revealed[matching[0]] = False
            revealed[matching[1]] = False
        selected_card = None

def draw_cards():
    for i, rect in enumerate(cards_rects):
        if revealed[i]:
            pygame.draw.rect(screen, white, rect)
            pygame.draw.rect(screen, black, rect, 2)
            image = card_images[cards[i]]
            image_rect = image.get_rect(center=rect.center)
            screen.blit(image, image_rect)
        else:
            pygame.draw.rect(screen, black, rect)

def main():
    clock = pygame.time.Clock()
    running = True

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
                            if selected_card is None:
                                selected_card = i
                            else:
                                check_matching_cards()

        screen.fill(white)
        draw_cards()
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
