import json
import random
import sys

import pygame
import pygame.rect
import pygame.rect

from game.player import *
from libts.block import *
from libts.item import ITEMS
from libts.world import WorldData, WORLD_HEIGHT, WORLD_WIDTH

class World:
    def __init__(self, world_file):
        self.left_click = 0
        self.right_click = 0
        self.mouse_pos = (0, 0)
        world_data = WorldData()
        world_data.open(world_file)
        self.world_data = world_data
        self.player = Player((255, 0, 0))
        self.player.inventory.from_inventory_data(self.world_data.inventory_data)

    def display(self, screen):
        # Display blocks
        for y in range(WORLD_HEIGHT):
            for x in range(WORLD_WIDTH):
                block = BLOCKS[self.world_data.blocks[y][x]]
                pygame.draw.rect(screen, block.color, pygame.rect.Rect((x * BLOCK_SIZE, y * BLOCK_SIZE), (BLOCK_SIZE, BLOCK_SIZE)))
        
        # Display current inventory
        for ci in range(len(self.world_data.inventory_data.current_inventory)):
            block = BLOCKS[self.player.inventory.current_items[ci].id]
            item_count_text = pygame.font.SysFont('Arial', 10).render(f"{self.player.inventory.current_items[ci].count}", True, (0, 0, 0))
            pygame.draw.rect(screen, block.color, pygame.rect.Rect((900 + (ci * 15), 10), (BLOCK_SIZE, BLOCK_SIZE)))
            screen.blit(item_count_text, (900 + (ci * 15), 11))
        
        item_selected_text = pygame.font.SysFont('Arial', 12).render(f"{self.player.inventory.current_items[self.player.inventory_item_selected].name}", True, (0, 0, 0))
        screen.blit(item_selected_text, (900, 20))

        pygame.draw.rect(screen, self.player.color, pygame.rect.Rect((self.player.x * BLOCK_SIZE, self.player.y * BLOCK_SIZE), PLAYER_SIZE))

        # Display all inventory

    def update(self):
        if self.player.inventory_open:
            # todo
            x_pos, y_pos = self.mouse_pos
        else:
            if self.left_click == 1:
                item = self.player.inventory.current_items[self.player.inventory_item_selected]
                item.use_fun(self, item)

        player_on_block = self.world_data.blocks[self.player.y + 2][self.player.x]
        if BLOCKS[player_on_block].solid == False:
            self.player.my = 0
            self.player.y += 1
        for y in range(2):
            block = BLOCKS[self.world_data.blocks[self.player.y + y][self.player.x]]
            if block.solid == True:
                if self.player.right:
                    self.player.x -= 1
                else:
                    self.player.x += 1
                self.player.mx = 0

        if self.player.mx > 0:
            self.player.right = True
        elif self.player.mx < 0:
            self.player.right = False

        self.player.x += self.player.mx
        self.player.y += self.player.my
        self.player.mx = 0
        self.player.my = 0
