from dojenv import dojEnv

env = dojEnv()
episodes = 50

for episode in range(episodes):
    observation = env.reset()
    done = False
    while not done:
        action = env.action_space.sample()
        env.render()
        observation, reward, done, info = env.step(action)
        print(observation)
        print(reward)
        print(done)
        print(info)
        print("\n")




