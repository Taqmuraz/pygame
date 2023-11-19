import pygame
from sprite import load_sprite

pygame.init()

window = pygame.display.set_mode((500, 500))
player = load_sprite('image.png')

running = True
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	if not running: break

	window.fill((100, 100, 100))
	player.paint(window, (50, 50, 100, 100))

	pygame.display.flip()

pygame.quit()