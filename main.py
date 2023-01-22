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
 
displaysurface = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Cnvoluted")

# Main player object and solid block(s)
player = Kyle(48, 200)
block = Block(320, 320-12, 640, 24)
block_two = Block(320, 320-36, 24, 24)
block_three = Block(320+48+72, 320-36-24-48, 24, 72)
block_four = Block(320+48+72+72, 320-36-24-48-48, 24, 72+24)
block_five = Block(320+48, 320-36-24-48-48, 96+48+24, 24)
spring = Spring(48+24, 320-36, 24, 24)
step = SemiSolid(48+24+48, 320-36-36, 24)


sprites = pygame.sprite.Group()
sprites.add(player)

other_sprites = pygame.sprite.Group()
other_sprites.add(step)

solid_sprites = pygame.sprite.Group()
solid_sprites.add(block)
solid_sprites.add(block_two)
solid_sprites.add(block_three)
solid_sprites.add(block_four)
solid_sprites.add(block_five)
solid_sprites.add(spring)

sprites.add(solid_sprites)
sprites.add(other_sprites)



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
	cam_x = player.rect.x 
	cam_y = player.rect.y

	# Draws all of the sprites in the stage
	# Also applies offset to each of them, so they are drawn
	# in correlation to the camera position
	for sprite in sprites:
		offset_x = sprite.rect.x - cam_x + scroll_limit_width
		offset_y  = sprite.rect.y - cam_y + scroll_limit_height
		displaysurface.blit(sprite.surf, (offset_x, offset_y))

	# Redraws everything
	pygame.display.update()
	game_clock.tick(fps)