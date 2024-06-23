from enum import Enum

import pygame


class ItemType(Enum):
    TOOL = 0
    BLOCK = 1
    FOOD = 2

class Item:
    def __init__(self, name, id, item_type: ItemType, show_grid, color, usage):
        self.name = name
        self.id = id
        self.count = 1
        self.type = item_type
        self.show_grid = show_grid
        # Usage should be a function
        self.usage = usage
        # Until there are images
        self.color = color

    def display(self, x, y, screen):
        item = pygame.Rect(x, y, 5, 5)
        pygame.draw.rect(screen, self.color, item)

    def use(self, screen, world, mouse_pos):
        self.usage(screen, self, world, mouse_pos)
