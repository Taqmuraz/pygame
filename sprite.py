from collections import namedtuple
import os
import pygame

Sprite = namedtuple('Sprite', 'paint')

def load_sprite(path):
	sprite = pygame.image.load(os.path.join(path))
	def paint(target, rect):
		target.blit(sprite, rect)
	return Sprite(paint)