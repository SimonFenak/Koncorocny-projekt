import pygame

def main():
    pygame.init()

    width, height = 840, 660

    window = pygame.display.set_mode((width, height))

    pygame.display.set_caption("O nás")

    background_image = pygame.image.load("background.jpg")
    background_image = pygame.transform.scale(background_image, (width, height))

    font_heading = pygame.font.SysFont("Arial", 24, bold=True)
    font_content = pygame.font.SysFont("Arial", 18)

    column_heading = font_heading.render("FPF Studio", True, (255, 255, 255))

    column_content = [
        font_content.render("Naše herné štúdio vzniklo v roku 2023 za účelom robenia koncoročného školského projektu.", True, (255, 255, 255)),
        font_content.render("Tvoria ho traja členovia: Jakub Petrila, Dominik Fečo a Šimon Feňak.", True, (255, 255, 255)),

    ]

    column_x = width // 2
    heading_y = 50
    content_y = 100
    row_spacing = 30

    button_image = pygame.image.load("hlavnemenu.png")
    button_rect = button_image.get_rect()
    button_rect.center = (width // 2, height - 75)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if button_rect.collidepoint(event.pos):
                    import menuexe
                    menuexe.main_menu()

        window.blit(background_image, (0, 0))

        window.blit(column_heading, column_heading.get_rect(center=(column_x, heading_y)))

        for i in range(len(column_content)):
            window.blit(column_content[i], (column_x - column_content[i].get_width() // 2, content_y + i * row_spacing))

        window.blit(button_image, button_rect)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
