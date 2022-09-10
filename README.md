# A Test Environment for Reinforcement Learning with OpenAI Gym

![Gif](https://imgur.com/u6R0XAF.gif)

## Environment:

All of this takes place on a numpy grid, the example above being a 10x10 one. It is initialized with all 0s. Every 2 frames a green box is chosen to appear randomly along the grid at the top, and each box moves down 1 row every frame. These are represented with 1s in the array, and the agent is represented by a 2.

When running 1 environment, it can achieve around 1,000 frames per second on a RTX 3080.

## Agent:

The red box is the agent for this environment. Each frame the RL model has to choose whether to move left, right, or stay still.

## Reward Function:

The agent's reward is increased everytime a green box moves past the bottom border of the numpy array. After a few attempts, the most effective point system for this is to reward the agent based on how far away it is from the green box at its time of moving off the grid. If the agent is at index 2 in the grid, and the box was at index 7, the agent's reward would go up by 5.

The reward function was more complex than this at the start, but I had found the agent to act erratically and not behave well, so redcuing the function to be as simple as possible seemed to help it understand the environment better.

## Interesting Notes:
Usually, after training for over 100,000 steps, the agent seems to find an optimal pattern of staying on one side of the grid to maximize its reward, though it takes a longer time to for it to learn to accurately dodge the boxes falling directly overhead.
