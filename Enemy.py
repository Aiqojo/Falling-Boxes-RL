import random

class Enemy:

    def __init__(self, move_speed, board_size):
        self.board_size = board_size

        # x and y coords are top left corner of the agent
        self.x = random.randint(0, board_size - 1)
        self.y = 0
        self.speed = move_speed
        self.damage = 100
        self.size = 1

        # Enemies can have a random chance to spawn as a different type
        # Default just move straight down is 2
        # 3 is move at an angle
        # 4 is bigger agent
        # 5 is a boss
        self.type = 2


