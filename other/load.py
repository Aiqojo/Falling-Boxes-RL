import gym
from stable_baselines3 import PPO
import os

models_dir = "models/Car-PPO"
logdir = "logs"


env = gym.make('CarRacing-v0')
env.reset()

models_dir = "models/Car-PPO"
models_path = f"{models_dir}/290000.zip"

model = PPO.load(models_path, env = env)

episodes = 10
for ep in range(episodes):
    obs = env.reset()
    done = False
    while not done:
        env.render()
        action, _ = model.predict(obs)
        obs, reward, done, info = env.step(action)

env.close()





