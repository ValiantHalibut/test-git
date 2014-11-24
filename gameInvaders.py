# -*- coding: utf-8 -*-
import pygame
import spriteTest
import random
from constants import *


class Game(object):
    player = None
    block_list = None
    all_sprites_list = None
    bullet_list = None
    bullet_delay = 0
    game_over_state = 0
    score = 0
    name = "Invaders!"

    def __init__(self):
        self.score = 0
        self.game_over_state = 0
        self.block_list = pygame.sprite.Group()
        self.all_sprites_list = pygame.sprite.Group()
        self.bullet_list = pygame.sprite.Group()

        for i in range(5):
            block = spriteTest.Enemy(BLACK, 20, 15,)
            block.reset_pos()
            self.block_list.add(block)
            self.all_sprites_list.add(block)

        self.player = spriteTest.Player(RED, 20, 15,)
        self.all_sprites_list.add(self.player)

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.game_over_state != 0:
                    self.__init__()
        return False

    def capture_inputs(self):
        self.spacebar = pygame.key.get_pressed()[pygame.K_SPACE]

    def run_logic(self):
        if self.game_over_state == 0:
            if self.spacebar and self.bullet_delay <= 0:
                bullet = spriteTest.Bullet(BLUE, 4, 10, 6)
                bullet.rect.x = self.player.rect.x
                bullet.rect.y = self.player.rect.y
                self.bullet_list.add(bullet)
                self.all_sprites_list.add(bullet)
                self.bullet_delay = 15
            else:
                self.bullet_delay -= 1

            self.all_sprites_list.update()

            for bullet in self.bullet_list:
                blocks_hit_list = pygame.sprite.spritecollide(
                    bullet, self.block_list, True
                    )
                for block in blocks_hit_list:
                    self.bullet_list.remove(bullet)
                    self.all_sprites_list.remove(bullet)
                    self.score += 1
                    print(self.score)
                if bullet.rect.y < -10:
                    self.bullet_list.remove(bullet)

            for block in self.block_list:
                if block.rect.y > SCREEN_HEIGHT:
                    self.game_over_state = 2

            if len(self.block_list) == 0:
                self.game_over_state = 1

    def display_frame(self, screen):
        screen.fill(WHITE)

        if self.game_over_state > 0:
            font = pygame.font.SysFont("serif", 25)
            if self.game_over_state == 1:
                text = font.render("You've Won! Click to restart...", True,
                BLACK)
            elif self.game_over_state == 2:
                text = font.render("You've Lost. Click to restart...", True,
                BLACK)
            center_x = (SCREEN_WIDTH // 2) - (text.get_width() // 2)
            center_y = (SCREEN_HEIGHT // 2) - (text.get_height() // 2)
            screen.blit(text, [center_x, center_y])

        if self.game_over_state == 0:
            self.all_sprites_list.draw(screen)

        pygame.display.flip()
