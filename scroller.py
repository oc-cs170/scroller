#!/usr/bin/env python

"""Main file with game loop for Scroller.
"""

import pygame
import hero


WINDOW_TITLE = 'Scroller'
WINDOW_WIDTH = 1024
WINDOW_HEIGHT = 768
FPS = 30

WORLD_WIDTH = 5 * WINDOW_WIDTH


class Scroller(object):
    """Create a game of Scroller."""
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(WINDOW_TITLE)

        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
                                              # pygame.FULLSCREEN)

        pygame.key.set_repeat(10, 10)

        # Use a clock to control frame rate
        self.clock = pygame.time.Clock()

        self.dirt_block = pygame.image.load('Dirt Block.png').convert_alpha()

        self.world = pygame.Surface((WORLD_WIDTH, WINDOW_HEIGHT))
        self.world.fill((pygame.Color('Sky Blue')))
        x = 0
        while x < WORLD_WIDTH:
            self.world.blit(self.dirt_block, (x, 514))
            self.world.blit(self.dirt_block, (x, 598))
            x += 101
        self.vp = [0, 0]

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
                        self.vp = self.hero.move((-13, 0), self.vp)
                    elif event.key == pygame.K_RIGHT:
                        self.vp = self.hero.move((13, 0), self.vp)

            # Draw the scene
            self.screen.fill((0, 0, 0))
            self.screen.blit(self.world, (-self.vp[0], self.vp[1]))
            self.screen.blit(self.hero.image, self.hero.rect)
            pygame.display.flip()


if __name__ == '__main__':
    game = Scroller()
    game.play()
