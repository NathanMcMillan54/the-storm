import getpass
import pygame
import sys
from game.world import World

worlds = [World("world1.json"), World("world2.json"), World("world3.json")]


def main_game_loop(world: int):
    screen = pygame.display.set_mode((1100, 600))
    clock = pygame.time.Clock()

    current_world = worlds[world]
    while True:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        lc, mc, rc = pygame.mouse.get_pressed()
        current_world.mouse_pos = (mouse_x, mouse_y)
        current_world.left_click = lc
        current_world.right_click = rc

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                current_world.world_data.write(f"world{world}.json")
                sys.exit(0)

        key = pygame.key.get_pressed()
        if key[pygame.K_ESCAPE]:
            current_world.world_data.write(f"world{world}.json")
            sys.exit(0)
        if key[pygame.K_w]:
            current_world.player.my -= 3
        if key[pygame.K_d]:
            current_world.player.mx += 1
                    #elif key[pygame.K_s]:
                     #   self.player.my += 1
        if key[pygame.K_a]:
            current_world.player.mx -= 1
        if key[pygame.K_1]:
            current_world.player.inventory_item_selected = 0
        if key[pygame.K_2]:
            current_world.player.inventory_item_selected = 1
        if key[pygame.K_3]:
            current_world.player.inventory_item_selected = 2
        if key[pygame.K_4]:
            current_world.player.inventory_item_selected = 3
        if key[pygame.K_5]:
            current_world.player.inventory_item_selected = 4
        if key[pygame.K_6]:
            current_world.player.inventory_item_selected = 5
        if key[pygame.K_7]:
            current_world.player.inventory_item_selected = 6
        if key[pygame.K_8]:
            current_world.player.inventory_item_selected = 7
        if key[pygame.K_9]:
            current_world.player.inventory_item_selected = 8
        if key[pygame.K_0]:
            current_world.player.inventory_item_selected = 9
        
        if key[pygame.K_e]:
            current_world.player.inventory_open = True

        current_world.update()
        current_world.display(screen)
        pygame.draw.rect(screen, (255, 255, 0), pygame.rect.Rect((round(mouse_x / 10) * 10, round(mouse_y / 10) * 10), (10, 10)))

        clock.tick(10)
        pygame.display.flip()
