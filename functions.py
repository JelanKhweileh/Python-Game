import pygame
from shield import Shield
from bullet import Bullet
from attackers import Attackers
from player import Player

def check_event(screen, player, bullets):
    # Check for events and update player and bullet movement
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.moving_top = True
            elif event.key == pygame.K_DOWN:
                player.moving_bottom = True
            elif event.key == pygame.K_RIGHT:
                player.moving_right = True
            elif event.key == pygame.K_LEFT:
                player.moving_left = True
            elif event.key == pygame.K_SPACE:
                if len(bullets) < 1000:
                    new_bullet = Bullet(screen, player)
                    bullets.add(new_bullet)
                    new_bullet.fire_sound()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player.moving_top = False
            elif event.key == pygame.K_DOWN:
                player.moving_bottom = False
            elif event.key == pygame.K_RIGHT:
                player.moving_right = False
            elif event.key == pygame.K_LEFT:
                player.moving_left = False

def update_screen(ai_settings, screen, player, bullets, attackerss, sb, player_lives):
    # Update the game screen with player, bullets, attackers, and score
    background = pygame.image.load("images/background.jpg")
    background = pygame.transform.scale(background, (ai_settings.screen_width, ai_settings.screen_height))
    screen.blit(background, (0, 0))

    player.draw()
    bullets.draw(screen)
    update_bullets(bullets, attackerss, ai_settings, sb)
    sb.show_score()
    attackerss.draw(screen)

    # Draw player lives
    life_image = pygame.image.load("images/heart.png")
    life_rect = life_image.get_rect()
    lives_spacing = 10
    max_lives = 3
    for i in range(min(player_lives, max_lives)):
        x = ai_settings.screen_width - (life_rect.width + lives_spacing) * (i + 1)
        y = 10
        screen.blit(life_image, (x, y))

    pygame.display.flip()

def create_fleet(ai_settings, screen, attackerss, player):
    # Create a fleet of attackers with a defined layout
    attackers = Attackers(screen, ai_settings)
    attackers_width = attackers.rect.width
    attackers_height = attackers.rect.height
    available_space_y = (ai_settings.screen_height - (3 * attackers_height) - player.rect.height)
    number_rows = int(available_space_y / (2 * attackers_height))

    for row_number in range(number_rows):
        for a in range(ai_settings.attackers_per_row):
            attacker = Attackers(screen, ai_settings)
            attacker.rect.y = ai_settings.screen_width + a * attackers_width
            attacker.rect.x = attackers_height + 2 * attackers_height * row_number
            attacker.initial_y = attacker.rect.y
            attacker.row_number = row_number
            attackerss.add(attacker)

def update_bullets(bullets, attackerss, ai_settings, sb):
    # Update bullet position and detect collisions with attackers
    for b in bullets:
        if b.rect.right >= ai_settings.screen_width:
            bullets.remove(b)
            print(len(bullets))
        b.draw()
    collisions = pygame.sprite.groupcollide(bullets, attackerss, True, True)
    if collisions:
        for attackerss in collisions.values():
            ai_settings.score += ai_settings.attackers_points
            sb.prep_score()
