import random

import pygame

from parameters import *


class World(object):
    def __init__(self):
        # Load some art
        self.dirt_block = pygame.image.load('Dirt Block.png').convert_alpha()
        self.grass_block = pygame.image.load('Grass Block.png').convert_alpha()
        self.stone_block = pygame.image.load('Stone Block.png').convert_alpha()
        blocks = [self.dirt_block, self.grass_block, self.stone_block]

        # Create a surface fill it with sky...
        self.image = pygame.Surface((WORLD_WIDTH, WINDOW_HEIGHT))
        self.image.fill((pygame.Color('Sky Blue')))

        # ... then draw
        num_blocks = WORLD_WIDTH / BLOCK_HOFFSET + 1
        self.terrain = [random.randint(0, 2) for i in range(num_blocks)]
        self.height = [random.randint(1, 3) for i in range(num_blocks)]
        for i in range(num_blocks):
            base = GROUND
            terrain = blocks[self.terrain[i]]
            height = self.height[i]

            x = i * BLOCK_HOFFSET
            for i in range(height):
                self.image.blit(terrain, (x, base - (BLOCK_LOFFSET * i)))
                self.image.blit(terrain, (x, base + BLOCK_VOFFSET - (BLOCK_LOFFSET * i)))
