import pygame


class Block:
    def __init__(self, name, id, color, solid):
        self.name = name
        self.id = id
        self.color = color
        self.solid = solid

    def display(self, x, y, screen):
        block = pygame.Rect((x * 10, y * 10), (10, 10))

        pygame.draw.rect(screen, self.color, block)


AIR = 0
GRASS = 1
DIRT = 2
GROUNDWOOD = 8

blocks = {
    # Air, 0
    0: Block("Air", 0, (168, 202, 255), False),
    # Grass, 1
    1: Block("Grass", 1, (12, 117, 0), True),
    # Dirt, 2
    2: Block("Dirt", 2, (135, 74, 0), True),
    # "Storm", 6
    6: Block("Storm", 6, (105, 151, 201), False),
    # "Ground Wood", 8
    8: Block("Ground Wood", 8, (82, 20, 1), True),
    # "Cut Ground Wood"
    9: Block("Cut Ground Wood", 9, (133, 77, 34), True),
    # Door
    11: Block("Door", 11, (173, 121, 0), False),
    # "Ground Wood Wall"
    12: Block("Ground Wood Wall", 12, (94, 51, 1), False),
    # Stone
    15: Block("Stone", 15, (153, 144, 144), True),
    # Underground Vine
    16: Block("Underground Vine", 16, (13, 97, 0), True),
}
