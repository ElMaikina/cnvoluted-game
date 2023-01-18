import pygame
import sys

from pygame.locals import *

class Player(pygame.sprite.Sprite):

    # Player character initialization script
    def __init__(self, x, y, width, height):
        super().__init__() 
        
        # Creates a surface
        self.surf = pygame.Surface((width, height))
        self.surf.fill((128, 255, 40))
        self.rect = self.surf.get_rect()

        self.width = width
        self.height = height

        self.rect.x = x
        self.rect.y = y
        self.vel_x = 0
        self.vel_y = 0

        self.on_land = False
        self.on_left_wall = False
        self.on_right_wall = False
        self.in_control = True
        self.can_jump = True
        self.max_vel_y = 12
        self.time_to_normal_state = 0

        self.walk_speed = 3
        self.run_speed = 6
        self.curr_speed = self.walk_speed

    # Checks for collisions regarding solid objects
    def check_blocks(self, blocks, vel_x, vel_y):
        self.rect.x += vel_x
        self.rect.y += vel_y

        # Search for detected collisions
        for block in blocks:
            if self.rect.colliderect(block.rect):
                if vel_x > 0:
                    self.rect.right = block.rect.left
                    self.on_right_wall = True
                    
                if vel_x < 0:
                    self.rect.left = block.rect.right
                    self.on_left_wall = True
                    
                if vel_y > 0:
                    self.rect.bottom = block.rect.top
                    self.on_land = True
                    self.vel_y = 0
                    
                if vel_y < 0:
                    self.rect.top = block.rect.bottom
                    self.vel_y = 0

    # Manages horizontal movement
    def run_or_walk(self):
        pressed_keys = pygame.key.get_pressed()
        
        if self.in_control:
            if not pressed_keys[K_z]:
                self.curr_speed = self.walk_speed # Walking

            if pressed_keys[K_z]:
                self.curr_speed = self.run_speed # Running

            if pressed_keys[K_LEFT]:
                self.vel_x = -self.curr_speed # Left

            if pressed_keys[K_RIGHT]:
                self.vel_x = self.curr_speed # Right

            if not pressed_keys[K_LEFT] and not pressed_keys[K_RIGHT]:
                self.vel_x = 0 # Standing still

    # Applies gravity to player
    def apply_gravity(self):
        if self.vel_y < self.max_vel_y:
            self.vel_y += 1

        if self.vel_y >= self.max_vel_y:
            self.vel_y = self.max_vel_y

    # Manages jumping while grounded
    def jump_on_land(self):
        pressed_keys = pygame.key.get_pressed()

        if self.in_control and self.on_land:
            if pressed_keys[K_x] and self.can_jump:
                self.vel_y = -12
                self.can_jump = False

        if not pressed_keys[K_x]:
            self.can_jump = True

    # Manages jumping when pressed against a wall
    # Only works in midair
    def jump_on_wall(self):
        pressed_keys = pygame.key.get_pressed()

        if self.in_control and not self.on_land:
            if pressed_keys[K_x]:
                if self.on_left_wall and self.can_jump:
                    self.vel_y = -10
                    self.vel_x = 5
                    self.can_jump = False
                    self.in_control = False
                    self.time_to_normal_state = 9

                if self.on_right_wall and self.can_jump:
                    self.vel_y = -10
                    self.vel_x = -5
                    self.can_jump = False
                    self.in_control = False
                    self.time_to_normal_state = 9

        if not pressed_keys[K_x]:
            self.can_jump = True

    # Certain actions requiere the player to lose control
    # of the character, this code manages returning to such
    # state
    def return_to_normal(self):
        if self.time_to_normal_state > 0:
            self.time_to_normal_state -= 1

        if self.time_to_normal_state == 0:
            self.in_control = True

    def move(self, blocks):
        self.on_land = False
        self.on_left_wall = False
        self.on_right_wall = False
        self.apply_gravity()
        self.check_blocks(blocks, self.vel_x, 0)
        self.check_blocks(blocks, 0, self.vel_y)
        self.run_or_walk()
        self.jump_on_land()
        self.jump_on_wall()
        self.return_to_normal()