import numpy as np
import math
from enum import Enum
import random

from qubit import Qubit
from spin import Spin

# summary of simulation:
# combined singlet state is entangled
# take measurement of locations (probabilities determined by schrodinger equation)
# state changed to eigenvector of corresponding eigenvalue of measurement (tbh im not sure abt this step)
# If locations agree on at least one positon, do CNOT with greater position as control (CNOT_1: H tensor I, CNOT_2: I tensor H)
# if locations don't agree at any position
# Choose one of the qubits randomly, apply hadamard to it


class Simulator:
    def __init__(self, x_pos_range=2, y_pos_range=2, init_state=x):
        super().__init__()
        self.x_positions = np.arange(-x_pos_range, x_pos_range + 1)
        self.y_positions = np.arange(-y_pos_range, y_pos_range + 1)
        self.possible_positions = np.array(
            [[x, y] for x in self.x_positions for y in self.y_positions])

        self.state = init_state
        self.qubits = [Qubit(init_state, init_position, possible_positions), Qubit(
            init_state, init_position, possible_positions)]

        self.updated_qubit_idx = -1
        self.points = 0  # points in game



    def compare_positions(self):
        position_diff = self.qubits[0].position - self.qubits[1].position
        zero_positions = np.where(position_diff == 0)[0]
        if zero_positions.size == 1:  # only have one of the same coordinate
            # index of differing coordinate
            diff_position = 1 - zero_positions[0]
            if position_diff[diff_position] > 0:
                # calls CNOT_1 on qubit 2 if its lower than qubit 1 in the differing coordinate
                self.qubits[1].update_state(self.CNOT_1(self.qubits[1].state))
                self.updated_qubit_idx = 1
            else:
                self.qubits[0].update_state(self.CNOT_2(self.qubits[0].state))
                self.updated_qubit_idx = 0
        else:  # if they're at the same position or don't have any shared coordinates, call Hadamard on a random one
            self.updated_qubit_idx = random.randint(0, len(self.qubits))
            chosen_qubit = self.qubits[updated_qubit_idx]
            chosen_qubit.update_state(self.Hadamard(chosen_qubit.state))

    def spin_strategy(self):  # TODO:implement
        '''Given the locations of the qubits, choose to multiply the unaltered qubit by one of the Pauli Matrices.
           Measure the spin of the qubit afterwards, and gain/lose points according to the spin'''
        pass

    def get_spin(self): #TODO: implement
        '''gets spin of qubit and adjusts the state accordingly'''
        pass 

    def step(self, delta_time):
        '''simulate the entire process'''
        for qubit in self.qubits:
            qubit.get_next_location()

        self.compare_positions()

    def simulate(self, delta_time, num_steps, is_graphing=true):  # TODO: implement graphing
        for i in num_steps:
            self.step(delta_time)

        if is_graphing:
            pass

    def create_plot(self):  # TODO: implement
        pass


if __name__ == "__main__":
    sim = Simulator()
    # TODO: uncomment and put in delta_time
    # sim.simulate()
