import gymnasium as gym
from gymnasium.wrappers import FlattenObservation

# env = gym.make("CarRacing-v3", render_mode="human")

env = gym.make("CarRacing-v3", domain_randomize=True)

# normal reset, this changes the colour scheme by default
# env.reset()

# # reset with colour scheme change
env.reset(options={"randomize": True})

# # reset with no colour scheme change
# env.reset(options={"randomize": False})

for _ in range(1000):
    env.render()
    action = env.action_space.sample()  # 랜덤 액션
    env.step(action)

env.close()


# import gymnasium as gym

# env = gym.make("CarRacing-v3", render_mode="rgb_array", lap_complete_percent=0.95, domain_randomize=False, continuous=False)
# # env = gym.make("CarRacing-v3", domain_randomize=True)

# # normal reset, this changes the colour scheme by default
# obs, _ = env.reset()

# # reset with colour scheme change
# randomize_obs, _ = env.reset(options={"randomize": True})

# # reset with no colour scheme change
# non_random_obs, _ = env.reset(options={"randomize": False})
