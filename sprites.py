import pygame


class Actor(pygame.sprite.Sprite):
    def __init__(self, game, groups):
        pygame.sprite.Sprite.__init__(self, groups)
        self.game = game

    def move(self, dx, dy):
        # Move each axis separately. Note that this checks for collisions both times.
        if dx != 0:
            self.move_single_axis(dx, 0)
        if dy != 0:
            self.move_single_axis(0, dy)

    def move_single_axis(self, dx, dy):
        # Move the rect
        self.rect.x += dx
        self.rect.y += dy

        # If you collide with a wall, move out based on movement direction
        for wall in self.game.walls:
            if self.rect.colliderect(wall.rect):
                # Moving right; Hit the left side of the wall
                if dx > 0:
                    self.rect.right = wall.rect.left
                # Moving left; Hit the right side of the wall
                if dx < 0:
                    self.rect.left = wall.rect.right
                # Moving down; Hit top side of the wall
                if dy > 0:
                    self.rect.bottom = wall.rect.top
                # Moving up; Hit the bottom side of the wall
                if dy < 0:
                    self.rect.top = wall.rect.bottom

    def sprite_collide(self):
        for sprite in self.game.all_sprites:
            pass


class Wall(pygame.sprite.Sprite):
    def __init__(self, game, x, y, w, h):
        self.groups = game.walls
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.rect = pygame.Rect(x, y, w, h)
        self.x = x
        self.y = y












