import random

class Enemy:

    def __init__(self, move_speed):
        # x and y coords are top left corner of the agent
        self.x = random.randint(0, 1000)
        self.y = 0
        self.speed = move_speed
        self.damage = 100
        self.size = 80

        # Enemies can have a random chance to spawn as a different type
        # Default just move straight down is 0
        # 1 is move at an angle
        # 2 is bigger agent
        # 3 is a boss
        self.enemy_type = 0


