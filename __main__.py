# -*- coding: utf-8 -*-
import pygame
#import gameObjects
import gameInvaders
from constants import *


def main():
    pygame.init()
    size = (SCREEN_WIDTH, SCREEN_HEIGHT)

    screen = pygame.display.set_mode(size)
    #pygame.display.set_caption("My Game")

    done = False
    clock = pygame.time.Clock()

    game = gameInvaders.Game()
    pygame.display.set_caption(game.name)

    while not done:
        done = game.process_events()

        game.capture_inputs()

        game.run_logic()

        game.display_frame(screen)

        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()