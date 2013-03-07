import pygame

from parameters import *


class Hero(pygame.sprite.Sprite):
    def __init__(self, screen, world, png='Character Princess Girl.png'):
        super(Hero, self).__init__()

        self.image = pygame.image.load(png).convert_alpha()
        self.rect = self.image.get_rect(bottomleft=(0, 585))
        self.world = world
        self.srect = screen.get_rect()
        self.wrect = world.get_rect()

        self.last_screen = self.wrect.width - self.srect.width
        self.goal = self.srect.width - 200

    def move(self, motion, vp):
        pre_index = (self.rect.centerx + vp[0]) / BLOCK_HOFFSET
        new_rect = self.rect.move(motion[0], motion[1])
        new_rect.left = max(0, new_rect.left)
        new_rect.right = min(self.goal, new_rect.right)
        index = (new_rect.centerx + vp[0]) / BLOCK_HOFFSET
        print pre_index, index, self.world.terrain[index], self.world.height[index], self.rect.bottomleft

        # If new location is in the same block
        # or if new location is equal or lower, allow move to rect
        if index == pre_index or self.world.height[index] <= self.world.height[pre_index]:
            self.rect = new_rect
        else:
            pass   # A good place for a speech bubble (@$&^%!)

        if self.rect.centerx > self.srect.centerx:
            # Move the viewport
            diff = self.rect.centerx - self.srect.centerx
            if vp[0] < self.last_screen:  # there's more room
                self.rect.centerx -= diff
                vp[0] += diff

        return vp

    def update(self, motion, vp):
        # self.move((-13, 0), vp)
        index = (self.rect.centerx + vp[0]) / BLOCK_HOFFSET
        
        if self.world.height[index] == 1:
            self.rect
        if self.world.height[index] == 2:
            self.rect.bottomleft = (0, 545)
        if self.world.height[index] == 3:
            self.rect.bottomleft = (0, 505)

        # print self.rect.bottomleft



