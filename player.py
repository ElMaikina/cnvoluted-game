import pygame
import sys

from pygame.locals import *
from block import *

class Player(pygame.sprite.Sprite):

    # Player character initialization script
    def __init__(self, x, y):
        super().__init__() 
        
        # Creates a surface
        self.surf = pygame.Surface((4, 24))
        self.surf.fill((128, 255, 40))
        self.rect = self.surf.get_rect()

        self.width = 4
        self.height = 24

        self.rect.x = x
        self.rect.y = y
        self.vel_x = 0
        self.vel_y = 0

        self.is_facing_right = True
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
    def check_blocks(self, blocks, others, vel_x, vel_y):
        self.rect.x += vel_x
        self.rect.y += vel_y

        pressed_keys = pygame.key.get_pressed()

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

                    # Checks if the block is a spring
                    if type(block) is Spring:
                        if not pressed_keys[K_x]:
                            self.vel_y = -10
                        if pressed_keys[K_x]:
                            self.vel_y = -18
                    
                if vel_y < 0:
                    self.rect.top = block.rect.bottom
                    self.vel_y = 0

        # Search for special collisions
        for other in others:

            # Checks for Semi-Solids
            if self.rect.colliderect(other.rect):
                if type(other) is SemiSolid:
                    if vel_y > 0:
                        self.rect.bottom = other.rect.bottom
                        self.on_land = True
                        self.vel_y = 0

    # Checks if player is sliding on wall
    def check_slide_on_wall(self):
        pressed_keys = pygame.key.get_pressed()

        if self.vel_y >= 2:
            if self.on_right_wall and pressed_keys[K_RIGHT]:
                self.is_facing_right = False
                self.max_vel_y = 2
                self.vel_y = 2
                
            if self.on_left_wall and pressed_keys[K_LEFT]:
                self.is_facing_right = True
                self.max_vel_y = 2
                self.vel_y = 2
    
            else:
                self.max_vel_y = 12

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
                self.is_facing_right = False

            if pressed_keys[K_RIGHT]:
                self.vel_x = self.curr_speed # Right
                self.is_facing_right = True

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
                    self.is_facing_right = True
                    self.time_to_normal_state = 9

                if self.on_right_wall and self.can_jump:
                    self.vel_y = -10
                    self.vel_x = -5
                    self.can_jump = False
                    self.in_control = False
                    self.is_facing_right = False
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

    # Manages both collisions with solid objects and
    # other object that don't necesarily collide
    # (NPC's, slopes, items, etc.)
    def move(self, blocks, others):
        self.on_land = False
        self.on_left_wall = False
        self.on_right_wall = False
        self.apply_gravity()
        self.check_blocks(blocks, others, self.vel_x, 0)
        self.check_blocks(blocks, others, 0, self.vel_y)
        self.run_or_walk()
        self.jump_on_land()
        self.jump_on_wall()
        self.return_to_normal()
        self.check_slide_on_wall()

class Kyle(Player):
    
    # Player character initialization script
    def __init__(self, x, y):
        super().__init__(x, y)

        self.is_sliding = False
        self.slide_speed = 4
        self.slide_time = 44
        self.super_speed = 12
        self.is_super = 0

    def super_run(self):
        pressed_keys = pygame.key.get_pressed()
        
        if self.in_control:
            if pressed_keys[K_LSHIFT]:

                if self.walk_speed < self.super_speed:
                    self.walk_speed += 1
                
                if self.run_speed < self.super_speed:
                    self.run_speed += 1
            
            if not pressed_keys[K_LSHIFT]:
                self.walk_speed = 3
                self.run_speed = 6

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

            # If the keys are released
            # return to normal state
            if not pressed_keys[K_c]:
                self.time_to_normal_state = self.slide_time
                self.in_control = False
                self.is_sliding = False
                self.vel_x = 0
                return

            # Apply the slide speed
            if self.is_facing_right:
                self.vel_x = self.slide_speed

            if not self.is_facing_right:
                self.vel_x = -self.slide_speed



    def move(self, blocks, others):
        self.on_land = False
        self.on_left_wall = False
        self.on_right_wall = False
        self.apply_gravity()
        self.check_blocks(blocks, others, self.vel_x, 0)
        self.check_blocks(blocks, others, 0, self.vel_y)
        self.run_or_walk()
        self.jump_on_land()
        self.jump_on_wall()
        self.return_to_normal()
        self.check_slide_on_wall()
        self.super_run()
        self.super_slide()
