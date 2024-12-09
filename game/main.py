import getpass
import pygame
from game.world import World

worlds = [World("world1.json"), World("world2.json"), World("world3.json")]


def main_game_loop(world: int):
    screen = pygame.display.set_mode((1100, 600))
    clock = pygame.time.Clock()

    current_world = worlds[world]
    current_world.display(screen)
    while True:

        clock.tick(15)
        pygame.display.flip()
