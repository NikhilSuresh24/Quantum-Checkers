import numpy as np
from numpy import linalg as LA
import math
import random


class StateTracker:
    def __init__(self, init_state):
        self.state = init_state

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
        self.PAULI_MATRIX_X_2 = np.kron(
            np.identity(2), np.array([[0, 1], [1, 0]]))
        self.PAULI_MATRIX_Y_2 = np.kron(
            np.identity(2), np.array([[0, -1j], [1j, 0]]))
        self.PAULI_MATRIX_Z_2 = np.kron(
            np.identity(2), np.array([[1, 0], [0, -1]]))

    # Gates: G1 says it applies G to Qubit 1; G2 says it applies G to Qubit 2

    def CNOT1(self):
        self.spin = np.matmul(
            self.CNOT_MATRIX_1, self.state)

    def CNOT2(self):
        self.spin = np.matmul(self.CNOT_MATRIX_2, self.state)

    def Hadamard1(self):
        self.spin = np.matmul(self.HADAMARD_MATRIX_1, self.state)

    def Hadamard2(self):
        self.spin = np.matmul(self.HADAMARD_MATRIX_2, self.state)

    def Pauli_X1(self):
        self.spin = np.matmul(
            self.PAULI_MATRIX_X_1, self.state)

    def Pauli_Y1(self):
        self.spin = np.matmul(
            self.PAULI_MATRIX_Y_1, self.state)

    def Pauli_Z1(self):
        self.spin = np.matmul(
            self.PAULI_MATRIX_Z_1, self.state)

    def Pauli_X2(self):
        self.spin = np.matmul(
            self.PAULI_MATRIX_X_2, self.state)

    def Pauli_Y2(self):
        self.spin = np.matmul(
            self.PAULI_MATRIX_Y_2, self.state)

    def Pauli_Z2(self):
        self.spin = np.matmul(
            self.PAULI_MATRIX_Z_2, self.state)

    def get_probability(self, eigenvector):
        '''Probability of getting a certain eigenvalue from a measurement using state and correponding eigenvectorß'''
        return np.matmul(self.state, eigenvector.T) * np.matmul(eigenvector, self.state.T)

    def get_spin(self, measurement_matrix):  # TODO: adjust state
        '''gets spin of qubit and adjusts the state accordingly'''
        values, vecs = LA.eig(measurement_matrix)
        neg_1_position = np.where(values == -1)[0][0]
        neg_1_vec = vecs[neg_1_position]
        prob_neg_one = self.get_probability(
            neg_1_vec)  # prob +1 is 1- prob(-1)
        if random.random() <= prob_neg_one:
            return -1
        else:
            return 1
