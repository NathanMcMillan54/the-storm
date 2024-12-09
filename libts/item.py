from typing import Optional
from libts.block import *

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
    NULL_BLOCK: Item(BLOCKS[NULL_BLOCK], 0),
    AIR_BLOCK: Item(BLOCKS[AIR_BLOCK], 0),
    GRASS_BLOCK: Item(BLOCKS[GRASS_BLOCK], 0),
    DIRT_BLOCK: Item(BLOCKS[DIRT_BLOCK], 0),
    GROUND_WOOD_BLOCK: Item(BLOCKS[GROUND_WOOD_BLOCK], 0),
    STORM_BLOCK: Item(BLOCKS[STORM_BLOCK], 0),

    STONE_BLOCK: Item(BLOCKS[STONE_BLOCK], 0),
    UNDERGROUND_VINE: Item(BLOCKS[UNDERGROUND_VINE])
}
