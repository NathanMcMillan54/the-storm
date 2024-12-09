import json
import random
import sys

import pygame

from game.player import *
from libts.block import BLOCKS, BLOCK_SIZE
from libts.item import ITEMS
from libts.world import WorldData, WORLD_HEIGHT, WORLD_WIDTH

class World:
    def __init__(self, world_file):
        world_data = WorldData()
        world_data.open(world_file)
        self.world_data = world_data
        self.player = Player((255, 0, 0))

    def display(self, screen):
        for y in range(WORLD_HEIGHT):
            for x in range(WORLD_WIDTH):
                block = BLOCKS[self.world_data.blocks[y][x]]
                pygame.draw.rect(screen, block.color, pygame.rect.Rect((x * BLOCK_SIZE, y * BLOCK_SIZE), (BLOCK_SIZE, BLOCK_SIZE)))
