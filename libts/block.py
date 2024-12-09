BLOCK_SIZE = 10

class Block:
    def __init__(self, name: str, id: int, color: (int, int, int), solid: bool, durable: bool) -> None:
        self.name = name
        self.id = id
        self.color = color
        self.solid = solid
        self.durable = durable

# All block Ids
NULL_BLOCK = 0
AIR_BLOCK = 1
GRASS_BLOCK = 2
DIRT_BLOCK = 3
GROUND_WOOD_BLOCK = 4
STORM_BLOCK = 5

STONE_BLOCK = 15
UNDERGROUND_VINE = 16

# A dictonary of all blocks
BLOCKS = {
    NULL_BLOCK: Block("null", NULL_BLOCK, (0, 0, 0), False, False),
    AIR_BLOCK: Block("Air", AIR_BLOCK, (168, 202, 255), False, False),
    GRASS_BLOCK: Block("Grass", GRASS_BLOCK, (12, 117, 0), True, False),
    DIRT_BLOCK: Block("Dirt", DIRT_BLOCK, (135, 74, 0), True, False),
    GROUND_WOOD_BLOCK: Block("Ground Wood", GROUND_WOOD_BLOCK, (82, 20, 1), True, True),
    STORM_BLOCK: Block("Storm", STORM_BLOCK, (105, 151, 201), False, False),

    STONE_BLOCK: Block("Stone", STONE_BLOCK, (153, 144, 144), True, True),
    UNDERGROUND_VINE: Block("Underground Vine", UNDERGROUND_VINE, (13, 97, 0), False, False)
}
