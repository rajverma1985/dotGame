# Entrypoint for Game
from player import HumanPlayer, pygame
from screen import Screen
from game import Game
import sys


def playgame(screen, player, game):
    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.x_pos -= player.size
                elif event.key == pygame.K_RIGHT:
                    player.x_pos += player.size
        game.spawn_enemies(screen.w)
        game.update_enemy_positions(screen.h)
        game.set_level()
        screen.update_screen(game.enemy_list, player, game.score)

        if game.collision_check(player):
            game_over = True
            break


if __name__ == "__main__":
    pygame.init()
    screen = Screen()
    player = HumanPlayer(x_pos=screen.w / 2, y_pos=500)
    game = Game()
    playgame(screen, player, game)
