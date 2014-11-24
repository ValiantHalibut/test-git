# -*- coding: utf-8 -*-
import pygame
from constants import *


def draw_snowman(screen, x, y):
    """Draws a simple snowman"""
    pygame.draw.ellipse(screen, WHITE, [35 + x, 0 + y, 25, 25])
    pygame.draw.ellipse(screen, WHITE, [23 + x, 20 + y, 50, 50])
    pygame.draw.ellipse(screen, WHITE, [0 + x, 65 + y, 100, 100])


def draw_stickman(screen, x, y):
    """Draws a simple stick figure"""
    pygame.draw.ellipse(screen, RED, [1 + x, y, 10, 10], 0)
    pygame.draw.line(screen, RED, [5 + x, 17 + y], [10 + x, 27 + y], 2)
    pygame.draw.line(screen, RED, [5 + x, 17 + y], [x, 27 + y], 2)
    pygame.draw.line(screen, BLUE, [5 + x, 17 + y], [5 + x, 7 + y], 2)
    pygame.draw.line(screen, BLUE, [5 + x, 7 + y], [9 + x, 17 + y], 2)
    pygame.draw.line(screen, BLUE, [5 + x, 7 + y], [1 + x, 17 + y], 2)


class Mover(object):
    def __init__(self, screen, asset, ckey):
        self.speed = 6
        self.x_vel = 0
        self.y_vel = 0
        self.asset = asset
        self.sWidth = screen.get_width()
        self.sHeight = screen.get_height()
        self.rect = self.asset.get_rect()
        self.asset.set_colorkey(ckey)

    def update(self):
        self.getMovement()
        self.rect.x = self.rect.x + self.x_vel
        self.rect.y = self.rect.y + self.y_vel
        if self.rect.x > self.sWidth - self.rect.width:
            self.rect.x = self.sWidth - self.rect.width
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.y > self.sHeight - self.rect.height:
            self.rect.y = self.sHeight - self.rect.height
        if self.rect.y < 0:
            self.rect.y = 0

    def getMovement(self):
        return


class PlayerShip(Mover):

    def __init__(self, screen, player, ckey):
        super(PlayerShip, self).__init__(screen, player, ckey)

    def getMovement(self):
        k_up = pygame.key.get_pressed()[pygame.K_UP]
        k_down = pygame.key.get_pressed()[pygame.K_DOWN]
        k_left = pygame.key.get_pressed()[pygame.K_LEFT]
        k_right = pygame.key.get_pressed()[pygame.K_RIGHT]
        self.x_vel = self.speed * (k_right - k_left)
        self.y_vel = self.speed * (k_down - k_up)


class RandoShip(Mover):

    def __init__(self, screen, asset, ckey):
        super(RandoShip, self).__init__(screen, asset, ckey)

    def getMovement(self):
        self.x_vel = 1
        self.y_vel = 1

