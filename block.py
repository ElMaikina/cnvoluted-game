import pygame
import sys

class Block(pygame.sprite.Sprite):

    # Solid block initializaction script
    def __init__(self, x, y, width, height):
        super().__init__() 
        self.x = x
        self.y = y

        self.width = width
        self.height = height

        self.surf = pygame.Surface((width, height))
        self.surf.fill((255, 0, 0))
        self.rect = self.surf.get_rect(center = (x, y))