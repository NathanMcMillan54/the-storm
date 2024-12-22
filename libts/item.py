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
    if BLOCKS[world.world_data.blocks[y_pos + 1][x_pos]].solid == False:
        return False

    player_x = round(world.player.x / 10) * 10
    player_y = round(world.player.y / 10) * 10

    x_distance = abs(player_x - x_pos)
    y_distance = abs(player_y - y_pos)

    if x_distance > 3 or y_distance > 3:
        return False
    world.world_data.blocks[y_pos][x_pos] = item.id

    return True

def remove_block(world, item):
    x_pos, y_pos = world.mouse_pos
    x_pos = round(x_pos / 10)
    y_pos = round(y_pos / 10)

    block = BLOCKS[world.world_data.blocks[y_pos][x_pos]]
    if block.solid == False:
        return False

    for i in range(len(world.player.inventory.current_items)):
        if world.player.inventory.current_items[i].name == block.name:
            world.player.inventory.current_items[i].count += 1
            world.world_data.blocks[y_pos][x_pos] = AIR_BLOCK
            return True
    
    for i in range(len(world.player.inventory.stored_items)):
        if world.player.inventory.stored_items[i].name == block.name:
            world.player.inventory.stored_items[i].count += 1
            world.world_data.blocks[y_pos][x_pos] = AIR_BLOCK
            return True
    
    # Add item to inventory
    for i in range(len(world.player.inventory.current_items)):
        if world.player.inventory.current_items[i].name == ITEMS[NULL_BLOCK].name:
            world.player.inventory.current_items[i] = ITEMS[block.id]
            world.player.inventory.current_items[i].count = 1
            world.world_data.blocks[y_pos][x_pos] = AIR_BLOCK
            return True
    
    for i in range(len(world.player.inventory.stored_items)):
        if world.player.inventory.stored_items[i].name == ITEMS[NULL_BLOCK].name:
            world.player.inventory.stored_items[i] = ITEMS[block.id]
            world.player.inventory.stored_items[i].count = 1
            world.world_data.blocks[y_pos][x_pos] = AIR_BLOCK
            return True

    return False

def use_sword(world, item):
    return False

class Item:
    def __init__(self, block: Optional[Block], id=None, name=None, use_fun=None, count=0, color=(0, 0, 0)) -> None:
        self.block = block
        if block != None:
            self.name = block.name
            self.id = block.id
            self.color = block.color
        else:
            self.name = name
            self.id = id
            self.color = color
        self.use_fun = use_fun
        self.count = count

# Item Ids
PICKAXE = 6
SWORD = 7

# A dictonary of all items
ITEMS = {
    NULL_BLOCK: Item(BLOCKS[NULL_BLOCK], 0, use_fun=place_block),
    AIR_BLOCK: Item(BLOCKS[AIR_BLOCK], 0, use_fun=empty_use),
    GRASS_BLOCK: Item(BLOCKS[GRASS_BLOCK], 0, use_fun=place_block),
    DIRT_BLOCK: Item(BLOCKS[DIRT_BLOCK], 0),
    GROUND_WOOD_BLOCK: Item(BLOCKS[GROUND_WOOD_BLOCK], 0),
    STORM_BLOCK: Item(BLOCKS[STORM_BLOCK], 0),
    PICKAXE: Item(id=PICKAXE, name="Pick Axe", use_fun=remove_block, block=None),
    SWORD: Item(id=SWORD, name="Sword", use_fun=use_sword, block=None),

    STONE_BLOCK: Item(BLOCKS[STONE_BLOCK], 0),
    UNDERGROUND_VINE: Item(BLOCKS[UNDERGROUND_VINE])
}
