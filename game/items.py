import random
import time

import pygame

from game.item import Item, ItemType
from game.block import *


def update_item_count(world, id):
    found_in_items = False

    for i in range(1, len(world.player.inventory) - 10):
        if world.player.inventory[i].id == id:
            world.player.inventory[i].count -= 1
            if world.player.inventory[i].count == 0:
                world.player.inventory[i] = items[AIR]
                found_in_items = True
                break

    if found_in_items:
        return
    else:
        for i in range(1, len(world.player.inventory)):
            if world.player.inventory[i].id == id:
                world.player.inventory[i].count -= 1
                if world.player.inventory[i].count == 0:
                    world.player.inventory[i] = items[AIR]
                    found_in_items = True
                    break


def place_block(world, x: int, y: int, block: int):
    if world.player.x - 3 <= x <= world.player.x + 3 and world.player.y - 3 <= y <= world.player.y + 3:
        if world.get_block(x, y + 1).id == 0 or world.get_block(x, y + 1).id == 6 and world.get_block(x + 1, y).id == 0 or world.get_block(x + 1, y).id == 6 and world.get_block(x - 1, y).id == 0 or world.get_block(x - 1, y).id == 6:
            return
        else:
            world.set_block(x, y, block)
            update_item_count(world, block)


def replace_block(world, x: int, y: int, block: int):
    if world.player.x - 3 <= x <= world.player.x + 3 and world.player.y - 3 <= y <= world.player.y + 3:
        first_block = world.get_block(x, y)
        world.set_block(x, y, block)

        if not first_block.solid:
            return items[0]

        for i in range(0, len(items)):
            if items[i].name == first_block.name:
                return items[i]

    return items[0]


def use_nothing(screen, item, world, mouse):
    pass


def use_woodsword(screen, item, world, mouse):
    x_pos = world.player.x * 10

    if world.player.right:
        x_pos += 10
    else:
        x_pos -= 20

    sword_display = pygame.Rect((x_pos, world.player.y * 10 - 30), (20, 10))

    for npc in world.npcs:
        if sword_display.collidepoint(npc.x * 10, npc.y * 10 - 30):
            npc.health -= 10
            if npc.right:
                npc.x += 1
            else:
                npc.x -= 1

    pygame.draw.rect(screen, item.color, sword_display)

    return world


def use_stonesword(screen, item, world, mouse):
    x_pos = world.player.x * 10

    if world.player.right:
        x_pos += 10
    else:
        x_pos -= 20

    sword_display = pygame.Rect((x_pos, world.player.y * 10 - 30), (20, 10))

    for npc in world.npcs:
        if sword_display.collidepoint(npc.x * 10, npc.y * 10 - 30):
            npc.health -= 19
            if npc.right:
                npc.x += 1
            else:
                npc.x -= 1

    pygame.draw.rect(screen, item.color, sword_display)

    return world

def use_dirt(screen, item, world, mouse):
    (x, y) = mouse

    place_block(world, round(x / 10), round(y / 10), DIRT)

    return world


def use_pickaxe(screen, item, world, mouse):
    (mx, my) = mouse
    x_pos = world.player.x * 10

    if world.player.right:
        x_pos += 10
    else:
        x_pos -= 20

    pickaxe_display = pygame.Rect((x_pos, world.player.y * 10 - 30), (20, 10))

    pygame.draw.rect(screen, item.color, pickaxe_display)

    block = replace_block(world, round(mx / 10), round(my / 10), AIR)
    new_item = items[block.id]

    if new_item.id == 0:
        return world

    for i in range(1, 10):
        if world.player.inventory[i].id == new_item.id:
            world.player.inventory[i].count += 1
            return world

    for ii in range(1, 10):
        if world.player.inventory[ii].id == 0:
            world.player.inventory[ii] = new_item
            return world

    return world


def use_grass(screen, item, world, mouse):
    (x, y) = mouse

    place_block(world, round(x / 10), round(y / 10), GRASS)

    return world


def use_groundwood(screen, item, world, mouse):
    (x, y) = mouse

    place_block(world, round(x / 10), round(y / 10), GROUNDWOOD)

    return world


def use_door(screen, item, world, mouse):
    (x, y) = mouse

    place_block(world, round(x / 10), round(y / 10), 11)
    place_block(world, round(x / 10), round(y / 10) - 1, 11)

    return world


