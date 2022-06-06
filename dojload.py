import gym
from stable_baselines3 import PPO, DQN
from dojenv import dojEnv
import time


logdir = "logs"


env = dojEnv()
env.reset()

models_dir = "models/Doj-A2C1"
models_path = f"{models_dir}/810000.zip"

model = PPO.load(models_path, env = env)

episodes = 10
for ep in range(episodes):
    obs = env.reset()
    done = False
    while not done:
        time.sleep(.05)
        env.render()
        action, _ = model.predict(obs)
        obs, reward, done, info = env.step(action)
        print(obs)
        print(reward)

env.close()





