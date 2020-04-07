import numpy as np
from enum import Enum

class Pauli(Enum):
    X = np.kron(np.array([[0, 1], [1, 0]]), np.identity(2))
    Y = np.kron(np.array([[0, -1j], [1j, 0]]), np.identity(2))
    Z = np.kron(np.array([[1, 0], [0, -1]]), np.identity(2))