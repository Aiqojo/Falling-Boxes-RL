
class Agent:

    def __init__(self, board_size):
        self.board_size = board_size
        self.size = 1

        # x and y coords are top left corner of the agent
        self.x = board_size // 2
        self.y = board_size - 1
        self.alive = True
        self.move_speed = 1
        self.health = 100
        self.type = 1
    
    
    def move(self, direction):
        # 0 is left 1 is right 2 is stand still
        if direction == 0:
            self.x -= self.move_speed
            if self.check_in_bounds():
                return True
            else:
                return False
        if direction == 1:
            self.x += self.move_speed
            if self.check_in_bounds():
                return True
            else:
                return False
        if direction == 2:
            return True

        # # 0 = up, 1 = right, 2 = down, 3 = left
        # if direction == 0:
        #     self.y -= self.move_speed
        #     self.check_in_bounds()
        # elif direction == 1:
        #     self.x += self.move_speed
        #     self.check_in_bounds()
        # elif direction == 2:
        #     self.y += self.move_speed
        #     self.check_in_bounds()
        # elif direction == 3:
        #     self.x -= self.move_speed
        #     self.check_in_bounds()

    # The agent can move all along x axis but only from 800 to 1000 on y axis
    def check_in_bounds(self):
        if self.x < 0:
            self.x = 0
            return False
        if self.x >= self.board_size:
            self.x = self.board_size - 1
            return False
        # This is redundant cause it cant move up or down
        if self.y < 1 - self.board_size//5:
            self.y = self.board_size//5
            return False
        if self.y >= self.board_size:
            self.y = self.board_size - 1
            return False
        return True

    # checks the x and y coords to see if it is within the agents hitbox
    def check_collision(self, x, y, enemy_size):
        
        if x <= self.x < x + 1 and y <= self.y < y + 1:
            return True
        # Checks all 4 corners of the agent is within the enemy hitbox
        if x < self.x < x + enemy_size and y < self.y < y + enemy_size:
            return True
        if x < self.x + self.size < x + enemy_size and y < self.y < y + enemy_size:
            return True
        if x < self.x < x + enemy_size and y < self.y + self.size < y + enemy_size:
            return True
        if x < self.x + self.size < x + enemy_size and y < self.y + self.size < y + enemy_size:
            return True
        return False
        
    # Returns False if dead and True if alive
    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.alive = False
            self.health = 0
            return False
        return True

