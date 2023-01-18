import pygame
import sys

from player import *
from block import *

pygame.init()

# Set the initial conditions for the game
window_width = 640
window_height = 320
game_is_running = True
game_clock = pygame.time.Clock()
grid_size = 24
fps = 60
 
displaysurface = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Cnvoluted")

# Main player object and solid block
player = Player(48, 200, 4, 24)
block = Block(320, 320-12, 640, 24)
block_two = Block(320, 320-36, 24, 24)
block_three = Block(320+48+72, 320-36-24-48, 24, 72)
block_four = Block(320+48+72+72, 320-36-24-48-48, 24, 72+24)
block_five = Block(320+48, 320-36-24-48-48, 96+48+24, 24)

sprites = pygame.sprite.Group()
sprites.add(player)

solid_sprites = pygame.sprite.Group()
solid_sprites.add(block)
solid_sprites.add(block_two)
solid_sprites.add(block_three)
solid_sprites.add(block_four)
solid_sprites.add(block_five)

sprites.add(solid_sprites)

# General game loop
while game_is_running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	displaysurface.fill((0,0,0))
	player.move(solid_sprites)

	for sprite in sprites:
		displaysurface.blit(sprite.surf, sprite.rect)

	pygame.display.update()
	game_clock.tick(fps)