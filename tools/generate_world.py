import random
import sys

from libts.block import *
from libts.world import WorldData, WORLD_HEIGHT, WORLD_WIDTH

sections = [
    [AIR_BLOCK, AIR_BLOCK],
    [AIR_BLOCK, GRASS_BLOCK, GRASS_BLOCK, GRASS_BLOCK, AIR_BLOCK, AIR_BLOCK],
    [GRASS_BLOCK, GRASS_BLOCK],
    [GROUND_WOOD_BLOCK, DIRT_BLOCK, DIRT_BLOCK, DIRT_BLOCK],
    [DIRT_BLOCK, DIRT_BLOCK, GROUND_WOOD_BLOCK, DIRT_BLOCK, DIRT_BLOCK, GROUND_WOOD_BLOCK, DIRT_BLOCK, DIRT_BLOCK],
    [DIRT_BLOCK, DIRT_BLOCK, DIRT_BLOCK, DIRT_BLOCK, DIRT_BLOCK, DIRT_BLOCK, STONE_BLOCK, DIRT_BLOCK, DIRT_BLOCK, STONE_BLOCK, DIRT_BLOCK, UNDERGROUND_VINE, DIRT_BLOCK, DIRT_BLOCK],
]

def main(world_name):
    new_world = WorldData()

    for y in range(WORLD_HEIGHT):
        for x in range(WORLD_WIDTH):
           # if x == 0:
            #    print(f"{y}: {new_world.blocks[0]}")

            if y <= 30:
                new_world.blocks[y][x] = sections[0][random.randint(0, len(sections[0]) - 1)]
                continue
            elif y == 31:
                new_world.blocks[y][x] = sections[1][random.randint(0, len(sections[1]) - 1)]
                continue
            elif y == 32:
                new_world.blocks[y][x] = sections[2][random.randint(0, len(sections[2]) - 1)]
                continue
            elif 36 > y > 32:
                new_world.blocks[y][x] = sections[3][random.randint(0, len(sections[3]) - 1)]
                continue
            elif 42 > y >= 36:
                new_world.blocks[y][x] = sections[4][random.randint(0, len(sections[4]) - 1)]
                continue
            elif y >= 42:
                new_world.blocks[y][x] = sections[5][random.randint(0, len(sections[5]) - 1)]
                continue
            
            print(f"skipped {y}")
    
    print(new_world.blocks[0])
    new_world.write(f"world{world_name}.json")


if __name__ == '__main__':
    world_name = sys.argv[1]
    main(world_name)
