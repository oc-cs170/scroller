#!/usr/bin/env python

"""Main file with game loop for Scroller.
"""
import pygame

import hero
import world
from parameters import *

WINDOW_TITLE = 'Scroller'
FPS = 30


class Scroller(object):
    """Create a game of Scroller."""
    def __init__(self):
        pygame.init()
        pygame.key.set_repeat(10, 10)
        pygame.display.set_caption(WINDOW_TITLE)

        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
                                              # pygame.FULLSCREEN)

        # Use a clock to control frame rate
        self.clock = pygame.time.Clock()

        self.world = world.World()

        self.hero = hero.Hero(self.screen, self.world)

    def play(self):
        """Start Scroller program.
        """


        running = True
        while running:
            self.clock.tick(FPS)  # Max frames per second

            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.hero.move([-13, 0])
                    elif event.key == pygame.K_RIGHT:
                        self.hero.move([13, 0])
                    elif event.key == pygame.K_SPACE:
                        self.hero.jump(15)
                if event.type == pygame.KEYUP:
                    if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                        self.hero.move((0, 0))

            # Draw the scene
            self.screen.fill((0, 0, 0))
            self.screen.blit(self.world.image, (-self.world.vp[0], self.world.vp[1]))
            self.hero.update()
            self.screen.blit(self.hero.image, self.hero.rect)
            pygame.display.flip()


if __name__ == '__main__':
    game = Scroller()
    game.play()
