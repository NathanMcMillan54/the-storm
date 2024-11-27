import random

import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import sys

from game.menu import main_menu
from setup.errors import errors, error_message
from setup.main import setup_main

screen = pygame.display.set_mode((1100, 600))
clock = pygame.time.Clock()
pygame.display.set_caption('The Storm')

VERSION = "0.1.0-alpha (2022/12/26)"

messages = [
    "Wood comes from the ground",
    "There aren't any bugs - just unecessary annoying features",
    "Build a house with walls to stay safe during the storm",
    "Is it Christmas?",
    "Monsters disappear at the end of the day",
    "Fish",
    "Physics don't apply!",
    "Matter can be created and destroyed",
    "A day is 24 hours. A day is ~2 minutes",
    "Some of these texts are inspired by the Minecraft splash texts",
	"Why'd I say that?",
    "...",
    "'_'",
    "The storm's scary",
    "For more information go to: https://nathanmcmillan54.github.io/the-storm/",
    "A wall can mean two different things here",
    "Tell your friends to tell their friends!",
    "Get creative!",
    "I don't go outside",
    "You should go outside",
    "Horrible graphics",
    "stuff",
    "where am i?",
    "the sTorm",
    "Some of these texts are inspired by the Minecraft splash texts",
    "sdrawkcab",
    "forward",
    "'What' is not a palindrome",
    "Wood shouldn't come from the ground",
    "Cool!",
    "Help! I'm stuck in here!",
    "Venus",
    "Report bugs at: https://nathanmcmillan54/the-storm/issues",
    "Mars",
    "You have to force the blocks to float",
    "Up, up, up, down down",
    "Some of these texts are inspired by the Minecraft splash texts",
    "The Storm Coat protects you",
    "Bows work pretty well!",
    "3, 4, 5, 6, 9, 13, 20, 35",
    "Report bugs at: https://nathanmcmillan54/the-storm/issues",
    "1, 2, 7 10, 12, 14, 24, 60",
    "Bagels",
    "Garlic bread is good",
    "If an apple a day keeps the doctor away, what happens if you eat two?",
    "Very expensive keyboard",
    "Report bugs at: https://nathanmcmillan54/the-storm/issues",
    "Have you drank enough water today?",
    "Some of these texts are inspired by the Minecraft splash texts",
    "Your honor... on skibidi... my client did in fact do it."
]


def main():
    setup_main()

    pygame.font.init()

    top_rect = pygame.Rect(0, 0, 1100, 226)
    bottom_rect = pygame.Rect(0, 226, 1100, 374)

    font = pygame.font.SysFont('Arial', 20)
    title_font = pygame.font.SysFont('Arial', 24, bold=True, italic=True)

    title_text = title_font.render("The Storm", True, (105, 151, 201))

    world_list_text = font.render("World list", True, (175, 175, 175))
    quit_text = font.render("Quit", True, (0, 0, 0))
    version_text = font.render("0.1.0-alpha (2022/12/26)", True, (200, 200, 200))

    world_list_button = pygame.rect.Rect(450, 200, 200, 100)
    quit_button = pygame.rect.Rect(450, 325, 200, 100)

    random_text = font.render(messages[random.randint(0, len(messages) - 1)], True, (255, 230, 38))

    start_screen_running = True

    while start_screen_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit(0)

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = event.pos
                if world_list_button.collidepoint(mouse_position):
                    start_screen_running = False
                    main_menu()
                elif quit_button.collidepoint(mouse_position):
                    sys.exit(0)

        clock.tick(60)
        screen.fill((255, 255, 255))

        pygame.draw.rect(screen, (12, 117, 0), top_rect)
        pygame.draw.rect(screen, (135, 74, 0), bottom_rect)

        pygame.draw.rect(screen, (0, 0, 255), world_list_button)
        pygame.draw.rect(screen, (200, 200, 200), quit_button)

        screen.blit(world_list_text, (505, 220))
        screen.blit(quit_text, (525, 355))
        screen.blit(random_text, (320, 10))

        screen.blit(title_text, (493, 150))
        screen.blit(version_text, (10, 580))

        pygame.display.flip()


if __name__ == '__main__':
    main()
