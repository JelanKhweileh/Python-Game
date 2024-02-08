import pygame
import sys
from settings import Settings
import functions as fun
from player import Player
from pygame.sprite import Sprite
from bullet import Bullet
from attackers import Attackers
from score import ScoreBoard
from life import Life, check_collisions
import game_over
from start_screen import start_screen
from shield import Shield


def run_game():
    pygame.init()

    # Initialize game settings and create game window
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Shooting Flappy Birds")
    icon_image = pygame.image.load("images/icon.png")
    pygame.display.set_icon(icon_image)

    # Create player object with scaling
    player_scale = 0.4
    player = Player(screen, scale=player_scale)

    # Create groups for bullets and attackers
    bullets = pygame.sprite.Group()
    attackerss = pygame.sprite.Group()

    # Create the initial fleet of attackers
    fun.create_fleet(ai_settings, screen, attackerss, player)

    # Initialize the scoreboard
    sb = ScoreBoard(ai_settings, screen)

    # Initialize player lives and background music
    player_lives = 3
    pygame.mixer.music.load("audio/Game_of_Birds.mp3")
    pygame.mixer.music.play(-1)
    final_score = 0

    while True:
        # Show start screen before each game loop iteration
        start_screen(screen, ai_settings)
        # Execute the game loop
        game_loop(ai_settings, screen)


def game_loop(ai_settings, screen):
    # Create player, bullet, and attacker groups
    player = Player(screen)
    bullets = pygame.sprite.Group()
    attackerss = pygame.sprite.Group()

    # Create initial fleet of attackers
    fun.create_fleet(ai_settings, screen, attackerss, player)

    # Initialize scoreboard and player lives
    sb = ScoreBoard(ai_settings, screen)
    player_lives = 3
    final_score = 0

    # Load and play background music
    pygame.mixer.music.load("audio/Game_of_Birds.mp3")
    pygame.mixer.music.play(-1)

    while True:
        # Check for events and update game elements
        fun.check_event(screen, player, bullets)
        player.update()
        bullets.update()
        for attacker in attackerss:
            attacker.update()

            # Check if attacker has passed player
            if attacker.rect.right < 0:
                player_lives -= 1
                final_score -= 5
                attackerss.remove(attacker)

        # Check for collisions between player and attackers
        lost_life = check_collisions(player, attackerss,player_lives)
        if lost_life:
            player_lives -= 1
            final_score += 10
            if player_lives <= 0:
                # Stop music, show game over screen, and restart game
                pygame.mixer.music.stop()
                game_over.game_over(screen, final_score)
                restart_game(screen, player_lives, final_score, attackerss, ai_settings)
                start_screen(screen, ai_settings, show_start_screen=True)
                while True:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                            player_lives = 3
                            final_score = 0
                            pygame.mixer.music.play(-1)
                            fun.create_fleet(ai_settings, screen, attackerss, player)
                            break


def restart_game(screen, player_lives, final_score, attackerss, ai_settings):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                player_lives = 3
                final_score = 0
                pygame.mixer.music.play(-1)
                import player
                fun.create_fleet(ai_settings, screen, attackerss, player)
                start_screen(screen, ai_settings, show_start_screen=False)
                return


# Start the game by calling the run_game function
run_game()
