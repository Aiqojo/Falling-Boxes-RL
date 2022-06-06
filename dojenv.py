import time
import numpy as np
import pygame
import Agent
import Enemy
import gym
from gym import spaces


class dojEnv(gym.Env):
    metadata = {'render.modes': ['human']}
    reward = 0
    delay = 0
    # This is how big the array will be when returned
    # It will be a square so if 20, np grid is 20x20
    # This is also used to scale the agent and enemies
    board_size = 10

    # Size of the render window
    render_size = 1000

    # Frame count used to spawn enemies
    frame = 0
    # Could increase difficulty over time
    spawn_rate = 5
    # Default of the enemies
    enemy_move_speed = .5
    ## Max amount of enemies
    max_enemies = 7
    # Store enemies in array
    enemies = []
    # The player is placed at the bottom middle of the map
    agent = Agent.Agent(board_size)
    # Create grid of 100x100 to store information about the environment
    return_array = np.zeros((board_size, board_size), dtype=np.uint8)

    def __init__(self):
        # Move left, right, or stay still
        self.action_space = spaces.Discrete(3)
         
        self.observation_space = spaces.Box(low=0, high=20, shape=(self.board_size, self.board_size), dtype=np.uint8)
        self.done = False
        pygame.init()
        self.screen = pygame.display.set_mode((self.render_size, self.render_size))
        self.reward = 0

    # takes a step in the environment moving the agent in the direction of the action
    # and moves all of the enemies
    def step(self, action_direction):
        time.sleep(self.delay)

        # Randomly spawns enemies based on how many are already spawned
        if len(self.enemies) < self.max_enemies:
            if self.frame == 0:
                self.enemies.append(Enemy.Enemy(
                    self.enemy_move_speed, self.board_size))
            if self.frame % self.spawn_rate == 0:
                self.enemies.append(Enemy.Enemy(
                    self.enemy_move_speed, self.board_size))

        # Move the agent
        move_success = self.agent.move(action_direction)
        # If it wasn't a succcess because the agent tried moving out of bounds
        # lower its reward
        if not move_success:
            self.reward += -5

        # Remove the enemies from the return array, reset the return array
        self.return_array = np.zeros((self.board_size, self.board_size), dtype=np.uint8)

        # Move the enemies
        for enemy in self.enemies:
            
            # For now all enemies just travel straight downwards
            # so increase y by the speed
            enemy.y += enemy.speed

            # Check if the enemy is out of bounds
            if enemy.y >= self.board_size:
                # If so find distance from agent and add to reward then remove
                self.reward += abs(enemy.x - self.agent.x)
                self.enemies.remove(enemy)

            # Check if the agent is in the same location as an enemy
            if self.agent.check_collision(enemy.x, enemy.y, enemy.size):
                # If so then the agent takes damage
                alive = self.agent.take_damage(enemy.damage)
                # If the agent is dead then return the return_array and the reward
                if not alive:
                    self.done = True
                    # Add the enemies to the return array
                    # Have to use enemy_ because enemy is var of for loop
                    for enemy_ in self.enemies:
                        for i in range(enemy_.size):
                            for j in range(enemy_.size):
                                # If it is out of bounds dont bother
                                if enemy_.x + i < self.board_size and enemy_.y + j < self.board_size:
                                    self.return_array[int(enemy_.x + i)][int(enemy_.y + j)] = enemy_.type
                    # Add the agent to the return array
                    for i in range(self.agent.size):
                        for j in range(self.agent.size):
                            self.return_array[int(
                                self.agent.x + i)][int(self.agent.y + j)] = self.agent.type
                    self.reward += int(-1000/self.frame)
                    return self.return_array, self.reward, self.done, {}

            # Add the enemy to the observation array
            for i in range(enemy.size):
                for j in range(enemy.size):
                    # Only adds pixels that are in bounds
                    if enemy.x + i < self.board_size and enemy.y + j < self.board_size \
                        and enemy.x + i >= 0 and enemy.y + j >= 0:
                        self.return_array[int(
                            enemy.x + i)][int(enemy.y + j)] = enemy.type

        # Add the agent to the observation array
        for i in range(self.agent.size):
            for j in range(self.agent.size):
                # print all info here
                self.return_array[int(
                    self.agent.x + i)][int(self.agent.y + j)] = self.agent.type

        # Increase the frame count
        self.frame += 1
        # Return the return_array and the reward
        # The reward will be 2 * the number of enemies that are alive
        # plus the natural log of the frames
        #self.reward += 1
        return self.return_array, self.reward, self.done, {}

    def reset(self):
        self.done = False
        self.reward = 0
        self.frame = 0
        self.agent = Agent.Agent(self.board_size)
        self.enemies = []

        return_array = np.zeros((self.board_size, self.board_size), dtype=np.uint8)
        return return_array

    def render(self, mode='human'):
        pygame.display.flip()
        pygame.display.set_caption("DojEnv")

        render_multiply = self.render_size//self.board_size

        self.screen.fill((0, 0, 0))
        # Draw the agent
        pygame.draw.rect(self.screen, (255, 0, 0), (self.agent.x*render_multiply,
                         self.agent.y*render_multiply, self.agent.size*render_multiply, 
                         self.agent.size*render_multiply), 0)
        # Draw the enemies
        for enemy in self.enemies:
            pygame.draw.rect(self.screen, (0, 255, 0),
                             (enemy.x*render_multiply, enemy.y*render_multiply, 
                             enemy.size*render_multiply, enemy.size*render_multiply), 0)
        pygame.display.flip()
        #time.sleep(.1)
