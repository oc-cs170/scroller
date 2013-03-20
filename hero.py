import os
import pygame

from parameters import *


class Hero(pygame.sprite.Sprite):
    def __init__(self, screen, world, png='images/Character Princess Girl.png'):
        super(Hero, self).__init__()

        walk = os.listdir('walk')
        walk.sort()
        self.images = [pygame.image.load('walk/' + w).convert_alpha()
                       for w in walk]
        self.index = 0
        self.image = self.images[self.index]

        # self.image = pygame.image.load(png).convert_alpha()
        # self.rect = self.image.get_rect(bottomleft=(0, 681))
        self.rect = self.images[0].get_rect(bottomleft=(0, 681))
        self.world = world
        self.srect = screen.get_rect()
        self.wrect = world.get_rect()

        self.last_screen = self.wrect.width - self.srect.width
        self.goal = self.srect.width - 200

        self.velocity = [0, 0]

    def update(self):
        self.index = (self.index + 1) % 11
        self.image = self.images[self.index]

        # If we're above ground, gravity is in effect
        if self.rect.bottom < 681:
            self.velocity[1] += 0.8

        # Move based on current velocity
        self.rect.move_ip(*self.velocity)

        # Restrict movement to live above ground
        if self.rect.bottom > 681:
            self.rect.bottom = 681
            self.velocity[1] = 0

    def jump(self, power=10):
        # If we're on the ground, change vertical velocity
        if self.rect.bottom == 681:
            self.velocity[1] = -power

    def move(self, motion):
        vp = self.world.vp
        self.velocity = motion
        pre_index = (self.rect.centerx + vp[0]) / BLOCK_HOFFSET
        new_rect = self.rect.move(motion[0], motion[1])
        new_rect.left = max(0, new_rect.left)
        new_rect.right = min(self.goal, new_rect.right)
        index = (new_rect.centerx + vp[0]) / BLOCK_HOFFSET
        print pre_index, index, self.world.terrain[index], self.world.height[index]

        # If new location is in the same block
        # or if new location is equal or lower, allow move to rect
        if index == pre_index or self.world.height[index] <= self.world.height[pre_index]:
            self.rect = new_rect
        else:
            pass   # A good place for a speech bubble (@$&^%!)
            self.rect = new_rect

        if self.rect.centerx > self.srect.centerx:
            # Move the viewport
            diff = self.rect.centerx - self.srect.centerx
            if vp[0] < self.last_screen:  # there's more room
                self.rect.centerx -= diff
                vp[0] += diff

        self.world.set_viewport(vp)
