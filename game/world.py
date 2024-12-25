import json
import random
import sys
import math
import pygame
import pygame.rect
import pygame.rect
import pygame.rect

from game.player import *
from game.npc import Npc
from libts.block import *
from libts.item import ITEMS
from libts.world import WorldData, WORLD_HEIGHT, WORLD_WIDTH

class World:
    def __init__(self, world_file):
        self.left_click = 0
        self.right_click = 0
        self.mouse_pos = (0, 0)
        self.strom_running = False
        world_data = WorldData()
        world_data.open(world_file)
        self.world_data = world_data
        self.player = Player((255, 0, 0))
        self.player.inventory.from_inventory_data(self.world_data.inventory_data)
        self.npcs = []

    def display(self, screen):
        # Display blocks
        for y in range(WORLD_HEIGHT):
            for x in range(WORLD_WIDTH):
                block = BLOCKS[self.world_data.blocks[y][x]]
                pygame.draw.rect(screen, block.color, pygame.rect.Rect((x * BLOCK_SIZE, y * BLOCK_SIZE), (BLOCK_SIZE, BLOCK_SIZE)))
        
        # Display current inventory
        for ci in range(len(self.world_data.inventory_data.current_inventory)):
            item = ITEMS[self.player.inventory.current_items[ci].id]
            item_count_text = pygame.font.SysFont('Arial', 10).render(f"{self.player.inventory.current_items[ci].count}", True, (0, 0, 0))
            pygame.draw.rect(screen, item.color, pygame.rect.Rect((900 + (ci * 15), 10), (BLOCK_SIZE, BLOCK_SIZE)))
            screen.blit(item_count_text, (900 + (ci * 15), 11))
        
        item_selected_text = pygame.font.SysFont('Arial', 12).render(f"{self.player.inventory.current_items[self.player.inventory_item_selected].name}", True, (0, 0, 0))
        screen.blit(item_selected_text, (900, 20))
        time_day_text = pygame.font.SysFont('Arial', 12).render(f"Time: {round(self.world_data.time, 2)} Day: {self.world_data.day}", True, (0, 0, 0))
        screen.blit(time_day_text, (15, 75))

        health_length = round(self.player.health) * 3
        health_background = 310
        pygame.draw.rect(screen, (75, 0, 0), pygame.rect.Rect(10, 10, health_background, 60))
        pygame.draw.rect(screen, (255, 0, 0), pygame.rect.Rect(15, 15, health_length, 50))

        pygame.draw.rect(screen, self.player.color, pygame.rect.Rect((self.player.x * BLOCK_SIZE, self.player.y * BLOCK_SIZE), PLAYER_SIZE))

        for i in range(len(self.npcs)):
            pygame.draw.rect(screen, self.npcs[i].color, pygame.rect.Rect((self.npcs[i].x * BLOCK_SIZE, self.npcs[i].y * BLOCK_SIZE), PLAYER_SIZE))

        # Display all inventory
    
    def on_block(self, x, y):
        on_block = self.world_data.blocks[y + 2][x]
        if BLOCKS[on_block].solid == False:
            return False
        #for y in range(2):
         #   block = BLOCKS[self.world_data.blocks[self.player.y + y][self.player.x]]
          #  if block.solid == True:
           #     if self.player.right:
            #        self.player.x -= 1
             #   else:
              #      self.player.x += 1
              #  self.player.mx = 0
        return True
    
    def in_block(self, x, y):
        for check_y in range(2):
            block = BLOCKS[self.world_data.blocks[y + check_y][x]]
            if block.solid == True:
                return True
        return False

    def update(self):
        if self.strom_running:
            if self.world_data.day == 6:
                self.strom_running = False
                self.world_data.time = 0.0
                self.world_data.day = 0
            if self.world_data.blocks[self.player.y][self.player.x] == STORM_BLOCK:
                self.player.health -= 0.05

        if self.player.inventory_open:
            # todo
            x_pos, y_pos = self.mouse_pos
        else:
            if self.left_click == 1:
                item = self.player.inventory.current_items[self.player.inventory_item_selected]
                use_fun_ret = item.use_fun(self, item)
                # Place block
                if use_fun_ret == True and item.block != None:
                    self.player.inventory.current_items[self.player.inventory_item_selected].count -= 1
                # Use tool
                elif use_fun_ret == True and item.block == None:
                    ###
                    1 + 1

        player_on_block = self.world_data.blocks[self.player.y + 2][self.player.x]
        
        #if BLOCKS[player_on_block].solid == False:
            #self.player.my = 0
            #self.player.y += 1
        if not self.on_block(self.player.x, self.player.y):
            self.player.my = 0
            self.player.y += 1
        if self.in_block(self.player.x, self.player.y):
            if self.player.right:
                self.player.x -= 1
                self.player.mx = 0
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

        for npc in range(len(self.npcs)):
            self.npcs[npc].update(self.player)
            if not self.on_block(self.npcs[npc].x, self.npcs[npc].y):
                self.npcs[npc].y += 1
            if self.in_block(self.npcs[npc].x, self.npcs[npc].y):
                if self.npcs[npc].moving_right:
                    self.npcs[npc].x -= 1
                else:
                    self.npcs[npc].y += 1
        
        self.world_data.time += 0.001
        minute, hour = math.modf(self.world_data.time)
        if hour == 24:
            self.world_data.time = 0.0
            self.world_data.day += 1
        if round(minute, 2) == 0.6:
            self.world_data.time -= 0.6
            self.world_data.time += 1
        if self.world_data.day == 5:
            self.strom_running = True
            for y in range(WORLD_HEIGHT):
                for x in range(WORLD_WIDTH):
                    if self.world_data.blocks[y][x] == AIR_BLOCK:
                        self.world_data.blocks[y][x] = STORM_BLOCK
