# creating player class for player and enemies with parent class as player
import pygame
from pcolour import Color


class Player:
    def __init__(self, size, x_pos, y_pos, color=Color.BLUE):
        self.size = size
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x_pos, self.y_pos, self.size, self.size))

    # as the player can be an enemy or a player we pass a_player to the collision function
    def collision(self, a_player):
        if (self.x_pos <= a_player.x_pos < (self.x_pos + self.size)) or (
                a_player.x_pos <= self.x_pos < (a_player.x_pos + a_player.size)):
            if (self.y_pos <= a_player.y_pos < (self.y_pos + self.size)) or (
                    a_player.y_pos <= self.y_pos < (a_player.y_pos + a_player.size)):
                return True
        return False


class Enemy(Player):
    def __init__(self, x_pos, y_pos):
        super.__init__(x_pos, y_pos, size=50, color=Color.RED)


class BigEnemy(Player):
    def __init__(self, x_pos, y_pos):
        super.__init__(x_pos, y_pos, size=100, color=Color.YELLOW)


class HumanPlayer(Player):
    def __init__(self, x_pos, y_pos):
        super.__init__(x_pos, y_pos, size=50, color=Color.GREEN)
