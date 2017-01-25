import pygame
import settings
import sprites
import math


class Player(sprites.Actor):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.player_sprites
        sprites.Actor.__init__(self, game, self.groups)

        self.image = game.player_img_right
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.max_health = settings.PLAYER_HEALTH
        self.current_health = settings.PLAYER_HEALTH

        self.attack_power = 10


        self.direction_facing = 'right'
        self.attacking = False
        self.attack_timer = pygame.time.get_ticks()
        self.attack_img_horizontal = pygame.Surface((32, 16))
        self.attack_img_vertical = pygame.Surface((16, 32))
        self.attack_rect_horizontal = self.attack_img_horizontal.get_rect()
        self.attack_rect_vertical = self.attack_img_vertical.get_rect()
        self.attack_img_horizontal.fill(settings.RED, self.attack_rect_horizontal)
        self.attack_img_vertical.fill(settings.RED, self.attack_rect_vertical)
        self.attack_img = self.attack_img_horizontal
        self.attack_rect = self.attack_rect_horizontal

    def update(self, now):
        self.keyboard_movement()

        if self.attacking and now - self.attack_timer > settings.PLAYER_ATTACK_SPEED:
            self.attacking = False

        if self.direction_facing == 'right':
            self.image = self.game.player_img_right
        elif self.direction_facing == 'left':
            self.image = self.game.player_img_left
        elif self.direction_facing == 'up':
            self.image = self.game.player_img_up
        elif self.direction_facing == 'down':
            self.image = self.game.player_img_down

    def keyboard_movement(self):
        dx = 0
        dy = 0
        if not self.attacking:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                dx = -settings.PLAYER_SPEED
                self.direction_facing = 'left'
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                dx = settings.PLAYER_SPEED
                self.direction_facing = 'right'
            if keys[pygame.K_UP] or keys[pygame.K_w]:
                dy = -settings.PLAYER_SPEED
                self.direction_facing = 'up'
            if keys[pygame.K_DOWN] or keys[pygame.K_s]:
                dy = settings.PLAYER_SPEED
                self.direction_facing = 'down'

        # corrects speed when moving diagonally
        if dx != 0 and dy != 0:
            dx /= math.sqrt(2)
            dy /= math.sqrt(2)

        self.move(dx, dy)

    def attack(self):
        self.attacking = True
        self.attack_timer = pygame.time.get_ticks()

        if self.direction_facing == 'right':
            self.attack_img = self.attack_img_horizontal
            self.attack_rect = self.attack_rect_horizontal
            self.attack_rect.left = self.rect.right
            self.attack_rect.y = self.rect.centery - self.attack_img.get_height() / 2
        elif self.direction_facing == 'left':
            self.attack_img = self.attack_img_horizontal
            self.attack_rect = self.attack_rect_horizontal
            self.attack_rect.right = self.rect.left
            self.attack_rect.y = self.rect.centery - self.attack_img.get_height() / 2
        elif self.direction_facing == 'up':
            self.attack_img = self.attack_img_vertical
            self.attack_rect = self.attack_rect_vertical
            self.attack_rect.x = self.rect.centerx - self.attack_img.get_width() / 2
            self.attack_rect.bottom = self.rect.top
        elif self.direction_facing == 'down':
            self.attack_img = self.attack_img_vertical
            self.attack_rect = self.attack_rect_vertical
            self.attack_rect.x = self.rect.centerx - self.attack_img.get_width() / 2
            self.attack_rect.top = self.rect.bottom





