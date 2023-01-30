import pygame
import sys

from pygame.locals import *
from playercontroller import *
from block import *

# One of the playable character
class Kyle(PlayerController):
    
    # Player character initialization script
    def __init__(self, x, y,lvl):
        super().__init__(x, y, lvl)

        self.is_sliding = False
        self.slide_speed = 12
        self.super_speed = 12
        self.can_slide = True
        self.is_super = 0
        
    # Allows the player to run really fast
    # for a limited amount of time
    def zoom(self):
        pressed_keys = pygame.key.get_pressed()
        
        if self.in_control and self.on_land:
            if pressed_keys[K_LSHIFT]:
                
                self.action = "zoom"
                if self.walk_speed < self.super_speed:
                    self.walk_speed += 1
                
                if self.run_speed < self.super_speed:
                    self.run_speed += 1
            
            if not pressed_keys[K_LSHIFT]:
                self.walk_speed = 3
                self.run_speed = 6

    # Allows the player to pass through tight
    # spaces
    def slide(self):
        pressed_keys = pygame.key.get_pressed()
        
        # If the key combination is pressed
        # start sliding
        if self.in_control and self.on_land:
            if pressed_keys[K_DOWN]:
                if pressed_keys[K_x] and self.can_slide:
                    self.time_to_normal_state = 100
                    self.in_control = False
                    self.is_sliding = True
                    self.can_slide = False
                    self.action = "slide"
                    self.vel_y = 0

                    if self.is_facing_right:
                        self.vel_x = self.slide_speed

                    if not self.is_facing_right:
                        self.vel_x = -self.slide_speed
        
        # Behaviour while sliding
        if self.is_sliding:
            self.vel_x *= 0.95
        
            if abs(self.vel_x) < 3:
                self.time_to_normal_state = 10
                self.is_sliding = False
                self.action = "kneel"
                self.vel_x = 0
            
            if not self.on_land:
                self.is_sliding = False
                self.vel_x = 0
                self.time_to_normal_state = 0
        
        if not pressed_keys[K_x]:
            self.can_slide = True

    # Allows the player to freeze time
    def time(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_SPACE]:
            return True

        return False

    def move(self, blocks, others):
        super().move(blocks, others)
        
        if self.lvl > 0:
            self.time_frozen = self.time()
            self.slide()

        if self.lvl > 1:
            self.zoom()

            