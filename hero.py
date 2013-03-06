import pygame


class Hero(pygame.sprite.Sprite):
    def __init__(self, screen, world, png='Character Princess Girl.png'):
        super(Hero, self).__init__()

        self.image = pygame.image.load(png).convert_alpha()
        self.rect = self.image.get_rect(bottomleft=(0, 681))
        self.srect = screen.get_rect()
        self.wrect = world.get_rect()

    def move(self, motion, vp):
        if self.rect.left >= self.srect.width / 2:
            # Move the viewport
            pass
        else:
            # Move the hero
            self.rect.move_ip(motion[0], motion[1])

        return vp
