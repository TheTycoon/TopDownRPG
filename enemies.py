import pygame
import sprites
import settings
import math


class Enemy(sprites.Actor):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.all_enemies
        sprites.Actor.__init__(self, game, self.groups)

        self.image = pygame.Surface((32, 32)).convert()
        self.rect = self.image.get_rect()
        self.image.fill(settings.YELLOW, self.rect)
        self.rect.topleft = (x, y)

        self.max_health = 200
        self.current_health = 200

        self.hit_timer = pygame.time.get_ticks()
        self.hit_cooldown = 200 #time in ms
        self.invulnerable = False

        self.speed = 2  # in pixels

        self.move_timer = pygame.time.get_ticks()
        self.move_wait_time = 10

    def update(self, now):
        if now - self.move_timer > self.move_wait_time:
            self.move_timer = now
            self.move_toward_player()

        if now - self.hit_timer > self.hit_cooldown:
            self.invulnerable = False


    def move_toward_player(self):

        dx = self.game.player.rect.x - self.rect.x
        if dx > 0:
            dx = self.speed
        elif dx < 0:
            dx = -self.speed
        else:
            dx = 0

        dy = self.game.player.rect.y - self.rect.y
        if dy > 0:
            dy = self.speed
        elif dy < 0:
            dy = -self.speed
        else:
            dy = 0

        if dx >= 0 and dy >= 0:
            dx /= math.sqrt(2)
            dy /= math.sqrt(2)


        self.move(dx, dy)

