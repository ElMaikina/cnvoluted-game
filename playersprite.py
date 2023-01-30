import pygame
import sys

from pygame.locals import *
from playercontroller import *
from kyle import *
from block import *

# Draws the Player sprite
class PlayerSprite(pygame.sprite.Sprite):
    
    # Loads all the sprites into memory
    def __init__(self, player, x, y):
        super().__init__()
        self.sprites = []
        self.offx = 0
        self.offy = 0

        # Loads sprites depending on character type
        if type(player) is Kyle:
            self.sprites.append(pygame.image.load("sprites\kyle\idle\\0.png").convert_alpha())
            self.sprites.append(pygame.image.load("sprites\kyle\walk\\0.png").convert_alpha())
            self.sprites.append(pygame.image.load("sprites\kyle\walk\\1.png").convert_alpha())
            self.sprites.append(pygame.image.load("sprites\kyle\walk\\2.png").convert_alpha())
            self.sprites.append(pygame.image.load("sprites\kyle\walk\\3.png").convert_alpha())
            self.sprites.append(pygame.image.load("sprites\kyle\walk\\4.png").convert_alpha())
            self.sprites.append(pygame.image.load("sprites\kyle\walk\\5.png").convert_alpha())
            self.sprites.append(pygame.image.load("sprites\kyle\\run\\0.png").convert_alpha())
            self.sprites.append(pygame.image.load("sprites\kyle\\run\\1.png").convert_alpha())
            self.sprites.append(pygame.image.load("sprites\kyle\\run\\2.png").convert_alpha())
            self.sprites.append(pygame.image.load("sprites\kyle\\run\\3.png").convert_alpha())
            self.sprites.append(pygame.image.load("sprites\kyle\jump\\0.png").convert_alpha())
            self.sprites.append(pygame.image.load("sprites\kyle\\fall\\0.png").convert_alpha())
            self.sprites.append(pygame.image.load("sprites\kyle\wall\\0.png").convert_alpha())
            self.sprites.append(pygame.image.load("sprites\kyle\wljmp\\0.png").convert_alpha())
            self.sprites.append(pygame.image.load("sprites\kyle\zoom\\0.png").convert_alpha())
            self.sprites.append(pygame.image.load("sprites\kyle\zoom\\1.png").convert_alpha())
            self.sprites.append(pygame.image.load("sprites\kyle\slide\\0.png").convert_alpha())
            self.sprites.append(pygame.image.load("sprites\kyle\kneel\\0.png").convert_alpha())
            
        self.frame = 0
        self.image = self.sprites[self.frame]
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]

    # Draws the specific sprite on-screen
    def animate(self, player, x, y):
        action = player.action
        
        if type(player) is Kyle:

            start = 0
            end = 0
            self.offx = 0
            self.offy = 0
            
            if action == "idle":
                start = 0
                end = 0
                self.frame = 0
                self.offx = 1
                self.offy = 0
            
            if action == "walk":
                start = 1
                end = 7
                self.offx = 1
                self.offy = 0
            
                if self.frame > end:
                    self.frame = start

            if action == "run":
                start = 7
                end = 11
                self.offx = 2
                self.offy = 0

                if self.frame > end:
                    self.frame = start

            if action == "jump":
                start = 11
                end = 11
                self.offx = 1
                self.offy = 0
            
                self.frame = 11
            
            if action == "fall":
                start = 12
                end = 12
                self.offx = 1
                self.offy = 0

                self.frame = 12
            
            if action == "wall":
                start = 13
                end = 13
                self.offx = 8
                self.offy = 0

                self.frame = 13
            
            if action == "wljmp":
                start = 14
                end = 14
                self.offx = 8
                self.offy = 0

                self.frame = 14
            
            if action == "zoom":
                start = 15
                end = 17
                self.offx = 2
                self.offy = 0

                if self.frame > end:
                    self.frame = start

            if action == "slide":
                start = 17
                end = 17
                self.offx = -1
                self.offy = 0

                self.frame = 17
            
            if action == "kneel":
                start = 18
                end = 18
                self.offx = -1
                self.offy = 0

                self.frame = 18

            if self.frame > end:
                self.frame = start
            
            if self.frame < start:
                self.frame = start

            if player.is_facing_right:
                self.image = self.sprites[int(self.frame)]
                self.rect = self.image.get_rect()
                self.rect.center = [x,y]

            if not player.is_facing_right:
                self.image = self.sprites[int(self.frame)]
                self.image = pygame.transform.flip(self.image, True, False)
                self.rect = self.image.get_rect()
                self.rect.center = [x,y]
                self.offx *= -1
                self.offx += 2

        self.frame += 0.225