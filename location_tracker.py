import numpy as np
from numpy import linalg as LA
import math



class LocationTracker:
    def __init__(self, init_location, x_min, x_max, y_min, y_max, num_steps=10):
        self.location = init_location
        self.x_positions = np.arange(x_min, x_max + 1)
        self.y_positions = np.arange(y_min, y_max + 1)
        self.possible_locations = np.array(
            [[x, y] for x in self.x_positions for y in self.y_positions])
        self.start_idx = np.argwhere(
            np.all((self.possible_locations - init_location) == 0, axis=1)).item(0)
        self.start_location = self.possible_locations[self.start_idx]
        self.k = 0
        self.num_steps = num_steps
        self.wave_function = np.zeros(
            (self.num_steps + 1, self.x_positions.size * self.y_positions.size), dtype='complex128')
        self.loc_probabilities = np.zeros(
            (self.num_steps + 1, self.x_positions.size * self.y_positions.size))
        self.wave_function[0][self.start_idx] = 1
        # guaranteed to be at start position
        self.loc_probabilities[0][self.start_idx] = 1

    def step(self, measurement_speed):
        self.k += 1
        it = np.nditer(self.wave_function[self.k], flags=[
                       'f_index'], op_flags=['readwrite'])
        for loc in it:
            it_prev = np.nditer(
                self.wave_function[self.k - 1], flags=['f_index'])
            for loc_prev in it_prev:
                loc += loc_prev * math.e ** ((measurement_speed / 2) * 1j * LA.norm(
                    self.possible_locations[it_prev.index] - self.possible_locations[it.index]) ** 2)

        it_prob = np.nditer(self.wave_function[self.k], flags=[
            'f_index'])
        self.loc_probabilities[self.k] = np.array(
            [prob * np.conj(prob) for prob in it_prob])
        self.loc_probabilities[self.k] /= sum(self.loc_probabilities[self.k])

    def simulate(self, measurement_speed):
        for i in range(self.num_steps):
            self.step(measurement_speed)

    def get_location(self, timestep):
        return self.possible_locations[np.random.choice(np.arange(25), p=self.loc_probabilities[timestep])]

if __name__ == '__main__':
    l = LocationTracker(np.zeros(2), -2, 2, -2, 2)
    
