import stable_baselines3
import gym
from stable_baselines3 import PPO
import scipy
import os

logdir = "logs/Walk-PPO"
if not os.path.exists(logdir):
    os.makedirs(logdir)

env = gym.make("BipedalWalker-v3")

model = PPO('MlpPolicy', env, verbose=1, tensorboard_log=logdir)

model.learn(total_timesteps=4000000, tb_log_name="PPO")
model.save("BipedalWalker-v3-4mil")

model = PPO.load("BipedalWalker-v3-4mil")

input("Press Enter to continue...")

episodes = 10
for ep in range(episodes):
    obs = env.reset()
    done = False
    while not done:
        env.render()
        action, _ = model.predict(obs)
        obs, reward, done, info = env.step(action)
        print(reward)





