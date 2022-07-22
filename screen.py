from player import pygame
from pcolour import Color


class Screen:
    def __init__(self, w=800, h=600, bgcolor=Color.BACKGROUND_COLOR, font_type="monospace", font_size=35,
                 clock_tick=30):
        self.w = w
        self.h = h
        self.bgcolor = bgcolor
        self.font = pygame.font.SysFont(font_type, font_size)
        self.screen = pygame.display.set_mode((w, h))
        self.clock = pygame.time.Clock()
        self.clock_tick = clock_tick

    def draw_enemies(self, enemy_list):
        for enemy in enemy_list:
            enemy.draw(self.screen)

    def draw_player(self, player):
        player.draw(self.screen)

    def draw_score(self, score, color=Color.YELLOW):
        text = f"Score: {score}"
        label = self.font.render(text, 1, color)
        self.screen.blit(label, (self.w - 200, self.h - 40))

    def update_screen(self, enemy_list, player, score):
        self.refresh_s()
        self.draw_enemies(enemy_list)
        self.draw_player(player)
        self.draw_score(score)
        self.clock.tick(self.clock_tick)
        pygame.display.update()

    def refresh_s(self):
        self.screen.fill(self.bgcolor)


