# -*- coding: utf-8 -*-
import pygame
import random
from constants import *


class Block(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        super(Block, self).__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()


class Bullet(Block):

    def __init__(self, color, width, height, speed):
        super(Bullet, self).__init__(color, width, height)
        self.speed = speed

    def update(self):
        self.rect.y -= self.speed


class Player(Block):

    def __init__(self, color, width, height):
        super(Player, self).__init__(color, width, height)

    def update(self):
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0]
        #self.rect.y = pos[1]
        self.rect.y = SCREEN_HEIGHT - 50


class Enemy(Block):

    def __init__(self, color, width, height):
        super(Enemy, self).__init__(color, width, height)

    def update(self):
        self.rect.y += 1
        if self.rect.y > SCREEN_HEIGHT + 10:
            self.reset_pos()

    def reset_pos(self):
        self.rect.x = random.randrange(SCREEN_WIDTH)
        self.rect.y = random.randrange(-100, -10)