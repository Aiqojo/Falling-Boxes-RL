import time
import numpy as np
import pygame
import Agent
import Enemy
import gym
from gym import spaces

class dojEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    # Frame count used to spawn enemies
    frame = 0
    # Increases difficulty over time
    spawn_rate = 75
    # Default of the enemies
    enemy_move_speed = 3
    ## Max amount of enemies
    max_enemies = 5
    # Store enemies in array
    enemies = []
    # The player is placed at the bottom middle of the map
    agent = Agent.Agent()

    def __init__(self):
        self.action_space = spaces.Discrete(3)
        self.observation_space = spaces.Box(low=-1, high=1000, shape=((self.max_enemies+1)*2,), dtype=np.float32)
        self.done = False
        pygame.init()
        self.screen = pygame.display.set_mode((1000, 1000))

    # takes a step in the environment moving the agent in the direction of the action
    # and moves all of the enemies
    def step(self, action_direction):
        self.frame += 1
        reward = 0
        # if self.frame % 1000 == 0:
        #     self.spawn_rate -= 5

        # Randomly spawns enemies based on how many are already spawned
        if len(self.enemies) < self.max_enemies:
            if self.frame == 0:
                self.enemies.append(Enemy.Enemy(self.enemy_move_speed))
            if self.frame % self.spawn_rate == 0:
                self.enemies.append(Enemy.Enemy(self.enemy_move_speed))

        # Move the agent
        move_success = self.agent.move(action_direction)
        if not move_success:
            reward = -50

        # Move the enemies
        for enemy in self.enemies:
            # For now all enemies just travel straight downwards
            # so increase y by the speed
            enemy.y += enemy.speed

            # Check if the enemy is out of bounds
            if enemy.y > 1000:
                # Find distance from agent and add to reward
                reward += abs(enemy.x - self.agent.x)
                self.enemies.remove(enemy)

        
            # Check if the agent is in the same location as an enemy
            if self.agent.check_collision(enemy.x, enemy.y, enemy.size):
                # If so then the agent takes damage
                alive = self.agent.take_damage(enemy.damage)
                # If the agent is dead then return the return_array and the reward
                if not alive:
                    self.done = True
                    return_array = np.zeros((self.max_enemies+1,2), dtype=np.float32)
                    return_array[0][0] = self.agent.x
                    return_array[0][1] = self.agent.y
                    for i in range(len(self.enemies)):
                        return_array[i+1][0] = self.enemies[i].x
                        return_array[i+1][1] = self.enemies[i].y
                    return return_array.flatten(), reward, self.done, {}
        # Return the return_array and the reward
        # Create 1d numpy array that has the agents location and the enemies location
        return_array = np.zeros((self.max_enemies+1,2), dtype=np.float32)
        return_array[0][0] = self.agent.x
        return_array[0][1] = self.agent.y
        for i in range(len(self.enemies)):
            return_array[i+1][0] = self.enemies[i].x
            return_array[i+1][1] = self.enemies[i].y
        # The reward will be 2 * the number of enemies that are alive
        # plus the natural log of the frames
        return return_array.flatten(), reward, self.done, {}


    def reset(self):
        self.done = False

        self.frame = 0
        self.agent = Agent.Agent()
        self.enemies = []
        
        return_array = np.zeros((self.max_enemies+1,2), dtype=np.float32)
        return return_array.flatten()


    def render(self, mode='human'):
        pygame.display.flip()
        pygame.display.set_caption("DojEnv")

        self.screen.fill((0,0,0))
        # Draw the agent
        pygame.draw.rect(self.screen, (255,0,0), (self.agent.x, self.agent.y, self.agent.size, self.agent.size), 0)
        # Draw the enemies
        for enemy in self.enemies:
            pygame.draw.rect(self.screen, (0,255,0), (enemy.x, enemy.y, enemy.size, enemy.size), 0)
        pygame.display.flip()
        #time.sleep(.1)

