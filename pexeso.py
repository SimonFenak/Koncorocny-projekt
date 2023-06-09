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
cards = random.sample(range(1, len(card_images) + 1), len(card_images)) * 2
random.shuffle(cards)
revealed = [False for _ in cards]
matching_pairs = 0

# Card dimensions
NUM_COLS = 6
NUM_ROWS = 5
GAP = 10

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
                print("You won!")
        else:
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
                            selected_cards.append(i)
                            if len(selected_cards) == 2:
                                check_matching_cards()

        screen.fill(white)
        draw_cards()
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
