import pygame
import sys
from player import Player, Obstacle

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Dodging Simulator - Refactored")
pygame.font.init()
# Use a clean system font, size 30
game_font = pygame.font.SysFont(None, 30)

# Track the starting time using Pygame's internal millisecond clock
start_time = pygame.time.get_ticks()


clock = pygame.time.Clock()
player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

# 1. Create a Pygame Sprite Group for all obstacles
obstacle_group = pygame.sprite.Group()

# Set up the custom spawning timer event (every 1 second)
SPAWN_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_EVENT, 1000)

running = True
game_over = False

while running:
    # --- EVENT LOOP ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == SPAWN_EVENT and not game_over:
            # Create a new enemy and add it directly into our sprite group
            new_enemy = Obstacle()
            obstacle_group.add(new_enemy)
            
    # --- GAME LOGIC ---
    if not game_over:
        player.update()
        
        # 2. Automatically update ALL obstacles inside the group at once!
        obstacle_group.update()
        
        # 3. Super Clean Collision Check
        # spritecollideany checks if the player overlaps with ANY sprite inside the group
        if pygame.sprite.spritecollideany(player, obstacle_group):
            print("GAME OVER! You got hit.")
            game_over = True

        # Optimization: Remove obstacles that left the screen
        for obstacle in obstacle_group:
            if obstacle.rect.y > SCREEN_HEIGHT:
                obstacle.kill() # .kill() instantly deletes it from all sprite groups!
        current_time = pygame.time.get_ticks()
        score_seconds = (current_time - start_time) // 1000

    # --- DRAWING ---
    screen.fill((30, 30, 30)) 
    
    # 4. Automatically blit every single obstacle's surface using their rects!
    obstacle_group.draw(screen)
    
    screen.blit(player.image, player.rect)
    # Create the text image surface (White text)
    score_text = f"Time Survived: {score_seconds}s"
    text_surface = game_font.render(score_text, True, (255, 255, 255))

    # Draw it at coordinates X=20, Y=20 (Top left corner)
    screen.blit(text_surface, (20, 20))

    # If it's Game Over, draw a big red message in the center!
    if game_over:
        over_surface = game_font.render("GAME OVER! Press Esc to Close", True, (255, 50, 50))
        end_score = game_font.render(f"You have survived {score_seconds} seconds", True, (255, 50, 50))
        screen.blit(over_surface, (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2))
        screen.blit(end_score, (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 + 50))

    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()