import pygame
import sys

from playercontroller import *
from playersprite import *
from kyle import *
from block import *

pygame.init()

# Main graphical settings for the game
# Set the initial conditions for the game
window_width = 640
window_height = 320
mid_width = window_width / 2
mid_height = window_height / 2
game_clock = pygame.time.Clock()
game_is_running = True
fps = 60

# Window settings 
display = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Cnvoluted")

# Main Player Controller object and Solid Block(s)
sprites = pygame.sprite.Group()

# Player Controller and Sprite
plyrctrl = Kyle(0, -5, 1)
plyrspr = PlayerSprite(plyrctrl, 0, 0)
sprites.add(plyrctrl)

# Solid block, X, Y coordinates, Width and Height
solid_sprites = pygame.sprite.Group()
moving_solid_sprites = pygame.sprite.Group()

# Other types of sprites
other_sprites = pygame.sprite.Group()

solid = Solid(-6, -9, 1, 15)
solid_sprites.add(solid)

solid = Solid(-5, 5, 40, 1)
solid_sprites.add(solid)

solid = Solid(35, 5, 40, 1)
solid_sprites.add(solid)

solid = Solid(80, 5, 20, 1)
solid_sprites.add(solid)

solid = Ice(100, 5, 20, 1)
solid_sprites.add(solid)

solid = Solid(10, -2, 1, 5)
solid_sprites.add(solid)

solid = Solid(13, 0, 5, 5)
solid_sprites.add(solid)

solid = Solid(20, -2, 5, 2)
solid_sprites.add(solid)

solid = Solid(20, 0, 1, 3)
solid_sprites.add(solid)

solid = Solid(27, -1, 3, 1)
solid_sprites.add(solid)

solid = Solid(33, -3, 2, 3)
solid_sprites.add(solid)

solid = Spring(38, -3, 3, 1)
solid_sprites.add(solid)

solid = Spring(43, -3, 3, 1)
solid_sprites.add(solid)

solid = Solid(43, 2, 3, 3)
solid_sprites.add(solid)

solid = Solid(50, -1, 3, 3)
solid_sprites.add(solid)

solid = Solid(55, 0, 4, 1)
solid_sprites.add(solid)

solid = Solid(75, -5, 5, 11)
solid_sprites.add(solid)

solid = MovingSolid(59, -3, 65, -3, 4, 1, 20, 4, True)
moving_solid_sprites.add(solid)

solid = MovingSolid(70, 0, 70, -5, 5, 1, 30, -1, False)
moving_solid_sprites.add(solid)

solid = MovingSolid(80, -5, 80, 4, 5, 1, 30, 3, False)
moving_solid_sprites.add(solid)

solid = MovingSolid(59, -2, 69, -2, 1, 7, 20, 2, True)
moving_solid_sprites.add(solid)

solid = Solid(85, 0, 5, 3)
solid_sprites.add(solid)

solid = Solid(92, -2, 5, 5)
solid_sprites.add(solid)


solid_sprites.add(moving_solid_sprites)
sprites.add(solid_sprites)
sprites.add(other_sprites)


# General game loop
while game_is_running:

	pressed_keys = pygame.key.get_pressed()

	# See if the window has closed
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	if pressed_keys[K_ESCAPE]:
		pygame.quit()
		sys.exit()

	# Draws the background color
	display.fill((0,0,0))
	
	# Manages plyrctrl position
	plyrctrl.move(solid_sprites, other_sprites)

	# Sets the camera position
	cam_x = plyrctrl.rect.x - mid_width
	cam_y = plyrctrl.rect.y - mid_height

	# Movment for obstacles that move dynamically
	for solid in moving_solid_sprites:
		solid.move(plyrctrl)

	# Draws all of the sprites in the stage
	for sprite in sprites:
		x = sprite.rect.x - cam_x
		y  = sprite.rect.y - cam_y
		display.blit(sprite.surf, (x, y))
	
	# Draws the plyrctrl sprite over the stage
	plyrspr.animate(plyrctrl, mid_width-12, mid_height-6)
	x = plyrspr.offx
	y = plyrspr.offy

	display.blit(plyrspr.image, (mid_width-12+x, mid_height-6+y))

	# Draws the Heads-Up-Display over everything

	# Redraws everything
	pygame.display.update()
	game_clock.tick(fps)

	#print(game_clock.get_fps())