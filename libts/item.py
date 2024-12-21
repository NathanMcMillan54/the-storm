from typing import Optional
from libts.block import *

def empty_use(mouse_pos, world):
    return world

def place_block(world, item):
    if item.count == 0:
        return world

    x_pos, y_pos = world.mouse_pos
    x_pos = round(x_pos / 10)
    y_pos = round(y_pos / 10)
    player_x = round(world.player.x / 10) * 10
    player_y = round(world.player.y / 10) * 10

    x_distance = abs(player_x - x_pos)
    y_distance = abs(player_y - y_pos)

    if x_distance > 3 or y_distance > 3:
        return world
    world.blocks[y_pos][x_pos] = item.id

    return world

class Item:
    def __init__(self, block: Optional[Block], id=None, name=None, use_fun=None, count=0) -> None:
        self.block = block
        if block != None:
            self.name = block.name
            self.id = block.id
        else:
            self.name = name
            self.id = id
        self.use_fun = use_fun
        self.count = count

# A dictonary of all items
ITEMS = {
    NULL_BLOCK: Item(BLOCKS[NULL_BLOCK], 0, use_fun=place_block),
    AIR_BLOCK: Item(BLOCKS[AIR_BLOCK], 0, use_fun=empty_use),
    GRASS_BLOCK: Item(BLOCKS[GRASS_BLOCK], 0, use_fun=place_block),
    DIRT_BLOCK: Item(BLOCKS[DIRT_BLOCK], 0),
    GROUND_WOOD_BLOCK: Item(BLOCKS[GROUND_WOOD_BLOCK], 0),
    STORM_BLOCK: Item(BLOCKS[STORM_BLOCK], 0),

    STONE_BLOCK: Item(BLOCKS[STONE_BLOCK], 0),
    UNDERGROUND_VINE: Item(BLOCKS[UNDERGROUND_VINE])
}
