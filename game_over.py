import pygame


def game_over(screen, final_score):
    # Display "Game Over" message
    font = pygame.font.Font(None, 48)
    text = font.render("Game Over", True, (255, 0, 0))
    text_rect = text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 - 30))

    # Display final score
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Final Score: {final_score}", True, (0, 0, 0))
    score_rect = score_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 30))

    # Display restart instructions
    restart_text = font.render("Press Enter to Restart", True, (0, 0, 0))
    restart_rect = restart_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 80))

    # Blit the messages on the screen and update display
    screen.blit(text, text_rect)
    screen.blit(score_text, score_rect)
    screen.blit(restart_text, restart_rect)
    pygame.display.flip()
