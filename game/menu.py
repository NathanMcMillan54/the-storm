import sys

import pygame.display

from game.main import game_main


def main_menu():
    screen = pygame.display.set_mode((1100, 600))
    clock = pygame.time.Clock()

    menu_running = True
    font = pygame.font.SysFont('Arial', 20)


    top_rect = pygame.Rect(0, 0, 1100, 226)
    bottom_rect = pygame.Rect(0, 226, 1100, 374)

    world1_btn = pygame.Rect(450, 200, 200, 100)
    world2_btn = pygame.Rect(450, 325, 200, 100)
    world3_btn = pygame.Rect(450, 450, 200, 100)
    world1_text = font.render("World 1", True, (0, 0, 0))
    world2_text = font.render("World 2", True, (0, 0, 0))
    world3_text = font.render("World 3", True, (0, 0, 0))


    title_font = pygame.font.SysFont('Arial', 24, bold=True, italic=True)

    title_text = title_font.render("The Storm", True, (105, 151, 201))

    while menu_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit(0)

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if world1_btn.collidepoint(mouse_pos):
                    menu_running = False
                    game_main(0)
                    menu_running = True
                elif world2_btn.collidepoint(mouse_pos):
                    menu_running = False
                    game_main(1)
                elif world3_btn.collidepoint(mouse_pos):
                    menu_running = False
                    game_main(2)

        clock.tick(60)

        screen.fill((255, 255, 255))

        pygame.draw.rect(screen, (12, 117, 0), top_rect)
        pygame.draw.rect(screen, (135, 74, 0), bottom_rect)

        screen.blit(title_text, (493, 150))

        pygame.draw.rect(screen, (175, 175, 175), world1_btn)
        pygame.draw.rect(screen, (175, 175, 175), world2_btn)
        pygame.draw.rect(screen, (175, 175, 175), world3_btn)
        screen.blit(world1_text, (505, 220))
        screen.blit(world2_text, (505, 355))
        screen.blit(world3_text, (505, 480))

        pygame.display.flip()
