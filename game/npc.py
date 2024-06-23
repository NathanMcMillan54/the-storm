from game.items import items
import random

import pygame


class Npc:
    def __init__(self, name, speed, health, hostile, damage, color, ranged, proj_color, item):
        self.name = name
        self.right = True
        self.speed = speed
        self.health = health
        self.alive = True
        self.hostile = hostile
        self.ranged = ranged
        self.proj_info = (1, 1, False)
        self.proj_color = proj_color
        self.damage = damage
        self.color = color
        self.x = random.randint(5, 100)
        self.y = random.randint(28, 32)
        self.y = 0
        self.drop_item = item
        self.my = 0
        self.mx = 0
        self.first_update = True

    def update(self, world):
        if self.x <= 0:
            self.x = 1
        elif self.x >= 1000:
            self.x = 1000

        if self.health <= 0:
            found_item = False
            for i in range(0, len(world.player.inventory) - 1):
                if world.player.inventory[i].id == self.drop_item:
                    found_item = True
                    world.player.inventory[i].count += 1
                    break

            if not found_item:
                for i in range(0, len(world.player.inventory) - 1):
                    if world.player.inventory[i].id == 0:
                        world.player.inventory[i] = items[self.drop_item]
                        break

            self.alive = False

        ud_near_blocks = [world.get_block(round(self.x), round(self.y) - 1), world.get_block(round(self.x), round(self.y)), world.get_block(round(self.x), round(self.y) + 1)]
        lr_near_blocks = [world.get_block(round(self.x - 1), round(self.y)), world.get_block(round(self.x), round(self.y - 2)), (world.get_block(round(self.x + 1), round(self.y)))]

        if not ud_near_blocks[0].solid:
            self.y += 1

        if lr_near_blocks[1].solid:
            if world.get_block(round(self.x), round(self.y - 3)).solid:
                if self.right:
                    self.x -= 1
                else:
                    self.x += 1
            else:
                self.y -= 1

        if self.my > 0:
            if ud_near_blocks[0].solid:
                self.y -= 1

        if self.hostile:
            if not self.ranged:
                if self.x > world.player.x:
                    self.right = False
                    self.x -= self.speed
                elif self.x < world.player.x:
                    self.x += self.speed
                    self.right = True

                if world.get_block(round(self.x), round(self.y - 3)).id == 11:
                    if self.right:
                        self.x -= self.speed
                    else:
                        self.x += self.speed
            else:
                x, y, on = self.proj_info

                if on:
                    if x < world.player.x:
                        x += 1
                    elif x > world.player.x:
                        x -= 1

                    if y < world.player.y:
                        y += 1
                    elif y > world.player.y:
                        y -= 1

                    self.proj_info = (x, y, on)
                else:
                    self.proj_info = (self.x + 1, self.y, True)

    def display(self, screen):
        npc_body = pygame.Rect(round(self.x) * 10, round(self.y) * 10 - 30, 10, 20)

        pygame.draw.rect(screen, self.color, npc_body)

        x, y, on = self.proj_info

        if on:
            pygame.draw.rect(screen, self.proj_color, pygame.Rect(round(x) * 10, round(y) * 10 - 30, 5, 5))
