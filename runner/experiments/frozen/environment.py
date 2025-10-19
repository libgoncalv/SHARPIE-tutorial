import gymnasium as gym

# Mapping of the inputs from the user to the environment actions or reward
# inputs is given as a dict with key being the name of the agent and value being a list of pressed keys
# example: inputs = {'agent_0': ['ArrowUp']}
def input_mapping(inputs):
    # This environment requires a scalar reward
    return 0

def termination_condition(terminated, truncated):
    return terminated or truncated

environment = gym.make('FrozenLake-v1', is_slippery=False, render_mode="rgb_array")