def use_cgw(screen, item, world, mouse):
    (x, y) = mouse

    place_block(world, round(x / 10), round(y / 10), 9)

    return world


def use_gww(screen, item, world, mouse):
    (x, y) = mouse

    place_block(world, round(x / 10), round(y / 10), 12)

    return world


def use_meat(screen, item, world, mouse):
    world.player.health += random.randint(12, 24)

    update_item_count(world, 13)

    if world.player.health >= 100.0:
        world.player.health = 100.0

    return world


def use_stone(screen, item, world, mouse):
    x, y = mouse

    place_block(world, round(x / 10), round(y / 10), 15)

    return world


def use_ugv(screen, item, world, mouse):
    x, y = mouse

    place_block(world, round(x / 10), round(y / 10), 16)

    return world


def use_bow(screen, item, world, mouse):
    has_arrows = False
    ind = 0

    for i in range(0, len(world.player.inventory) - 1):
        if world.player.inventory[i].id == 20:
            has_arrows = True
            ind = i
            break

    if not has_arrows:
        return world

    if world.player.right:
        arrow_streak = pygame.Rect(world.player.x * 10, (world.player.y * 10) - 30, 1100, 2)

        pygame.draw.rect(screen, (105, 73, 39), arrow_streak)

        for i in range(0, len(world.npcs) - 1):
            if world.npcs[i].x >= world.player.x:
                world.npcs[i].health -= random.randint(9, 13)
    else:
        arrow_streak = pygame.Rect(0, (world.player.y * 10) - 30, world.player.x * 10, 2)

        pygame.draw.rect(screen, (105, 73, 39), arrow_streak)

        for i in range(0, len(world.npcs) - 1):
            if world.npcs[i].x <= world.player.x:
                world.npcs[i].health -= random.randint(9, 13)

    world.player.inventory[ind].count -= 1

    return world

items = {
    # An empty item
    0: Item("Nothing", 0, ItemType.BLOCK, False, (255, 255, 255), use_nothing),
    1: Item("Grass", 1, ItemType.BLOCK, True, (12, 117, 0), use_grass),
    2: Item("Dirt", 2, ItemType.BLOCK, True, (255, 50, 50), use_dirt),
    3: Item("Void", 3, ItemType.BLOCK, False, (0, 0, 0), use_nothing),
    4: Item("Sword", 4, ItemType.TOOL, False, (0, 0, 0), use_nothing),
    5: Item("Pick Axe", 5, ItemType.TOOL, True, (50, 50, 50), use_pickaxe),
    6: Item("Storm", 6, ItemType.BLOCK, False, (105, 151, 201), use_nothing),
    7: Item("Void", 7, ItemType.BLOCK, False, (0, 0, 0), use_nothing),
    8: Item("Ground Wood", 8, ItemType.BLOCK, True, (82, 20, 1), use_groundwood),
    9: Item("Cut Ground Wood", 9, ItemType.BLOCK, True, (133, 77, 34), use_cgw),
    10: Item("Sticks", 10, ItemType.TOOL, False, (97, 55, 0), use_nothing),
    11: Item("Door", 11, ItemType.BLOCK, True, (173, 121, 0), use_door),
    12: Item("Ground Wood Wall", 12, ItemType.BLOCK, True, (94, 51, 1), use_gww),
    13: Item("Meat", 13, ItemType.FOOD, False, (186, 71, 35), use_meat),
    14: Item("Storm Coat", 14, ItemType.TOOL, False, (0, 9, 135), use_nothing),
    15: Item("Stone", 15, ItemType.BLOCK, True, (153, 144, 144), use_stone),
    16: Item("Underground Vine", 16, ItemType.BLOCK, True, (13, 97, 0), use_ugv),
    17: Item("Wood Sword", 17, ItemType.TOOL, False, (87, 44, 10), use_woodsword),
    18: Item("Stone Sword", 18, ItemType.TOOL, False, (99, 99, 99), use_stonesword),
    19: Item("Bow", 19, ItemType.TOOL, False, (156, 110, 75), use_bow),
    20: Item("Arrow", 20, ItemType.TOOL, False, (143, 99, 51), use_nothing),
}
