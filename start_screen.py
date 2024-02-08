import pygame
import sys


def start_screen(screen, ai_settings, show_start_screen=True):
    # Display the start screen if specified, otherwise skip it
    if not show_start_screen:
        return

    # Load and scale the background image for the start screen
    start_screen_bg = pygame.image.load("images/Game_of_Birds.png.crdownload")
    start_screen_bg = pygame.transform.scale(start_screen_bg, (ai_settings.screen_width, ai_settings.screen_height))

    # Load the image for the start button and position it in the center
    start_button_img = pygame.image.load("images/th.jpg")
    start_button_rect = start_button_img.get_rect(
        center=(ai_settings.screen_width // 2, ai_settings.screen_height // 2 + 100))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                # Check if the mouse click is within the start button's area
                if start_button_rect.collidepoint(mouse_pos):
                    return  # Exit the start screen loop

        # Display the background image and start button on the screen
        screen.blit(start_screen_bg, (0, 0))
        screen.blit(start_button_img, start_button_rect)

        # Update the display to show the changes
        pygame.display.flip()
