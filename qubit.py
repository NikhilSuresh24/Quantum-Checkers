
class Qubit:
    def __init__(self, init_state, init_position, possible_positions):
        super().__init__()
        self.state = init_state
        self.position = init_position
        self.possible_positions = possible_positions

    def get_probability(self, x_position, y_position, delta_time): #TODO:implement
        '''Get the probability of being at (x,y) after delta_time'''
        pass

    def get_next_location(self, delta_time): #TODO:implement
        '''Use get_probability to get probability of being at any locations, uses those probabilities to get the next position, then finally updates position'''
        pass

    def update_state(self, new_state):
        '''set new state depending on what simulation does'''
        self.state = new_state