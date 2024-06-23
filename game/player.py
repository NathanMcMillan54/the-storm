import random

import pygame
from game.asm import assemble
from game.block import *
from game.items import items

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

# TODO: Turn inventory into it's own file someday. Just so it's more organized

c_btns = [
    pygame.Rect(415, 205, 10, 10),
    pygame.Rect(430, 205, 10, 10),
    pygame.Rect(445, 205, 10, 10),

    pygame.Rect(415, 217, 10, 10),
    pygame.Rect(430, 217, 10, 10),
    pygame.Rect(445, 217, 10, 10),

    pygame.Rect(415, 229, 10, 10),
    pygame.Rect(430, 229, 10, 10),
    pygame.Rect(445, 229, 10, 10),
]

co_btn = pygame.Rect(460, 217, 10, 10)

class Player:
    def __init__(self, color):
        self.health = 100.0
        self.alive = True
        self.mx = 0
        self.my = 0
        self.x = 8
        self.y = random.randint(28, 32)
        self.right = True
        self.use_item = False
        self.inventory = []
        self.inventory_item_selected = items[0]
        self.inventory_open = False
        self.ci = [items[0]] * 10
        self.selected_item = 0
        self.color = color

    def display(self, screen):
        player_body = pygame.Rect(self.x * 10, self.y * 10 - 30, 10, 20)

        pygame.draw.rect(screen, self.color, player_body)

        health_bar_bg = pygame.Rect(8, 13, 303, 44)
        health_bar = pygame.Rect(10, 15, self.health * 3, 40)

        pygame.draw.rect(screen, (75, 50, 50), health_bar_bg)
        pygame.draw.rect(screen, (255, 0, 0), health_bar)

        if self.inventory[self.selected_item].show_grid:
            (x, y) = pygame.mouse.get_pos()
            highlight = pygame.Rect(round(x / 10) * 10, round(y / 10) * 10, 10, 10)

            pygame.draw.rect(screen, (255, 255, 0), highlight)

        for i in range(1, len(self.inventory) - 9):
            if i == self.selected_item:
                selected_box = pygame.Rect(899 + i * 15, 9, 12, 12)
                pygame.draw.rect(screen, (255, 255, 0), selected_box)

                font = pygame.font.SysFont('Arial', 15)
                text = font.render(f"{self.inventory[i].name} selected", True, (0, 0, 0))

                screen.blit(text, (900, 28))

            item_icon = pygame.Rect(900 + i * 15, 10, 10, 10)
            pygame.draw.rect(screen, self.inventory[i].color, item_icon)

            item_count_text = pygame.font.SysFont('Arial', 10).render(f"{self.inventory[i].count}", True, (0, 0, 0))

            screen.blit(item_count_text, (900 + i * 15, 10))

    def display_inventory(self, screen, event):
        inventory_background = pygame.Rect(395, 200, 200, 75)
        pygame.draw.rect(screen, (247, 239, 223), inventory_background)
        co_color = (255, 255, 255)
        asm_item = assemble(self.ci)

        ci_index = 0

        for btn in c_btns:
            ci_index += 1

            if event != None:
                if btn.collidepoint(event.pos):
                    if event.button == 3:
                        if self.ci[ci_index].id == 0:
                            self.ci[ci_index] = self.inventory_item_selected
                            # self.ci[ci_index].count = 1
                            # self.inventory[self.selected_item].count -= 1
                            for i in range(0, len(self.inventory) - 1):
                                if self.inventory[i].id == self.inventory_item_selected.id:
                                    self.inventory[i].count -= 1
                                    if self.inventory[i].count <= 0:
                                        self.inventory_item_selected = items[0]
                                        return
                                    break
                            break
                        elif self.ci[ci_index].id == self.inventory_item_selected.id:
                            found_item = False
                            for i in range(0, len(self.inventory) - 1):
                                if self.inventory[i].id == self.ci[ci_index].id:
                                    found_item = True
                                    self.inventory[i].count += 1
                                    self.ci[ci_index] = items[0]
                                    break

                            if not found_item:
                                self.inventory.append(self.ci[ci_index])
                        else:
                            self.ci[ci_index].count += 1

            pygame.draw.rect(screen, self.ci[ci_index].color, btn)

            if event != None:
                if co_btn.collidepoint(event.pos):
                    if asm_item.id != items[0].id:
                        added_item = False

                        for i in range(0, len(self.inventory)):
                            self.ci = [items[0]] * 10
                            if self.inventory[i].id == asm_item.id:
                                self.inventory[i].count += 1
                                added_item = True
                                break

                        if not added_item:
                            for i in range(0, len(self.inventory)):
                                if self.inventory[i].id == items[0].id:
                                    self.inventory[i] = asm_item
                                    break
                            break

        for i in range(1, 10):
            item_icon = pygame.Rect(400 + i * 15, 250, 10, 10)
            pygame.draw.rect(screen, self.inventory[i].color, item_icon)

            if event != None:
                if event.button == 1:
                    if item_icon.collidepoint(event.pos):
                        self.inventory_item_selected = self.inventory[i]

            item_count_text = pygame.font.SysFont('Arial', 10).render(f"{self.inventory[i].count}", True, (0, 0, 0))

            screen.blit(item_count_text, (400 + i * 15, 250))

        for i in range(1, 10):
            item_icon = pygame.Rect(400 + i * 15, 262, 10, 10)
            pygame.draw.rect(screen, self.inventory[i + 10].color, item_icon)

            if event != None:
                if event.button == 1:
                    if item_icon.collidepoint(event.pos):
                        self.inventory_item_selected = self.inventory[i + 10]

            item_count_text = pygame.font.SysFont('Arial', 10).render(f"{self.inventory[i + 10].count}", True,
                                                                      (0, 0, 0))
            screen.blit(item_count_text, (400 + i * 15, 262))

        co_text = pygame.font.SysFont('Arial', 10).render(f"{asm_item.name}", True, (0, 0, 0))
        screen.blit(co_text, (460, 227))

        co_color = asm_item.color
        pygame.draw.rect(screen, co_color, co_btn)

    def update_inventory(self):
        item = items[0]
        item.count = 1
        for i in range(0, len(self.inventory)):
            if self.inventory[i].count <= 0:
                self.inventory[i] = item


    def update(self, screen, world, mouse):
        ud_near_blocks = [world.get_block(self.x, self.y - 1), world.get_block(self.x, self.y),
                          world.get_block(self.x, self.y + 1)]
        lr_near_blocks = [world.get_block(self.x - 1, self.y), world.get_block(self.x, self.y - 2),
                          (world.get_block(self.x + 1, self.y))]

        if not ud_near_blocks[0].solid:
            self.y += 1
            return world

        self.update_inventory()

        if lr_near_blocks[1].solid:
            if self.right:
                self.x -= 1
            else:
                self.x += 1

        if self.mx < 0:
            self.right = False
        elif self.mx > 0:
            self.right = True
        else:
            self.right = self.right

        self.x += self.mx
        self.y += self.my

        if self.use_item:
            self.inventory[self.selected_item].use(screen, world, mouse)

        for npc in range(0, len(world.npcs)):
            if world.npcs[npc].hostile:
                npc_box = pygame.Rect(round(world.npcs[npc].x) * 10, round(world.npcs[npc].y) * 10, 10, 20)

                if npc_box.collidepoint(world.player.x * 10, world.player.y * 10):
                    world.npcs[npc].x += 1.5
                    self.health -= world.npcs[npc].damage

                x, y, on = world.npcs[npc].proj_info
                proj_box = pygame.Rect(x * 10, y * 10, 5, 5)

                if proj_box.collidepoint(world.player.x * 10, world.player.y * 10):
                    self.health -= world.npcs[npc].damage
                    world.npcs[npc].proj_info = (0, 0, False)

        if self.health <= 0:
            self.alive = False
        elif self.health >= 100:
            self.health = 100

        self.mx = 0
        self.my = 0
        self.use_item = False

        return world
