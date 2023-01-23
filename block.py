import pygame
import sys

# Main solid object
class Block(pygame.sprite.Sprite):

    # Solid block init script
    def __init__(self, x, y, width, height):
        super().__init__() 
        self.x = x + (width / 2)
        self.y = y + (height / 2)

        self.width = width
        self.height = height

        self.surf = pygame.Surface((width, height))
        self.surf.fill((255, 0, 0))
        self.rect = self.surf.get_rect(center = (self.x, self.y))

# Solid object that makes the player bounce
class Spring(Block):

    # Uses the same init function as a block
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.surf.fill((0, 0, 255))

# Semi-solid block the player can pass through
class SemiSolid(pygame.sprite.Sprite):
    
    # Solid block init script
    def __init__(self, x, y, width):
        super().__init__() 
        self.x = x
        self.y = y

        self.width = width
        self.height = 2

        self.surf = pygame.Surface((width, 2))
        self.surf.fill((255, 0, 0))
        self.rect = self.surf.get_rect(center = (x, y))
