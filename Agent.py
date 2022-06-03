
class Agent:

    def __init__(self):
        # The agent is a square with a size of 20x20)
        self.size = 40

        # x and y coords are top left corner of the agent
        self.x = 500 - self.size/2
        self.y = 1000 - self.size
        self.alive = True
        self.move_speed = 5
        self.health = 100
        self.type = -1
    
    
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
        if self.x > 1000 - self.size:
            self.x = 1000 - self.size
            return False
        if self.y < 800:
            self.y = 800
            return False
        if self.y > 1000 - self.size:
            self.y = 1000 - self.size
            return False
        return True

    # checks the x and y coords to see if it is within the agents hitbox
    def check_collision(self, x, y, enemy_size):
        # Checks all 4 corners of the agent is within the enemy hitbox
        if self.x <= x + enemy_size and self.x >= x:
            if self.y <= y + enemy_size and self.y >= y:
                return True
        if self.x + self.size <= x + enemy_size and self.x + self.size >= x:
            if self.y <= y + enemy_size and self.y >= y:
                return True
        if self.x <= x + enemy_size and self.x >= x:
            if self.y + self.size <= y + enemy_size and self.y + self.size >= y:
                return True
        if self.x + self.size <= x + enemy_size and self.x + self.size >= x:
            if self.y + self.size <= y + enemy_size and self.y + self.size >= y:
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

