import numpy as np

class Spin:
    def __init__(self, init_spin=((1/math.sqrt(2)) * np.array([0, 1, -1, 0]))):
        self.spin = init_spin

    # Gates: G1 says it applies G to 1; G2 says it applies G to 2
    def CNOT1(self): self.spin = np.matmul(np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]]), self.spin)
    def CNOT2(self): self.spin = np.matmul(self.np.array([[1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0]]), self.spin)
    def Hadamard(self): self.spin = np.matmul((1 / math.sqrt(2)) * np.array([[1, 0, 1, 0], [0, 1, 0, 1], [0, 1, 0, -1], [1, 0, -1, 0]]), self.spin)
    def Pauli_X1(self): self.spin = np.matmul(self.PAULI_MATRIX_X_1, self.spin)
    def Pauli_Y1(self): self.spin = np.matmul(np.kron(np.array([[0, -1j], [1j, 0]]), np.identity(2)), self.spin)
    def Pauli_Z1(self): self.spin = np.matmul(np.kron(np.array([[1, 0], [0, -1]]), np.identity(2)), self.spin)
    def Pauli_X2(self): self.spin = np.matmul(np.kron(np.identity(2), np.array([[0, 1], [1, 0]])), self.spin)
    def Pauli_Y2(self): self.spin = np.matmul(np.kron(np.identity(2), np.array([[0, -1j], [1j, 0]])), self.spin)
    def Pauli_Z2(self): self.spin = np.matmul(np.kron(np.identity(2), np.array([[1, 0], [0, -1]])), self.spin)



# self.CNOT_MATRIX_1 = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])
# self.CNOT_MATRIX_2 = np.array([[1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0]])
# self.HADAMARD_MATRIX = (1 / math.sqrt(2)) * np.array([[1, 0, 1, 0], [0, 1, 0, 1], [0, 1, 0, -1], [1, 0, -1, 0]])
# self.PAULI_MATRIX_X_1 = np.kron(np.array([[0, 1], [1, 0]]), np.identity(2))
# self.PAULI_MATRIX_Y_1 = np.kron(np.array([[0, -1j], [1j, 0]]), np.identity(2))
# self.PAULI_MATRIX_Z_1 = np.kron(np.array([[1, 0], [0, -1]]), np.identity(2))
# self.PAULI_MATRIX_X_2 = np.kron(np.identity(2), np.array([[0, 1], [1, 0]]))
# self.PAULI_MATRIX_Y_2 = np.kron(np.identity(2), np.array([[0, -1j], [1j, 0]]))
# self.PAULI_MATRIX_Z_2 = np.kron(np.identity(2), np.array([[1, 0], [0, -1]]))