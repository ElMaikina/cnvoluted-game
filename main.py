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
scroll_limit_width = window_width / 2
scroll_limit_height = window_height / 2
game_clock = pygame.time.Clock()
game_is_running = True
grid_size = 24
fps = 60

# Window settings 
#display = pygame.display.set_mode((window_width, window_height), pygame.FULLSCREEN)
display = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Cnvoluted")

# Main player object and solid block(s)
sprites = pygame.sprite.Group()

# Player type and X, Y coordinates
player = Kyle(48, 160)
playersprite = PlayerSprite(player, 48, 160)
sprites.add(player)

# Solid block, X, Y coordinates, Width and Height
solid_sprites = pygame.sprite.Group()

# Other types of sprites
other_sprites = pygame.sprite.Group()

solid = Solid(0, 320-24, 640, 24)
solid_sprites.add(solid)

solid = Solid(320+48+24+48, 320-24, 640, 24)
solid_sprites.add(solid)

solid = Solid(320, 320-48-24-120, 24, 120)
solid_sprites.add(solid)

solid = Solid(320+48+24, 320-48-24-120+32, 24, 120)
solid_sprites.add(solid)

solid = Solid(640, 320-48, 48, 24)
solid_sprites.add(solid)

solid = Spring(640+48, 320-48, 48, 24)
solid_sprites.add(solid)

solid = Spring(640+48+48+48, 320-48-48, 48, 24)
solid_sprites.add(solid)

semi = SemiSolid(640+48+48+48+48+48, 320-48-48, 48)
other_sprites.add(semi)

semi = SemiSolid(640+48+48+48+48+48, 320-48-48-24*3, 48)
other_sprites.add(semi)

solid = Solid(640+48+48+48+48+48+48, 320-48-48-24*3, 24, 24)
solid_sprites.add(solid)

solid = Ice(640+48+48+48+48+48+48+48, 320-24-24, 1200, 24)
solid_sprites.add(solid)

sprites.add(solid_sprites)
sprites.add(other_sprites)


# Level settings
level_width = 1200
level_height = 320

# General game loop
while game_is_running:

	# See if the window has closed
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	# Draws the background color
	display.fill((0,0,0))
	
	# Manages player position
	player.move(solid_sprites, other_sprites)

	# Sets the camera position
	cam_x = player.rect.x - scroll_limit_width
	cam_y = player.rect.y - scroll_limit_height

	# Draws all of the sprites in the stage
	for sprite in sprites:
		x = sprite.rect.x - cam_x
		y  = sprite.rect.y - cam_y
		display.blit(sprite.surf, (x, y))
	
	# Draws the player sprite over the stage
	playersprite.animate(player, 320-12, 160-6)
	x = playersprite.offx
	y = playersprite.offy
	display.blit(playersprite.image, (320-12+x, 160-6+y))

	# Draws the Heads-Up-Display over everything

	# Redraws everything
	pygame.display.update()
	game_clock.tick(fps)

	print (game_clock.get_fps())