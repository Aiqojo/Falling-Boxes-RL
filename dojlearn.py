import gym
from stable_baselines3 import PPO
import os
import time
from dojenv import dojEnv

models_dir = f"models/Doj-PPO1"
logdir = f"logs/Doj-PPO1"

if not os.path.exists(models_dir):
    os.makedirs(models_dir)

if not os.path.exists(logdir):
    os.makedirs(logdir)

env = dojEnv()
env.reset()

model = PPO('MlpPolicy', env, verbose=1, tensorboard_log=logdir)
TIMESTEPS = 10000
for i in range(1,100000):
    model.learn(total_timesteps=TIMESTEPS, reset_num_timesteps=False, tb_log_name="PPO")
    model.save(f"{models_dir}/{TIMESTEPS*i}")

# episodes = 10
# for ep in range(episodes):
#     obs = env.reset()
#     done = False
#     while not done:
#         env.render()
        # obs, reward, done, info = env.step(env.action_space.sample())

env.close()





