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
        if key[pygame.K_w]:
            current_world.player.my -= 3
        if key[pygame.K_d]:
            current_world.player.mx += 1
                    #elif key[pygame.K_s]:
                     #   self.player.my += 1
        if key[pygame.K_a]:
            current_world.player.mx -= 1
        
        if key[pygame.K_e]:
            current_world.player.inventory_open = True

        current_world.update()
        current_world.display(screen)
        pygame.draw.rect(screen, (255, 255, 0), pygame.rect.Rect((round(mouse_x / 10) * 10, round(mouse_y / 10) * 10), (10, 10)))

        clock.tick(10)
        pygame.display.flip()
