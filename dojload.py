import gym
from stable_baselines3 import PPO, DQN
from dojenv import dojEnv
import time
import numpy as np

# load tensorboard to find best performing

logdir = "logs"


env = dojEnv()
env.reset()

models_dir = "models/DojB-PPO4"
models_path = f"{models_dir}/1375000.zip"

model = PPO.load(models_path, env = env)

reward_array = []

episodes = 20
for ep in range(episodes):
    obs = env.reset()
    done = False
    while not done:
        time.sleep(.05)
        env.render()
        action, _ = model.predict(obs)
        obs, reward, done, info = env.step(action)
        #print(np.fliplr(np.rot90(m=obs, k=3)))
        print(reward)
    reward_array += [reward]

env.close()

print(reward_array)




