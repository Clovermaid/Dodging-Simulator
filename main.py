import pygame
import sys
from player import Player, Obstacle

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Dodging Simulator - Refactored")

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

    # --- DRAWING ---
    screen.fill((30, 30, 30)) 
    
    # 4. Automatically blit every single obstacle's surface using their rects!
    obstacle_group.draw(screen)
    
    screen.blit(player.image, player.rect) 
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()