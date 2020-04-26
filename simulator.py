import numpy as np
from numpy import linalg as LA
import math
from enum import Enum
import random

from location_tracker import LocationTracker
from state_tracker import StateTracker

# summary of simulation:
# combined singlet state is entangled
# take measurement of locations (probabilities determined by schrodinger equation)
# state changed to eigenvector of corresponding eigenvalue of measurement (tbh im not sure abt this step)
# If locations agree on at least one positon, do CNOT with greater position as control (CNOT_1: H tensor I, CNOT_2: I tensor H)
# if locations don't agree at any position
# Choose one of the qubits randomly, apply hadamard to it


class Simulator:
    def __init__(self, state_tracker: StateTracker, qubit1: LocationTracker, qubit2: LocationTracker):
        super().__init__()

        self.state_tracker = state_tracker
        self.qubit1 = qubit1
        self.qubit2 = qubit2
        self.num_qubits = 2

        self.updated_qubit_idx = -1  # qubit that was last passed through a gate
        self.points = 0  # points in game

    def compare_positions(self, time_step):
        '''Logic for comparing the positions of the qubits at two timesteps and performing the corresponding gateß'''
        loc1 = self.qubit1.get_location(time_step)
        loc2 = self.qubit2.get_location(time_step)
        print("-------------TIME STEP: %d---------------" % time_step)
        print("QUBIT 1 LOCATION:%s" % np.array2string(loc1))
        print("QUBIT 2 LOCATION:%s" % np.array2string(loc2))

        position_diff = loc1 - loc2
        zero_positions = np.where(position_diff == 0)[0]
        if zero_positions.size == 1:  # only have one of the same coordinate
            # index of differing coordinate
            diff_position = 1 - zero_positions[0]
            if position_diff[diff_position] > 0:
                print("APPLIED CNOT 2")
                # calls CNOT_2 on qubit 2 if its lower than qubit 1 in the differing coordinate
                self.state_tracker.CNOT2()
                self.updated_qubit_idx = 1
            else:
                print("APPLIED CNOT 1")

                self.state_tracker.CNOT1()
                self.updated_qubit_idx = 0
        else:  # if they're at the same position or don't have any shared coordinates, call Hadamard on a random one
            self.updated_qubit_idx = random.randint(
                0, self.num_qubits)
            if self.updated_qubit_idx == 0:
                print("APPLIED Hadamard 1")

                self.state_tracker.Hadamard1()
            else:
                print("APPLIED Hadamard 1")

                self.state_tracker.Hadamard2()

    def spin_strategy(self):  # TODO:implement
        '''Given the locations of the qubits, choose to multiply the unaltered qubit by one of the Pauli Matrices.
           Measure the spin of the qubit afterwards, and gain/lose points according to the spin'''
        pass

    def step(self, time_step, measurement_speed):
        '''simulate the entire process'''
        self.qubit1.step(measurement_speed)
        self.qubit2.step(measurement_speed)

        self.compare_positions(time_step)

    def simulate(self, num_steps, measurement_speed, is_graphing=False):  # TODO: implement graphing
        for i in range(num_steps):
            self.step(i, measurement_speed)
            self.spin_strategy()

        if is_graphing:
            pass

    def create_plot(self):  # TODO: implement
        pass


if __name__ == "__main__":
    init_state = (1/math.sqrt(2)) * np.array([0, 1, -1, 0])
    init_loc = np.zeros(2)
    x_min = -2
    x_max = 2
    y_min = -2
    y_max = 2
    num_steps = 10
    measurement_speed = 10
    state_tracker = StateTracker(init_state)
    qubit1 = LocationTracker(init_loc, x_min, x_max, y_min, y_max, num_steps)
    qubit2 = LocationTracker(init_loc, x_min, x_max, y_min, y_max, num_steps)
    sim = Simulator(state_tracker, qubit1, qubit2)
    sim.simulate(num_steps, measurement_speed)
