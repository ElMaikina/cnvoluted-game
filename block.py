import pygame
import sys

# Main solid object
class Solid(pygame.sprite.Sprite):

    # Solid block init script
    def __init__(self, x, y, width, height):
        super().__init__() 

        self.width = width * 24
        self.height = height * 24
        self.x = (x * 24) + (self.width / 2)
        self.y = (y * 24) + (self.height / 2)

        self.surf = pygame.Surface((self.width, self.height))
        self.surf.fill((255, 0, 0))
        self.rect = self.surf.get_rect(center = (self.x, self.y))

# Semi-solid block the player can pass through
class SemiSolid(pygame.sprite.Sprite):
    
    # Solid block init script
    def __init__(self, x, y, width):
        super().__init__() 
        self.x = x + (width / 2)
        self.y = y - 1

        self.width = width
        self.height = 1

        self.surf = pygame.Surface((width, 2))
        self.surf.fill((255, 0, 0))
        self.rect = self.surf.get_rect(center = (self.x, self.y))

# Solid object that makes the player bounce
class Spring(Solid):

    # Uses the same init function as a block
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.surf.fill((0, 0, 255))

# Solid object that has low friction
class Ice(Solid):

    # Uses the same init function as a block
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.surf.fill((0, 255, 255))

# Solid object that moves
class MovingSolid(Solid):

    # Uses the same init function as a block
    def __init__(self, x, y, xdest, ydest, width, height, time, speed, xovery):
        super().__init__(x, y, width, height)
        self.xinit = (x * 24) #+ (self.width / 2)
        self.yinit = (y * 24) #+ (self.height / 2)
        self.xdest = (xdest * 24) #+ (self.width / 2)
        self.ydest = (ydest * 24) #+ (self.height / 2)

        self.xovery = xovery
        self.vxinit = 0
        self.vyinit = 0
        self.vx = 0
        self.vy = 0

        if xovery:
            self.vxinit = speed

        if not xovery:
            self.vyinit = speed

        if xovery:
            self.vx = speed

        if not xovery:
            self.vy = speed

        self.resting = False
        self.rest_time = time
        self.rest_to_move = 0
    
    def move(self, player):
        if not player.time_frozen:
            if not self.resting:
                self.rect.x += self.vx
                self.rect.y += self.vy

                if self.xovery:
                    if self.rect.x == self.xdest:
                        self.vx = -self.vxinit
                        self.resting = True
                        self.rest_to_move = self.rest_time

                    if self.rect.x == self.xinit:
                        self.vx = self.vxinit
                        self.resting = True
                        self.rest_to_move = self.rest_time

                if not self.xovery:
                    if self.rect.y == self.ydest:
                        self.vy = -self.vyinit
                        self.resting = True
                        self.rest_to_move = self.rest_time

                    if self.rect.y == self.yinit:
                        self.vy = self.vyinit
                        self.resting = True
                        self.rest_to_move = self.rest_time


            if self.resting:
                self.rest_to_move -= 1
                if self.rest_to_move < 1:
                    self.resting = False

        