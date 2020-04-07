import numpy as np
import math
from enum import Enum
from pauli import Pauli

#summary of simulation:
#combined singlet state is entangled
#take measurement of locations (probabilities determined by schrodinger equation)
# state changed to eigenvector of corresponding eigenvalue of measurement (tbh im not sure abt this step)
# If locations agree on at least one positon, do CNOT with greater position as control (CNOT_1: H tensor I, CNOT_2: I tensor H)
# if locations don't agree at any position
# Choose one of the qubits randomly, apply hadamard to it

class Simulator:
    #measurement sends state to eigenvector of corresponding eigenvalue of measurement
    #eigenvalues are the locations
    def __init__(self, x_pos_range, y_pos_range):
        super().__init__()
        self.x_positions = np.arange(-x_pos_range, x_pos_range + 1)
        self.y_positions = np.arange(-y_pos_range, y_pos_range + 1)
        self.state_1 = np.array([0, 1, -1, 0])
        self.state_1 = np.array([0, 1, -1, 0])
        self.positions = np.array(
            [[x, y] for x in self.x_positions for y in self.y_positions])
        self.CNOT_MATRIX = np.array(
            [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]]) #TODO: there's a second CNOT
        self.CNOT_MATRIX2 = np.array(
            [[1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0]])
        self.HADAMARD_MATRIX = (
            1 / math.sqrt(2)) * np.array([[1, 0, 1, 0], [0, 1, 0, 1], [0, 1, 0, -1], [1, 0, -1, 0]])

    def CNOT(self, state):
        return np.matmul(self.CNOT_MATRIX, state)

    def Hadamard(self, state):
        return np.matmul(self.HADAMARD_MATRIX, state)

    def Pauli_X(self, state): 
        return np.matmul(Pauli.X, state)

    def Pauli_Y(self, state): 
        return np.matmul(Pauli.Y, state)
    
    def Pauli_Z(self, state): 
        return np.matmul(Pauli.Z, state)
    
    def measure_location(self, state):
        '''location measurement, return the locations received'''
        pass

    def compare_locations(self, loc_1, loc_2):
        '''this method may not be necessary, but just compare the two locations and apply the corresponding matrix'''
        pass
    
    def simulate(self, state):
        '''simulate the entire process'''
        pass

class Quibit:
	def __init__(self):
		self.loc=[[1,2],[3,4]]
	def get_prob(self, i, j):
		pass
	        
