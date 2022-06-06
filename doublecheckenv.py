from dojenv import dojEnv
import numpy as np

env = dojEnv()
episodes = 50
# for i in range(10):
#     print(env.observation_space.sample())


for episode in range(episodes):
    observation = env.reset()
    done = False
    while not done:
        action = env.action_space.sample()
        env.render()
        observation, reward, done, info = env.step(action)
        print(np.fliplr(np.rot90(m=observation, k=3)))
        print(reward)
        print(done)
        print(info)
        print("\n")




