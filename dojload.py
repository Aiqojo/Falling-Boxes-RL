import gym
from stable_baselines3 import PPO
from dojenv import dojEnv

models_dir = "models/Doj-PPO1"
logdir = "logs"


env = dojEnv()
env.reset()

models_dir = "models/Doj-PPO1"
models_path = f"{models_dir}/4950000.zip"

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





