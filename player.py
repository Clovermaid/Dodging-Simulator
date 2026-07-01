import pygame
import random

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        # 1. Create a 32x32 square surface for the player image
        self.image = pygame.Surface((32, 32))
        self.image.fill((0, 120, 255)) # Clean blue color
        
        # 2. Get the bounding box rectangle for position tracking
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        # 3. Speed attribute: How many pixels to move per frame
        self.speed = 5 

    def update(self):
        # Grab a list of every key currently pressed on the keyboard
        keys = pygame.key.get_pressed()
        
        # Free reign movement pixel-by-pixel
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.rect.y += self.speed
            
        # UX Polish: Stop the player from walking off the screen borders
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 800:
            self.rect.right = 800
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > 600:
            self.rect.bottom = 600

# Obstacles
class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # 1. Create a 20x20 red square for the obstacle asset
        self.image = pygame.Surface((20, 20))
        self.image.fill((255, 50, 50)) # Bright red
        
        self.rect = self.image.get_rect()
        
        # 2. Randomly spawn it along the top edge of the screen
        self.rect.x = random.randint(0, 780)
        self.rect.y = -20  # Start slightly above the screen
        
        # 3. Random speed between 3 and 7 to make it dynamic
        self.speed = random.randint(3, 7)

    def update(self):
        # Move downward frame-by-frame
        self.rect.y += self.speed

