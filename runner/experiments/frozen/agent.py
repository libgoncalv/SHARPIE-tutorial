from tamer import Tamer

# Wrap the TAMER algorithm
class Agent:
    def __init__(self, name, room_name):
        self.name = name
        self.room_name = room_name
        self.tamer = Tamer(model_file_to_load = room_name+'_model')

    # Sample an action from the agent during training
    def sample(self, observation):
        return 0
    
    # Sample an action from the agent when evaluating the policy
    def predict(self, observation):
        return 0
    
    # Train the agent based on human feedback/reward
    def train(self, state, action, reward, done, next_state):
        # You need to take into account the value of the reward, and whether the next state is the end of the game or not
        # Then you save the current model
        return
    
# Creates all the agents that will need to interact with the user during the episode
def create_agents(room_name):
    return [Agent('agent_0', room_name)]