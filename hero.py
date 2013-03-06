import pygame


class Hero(pygame.sprite.Sprite):
    def __init__(self, screen, world, png='Character Princess Girl.png'):
        super(Hero, self).__init__()

        self.image = pygame.image.load(png).convert_alpha()
        self.rect = self.image.get_rect(bottomleft=(0, 681))
        self.srect = screen.get_rect()
        self.wrect = world.get_rect()

        self.last_screen = self.wrect.width - self.srect.width
        self.goal = self.srect.width - 200

    def move(self, motion, vp):
        self.rect.move_ip(motion[0], motion[1])
        self.rect.left = max(0, self.rect.left)
        self.rect.right = min(self.goal, self.rect.right)

        if self.rect.centerx > self.srect.centerx:
            # Move the viewport
            diff = self.rect.centerx - self.srect.centerx
            if vp[0] < self.last_screen:  # there's more room
                self.rect.centerx -= diff
                vp[0] += diff

        return vp
