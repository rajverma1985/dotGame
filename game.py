import random
from player import Enemy


class Game:
    def __init__(self, speed=10, score=0, max_enemies=15, delay=0.1):
        self.speed = speed
        self.score = score
        self.max_enemies = max_enemies
        self.delay = delay
        self.enemy_list = []  # instance variable so that we can modify it whenever needed

    def spawn_enemies(self, screen_width):
        delay = random.random()
        if len(self.enemy_list) < 10 and delay < self.delay:
            x_pos = random.randint(0, screen_width)
            y_pos = 0
            enemy = Enemy(x_pos, y_pos)
            self.enemy_list.append(enemy)

    def update_enemy_positions(self, screen_height):
        new_enemy_list = []
        for enemy in self.enemy_list:
            if 0 <= enemy.y_pos < screen_height:
                enemy.y_pos += self.speed
                new_enemy_list.append(enemy)
            else:
                self.score += 1
        self.enemy_list = new_enemy_list

    def set_level(self):
        if self.score < 20:
            self.speed = 5
        elif self.score < 40:
            self.speed = 8
        elif self.score < 60:
            self.speed = 12
        else:
            self.speed = 15

    def collision_check(self, player):
        for enemy in self.enemy_list:
            if enemy.collision(player):
                return True
        return False
