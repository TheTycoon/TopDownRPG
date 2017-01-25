import pygame
import settings
import player
from os import path
import tilemap
import sprites
import enemies


class Game:
    def __init__(self):
        # initialize game window, sound, etc
        pygame.init()
        self.screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
        pygame.display.set_caption(settings.TITLE)
        self.clock = pygame.time.Clock()
        self.running = True

        joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
        if joysticks:
            self.joystick = joysticks[0]
            self.joystick.init()
            self.joystick_enabled = True
        else:
            self.joystick_enabled = False

        self.load_data()

    def load_data(self):
        # Easy names to start file directories
        self.game_folder = path.dirname(__file__)
        self.img_folder = path.join(self.game_folder, 'img')
        self.map_folder = path.join(self.game_folder, 'maps')

        # load Tiled map stuff
        self.map = tilemap.Map(path.join(self.map_folder, 'test_map.tmx'))
        self.map_img = self.map.make_map()
        self.map_rect = self.map_img.get_rect()
        self.camera = tilemap.Camera(self.map.width, self.map.height)


        # Temporary Player Character Images
        self.player_img_right = pygame.image.load(path.join(self.img_folder, 'player_img_right.png')).convert_alpha()
        self.player_img_left = pygame.image.load(path.join(self.img_folder, 'player_img_left.png')).convert_alpha()
        self.player_img_up = pygame.image.load(path.join(self.img_folder, 'player_img_up.png')).convert_alpha()
        self.player_img_down = pygame.image.load(path.join(self.img_folder, 'player_img_down.png')).convert_alpha()

    def new(self):
        self.all_sprites = pygame.sprite.Group()
        self.player_sprites = pygame.sprite.Group()
        self.all_enemies = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()

        # Initialize Map Objects
        for tile_object in self.map.tmxdata.objects:
            if tile_object.name == 'player':
                self.player = player.Player(self, tile_object.x, tile_object.y)
            if tile_object.name == 'enemy':
                enemies.Enemy(self, tile_object.x, tile_object.y)
            if tile_object.name == 'wall':
                sprites.Wall(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height)

    def run(self):
        # Game Loop
        self.playing = True
        while self.playing:
            self.clock.tick(settings.FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        now = pygame.time.get_ticks()
        self.all_sprites.update(now)
        self.camera.update(self.player)

        if self.player.attacking:
            for mob in self.all_enemies:
                if self.player.attack_rect.colliderect(mob.rect) and not mob.invulnerable:
                    mob.invulnerable = True
                    mob.hit_timer = now
                    mob.current_health -= self.player.attack_power
                    if mob.current_health <= 0:
                        mob.kill()

    def events(self):
        for event in pygame.event.get():

            # quit event / close window
            if event.type == pygame.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if self.playing:
                        self.playing = False
                    self.running = False
                if event.key == pygame.K_RETURN and not self.player.attacking:
                    self.player.attack()


    def draw(self):
        # DRAW STUFF
        self.screen.fill(settings.BLACK)
        self.screen.blit(self.map_img, self.camera.apply_rect(self.map_rect))

        self.all_sprites.draw(self.screen)

        if self.player.attacking:
            self.screen.blit(self.player.attack_img, self.player.attack_rect)

        self.draw_bar(20, 20, 100, 10, self.player.current_health / self.player.max_health)

        for mob in self.all_enemies:
            if mob.current_health != mob.max_health:
                self.draw_bar(mob.rect.left, mob.rect.top - 12, mob.rect.width, 10, mob.current_health / mob.max_health)

        # display frame
        pygame.display.flip()

    def draw_bar(self, x, y, width, height, percentage):
        color = settings.RED
        if percentage < 0:
            percentage = 0
        filled = percentage * width
        outline_rect = pygame.Rect(x, y, width, height)
        filled_rect = pygame.Rect(x, y, filled, height)
        pygame.draw.rect(self.screen, settings.BLACK, outline_rect)
        pygame.draw.rect(self.screen, color, filled_rect)
        pygame.draw.rect(self.screen, settings.WHITE, outline_rect, 2)

    def draw_text(self, text, size, color, x, y, centered):
        font = pygame.font.Font(settings.FONT, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.x = x
        text_rect.y = y
        if centered:
            text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)

game = Game()
while game.running:
    game.new()
    game.run()

pygame.quit()


