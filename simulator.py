import numpy as np
from numpy import linalg as LA
import math
from enum import Enum
from qubit import Qubit
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

        # Useful Matrices
        self.CNOT_MATRIX_1 = np.array(
            [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])
        self.CNOT_MATRIX_2 = np.array(
            [[1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0]])
        self.HADAMARD_MATRIX_1 = (
            1 / math.sqrt(2)) * np.kron(np.array([[1, 1], [1, -1]]), np.identity(2))
        self.HADAMARD_MATRIX_2 = (1 / math.sqrt(2)) * \
            np.kron(np.identity(2), np.array([[1, 1], [1, -1]]))

        self.PAULI_MATRIX_X_1 = np.kron(
            np.array([[0, 1], [1, 0]]), np.identity(2))
        self.PAULI_MATRIX_Y_1 = np.kron(
            np.array([[0, -1j], [1j, 0]]), np.identity(2))
        self.PAULI_MATRIX_Z_1 = np.kron(
            np.array([[1, 0], [0, -1]]), np.identity(2))

        self.PAULI_MATRIX_X_2 = np.kron(np.identity(2),
                                        np.array([[0, 1], [1, 0]]))
        self.PAULI_MATRIX_Y_2 = np.kron(np.identity(2),
                                        np.array([[0, -1j], [1j, 0]]))
        self.PAULI_MATRIX_Z_2 = np.kron(np.identity(2),
                                        np.array([[1, 0], [0, -1]]))

    def CNOT_1(self, state):
        '''CNOT with the first qubit as the control'''
        return np.matmul(self.CNOT_MATRIX_1, state)

    def CNOT_2(self, state):
        '''CNOT with the second qubit as the control'''
        return np.matmul(self.CNOT_MATRIX_2, state)

    def Hadamard_1(self, state):
        '''Hadamard on the first qubit'''
        return np.matmul(self.HADAMARD_MATRIX_1, state)

    def Hadamard_2(self, state):
        '''Hadamard on the second qubit'''
        return np.matmul(self.HADAMARD_MATRIX_2, state)

    def Pauli_X_1(self, state):
        '''Pauli X matrix on the first qubit'''
        return np.matmul(self.PAULI_MATRIX_X_1, state)

    def Pauli_Y_1(self, state):
        '''Pauli Y matrix on the first qubit'''
        return np.matmul(self.PAULI_MATRIX_Y_1, state)

    def Pauli_Z_1(self, state):
        '''Pauli Z matrix on the first qubit'''
        return np.matmul(self.PAULI_MATRIX_Z_1, state)

    def Pauli_X_2(self, state):
        '''Pauli X matrix on the second qubit'''
        return np.matmul(self.PAULI_MATRIX_X_2, state)

    def Pauli_Y_2(self, state):
        '''Pauli Y matrix on the second qubit'''
        return np.matmul(self.PAULI_MATRIX_Y_2, state)

    def Pauli_Z_2(self, state):
        '''Pauli Z matrix on the second qubit'''
        return np.matmul(self.PAULI_MATRIX_Z_2, state)

    def set_state(self, new_state):
        self.state = new_state

    def compare_positions(self):
        position_diff = self.qubits[0].position - self.qubits[1].position
        zero_positions = np.where(position_diff == 0)[0]
        if zero_positions.size == 1:  # only have one of the same coordinate
            # index of differing coordinate
            diff_position = 1 - zero_positions[0]
            if position_diff[diff_position] > 0:
                # calls CNOT_1 on qubit 2 if its lower than qubit 1 in the differing coordinate
                self.set_state(self.CNOT_1(self.state))
                self.updated_qubit_idx = 1
            else:
                self.set_state(self.CNOT_2(self.state))
                self.updated_qubit_idx = 0
        else:  # if they're at the same position or don't have any shared coordinates, call Hadamard on a random one
            self.updated_qubit_idx = random.randint(0, len(self.qubits))
            if self.updated_qubit_idx == 0:
                self.set_state(self.Hadamard_1(self.state))
            else:
                self.set_state(self.Hadamard_2(self.state))

    def spin_strategy(self):  # TODO:implement
        '''Given the locations of the qubits, choose to multiply the unaltered qubit by one of the Pauli Matrices.
           Measure the spin of the qubit afterwards, and gain/lose points according to the spin'''
        pass

    def get_spin(self, measurement_matrix):  #TODO: adjust state
        '''gets spin of qubit and adjusts the state accordingly'''
        values, vecs = LA.eig(measurement_matrix)
        neg_1_position = np.where(values==-1)[0][0] #TODO: this will only return the first index this is true (theoretically should only be one case, but it hasnt been that way in practice)
        neg_1_vec =  vecs[neg_1_position]
        prob_neg_one = self.get_probability(neg_1_vec) #prob +1 is 1- prob(-1)
        if random.random() <= prob_neg_one:
            return -1
        else:
            return 1

    def get_probability(self, eigenvector):
        return np.matmul(self.state, eigenvector.T) * np.matmul(eigenvector, self.state.T)

    def step(self, delta_time):
        '''simulate the entire process'''
        for qubit in self.qubits:
            qubit.get_next_location()

        self.compare_positions()

    def simulate(self, delta_time, num_steps, is_graphing=False):  # TODO: implement graphing
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
