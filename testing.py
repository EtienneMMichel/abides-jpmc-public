import gymnasium as gym
from abides_gym import abides_gym

if __name__ == "__main__":
    #import abides gym 
    env = gym.make(
            "markets-execution-v0",
            background_config="rmsc04"
        )
    #set the general seed
    env.seed(0)