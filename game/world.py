import json
import random
import sys

import pygame.display

from game.block import blocks
from game.player import *
from game.npc import Npc


class World:
    def __init__(self, world_file):
        self.file = world_file
        self.day = 0
        self.time = 0.0
        self.storm = False
        self.player = Player((255, 0, 0))
        self.npcs = []
        self.screen = pygame.display.set_mode((1100, 600))
        self.running = False

        file_contents = open(self.file).read()
        json_file = json.loads(file_contents)

        self.day = json_file['day']

    def display(self):
        file_contents = open(self.file)
        json_file = json.loads(file_contents.read())

        for y in range(61):
            for x in range(111):
                block = list(json_file[f'y{y}'].values())[x]

                if self.storm:
                    if block == 0:
                        json_file[f'y{y}'][x] = 6
                        block = 6
                else:
                    if block == 6:
                        json_file[f'y{y}'][x] = 0
                        block = 0

                blocks[block].display(x, y, self.screen)

    def get_block(self, x: int, y: int):
        file_contents = open(self.file)
        json_file = json.loads(file_contents.read())

        block = list(json_file[f'y{y}'].values())[x]

        return blocks[block]

    def set_block(self, x: int, y: int, block: int):
        file_contents = open(self.file).read()
        json_file = json.loads(file_contents)

        json_file[f'y{round(y)}'][f'x{round(x)}'] = block
        file = open(self.file, "w+")
        file.writelines(json.dumps(json_file))
        file.close()

        # self.file = json.dumps(self.world_file)

    def update_player(self, mouse_pos):
        self.player.update(self.screen, self, mouse_pos)

        json_file = json.loads(open(self.file).read())

        for i in range(0, len(json_file['inventory']) - 1):
            json_file['inventory'][i][0] = self.player.inventory[i].id
            json_file['inventory'][i][1] = self.player.inventory[i].count

        file = open(self.file, "w+")
        file.writelines(json.dumps(json_file))
        file.close()

    def spawn_npcs(self):
        chance = random.uniform(0.0, 100.0)

        if self.storm:
            if chance <= 0.9:
                self.npcs.append(Npc("Storm Monster", 0.1, 20, True, random.randint(19, 21), (153, 233, 255), False, (0, 0, 0), 0))
                self.npcs[len(self.npcs) - 1].x = random.randint(10, 80)
                self.npcs[len(self.npcs) - 1].y = random.randint(20, 30)
            if chance <= 0.09:
                self.npcs.append(Npc("Storm Wizard", 0.06, 120, True, random.randint(12, 19), (147, 135, 255), True, (83, 188, 252), 14))
                self.npcs[len(self.npcs) - 1].x = random.randint(10, 80)
                self.npcs[len(self.npcs) - 1].y = random.randint(20, 30)
        else:
            if chance <= 0.3:
                self.npcs.append(Npc("Zombie", 0.09, 100, True, random.randint(5, 8), (0, 255, 0), False, (0, 0, 0), 13))
                self.npcs[len(self.npcs) - 1].x = random.randint(10, 80)
                self.npcs[len(self.npcs) - 1].y = random.randint(20, 30)

    def update_storm(self):
        if self.storm:
            block = self.get_block(self.player.x, self.player.y - 2)

            if block.id == 0:
                has_coat = False

                for item in self.player.inventory:
                    if item.id == 14:
                        has_coat = True

                if not has_coat:
                    self.player.health -= random.uniform(0.2, 0.5)

        if self.day == 7:
            self.storm = True
        if self.day == 8:
            self.storm = False
            self.day = 0

    def update_time(self):
        self.time += 0.5

        if self.time >= 600.0:
            self.day += 1
            self.time = 0.0
            self.npcs = []

            file_contents = open(self.file).read()
            json_file = json.loads(file_contents)

            json_file['day'] = self.day
            file = open(self.file, "w+")
            file.writelines(json.dumps(json_file))
            file.close()

    def open(self):
        json_file = json.loads(open(self.file).read())

        for inv_ic in json_file['inventory']:
            item = items[inv_ic[0]]
            item.count = inv_ic[1]

            self.player.inventory.append(item)

        clock = pygame.time.Clock()
        self.running = True

        while self.running:
            g_event = None

            if not self.player.alive:
                self.running = False

            self.update_time()
            self.update_storm()

            player_movement = []
            mouse_pos = (0, 0)
            for event in pygame.event.get():
                g_event = event
                if event.type == pygame.QUIT:
                    sys.exit(0)

                if event.type == pygame.KEYDOWN:
                    key = pygame.key.get_pressed()
                    if event.key == pygame.K_ESCAPE:
                        if self.player.inventory_open:
                            self.player.inventory_open = False
                        else:
                            sys.exit(0)
                    if key[pygame.K_w]:
                        self.player.my -= random.randint(1, 2)
                    elif key[pygame.K_d]:
                        self.player.mx += 1
                    #elif key[pygame.K_s]:
                     #   self.player.my += 1
                    elif key[pygame.K_a]:
                        self.player.mx -= 1
                    elif key[pygame.K_e]:
                        self.player.inventory_open = True

                    if key[pygame.K_w] and key[pygame.K_d]:
                        self.player.mx += 1
                        self.player.my -= 2
                    elif key[pygame.K_w] and key[pygame.K_a]:
                        self.player.mx -= 1
                        self.player.my -= 2
                    # elif key[pygame.K_s] and key[pygame.K_d]:
                    #     self.player.mx += 1
                    #     self.player.my += 1
                    # elif key[pygame.K_s] and key[pygame.K_a]:
                    #     self.player.mx -= 1
                    #     self.player.my += 2

                    if key[pygame.K_1]:
                        self.player.selected_item = 1
                    elif key[pygame.K_2]:
                        self.player.selected_item = 2
                    elif key[pygame.K_3]:
                        self.player.selected_item = 3
                    elif key[pygame.K_4]:
                        self.player.selected_item = 4
                    elif key[pygame.K_5]:
                        self.player.selected_item = 5
                    elif key[pygame.K_6]:
                        self.player.selected_item = 6
                    elif key[pygame.K_7]:
                        self.player.selected_item = 7
                    elif key[pygame.K_8]:
                        self.player.selected_item = 8
                    elif key[pygame.K_9]:
                        self.player.selected_item = 9

                if event.type == pygame.MOUSEBUTTONUP:
                    mouse_pos = event.pos
                    self.player.use_item = True

                    if self.player.inventory_open:
                        self.player.display_inventory(self.screen, event)


            self.screen.fill((0, 0, 0))
            self.display()
            self.update_player(mouse_pos)
            self.player.display(self.screen)

            for npc in range(0, len(self.npcs) - 1):
                self.npcs[npc].update(self)

                if not self.npcs[npc].alive:
                    self.npcs.remove(self.npcs[npc])

                self.npcs[npc].display(self.screen)

            if self.player.inventory_open:
                self.player.display_inventory(self.screen, None)

            self.spawn_npcs()

            json_file = json.loads(open(self.file).read())
            text = pygame.font.SysFont('Arial', 10).render(f"Day: {json_file['day']}", True, (0, 0, 0))
            self.screen.blit(text, (865, 10))

            clock.tick(15)

            pygame.display.flip()
