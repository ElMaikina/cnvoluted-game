import pygame
import sys

from player import *
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
displaysurface = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Cnvoluted")

# Main player object and solid block(s)
sprites = pygame.sprite.Group()

# Player type and X, Y coordinates
playersprite = PlayerSprite(48, 160)
player = Kyle(48, 160)
#sprites.add(playersprite)
sprites.add(player)

# Solid block, X, Y coordinates, Width and Height
solid_sprites = pygame.sprite.Group()

solid = Block(0, 320-24, 640, 24)
solid_sprites.add(solid)

solid = Block(640, 320-48, 48, 24)
solid_sprites.add(solid)

sprites.add(solid_sprites)

# Other types of sprites
other_sprites = pygame.sprite.Group()

# Level settings
level_width = 1200
level_height = 320

# General game loop
while game_is_running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	# Draws the background color
	displaysurface.fill((0,0,0))
	
	# Manages player position
	player.move(solid_sprites, other_sprites)

	# Sets the camera position
	cam_x = scroll_limit_width
	cam_y = scroll_limit_height

	# Sets the player position
	player_x = player.rect.x
	player_y = player.rect.y

	if player.rect.x > scroll_limit_width and player.rect.x < level_width - scroll_limit_width:
		cam_x = player.rect.x 
		player_x = scroll_limit_width
	
	if player.rect.y > scroll_limit_height and player.rect.y < level_height - scroll_limit_height:
		cam_y = player.rect.y
		player_y = scroll_limit_height

	# Draws all of the sprites in the stage
	# Also applies offset to each of them, so they are drawn
	# in correlation to the camera position
	for sprite in sprites:
		offset_x = sprite.rect.x - cam_x + scroll_limit_width
		offset_y  = sprite.rect.y - cam_y + scroll_limit_height
		displaysurface.blit(sprite.surf, (offset_x, offset_y))
	
	displaysurface.blit(playersprite.image, (player_x - 12, player_y - 6))

	# Redraws everything
	pygame.display.update()
	game_clock.tick(fps)