import pygame
import sys

from pygame.locals import *
from playercontroller import *
from block import *

# One of the playable character
class Kyle(PlayerController):
    
    # Player character initialization script
    def __init__(self, x, y):
        super().__init__(x, y)

        self.is_sliding = False
        self.slide_speed = 4
        self.slide_time = 44
        self.super_speed = 12
        self.is_super = 0
        
    # Allows the player to run really fast
    # for a limited amount of time
    def super_run(self):
        pressed_keys = pygame.key.get_pressed()
        
        if self.in_control and self.on_land:
            if pressed_keys[K_LSHIFT]:

                if self.walk_speed < self.super_speed:
                    self.walk_speed += 1
                
                if self.run_speed < self.super_speed:
                    self.run_speed += 1
            
            if not pressed_keys[K_LSHIFT]:
                self.walk_speed = 3
                self.run_speed = 6

    # Allows the player to pass through tight
    # spaces
    def super_slide(self):
        pressed_keys = pygame.key.get_pressed()
        
        # If the key combination is pressed
        # start sliding
        if self.in_control and self.jump_on_land:
            if pressed_keys[K_DOWN] and pressed_keys[K_c]:
                
                self.in_control = False
                self.is_sliding = True
        
        # Behaviour while sliding
        if self.is_sliding:

            if not self.on_ice:
                if self.is_facing_right:
                    self.vel_x = self.slide_speed

                if not self.is_facing_right:
                    self.vel_x = -self.slide_speed

            if not pressed_keys[K_c]:
                self.time_to_normal_state = self.slide_time
                self.in_control = False
                self.is_sliding = False
                self.vel_x = 0
                return

    def move(self, blocks, others):
        super().move(blocks, others)
        self.super_run()
        #self.super_slide()  